# All Viewer plugins must inherit from the ViewerPlugin
from calibre.customize import ViewerPlugin
from PyQt5.Qt import QAction, QIcon, QWidget
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
    
    d_print("***NEW CALIBRE ASL PLUGIN INSTANCE SUCCESSFULLY STARTED***")
        
    def customize_ui(self, ui):
        icon = get_icons("images/ASLSettingsIcon.png")
        action = QAction(icon, 'ASL Plugin Settings', ui, triggered = self.preferences_clicked) #this icon calls preferences_clicked when it is "triggered" (clicked)
        ui.tool_bar.addAction(action)

    """
    This method is called when the user clicks on the ASL Configuration icon.
    It shows the widget returned by config_widget()
    """
    def preferences_clicked(self):
        dialog = self.config_widget()
        dialog.show()
        
    def customize_context_menu(self, menu, event, hit_test_result):
        webPage = hit_test_result.frame().page()
        selectedText = webPage.selectedText()
        selectedText = selectedText.replace('"', '')        #for security concerns, get rid of quotes
        
        icon = get_icons("images/PlayVideo.png")
        menu.addAction(icon, _("Show ASL video for '%s'") % selectedText, partial(self.show_asl, selectedText))

    def show_asl(self, text):
        html_lines = get_resources("Launcher.html")
        with open('Launcher.html', 'w+') as f:            
            #now that we have read in the file, do regex replacement to replace "var keyword = whatever" with the selected text, so we get "var keyword = 'text'"
            import re
            html_lines = re.sub(r'var keyword =.*;','var keyword = "%s";' % text , html_lines)
            #write the new html with keyword replaced back to the file
            f.write(html_lines)
            
        webbrowser.open_new('Launcher.html')
        
    
    """
    Implement this method and save_settings() in your plugin to use a custom configuration dialog, 
    rather then relying on the simple string based default customization.

    This method, if implemented, must return a QWidget. The widget can have an optional method validate() that takes 
    no arguments and is called immediately after the user clicks OK. Changes are applied if and only if the method returns True.

    If for some reason you cannot perform the configuration at this time, return a tuple of two strings (message, details), 
    these will be displayed as a warning dialog to the user and the process will be aborted. 
    """
    def config_widget(self):
        #create widget and 
        widget = QWidget()
        d_print("Widget created")
        return widget
    
    """
    Save the settings specified by the user with config_widget.
    @param config_widget – The widget returned by config_widget().
    """
    def save_settings(self, config_widget):
        pass
  
