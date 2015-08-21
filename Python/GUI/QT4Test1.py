import sys
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *

# create our window
app = QApplication(sys.argv)
w = QMainWindow()
w.setWindowTitle('Window Creation and Learning')
# Set window size.
w.resize(800, 600)

# Create a button in the window
btn = QPushButton('Click me', w)
btn.move(100,80)
# Create the actions
@pyqtSlot()
def on_click():
    print('clicked')

@pyqtSlot()
def on_press():
    # Show a message box
    result = QMessageBox.question(w, 'Message', "Do you like Python?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if result == QMessageBox.Yes:
        print 'Yes.'
    else:
        print 'No.'
    print('pressed')

@pyqtSlot()
def on_release():
    print('released')

# connect the signals to the slots
btn.clicked.connect(on_click)
btn.pressed.connect(on_press)
btn.released.connect(on_release)

# Adding the Menu
# Create main menu
mainMenu = w.menuBar()
fileMenu = mainMenu.addMenu('&File')

# Add exit button
exitButton = QAction(QIcon('exit24.png'), 'Exit', w)
exitButton.setShortcut('Ctrl+Q')
exitButton.setStatusTip('Exit application')
exitButton.triggered.connect(w.close)
fileMenu.addAction(exitButton)

# Create combobox
combo = QComboBox(w)
combo.addItem("Python")
combo.addItem("Perl")
combo.addItem("Java")
combo.addItem("C++")
combo.move(40,110)

# Create calendar
cal = QCalendarWidget(w)
cal.setGridVisible(True)
cal.move(0, 140)
cal.resize(320,240)

# Create textbox
textbox = QLineEdit(w)
textbox.move(20, 20)
textbox.resize(280,40)

# Create a button in the window new button
button = QPushButton('Click me', w)
button.move(20,80)

# Create the actions
@pyqtSlot()
def on_click():
    textbox.setText("Button clicked.")

# connect the signals to the slots
button.clicked.connect(on_click)

# Show the window and run the app
w.show()
app.exec_()
