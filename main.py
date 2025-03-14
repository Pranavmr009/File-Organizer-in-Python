import sys 
from PyQt6.QtWidgets import QApplication
from frontend import FileOrganizerFrontend


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileOrganizerFrontend()
    window.show()
    sys.exit(app.exec())