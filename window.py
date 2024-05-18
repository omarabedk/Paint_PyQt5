# -*- coding: utf-8 -*-
import os,sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtGui import QIcon

#from scene import Scene
from view import View

class Window(QtWidgets.QMainWindow):
    def __init__(self,position=(0,0),dimension=(500,300)):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("O&W Paint")
        icon_path = "Icons/Paint_logo.png" 
        self.setWindowIcon(QtGui.QIcon(icon_path))
        w,h=dimension
        x,y=position
        self.view=View()       
        self.scene=QtWidgets.QGraphicsScene()  # Model
        self.view.setScene(self.scene)
        self.setCentralWidget(self.view)

        # Get the screen dimensions
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        screen_width, screen_height = screen.width(), screen.height()

        # Set the window geometry to cover the entire screen
        self.setGeometry(0, 0, screen_width, screen_height)
        self.scene.setSceneRect(x,y,w,h) 

        self.create_actions()
        self.connect_actions()
        self.create_menus()

    def get_view(self) :
        return self.view
    def set_view(self,view) :
        self.view=view
    def get_scene(self) :
        return self.scene
    def set_scene(self,scene) :
        self.scene=scene


    def create_actions(self) :
        # File actions
        self.action_file_open=QtWidgets.QAction(QtGui.QIcon('Icons/open.png'),"Open",self)
        self.action_file_open.setShortcut("Ctrl+O")
        self.action_file_open.setStatusTip("Open file")
        self.action_save_as=QtWidgets.QAction(QtGui.QIcon('Icons/save_as.png'),"Save As",self)
        self.action_save_image=QtWidgets.QAction(QtGui.QIcon('Icons/save_png.png'),"Save Image",self)
        self.action_save_json=QtWidgets.QAction(QtGui.QIcon('Icons/save_json.png'),"Save JSON",self)
        # Tools actions
        self.action_tools=QtWidgets.QActionGroup(self)
        self.action_tools_line=QtWidgets.QAction(QtGui.QIcon('Icons/tool_line.png'),"Line",self)
        self.action_tools_rect=QtWidgets.QAction(QtGui.QIcon('Icons/tool_rectangle.png'),"Rectangle",self)
        self.action_tools_ellipse=QtWidgets.QAction(QtGui.QIcon('Icons/tool_ellipse.png'),"Ellipse",self)
        self.action_tools_polygone=QtWidgets.QAction(QtGui.QIcon('Icons/tool_polygon.png'),"Polygone",self)
        self.action_tools_text=QtWidgets.QAction(QtGui.QIcon('Icons/tool_text.png'),"Text",self)
        self.action_tools_eraser=QtWidgets.QAction(QtGui.QIcon('Icons/tool_eraser.png'),"Eraser",self)
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
        # Style actions    
        self.action_style_pen=QtWidgets.QAction(QtGui.QIcon('Icons/tool_pen.png'),"Pen",self)
        self.action_style_brush=QtWidgets.QAction(QtGui.QIcon('Icons/tool_brush.png'),"Brush",self)
        self.action_style_brush_logo=QtWidgets.QAction(QtGui.QIcon('Icons/tool_brush_style.png'),"Brush",self)
        self.action_style_pen_color=QtWidgets.QAction(QtGui.QIcon('Icons/colorize.png'),self.tr("&Pen Color"),self)
        self.action_style_pen_thickness=QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_thickness.png'),"Thickness",self)
        self.action_style_pen_solid=QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_solid.png'),"Solid Line",self)
        self.action_style_pen_dash=QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dash.png'),"Dash Line",self)
        self.action_style_pen_dot=QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dot.png'),"Dot Line",self)
        self.action_style_pen_dashdot=QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dashdot.png'),"Dash Dot Line",self)
        self.action_style_pen_dashdotdot=QtWidgets.QAction(QtGui.QIcon('Icons/tools_pen_dashdotdot.png'),"Dash Dot Dot Line",self)
        self.action_style_brush_color=QtWidgets.QAction(QtGui.QIcon('Icons/colorize.png'),self.tr("&Color"),self)
        self.action_style_brush_no = QtWidgets.QAction(QtGui.QIcon('Icons/tools_nobrush.png'),"No Brush", self)
        self.action_style_brush_hor = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_hor.png'),"Horizontal", self)
        self.action_style_brush_ver = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_ver.png'),"Vertical", self)
        self.action_style_brush_Bdiag = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_BDiag.png'),"BDiag", self)
        self.action_style_brush_Fdiag = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_FDiag.png'),"FDiag", self)
        self.action_style_brush_diagcross = QtWidgets.QAction(QtGui.QIcon('Icons/tools_brush_cross.png'),"DiagCross", self)
        # Help actions    
    def connect_actions(self) :
        self.action_file_open.triggered.connect(self.file_open)
        self.action_tools_line.triggered.connect(
            lambda checked,tool="line": self.tools_selection(checked,tool)
        )
        self.action_tools_rect.triggered.connect(
            lambda checked,tool="rectangle": self.tools_selection(checked,tool)
        )
        self.action_tools_ellipse.triggered.connect(
            lambda checked,tool="ellipse": self.tools_selection(checked,tool)
        )
        self.action_tools_polygone.triggered.connect(
            lambda checked,tool="polygon": self.tools_selection(checked,tool)
        )
        self.action_tools_text.triggered.connect(
            lambda checked,tool="text": self.tools_selection(checked,tool)
        )
        self.action_tools_eraser.triggered.connect(
            lambda checked,tool="eraser": self.tools_selection(checked,tool)
        )
        self.action_save_image.triggered.connect(self.file_save_image)
        self.action_save_json.triggered.connect(self.file_save_json)
        self.action_style_pen_color.triggered.connect(self.style_pen_color_selection)
        self.action_style_pen_thickness.triggered.connect(self.style_pen_thickness_selection)
        self.action_style_pen_solid.triggered.connect(self.style_pen_solid_selection)
        self.action_style_pen_dash.triggered.connect(self.style_pen_dash_selection)
        self.action_style_pen_dot.triggered.connect(self.style_pen_dot_selection)
        self.action_style_pen_dashdot.triggered.connect(self.style_pen_dashdot_selection)
        self.action_style_pen_dashdotdot.triggered.connect(self.style_pen_dashdotdot_selection)
        self.action_style_brush_color.triggered.connect(self.style_brush_color_selection)
        self.action_style_brush_no.triggered.connect(self.style_brush_no_selection)
        self.action_style_brush_hor.triggered.connect(self.style_brush_hor_selection)
        self.action_style_brush_ver.triggered.connect(self.style_brush_ver_selection)
        self.action_style_brush_Bdiag.triggered.connect(self.style_brush_BDiag_selection)
        self.action_style_brush_Fdiag.triggered.connect(self.style_brush_FDiag_selection)
        self.action_style_brush_diagcross.triggered.connect(self.style_brush_diagcross_selection)

    # File actions implementation
    def file_open(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,"Open File", os.getcwd())
        fileopen=QtCore.QFile(filename[0])
        print("open",fileopen)

    def file_save_image(self):
        # Get the file path to save the image
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", os.getcwd(), "Images (*.png *.jpg *.bmp)")

        if file_path:
            viewport = self.view.viewport()
            pixmap = QtGui.QPixmap(viewport.size())
            viewport.render(pixmap)
            pixmap.save(file_path)

    def file_save_json(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save JSON", os.getcwd(), "JSON Files (*.json)")

        if file_path:
            # Example JSON data to save
            data = {"example_key": "example_value"}

            # Write the JSON data to the file
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file)

    # Tools actions implementation
    def tools_selection(self,checked,tool) :
        print("MainWindow.action_set_tools()")
        print("checked : ",checked)
        print("tool : ",tool)
        self.view.set_tool(tool)

    # Style actions implementation
    def style_pen_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow,self)
        if color.isValid() :
            self.view.set_pen_color(color.name())

    def style_pen_thickness_selection(self):
        thickness, ok = QtWidgets.QInputDialog.getInt(self, "Thickness Input", "Enter a number:")
        if ok:
            self.view.set_thickness(thickness)


    def style_brush_color_selection(self):
        color = QtWidgets.QColorDialog.getColor(QtCore.Qt.yellow,self)
        if color.isValid() :
            self.view.set_brush_color(color.name())
    
        # Style brush actions implementation
    def style_brush_no_selection(self):
        self.view.set_brush_style(QtCore.Qt.NoBrush)

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
    def help_about_us(self) :
        pass

    # Menubar actions
    def create_menus(self) :
        menubar = self.menuBar()
        menu_file = menubar.addMenu('&File')
        menu_file.addAction(self.action_file_open)
        menu_file_saveAs=menu_file.addMenu('&Save As')
        menu_file_saveAs.setIcon(self.action_save_as.icon())
        menu_file_saveAs.addAction(self.action_save_image)
        menu_file_saveAs.addAction(self.action_save_json)
        menu_tool = menubar.addMenu('&Tools')
        menu_tool.addAction(self.action_tools_line)
        menu_tool.addAction(self.action_tools_rect)
        menu_tool.addAction(self.action_tools_ellipse)
        menu_tool.addAction(self.action_tools_polygone)
        menu_tool.addAction(self.action_tools_text)
        menu_tool.addAction(self.action_tools_eraser)

        menu_style= menubar.addMenu('&Style')
        menu_style_pen= menu_style.addMenu('&Pen')
        menu_style_pen.setIcon(self.action_style_pen.icon())
        menu_style_pen_style=menu_style_pen.addMenu('&Pen Style')
        menu_style_pen_style.addAction(self.action_style_pen_solid)
        menu_style_pen_style.addAction(self.action_style_pen_dash)
        menu_style_pen_style.addAction(self.action_style_pen_dot)
        menu_style_pen_style.addAction(self.action_style_pen_dashdot)
        menu_style_pen_style.addAction(self.action_style_pen_dashdotdot)
        menu_style_brush= menu_style.addMenu('&Brush')
        menu_style_brush.setIcon(self.action_style_brush.icon())
        menu_style_pen.addAction(self.action_style_pen_color)
        menu_style_pen.addAction(self.action_style_pen_thickness)
        menu_style_brush.addAction(self.action_style_brush_color)
        menu_style_brush_style=menu_style_brush.addMenu('&Brush Style')
        menu_style_brush_style.setIcon(self.action_style_brush_logo.icon())
        menu_style_brush_style.addAction(self.action_style_brush_no)
        menu_style_brush_style.addAction(self.action_style_brush_hor)
        menu_style_brush_style.addAction(self.action_style_brush_ver)
        menu_style_brush_style.addAction(self.action_style_brush_Bdiag)
        menu_style_brush_style.addAction(self.action_style_brush_Fdiag)
        menu_style_brush_style.addAction(self.action_style_brush_diagcross)


        
    def resizeEvent(self, event):
        print("MainWindow.resizeEvent() : View")
        if self.view :
            print("dx : ",self.size().width()-self.view.size().width())
            print("dy : ",self.size().height()-self.view.size().height())
        else :
            print("MainWindow need  a view !!!!! ")
        print("menubar size : ", self.menuBar().size())

if __name__ == "__main__" :  
    print(QtCore.QT_VERSION_STR)
    app=QtWidgets.QApplication(sys.argv)

    position=0,0
    dimension=600,400

    mw=Window(position,dimension)
    xd,yd=0,0
    xf,yf=200,100
    line=QtWidgets.QGraphicsLineItem(xd,yd,xf,yf)

    line.setPen(mw.get_view().get_pen())
    mw.get_scene().addItem(line)

    mw.show()

    sys.exit(app.exec_())
