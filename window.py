import os
import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QToolTip, QFrame

# from scene import Scene
from view import View
from SecondBar import SecondaryMenuBar
from ToolsBar import ToolsBar

class Window(QtWidgets.QMainWindow):
    def __init__(self, position=(0, 0), dimensions=(8000, 3000)):
        super(Window, self).__init__()
        self.setWindowTitle("O&W Paint")
        icon_path = "Icons/Paint_logo.png"
        self.setWindowIcon(QtGui.QIcon(icon_path))
        w, h = dimensions
        x, y = position
        self.view = View()
        self.scene = QtWidgets.QGraphicsScene()  # Model
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)

        # Get the screen dimensions
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        screen_width, screen_height = screen.width(), screen.height()

        # Set the window geometry to cover the entire screen
        self.setGeometry(0, 0, screen_width, screen_height)
        self.scene.setSceneRect(x, y, w, h)

        self.create_actions()
        self.connect_actions()
        
        self.create_menus()
        
        self.create_secondary_menubar()
        self.create_tools_bar()
        
        

    def create_secondary_menubar(self):
        self.secondary_menubar = SecondaryMenuBar(self)

    def create_tools_bar(self):
        self.tools_bar = ToolsBar(self)

        main_layout = QVBoxLayout()
        top_layout = QVBoxLayout()
        top_layout.addWidget(self.menuBar())
        top_layout.addWidget(self.secondary_menubar)


        central_layout = QHBoxLayout()
        # Adding a longer line above the tool icons
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        line.setStyleSheet("color: #FF6347;")  # Change color here
        line.setFixedHeight(2)  # Make the line thicker
        line.setFixedWidth(68)
        top_layout.addWidget(line)

        central_layout.addWidget(self.tools_bar)
        central_layout.addWidget(self.view)

        main_layout.addLayout(top_layout)
        main_layout.addLayout(central_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def get_view(self):
        return self.view

    def set_view(self, view):
        self.view = view

    def get_scene(self):
        return self.scene

    def set_scene(self, scene):
        self.scene = scene












    def get_view(self):
        return self.view

    def set_view(self, view):
        self.view = view

    def get_scene(self):
        return self.scene

    def set_scene(self, scene):
        self.scene = scene

    def create_actions(self):
        # File actions
        self.action_file_new = QtWidgets.QAction(QtGui.QIcon('Icons/new.png'), "New File", self)
        self.action_file_open = QtWidgets.QAction(QtGui.QIcon('Icons/open.png'), "Open", self)
        self.action_file_open.setShortcut("Ctrl+O")
        self.action_file_open.setStatusTip("Open file")
        self.action_save_as = QtWidgets.QAction(QtGui.QIcon('Icons/save_as.png'), "Save As", self)
        self.action_save_image = QtWidgets.QAction(QtGui.QIcon('Icons/save_png.png'), "Save Image", self)
        self.action_save_image.setShortcut("Ctrl+I")
        self.action_save_json = QtWidgets.QAction(QtGui.QIcon('Icons/save_json.png'), "Save JSON", self)
        self.action_save_json.setShortcut("Ctrl+S")
        self.action_exit = QtWidgets.QAction(QtGui.QIcon('Icons/exit.png'), "Exit", self)
        self.action_exit.setShortcut("Ctrl+Q")
        # Tools actions
        self.action_tools = QtWidgets.QActionGroup(self)
        self.action_tools_line = QtWidgets.QAction(QtGui.QIcon('Icons/tool_line.png'), "Line", self)
        self.action_tools_line.setShortcut("Ctrl+L")
        self.action_tools_rect = QtWidgets.QAction(QtGui.QIcon('Icons/tool_rectangle.png'), "Rectangle", self)
        self.action_tools_rect.setShortcut("Ctrl+R")
        self.action_tools_ellipse = QtWidgets.QAction(QtGui.QIcon('Icons/tool_ellipse.png'), "Ellipse", self)
        self.action_tools_ellipse.setShortcut("Ctrl+E")
        self.action_tools_polygone = QtWidgets.QAction(QtGui.QIcon('Icons/tool_polygon.png'), "Polygon", self)
        self.action_tools_polygone.setShortcut("Ctrl+P")
        self.action_tools_text = QtWidgets.QAction(QtGui.QIcon('Icons/tool_text.png'), "Text", self)
        self.action_tools_text.setShortcut("Ctrl+T")
        self.action_tools_eraser = QtWidgets.QAction(QtGui.QIcon('Icons/tool_eraser.png'), "Eraser", self)
        self.action_tools_eraser.setShortcut("Ctrl+D")
        self.action_tools_line.setCheckable(True)
        self.action_tools_line.setChecked(True)
        self.action_tools_rect.setCheckable(True)
        self.action_tools_rect.setChecked(True)
        self.action_tools_ellipse.setCheckable(True)
        self.action_tools_ellipse.setChecked(True)
        self.action_tools_polygone.setCheckable(True)
        self.action_tools_polygone.setChecked(True)
        self.action_tools_text.setCheckable(True)
        self.action_tools_text.setChecked(True)
        self.action_tools_eraser.setCheckable(True)
        self.action_tools_eraser.setChecked(True)
        self.action_tools.addAction(self.action_tools_line)
        self.action_tools.addAction(self.action_tools_rect)
        self.action_tools.addAction(self.action_tools_ellipse)
        self.action_tools.addAction(self.action_tools_polygone)
        self.action_tools.addAction(self.action_tools_text)
        self.action_tools.addAction(self.action_tools_eraser)
        # Edit actions
        self.action_edit_undo = QtWidgets.QAction(QtGui.QIcon('Icons/edit_undo.png'), "Undo", self)
        self.action_edit_undo.setShortcut("Ctrl+Z")
        self.action_edit_redo = QtWidgets.QAction(QtGui.QIcon('Icons/edit_redo.png'), "Redo", self)
        self.action_edit_redo.setShortcut("Ctrl+Y")
        # Style actions
        self.action_style_pen = QtWidgets.QAction(QtGui.QIcon('Icons/tool_pen.png'), "Pen", self)
        self.action_style_brush = QtWidgets.QAction(QtGui.QIcon('Icons/tool_brush.png'), "Brush", self)
        self.action_style_pen_color = QtWidgets.QAction(QtGui.QIcon('Icons/colorize.png'), self.tr("&Pen Color"), self)
        self.action_style_pen_thickness = QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_thickness.png'), "Thickness", self)
        self.action_style_pen_solid = QtWidgets.QAction(QtGui.QIcon('Icons/tool_line.png'), "Solid Line", self)
        self.action_style_pen_dash = QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dash.png'), "Dash Line", self)
        self.action_style_pen_dot = QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dot.png'), "Dot Line", self)
        self.action_style_pen_dashdot = QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dashdot.png'), "Dash Dot Line", self)
        self.action_style_pen_dashdotdot = QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dashdotdot.png'), "Dash Dot Dot Line", self)
        self.action_style_brush_color = QtWidgets.QAction(QtGui.QIcon('Icons/colorize.png'), self.tr("&Color"), self)
        self.action_style_brush_no = QtWidgets.QAction("No Brush", self)
        self.action_style_brush_solid = QtWidgets.QAction(QtGui.QIcon('Icons/tool_rectangle.png'), "Solid Brush", self)
        self.action_style_brush_hor = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_hor.png'), "Horizontal", self)
        self.action_style_brush_ver = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_ver.png'), "Vertical", self)
        self.action_style_brush_Bdiag = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_BDiag.png'), "BDiag", self)
        self.action_style_brush_Fdiag = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_FDiag.png'), "FDiag", self)
        self.action_style_brush_diagcross = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_cross.png'), "DiagCross", self)
        # Help actions
        self.action_aboutus = QtWidgets.QAction(QtGui.QIcon('Icons/help_aboutus.png'), "About Us", self)
        self.action_aboutapp = QtWidgets.QAction(QtGui.QIcon('Icons/help_aboutapp.png'), "About the application", self)
        self.action_shortcuts = QtWidgets.QAction(QtGui.QIcon('Icons/help_shortcuts.png'), "Shortcuts", self)

    def connect_actions(self):
        self.action_file_open.triggered.connect(self.file_open)
        self.action_tools_line.triggered.connect(
            lambda checked, tool="line": self.tools_selection(checked, tool)
        )
        self.action_tools_rect.triggered.connect(
            lambda checked, tool="rectangle": self.tools_selection(checked, tool)
        )
        self.action_tools_ellipse.triggered.connect(
            lambda checked, tool="ellipse": self.tools_selection(checked, tool)
        )
        self.action_tools_polygone.triggered.connect(
            lambda checked, tool="polygon": self.tools_selection(checked, tool)
        )
        self.action_tools_text.triggered.connect(
            lambda checked, tool="text": self.tools_selection(checked, tool)
        )
        self.action_tools_eraser.triggered.connect(
            lambda checked, tool="eraser": self.tools_selection(checked, tool)
        )
        self.action_file_new.triggered.connect(self.file_new)
        self.action_save_image.triggered.connect(self.file_save_image)
        self.action_save_json.triggered.connect(self.file_save_json)
        self.action_exit.triggered.connect(self.file_exit)
        self.action_edit_undo.triggered.connect(self.edit_undo)
        self.action_edit_redo.triggered.connect(self.edit_redo)
        self.action_style_pen_color.triggered.connect(self.style_pen_color_selection)
        self.action_style_pen_thickness.triggered.connect(self.style_pen_thickness_selection)
        self.action_style_pen_solid.triggered.connect(self.style_pen_solid_selection)
        self.action_style_pen_dash.triggered.connect(self.style_pen_dash_selection)
        self.action_style_pen_dot.triggered.connect(self.style_pen_dot_selection)
        self.action_style_pen_dashdot.triggered.connect(self.style_pen_dashdot_selection)
        self.action_style_pen_dashdotdot.triggered.connect(self.style_pen_dashdotdot_selection)
        self.action_style_brush_color.triggered.connect(self.style_brush_color_selection)
        self.action_style_brush_no.triggered.connect(self.style_brush_no_selection)
        self.action_style_brush_solid.triggered.connect(self.style_brush_solid_selection)
        self.action_style_brush_hor.triggered.connect(self.style_brush_hor_selection)
        self.action_style_brush_ver.triggered.connect(self.style_brush_ver_selection)
        self.action_style_brush_Bdiag.triggered.connect(self.style_brush_BDiag_selection)
        self.action_style_brush_Fdiag.triggered.connect(self.style_brush_FDiag_selection)
        self.action_style_brush_diagcross.triggered.connect(self.style_brush_diagcross_selection)
        self.action_aboutus.triggered.connect(self.help_aboutus)
        self.action_aboutapp.triggered.connect(self.help_aboutapp)
        self.action_shortcuts.triggered.connect(self.help_shortcuts)

    def file_new(self):
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Do you want to save your current drawing?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.file_save_json()
            self.scene.clear()
        else:
            self.scene.clear()

    # File actions implementation
    def file_open(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open JSON", os.getcwd(), "JSON Files (*.json)")

        if file_path:
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)

            for item_data in data:
                item_type = item_data.get("type")
                if item_type == "Rectangle":
                    rect_item = QtWidgets.QGraphicsRectItem(item_data["x"], item_data["y"], item_data["width"],
                                                            item_data["height"])
                    self.scene.addItem(rect_item)
                    self.set_pen_properties(rect_item, item_data)
                    self.set_brush_properties(rect_item, item_data)
                elif item_type == "Line":
                    line_item = QtWidgets.QGraphicsLineItem(item_data["x1"], item_data["y1"], item_data["x2"],
                                                            item_data["y2"])
                    self.scene.addItem(line_item)
                    self.set_pen_properties(line_item, item_data)
                elif item_type == "Ellipse":
                    ellipse_item = QtWidgets.QGraphicsEllipseItem(item_data["x"], item_data["y"], item_data["width"],
                                                                  item_data["height"])
                    self.scene.addItem(ellipse_item)
                    self.set_pen_properties(ellipse_item, item_data)
                    self.set_brush_properties(ellipse_item, item_data)
                elif item_type == "Polygon":
                    points = [QtCore.QPointF(point["x"], point["y"]) for point in item_data["points"]]
                    polygon_item = QtWidgets.QGraphicsPolygonItem(QtGui.QPolygonF(points))
                    self.scene.addItem(polygon_item)
                    self.set_pen_properties(polygon_item, item_data)
                    self.set_brush_properties(polygon_item, item_data)
                elif item_type == "Text":
                    text_item = QtWidgets.QGraphicsTextItem(item_data["text"])
                    text_item.setPos(item_data["x"], item_data["y"])
                    self.scene.addItem(text_item)
                    self.set_text_color(text_item, item_data)

    def set_pen_properties(self, item, item_data):
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor(item_data.get("Pen Color", "black")))
        pen.setWidth(item_data.get("Pen Thickness", 1))
        pen.setStyle(item_data.get("Pen Style", QtCore.Qt.SolidLine))
        item.setPen(pen)

    def set_brush_properties(self, item, item_data):
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(item_data.get("Brush Color", "white")))
        brush.setStyle(item_data.get("Brush Style", QtCore.Qt.SolidPattern))
        item.setBrush(brush)

    def set_text_color(self, item, item_data):
        text_color = QtGui.QColor(item_data.get("Text Color", "black"))
        item.setDefaultTextColor(text_color)

    def file_save_image(self):
        # Get the file path to save the image
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", os.getcwd(),
                                                             "Images (*.png *.jpg *.bmp)")

        if file_path:
            viewport = self.view.viewport()
            pixmap = QtGui.QPixmap(viewport.size())
            viewport.render(pixmap)
            pixmap.save(file_path)

    def file_save_json(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save JSON", os.getcwd(), "JSON Files (*.json)")

        if file_path:
            data = []

            # Iterate through each item in the scene
            for item in self.scene.items():
                item_data = {}

                # Save position and dimensions based on the type of item
                if isinstance(item, QtWidgets.QGraphicsRectItem):
                    item_data["type"] = "Rectangle"
                    item_data["x"] = item.rect().x()
                    item_data["y"] = item.rect().y()
                    item_data["width"] = item.rect().width()
                    item_data["height"] = item.rect().height()
                    pen = item.pen()
                    item_data["Pen Color"] = pen.color().name()
                    item_data["Pen Thickness"] = pen.width()
                    item_data["Pen Style"] = pen.style()
                    brush = item.brush()
                    item_data["Brush Color"] = brush.color().name()
                    item_data["Brush Style"] = brush.style()

                elif isinstance(item, QtWidgets.QGraphicsLineItem):
                    item_data["type"] = "Line"
                    item_data["x1"] = item.line().x1()
                    item_data["y1"] = item.line().y1()
                    item_data["x2"] = item.line().x2()
                    item_data["y2"] = item.line().y2()
                    pen = item.pen()
                    item_data["Pen Color"] = pen.color().name()
                    item_data["Pen Thickness"] = pen.width()
                    item_data["Pen Style"] = pen.style()
                elif isinstance(item, QtWidgets.QGraphicsEllipseItem):
                    item_data["type"] = "Ellipse"
                    bounding_rect = item.boundingRect()
                    item_data["x"] = bounding_rect.x()
                    item_data["y"] = bounding_rect.y()
                    item_data["width"] = bounding_rect.width()
                    item_data["height"] = bounding_rect.height()
                    pen = item.pen()
                    item_data["Pen Color"] = pen.color().name()
                    item_data["Pen Thickness"] = pen.width()
                    item_data["Pen Style"] = pen.style()
                    brush = item.brush()
                    item_data["Brush Color"] = brush.color().name()
                    item_data["Brush Style"] = brush.style()
                elif isinstance(item, QtWidgets.QGraphicsPolygonItem):
                    item_data["type"] = "Polygon"
                    polygon = item.polygon()
                    points = []
                    for point in polygon:
                        points.append({"x": point.x(), "y": point.y()})
                    item_data["points"] = points
                    pen = item.pen()
                    item_data["Pen Color"] = pen.color().name()
                    item_data["Pen Thickness"] = pen.width()
                    item_data["Pen Style"] = pen.style()
                    brush = item.brush()
                    item_data["Brush Color"] = brush.color().name()
                    item_data["Brush Style"] = brush.style()
                elif isinstance(item, QtWidgets.QGraphicsTextItem):
                    item_data["type"] = "Text"
                    item_data["text"] = item.toPlainText()
                    item_data["x"] = item.pos().x()
                    item_data["y"] = item.pos().y()
                    text_color = item.defaultTextColor()
                    item_data["Text Color"] = text_color.name()

                data.append(item_data)

            # Write the data to the JSON file
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)

    def file_exit(self):
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation',
                                               'Are you sure you want to close the application?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            sys.exit()

    # Tools actions implementation
    def tools_selection(self, checked, tool):
        print("MainWindow.action_set_tools()")
        print("checked : ", checked)
        print("tool : ", tool)
        self.view.set_tool(tool)

    # Edit actions implementation
    def edit_undo(self):
        print("Undo triggered")
        self.view.undo()

    def edit_redo(self):
        print("Redo triggered")
        self.view.redo()

    # Style actions implementation
    def style_pen_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self)
        if color.isValid():
            self.view.set_pen_color(color.name())

    def style_pen_thickness_selection(self):
        thickness, ok = QtWidgets.QInputDialog.getInt(self, "Thickness Input", "Enter a number:")
        if ok:
            self.view.set_thickness(thickness)

    def style_brush_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow, self)
        if color.isValid():
            self.view.set_brush_color(color.name())

    # Style brush actions implementation
    def style_brush_no_selection(self):
        self.view.set_brush_style(QtCore.Qt.NoBrush)

    def style_brush_solid_selection(self):
        self.view.set_brush_style(QtCore.Qt.SolidPattern)

    def style_brush_hor_selection(self):
        self.view.set_brush_style(QtCore.Qt.HorPattern)

    def style_brush_ver_selection(self):
        self.view.set_brush_style(QtCore.Qt.VerPattern)

    def style_brush_BDiag_selection(self):
        self.view.set_brush_style(QtCore.Qt.BDiagPattern)

    def style_brush_FDiag_selection(self):
        self.view.set_brush_style(QtCore.Qt.FDiagPattern)

    def style_brush_diagcross_selection(self):
        self.view.set_brush_style(QtCore.Qt.DiagCrossPattern)

    # Style pen actions implementation
    def style_pen_solid_selection(self):
        self.view.set_pen_style(QtCore.Qt.SolidLine)

    def style_pen_dash_selection(self):
        self.view.set_pen_style(QtCore.Qt.DashLine)

    def style_pen_dot_selection(self):
        self.view.set_pen_style(QtCore.Qt.DotLine)

    def style_pen_dashdot_selection(self):
        self.view.set_pen_style(QtCore.Qt.DashDotLine)

    def style_pen_dashdotdot_selection(self):
        self.view.set_pen_style(QtCore.Qt.DashDotDotLine)

    # Help actions implementation
    def help_aboutus(self):
        QtWidgets.QMessageBox.information(self, "About Us",
                                          "This application was created by Omar ABDEL KADER and Wiam HAMMACH using PyQt5 at ENIB in May 2024.")

    def help_aboutapp(self):
        QtWidgets.QMessageBox.information(self, "About the Application",
                                          "-------------------------------------------------\n"
                                          "This is a simple paint application created with PyQt5.\n"
                                          "-------------------------------------------------\n"
                                          "Omar & Wiam | All Rights Reserved \u00A9")

    def help_shortcuts(self):
        QtWidgets.QMessageBox.information(self, "Shortcuts",
                                          "-->Shortcuts<--\n"
                                          "---------------------\n"
                                          "Ctrl+N: Create a new file\n"
                                          "Ctrl+O: Open file\n"
                                          "Ctrl+S: Save JSON file\n"
                                          "Ctrl+I: Save image file\n"
                                          "Ctrl+Q: Quit\n"
                                          "Ctrl+Z: Undo\n"
                                          "Ctrl+Y: Redo\n"
                                          "Ctrl+L: Draw a line\n"
                                          "Ctrl+R: Draw a rectangle\n"
                                          "Ctrl+E: Draw an ellipse\n"
                                          "Ctrl+P: Draw a polygon\n"
                                          "Ctrl+T: Write a text\n"
                                          "Ctrl+D: Eraser")

    # Menubar actions
    def create_menus(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("color: #FFFFFF; background-color: #494949;font-size: 19px;")
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(self.action_file_new)
        menu_file.addAction(self.action_file_open)
        menu_file_saveAs = menu_file.addMenu('&Save As')
        menu_file_saveAs.setIcon(self.action_save_as.icon())
        menu_file_saveAs.addAction(self.action_save_image)
        menu_file_saveAs.addAction(self.action_save_json)
        menu_file.addAction(self.action_exit)
        menu_edit = menubar.addMenu('&Edit')
        menu_edit.addAction(self.action_edit_undo)
        menu_edit.addAction(self.action_edit_redo)
        menu_tool = menubar.addMenu('&Tools')
        menu_tool.addAction(self.action_tools_line)
        menu_tool.addAction(self.action_tools_rect)
        menu_tool.addAction(self.action_tools_ellipse)
        menu_tool.addAction(self.action_tools_polygone)
        menu_tool.addAction(self.action_tools_text)
        menu_tool.addAction(self.action_tools_eraser)
        menu_style = menubar.addMenu('&Style')
        menu_style_pen = menu_style.addMenu('&Pen')
        menu_style_pen.setIcon(self.action_style_pen.icon())
        menu_style_pen_style = menu_style_pen.addMenu('&Pen Style')
        menu_style_pen_style.addAction(self.action_style_pen_solid)
        menu_style_pen_style.addAction(self.action_style_pen_dash)
        menu_style_pen_style.addAction(self.action_style_pen_dot)
        menu_style_pen_style.addAction(self.action_style_pen_dashdot)
        menu_style_pen_style.addAction(self.action_style_pen_dashdotdot)
        menu_style_brush = menu_style.addMenu('&Brush')
        menu_style_brush.setIcon(self.action_style_brush.icon())
        menu_style_pen.addAction(self.action_style_pen_color)
        menu_style_pen.addAction(self.action_style_pen_thickness)
        menu_style_brush.addAction(self.action_style_brush_color)
        menu_style_brush_style = menu_style_brush.addMenu('&Brush Style')
        menu_style_brush_style.addAction(self.action_style_brush_no)
        menu_style_brush_style.addAction(self.action_style_brush_solid)
        menu_style_brush_style.addAction(self.action_style_brush_hor)
        menu_style_brush_style.addAction(self.action_style_brush_ver)
        menu_style_brush_style.addAction(self.action_style_brush_Bdiag)
        menu_style_brush_style.addAction(self.action_style_brush_Fdiag)
        menu_style_brush_style.addAction(self.action_style_brush_diagcross)
        menuhelp = menubar.addMenu('&Help')
        menuhelp.addAction(self.action_aboutus)
        menuhelp.addAction(self.action_aboutapp)
        menuhelp.addAction(self.action_shortcuts)

        menubar.setStyleSheet("""
        QMenuBar{
            background-color: #494949;
            color: #FFFFFF;
        }
        QMenuBar::item::selected {
            background-color: #2E2D2D;
        }
    """)

        menu_file.setStyleSheet("""
            QMenu::item {
                background-color: #333333;
                color: #FFFFFF;
            }
            QMenu::item:selected {
                background-color: #4CAF50;
            }
        """)

        menu_edit.setStyleSheet("""
            QMenu::item {
                background-color: #333333;
                color: #FFFFFF;
            }
            QMenu::item:selected {
                background-color: #4CAF50;
            }
        """)

        menu_tool.setStyleSheet("""
            QMenu::item {
                background-color: #333333;
                color: #FFFFFF;
            }
            QMenu::item:selected {
                background-color: #4CAF50;
            }
        """)

        # Style menu
        menu_style.setStyleSheet("""
            QMenu::item {
                background-color: #333333;
                color: #FFFFFF;
            }
            QMenu::item:selected {
                background-color: #4CAF50;
            }
        """)

        # Help menu
        menuhelp.setStyleSheet("""
            QMenu::item {
                background-color: #333333;
                color: #FFFFFF;
            }
            QMenu::item:selected {
                background-color: #4CAF50;
            }
        """)

    def resizeEvent(self, event):
        print("MainWindow.resizeEvent() : View")
        if self.view:
            print("dx : ", self.size().width() - self.view.size().width())
            print("dy : ", self.size().height() - self.view.size().height())
        else:
            print("MainWindow need a view !!!!! ")
        print("menubar size : ", self.menuBar().size())

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation',
                                               'Are you sure you want to close the application?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    print(QtCore.QT_VERSION_STR)
    app = QtWidgets.QApplication(sys.argv)

    position = 0, 0
    dimension = 600, 400

    mw = Window(position, dimension)
    xd, yd = 0, 0
    xf, yf = 200, 100
    line = QtWidgets.QGraphicsLineItem(xd, yd, xf, yf)

    line.setPen(mw.get_view().get_pen())
    mw.get_scene().addItem(line)

    mw.show()

    sys.exit(app.exec_())
