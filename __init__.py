# All Viewer plugins must inherit from the ViewerPlugin
from calibre.customize import ViewerPlugin
from PyQt5.Qt import QAction, QIcon
from functools import partial
import webbrowser

###########DEBUGGING METHODS FOR WINDOWS##################
import logging
open("debug.log", "w").close()      #clear log file for a new run
logging.basicConfig(filename = "debug.log", format='%(asctime)s: %(message)s', level = logging.DEBUG, datefmt = '%I:%M:%S %p')
def d_print(msg):
    logging.debug(msg)
    
class ASLExtension(ViewerPlugin):

    # This class is a wrapper that provides information about the actual plugin.
    # The interface plugin class is called InterfacePlugin and is defined in the ui.py file.

    name = 'ASL Extension'
    description = 'American Sign Language plugin to assist deaf children learning to read.'
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Naveen Chandran, Ryan Swing, Scott Vermeyen, John Verrone'
    version = (1, 0, 0)
    minimum_calibre_version = (0, 7, 53)

    """
    This method can be implemented when settings functionality is implemented
    """
#     def customize_ui(self, ui):
#         icon = get_icons("images/ASLSettingsIcon.png")
#         ac = QAction(icon, 'ASL Plugin Settings', ui)
#         ac.setObjectName('asl_popup')
#         ui.tool_bar.addAction(ac)
#
    def customize_context_menu(self, menu, event, hit_test_result):
        webPage = hit_test_result.frame().page()
        selectedText = webPage.selectedText()
        
        if selectedText:
            selectedText = selectedText.replace('"', '')        #for security concerns, get rid of quotes
            icon = get_icons("images/PlayVideo.png")
            menu.addAction(icon, _("Show ASL video for '%s'") % selectedText, partial(self.show_asl, selectedText))

    def show_asl(self, text):
        import re, tempfile, os
        
        html_lines_l = get_resources("Launcher.html")       #read in Launcher.html lines
        html_lines_a = get_resources("ASLVideo.html")       #read in ASLVideo.html lines
        
        _launcher, launcher_temp_name = tempfile.mkstemp(suffix = ".html")
        _asl, asl_temp_name = tempfile.mkstemp(suffix = ".html")
        
        #Launcher.html injection
        html_lines_l = re.sub(r'var keyword =.*;','var keyword = "%s";' % text , html_lines_l)          #Inject keyword into Launcher.html
        html_lines_l = re.sub(r'var name_asl =.*;', 'var name_asl = "%s";' % os.path.basename(asl_temp_name) , html_lines_l)    #Inject ASLVideo.html temporary file name into Launcher.html

        with open(launcher_temp_name, "w+") as temp_file:       #create Launcher.html temporary file
            temp_file.write(html_lines_l)

        with open(asl_temp_name, "w+") as temp_file2:           #create ASLVideo.html temporary file
            temp_file2.write(html_lines_a)
        
        webbrowser.open_new(launcher_temp_name)
        
        
        
      
        
    #def load_javascript(self, evaljs):
        #pass

    #def run_javascript(self, evaljs):
        #script = get_resources('js/test.js')
        #evaljs(script)
