import os
import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QToolTip


class SecondaryMenuBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SecondaryMenuBar, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()
        # Set the icon size
        icon_size = 35
        button_style = """
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton::hover {
                background-color: #d3d3d3; /* Light grey background on hover */
            }
        """

        new_file_btn = QtWidgets.QPushButton()
        new_file_btn.setIcon(QIcon('Icons/new.png'))
        new_file_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        new_file_btn.setStyleSheet(button_style)
        new_file_btn.setToolTip(self.tr("Create a new file"))

        open_file_btn = QtWidgets.QPushButton()
        open_file_btn.setIcon(QIcon('Icons/open.png'))
        open_file_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        open_file_btn.setStyleSheet(button_style)
        open_file_btn.setToolTip(self.tr("Open a file"))

        save_image_btn = QtWidgets.QPushButton()
        save_image_btn.setIcon(QIcon('Icons/save_png.png'))
        save_image_btn.setIconSize(QtCore.QSize(27, 27))
        save_image_btn.setStyleSheet(button_style)
        save_image_btn.setToolTip(self.tr("Save as image"))

        save_json_btn = QtWidgets.QPushButton()
        save_json_btn.setIcon(QIcon('Icons/save_json.png'))
        save_json_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        save_json_btn.setStyleSheet(button_style)
        save_json_btn.setToolTip(self.tr("Save as JSON file"))

        undo_btn = QtWidgets.QPushButton()
        undo_btn.setIcon(QIcon('Icons/edit_undo.png'))
        undo_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        undo_btn.setStyleSheet(button_style)
        undo_btn.setToolTip(self.tr("Undo"))

        redo_btn = QtWidgets.QPushButton()
        redo_btn.setIcon(QIcon('Icons/edit_redo.png'))
        redo_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        redo_btn.setStyleSheet(button_style)
        redo_btn.setToolTip(self.tr("Redo"))

        # Set button size
        button_size = 35
        new_file_btn.setFixedSize(button_size, button_size)
        open_file_btn.setFixedSize(button_size, button_size)
        save_image_btn.setFixedSize(button_size, button_size)
        save_json_btn.setFixedSize(button_size, button_size)
        undo_btn.setFixedSize(button_size, button_size)
        redo_btn.setFixedSize(button_size, button_size)

        # Connect buttons to the respective methods
        new_file_btn.clicked.connect(self.parent.file_new)
        open_file_btn.clicked.connect(self.parent.file_open)
        save_image_btn.clicked.connect(self.parent.file_save_image)
        save_json_btn.clicked.connect(self.parent.file_save_json)
        undo_btn.clicked.connect(self.parent.edit_undo)
        redo_btn.clicked.connect(self.parent.edit_redo)

        # Add buttons to the layout
        layout.addWidget(new_file_btn)
        layout.addWidget(open_file_btn)
        layout.addWidget(save_image_btn)
        layout.addWidget(save_json_btn)
        layout.addWidget(undo_btn)
        layout.addWidget(redo_btn)

        layout.addStretch()  # Add stretch to align buttons to the left
        
        self.setLayout(layout)