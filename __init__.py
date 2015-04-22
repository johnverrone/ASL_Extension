# All Viewer plugins must inherit from the ViewerPlugin
from calibre.customize import ViewerPlugin
from PyQt5.Qt import QAction, QIcon, QWidget
from functools import partial
import webbrowser

class ASLExtension(ViewerPlugin):

    # This class is a wrapper that provides information about the actual plugin.
    # The interface plugin class is called InterfacePlugin and is defined in the ui.py file.

    name = 'ASL Extension'
    description = 'American Sign Language plugin to assist deaf children learning to read.'
    supported_platforms = ['windows', 'osx', 'linux']
    author = 'Naveen Chandran, Ryan Swing, Scott Vermeyen, John Verrone'
    version = (1, 0, 0)
    minimum_calibre_version = (0, 7, 53)


    def customize_ui(self, ui):
        icon = get_icons("images/ASLSettingsIcon.png")
        ac = QAction(icon, 'ASL Plugin Settings', ui)
        ac.setObjectName('asl_popup')
        ui.tool_bar.addAction(ac)

    def customize_context_menu(self, menu, event, hit_test_result):
        webPage = hit_test_result.frame().page()
        selectedText = webPage.selectedText()
        selectedText = selectedText.replace('"', '')        #for security concerns, get rid of quotes
        
        icon = get_icons("images/PlayVideo.png")
        menu.addAction(icon, _("Show ASL video for '%s'") % selectedText, partial(self.show_asl, selectedText))

    def show_asl(self, text):
        with open('Launcher.html', 'r+') as f:
            html_lines = f.read()
            
            #now that we have read in the file, do regex replacement to replace "var keyword = whatever" with the selected text, so we get "var keyword = 'text'"
            import re
            html_lines = re.sub(r'var keyword =.*;','var keyword = "%s";' % text , html_lines)
            #write the new html with keyword replaced back to the file
            f.seek(0)
            f.write(html_lines)
            f.truncate()
            
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
        
        widget = QWidget()
        return widget
    """
    Save the settings specified by the user with config_widget.

    @param config_widget – The widget returned by config_widget().
    """
    def save_settings(self, config_widget):
    #def load_javascript(self, evaljs):
        #pass

    #def run_javascript(self, evaljs):
        #script = get_resources('js/test.js')
        #evaljs(script)
