from PyQt5 import QtWidgets, uic
import sys

class raceGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(raceGUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('..\\ui\\race.ui', self) # Load the .ui file
        self.show() # Show the GUI


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = raceGUI() # Create an instance of our class
app.exec_() # Start the application