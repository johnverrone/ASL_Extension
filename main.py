# from PyQt5.Qt import QAction, QInputDialog, QPushButton, QMessageBox
#
# # The base class that all toolbars must inherit from
# from calibre.gui2.tweak_book.plugin import Tool
#
# class ASLTool(Tool):
#
#     # Unique name to be used as a key
#     name = 'asl_tool'
#
#     allowed_in_toolbar = True
#     allowed_in_menu = True
#
#     def create_action(self, for_toolbar=True):
#         # Create an action that will be added to the plugins tool and menu.
#         ac = QAction(get_icons('images/icon.png'), 'Echo highlighted word', self.gui)
#         if not for_toolbar:
#             # Register keyboard shorcut for this action
#             self.register_shortcut(ac, 'echo-word-tool', default_keys=('Ctrl+Shift+Alt+E',))
#         ac.triggered.connect(self.echo_word)
#         return ac
#
#     def echo_word(self):
#         # Print the highlighted word in a dialog box
#         msgBox = QMessageBox()
#         msgBox.setText('This is a test')
#         msgBox.addButton(QPushButton('Dismiss'), QMessageBox.YesRole)
#         msgBox.exec_()