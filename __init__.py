# All Viewer plugins must inherit from the ViewerPlugin
from calibre.customize import ViewerPlugin
from PyQt5.Qt import QPushButton, QMessageBox


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
        print(ui.tool_bar2)

    def customize_context_menu(self, menu, event, hit_test_result):
        print(hit_test_result.isContentSelected())