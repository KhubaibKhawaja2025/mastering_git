# LABEL INTRODUCTION
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphical User Interface") # WINDOWS TITLE
        self.setGeometry(600, 300, 1000, 500) # WINDOWS GEOMETRY
        self.setWindowIcon(QIcon("png-transparent-directory-icon-folder-miscellaneous-angle-rectangle-thumbnail.png")) # GUI WINDOWS ICON
        label = QLabel("Hello", self) # GUI WINDOWS TEXT
        label.setFont(QFont("Consolas", 30)) # GUI WINDOWS FONT
        label.setGeometry(0, 0, 800, 200) # GUI WINDOWS TEXT GEOMETRY
        label.setStyleSheet("color: #074CD9;" # STYLING
                            "background-color: #0EE2ED;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
# ALIGNMENTS:
        label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        label.setAlignment(Qt.AlignRight) # VERTICALLY RIGHT
        label.setAlignment(Qt.AlignLeft) # VERTICALLY LEFT
        
        label.setAlignment(Qt.AlignRight) # VERTICALLY Right
        label.setAlignment(Qt.AlignHCenter) # VERTICALLY CENTER
        label.setAlignment(Qt.AlignLeft) # VERTICALLY Left

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER AND TOP
        label.setAlignment(Qt.AlignVCenter | Qt.AlignBottom) # CENTER AND BOTTOM
        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter) # CENTER AND CENTER
        label.setAlignment(Qt.AlignCenter) # CENTER SHORTCUT
        
        

        
# GUI WINDOW
def main():
    app = QApplication(sys.argv)
    window = Mainwindow()  # Use Mainwindow instead of QMainWindow
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
