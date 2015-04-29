'''
The Preferences Dialog corresponding to the ASL Video Calibre Extension
'''
from PyQt5.QtWidgets import QDialog
from calibre.utils.config import JSONConfig

class ASLPreferencesDialog(QDialog):
    settings = JSONConfig("plugins/ASLExtension")
    
    def __init__(self, parent = None):
        super(ASLPreferencesDialog, self).__init__(parent)    #call parent class constructor
        
        layout = QV
        
        
        

