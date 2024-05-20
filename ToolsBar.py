import os
import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QToolTip, QFrame


class ToolsBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ToolsBar, self).__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

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

        line_btn = QtWidgets.QPushButton()
        line_btn.setIcon(QIcon('Icons/tool_line.png'))
        line_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        line_btn.setStyleSheet(button_style)
        line_btn.setToolTip(self.tr("Draw a line"))

        rect_btn = QtWidgets.QPushButton()
        rect_btn.setIcon(QIcon('Icons/tool_rectangle.png'))
        rect_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        rect_btn.setStyleSheet(button_style)
        rect_btn.setToolTip(self.tr("Draw a rectangle"))

        ellipse_btn = QtWidgets.QPushButton()
        ellipse_btn.setIcon(QIcon('Icons/tool_ellipse.png'))
        ellipse_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        ellipse_btn.setStyleSheet(button_style)
        ellipse_btn.setToolTip(self.tr("Draw an ellipse"))

        polygon_btn = QtWidgets.QPushButton()
        polygon_btn.setIcon(QIcon('Icons/tool_polygon.png'))
        polygon_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        polygon_btn.setStyleSheet(button_style)
        polygon_btn.setToolTip(self.tr("Draw a polygon"))

        text_btn = QtWidgets.QPushButton()
        text_btn.setIcon(QIcon('Icons/tool_text.png'))
        text_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        text_btn.setStyleSheet(button_style)
        text_btn.setToolTip(self.tr("Add text"))

        eraser_btn = QtWidgets.QPushButton()
        eraser_btn.setIcon(QIcon('Icons/tool_eraser.png'))
        eraser_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        eraser_btn.setStyleSheet(button_style)
        eraser_btn.setToolTip(self.tr("Eraser"))

        pen_color_btn = QtWidgets.QPushButton()
        pen_color_btn.setIcon(QIcon('Icons/colorize.png'))
        pen_color_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        pen_color_btn.setStyleSheet(button_style)
        pen_color_btn.setToolTip(self.tr("Pen Color"))

        brush_color_btn = QtWidgets.QPushButton()
        brush_color_btn.setIcon(QIcon('Icons/colorize.png'))
        brush_color_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        brush_color_btn.setStyleSheet(button_style)
        brush_color_btn.setToolTip(self.tr("Brush Color"))

        pen_thickness_btn = QtWidgets.QPushButton()
        pen_thickness_btn.setIcon(QIcon('Icons/tools_pen_thickness.png'))
        pen_thickness_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        pen_thickness_btn.setStyleSheet(button_style)
        pen_thickness_btn.setToolTip(self.tr("Pen Thickness"))

        # Pen styles
        pen_solid_btn = QtWidgets.QPushButton()
        pen_solid_btn.setIcon(QIcon('Icons/tool_line.png'))
        pen_solid_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        pen_solid_btn.setStyleSheet(button_style)
        pen_solid_btn.setToolTip(self.tr("Solid Line"))

        pen_dash_btn = QtWidgets.QPushButton()
        pen_dash_btn.setIcon(QIcon('Icons/tools_pen_dash.png'))
        pen_dash_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        pen_dash_btn.setStyleSheet(button_style)
        pen_dash_btn.setToolTip(self.tr("Dash Line"))

        pen_dot_btn = QtWidgets.QPushButton()
        pen_dot_btn.setIcon(QIcon('Icons/tools_pen_dot.png'))
        pen_dot_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        pen_dot_btn.setStyleSheet(button_style)
        pen_dot_btn.setToolTip(self.tr("Dot Line"))

        pen_dashdot_btn = QtWidgets.QPushButton()
        pen_dashdot_btn.setIcon(QIcon('Icons/tools_pen_dashdot.png'))
        pen_dashdot_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        pen_dashdot_btn.setStyleSheet(button_style)
        pen_dashdot_btn.setToolTip(self.tr("Dash Dot Line"))

        pen_dashdotdot_btn = QtWidgets.QPushButton()
        pen_dashdotdot_btn.setIcon(QIcon('Icons/tools_pen_dashdotdot.png'))
        pen_dashdotdot_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        pen_dashdotdot_btn.setStyleSheet(button_style)
        pen_dashdotdot_btn.setToolTip(self.tr("Dash Dot Dot Line"))

        # Brush styles
        brush_solid_btn = QtWidgets.QPushButton()
        brush_solid_btn.setIcon(QIcon('Icons/tool_rectangle.png'))
        brush_solid_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        brush_solid_btn.setStyleSheet(button_style)
        brush_solid_btn.setToolTip(self.tr("Solid Brush"))

        brush_hor_btn = QtWidgets.QPushButton()
        brush_hor_btn.setIcon(QIcon('Icons/tools_brush_hor.png'))
        brush_hor_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        brush_hor_btn.setStyleSheet(button_style)
        brush_hor_btn.setToolTip(self.tr("Horizontal Brush"))

        brush_ver_btn = QtWidgets.QPushButton()
        brush_ver_btn.setIcon(QIcon('Icons/tools_brush_ver.png'))
        brush_ver_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        brush_ver_btn.setStyleSheet(button_style)
        brush_ver_btn.setToolTip(self.tr("Vertical Brush"))

        brush_Bdiag_btn = QtWidgets.QPushButton()
        brush_Bdiag_btn.setIcon(QIcon('Icons/tools_brush_BDiag.png'))
        brush_Bdiag_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        brush_Bdiag_btn.setStyleSheet(button_style)
        brush_Bdiag_btn.setToolTip(self.tr("BDiag Brush"))

        brush_Fdiag_btn = QtWidgets.QPushButton()
        brush_Fdiag_btn.setIcon(QIcon('Icons/tools_brush_FDiag.png'))
        brush_Fdiag_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        brush_Fdiag_btn.setStyleSheet(button_style)
        brush_Fdiag_btn.setToolTip(self.tr("FDiag Brush"))

        brush_diagcross_btn = QtWidgets.QPushButton()
        brush_diagcross_btn.setIcon(QIcon('Icons/tools_brush_cross.png'))
        brush_diagcross_btn.setIconSize(QtCore.QSize(icon_size, icon_size))
        brush_diagcross_btn.setStyleSheet(button_style)
        brush_diagcross_btn.setToolTip(self.tr("DiagCross Brush"))

        # Connect buttons to the respective methods
        line_btn.clicked.connect(lambda: self.parent.tools_selection(True, "line"))
        rect_btn.clicked.connect(lambda: self.parent.tools_selection(True, "rectangle"))
        ellipse_btn.clicked.connect(lambda: self.parent.tools_selection(True, "ellipse"))
        polygon_btn.clicked.connect(lambda: self.parent.tools_selection(True, "polygon"))
        text_btn.clicked.connect(lambda: self.parent.tools_selection(True, "text"))
        eraser_btn.clicked.connect(lambda: self.parent.tools_selection(True, "eraser"))
        pen_color_btn.clicked.connect(self.parent.style_pen_color_selection)
        brush_color_btn.clicked.connect(self.parent.style_brush_color_selection)
        pen_thickness_btn.clicked.connect(self.parent.style_pen_thickness_selection)
        pen_solid_btn.clicked.connect(self.parent.style_pen_solid_selection)
        pen_dash_btn.clicked.connect(self.parent.style_pen_dash_selection)
        pen_dot_btn.clicked.connect(self.parent.style_pen_dot_selection)
        pen_dashdot_btn.clicked.connect(self.parent.style_pen_dashdot_selection)
        pen_dashdotdot_btn.clicked.connect(self.parent.style_pen_dashdotdot_selection)
        brush_solid_btn.clicked.connect(self.parent.style_brush_solid_selection)
        brush_hor_btn.clicked.connect(self.parent.style_brush_hor_selection)
        brush_ver_btn.clicked.connect(self.parent.style_brush_ver_selection)
        brush_Bdiag_btn.clicked.connect(self.parent.style_brush_BDiag_selection)
        brush_Fdiag_btn.clicked.connect(self.parent.style_brush_FDiag_selection)
        brush_diagcross_btn.clicked.connect(self.parent.style_brush_diagcross_selection)

        # Add buttons to the layout
        layout.addWidget(line_btn)
        layout.addWidget(rect_btn)
        layout.addWidget(ellipse_btn)
        layout.addWidget(polygon_btn)
        layout.addWidget(text_btn)
        layout.addWidget(eraser_btn)
        layout.addWidget(pen_color_btn)
        layout.addWidget(brush_color_btn)
        layout.addWidget(pen_thickness_btn)
        layout.addWidget(pen_solid_btn)
        layout.addWidget(pen_dash_btn)
        layout.addWidget(pen_dot_btn)
        layout.addWidget(pen_dashdot_btn)
        layout.addWidget(pen_dashdotdot_btn)
        layout.addWidget(brush_solid_btn)
        layout.addWidget(brush_hor_btn)
        layout.addWidget(brush_ver_btn)
        layout.addWidget(brush_Bdiag_btn)
        layout.addWidget(brush_Fdiag_btn)
        layout.addWidget(brush_diagcross_btn)
        layout.addStretch()  # Add stretch to align buttons to the top
        self.setStyleSheet("background-color: #1e1e1e;")  # Set the background color here