# All Viewer plugins must inherit from the ViewerPlugin
from calibre.customize import ViewerPlugin
from PyQt5.Qt import QAction, QIcon, QLabel, QPushButton, QMessageBox, QVBoxLayout, QDialog


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
        ac = QAction(QIcon(I('rating.png')), 'ASL Plugin', ui)
        ac.setObjectName('asl_popup')
        ui.tool_bar.addAction(ac)
        print "OMG ANYTHING"

    def customize_context_menu(self, menu, event, hit_test_result):
        print "HELLO"
        print(hit_test_result)

    def load_javascript(self, evaljs):
        pass

    def run_javascript(self, evaljs):
        script = get_resources('js/test.js')
        evaljs(script)

    def popup(self):
        print('clicked!')