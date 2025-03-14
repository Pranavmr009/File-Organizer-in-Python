from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QFileDialog, QLabel
from PyQt6.QtGui import QPixmap, QIcon

import sys
from PyQt6.QtCore import Qt
import backend

class FileOrganizerFrontend(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dark_mode = False

    def initUI(self):
        self.setWindowTitle("PyFileOrganizer")
        self.setGeometry(200, 200, 600, 400)
        self.setWindowIcon(QIcon("icon.webp"))
        layout = QVBoxLayout()

        self.logo_label = QLabel(self)
        piximap = QPixmap("icon.webp")
        scaled_piximap = piximap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.logo_label.setPixmap(scaled_piximap)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        input_layout = QHBoxLayout()
    
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Enter folder path or select it")

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_folder)

        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.browse_button)

        self.output_display = QTextEdit(self)
        self.output_display.setReadOnly(True)
       
        self.sort_type_button = QPushButton("Sort by File Type")
        self.sort_type_button.clicked.connect(self.sort_by_type)

        self.sort_date_button = QPushButton("Sort by Date Modified")
        self.sort_date_button.clicked.connect(self.sort_by_date)

        self.find_duplicates_button = QPushButton("Find Duplicates")
        self.find_duplicates_button.clicked.connect(self.find_duplicates)



        self.toggle_button = QPushButton("Toggle Dark Mode")
        self.toggle_button.clicked.connect(self.toggle_dark_mode)
        
        layout.addLayout(input_layout)
        layout.addWidget(self.output_display)
        layout.addWidget(self.toggle_button)
        layout.addWidget(self.sort_type_button)
        layout.addWidget(self.sort_date_button)
        layout.addWidget(self.find_duplicates_button)
        layout.addWidget(self.logo_label)
        
        
        self.setLayout(layout)

    def browse_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")  # Open folder dialog
        if folder_path:
            self.input_box.setText(folder_path)

    def sort_by_type(self):
        path = self.input_box.text()
        if path:
            backend.sort_according_to_file_types(path)
            self.output_display.append(f"Sorted files in: {path}")
    
    def sort_by_date(self):
        path = self.input_box.text()
        if path:
            backend.sort_according_to_date_modified(path)
            self.output_display.append(f"Sorted files in: {path}")
    
    def find_duplicates(self):
        path = self.input_box.text()
        if path:
            backend.find_duplicates(path)
            self.output_display.append(f"Checked for duplicates in: {path}")

    def toggle_dark_mode(self):
        if self.dark_mode:
            self.setStyleSheet("")
            self.toggle_button.setText("Toggle Dark Mode")

        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: #2E2E2E;
                    color: white;
                }
                QLineEdit, QTextEdit {
                    background-color: #3E3E3E;
                    color: white;
                    border: 1px solid #555;
                }
                QPushButton {
                    background-color: #555;
                    color: white;
                    border: 1px solid #777;
                }
                QPushButton:hover {
                    background-color: #777;
                }
            """)
            self.toggle_button.setText("Toggle Light Mode")
        self.dark_mode = not self.dark_mode
