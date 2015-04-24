'''
The Preferences Dialog corresponding to the ASL Video Calibre Extension
'''
from PyQt.QT import QDialog
from calibre.utils.config import JSONConfig

class ASLPreferencesDialog(QDialog):
    settings = JSONConfig("plugins/ASLExtension")
    
    def __init__(self, parent = None):
        super(ASLPreferencesDialog, self).__init__()    #call parent class constructor
        self.register("Window Size")      #Window size setting for ASL Video
        self.register()      #Window autoplay setting
        self.register()      #Window 
        
        self.initialize()        #create dialog with all values read in from config file
        
        

