from PyQt5 import QtWidgets, uic
import sys

class qualiGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(qualiGUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('..\\ui\\qualifying.ui', self) # Load the .ui file


        #TODO load quali results



app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = qualiGUI() # Create an instance of our class
app.exec_() # Start the application