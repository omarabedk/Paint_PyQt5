import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class View(QtWidgets.QGraphicsView):
    def __init__(self, position=(0, 0), dimension=(600, 400)):
        super(View, self).__init__()
        x, y = position
        w, h = dimension
        self.setGeometry(x, y, w, h)
        self.thickness = 5
        self.begin, self.end = QtCore.QPoint(0, 0), QtCore.QPoint(0, 0)
        self.tool = "line"
        self.item = None
        self.pen, self.brush = None, None
        self.create_style()
        self.undo_stack = []
        self.redo_stack = []
        self.vertices = []
        self.temp_polygon = None
        self.rubber_band = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, self)
        self.selected_items = []
        self.move_start_position = None
        self.original_positions = []

    def __repr__(self):
        return "<View({},{},{})>".format(self.pen, self.brush, self.tool)
    
    def get_pen(self):
        return self.pen

    def set_pen(self, pen):
        self.pen = pen

    def get_brush(self):
        return self.brush

    def set_brush(self, brush):
        self.brush = brush

    def create_style(self):
        self.create_pen()
        self.create_brush()
     
    def create_pen(self):
        self.pen = QtGui.QPen()
        self.pen.setColor(QtCore.Qt.black)
        self.pen.setWidth(self.thickness)
        self.pen.setStyle(QtCore.Qt.SolidLine)

    def create_brush(self):
        self.brush = QtGui.QBrush()
        self.brush.setColor(QtCore.Qt.black)
        self.brush.setStyle(QtCore.Qt.NoBrush)
    
    def set_tool(self, tool):
        print("View.set_tool(self,tool)", tool)
        self.tool = tool
        self.vertices.clear()
        self.update_temp_polygon()

    def set_thickness(self, thickness):
        self.pen.setWidth(thickness)

    def set_pen_color(self, color):
        print("View.set_pen_color(self,color)", color)
        self.pen.setColor(QtGui.QColor(color))

    def set_pen_style(self, style):
        print("View.set_pen_style(self,style)", style)
        self.pen.setStyle(style)

    def set_brush_color(self, color):
        print("View.set_brush_color(self,color)", color)
        self.brush.setColor(QtGui.QColor(color))

    def set_brush_style(self, style):
        print("View.set_brush_style(self,style)", style)
        self.brush.setStyle(style)

    def add_item(self, item):
        self.scene().addItem(item)
        self.undo_stack.append(("add", item))

    def remove_item(self, item):
        self.scene().removeItem(item)
        self.undo_stack.append(("remove", item))

    def undo(self):
        if self.undo_stack:
            action_type, item = self.undo_stack.pop()
            if self.scene().items():
                if action_type == "add":
                    self.scene().removeItem(item)
                    self.redo_stack.append(("add", item))
                elif action_type == "remove":
                    self.scene().addItem(item)
                    self.redo_stack.append(("remove", item))
    
    def redo(self):
        if self.redo_stack:
            action_type, item = self.redo_stack.pop()
            if action_type == "add":
                self.scene().addItem(item)
                self.undo_stack.append(("add", item))
            elif action_type == "remove":
                self.scene().removeItem(item)
                self.undo_stack.append(("remove", item))

    # Events
    def mousePressEvent(self, event):
        self.begin = self.end = event.pos()
        self.move_start_position = event.pos()
        
        if self.scene():
            item = self.scene().itemAt(self.mapToScene(event.pos()), QtGui.QTransform())
            if self.tool == "select":
                if item and item in self.selected_items:
                    self.original_positions = [item.pos() for item in self.selected_items]
                else:
                    self.rubber_band.setGeometry(QtCore.QRect(self.begin, QtCore.QSize()))
                    self.rubber_band.show()
                    self.selected_items.clear()
                    self.original_positions.clear()
            else:
                self.item = item
                if self.item:
                    self.offset = self.begin - self.item.pos()
                if self.tool == "polygon":
                    self.vertices.append(event.pos())
                    self.update_temp_polygon()
        else:
            print("no scene associated!")

    def mouseMoveEvent(self, event):
        self.end = event.pos()

        if self.scene():
            if self.tool == "select":
                if self.rubber_band.isVisible():
                    self.rubber_band.setGeometry(QtCore.QRect(self.begin, self.end).normalized())
                elif self.selected_items:
                    delta = event.pos() - self.move_start_position
                    for i, item in enumerate(self.selected_items):
                        item.setPos(self.original_positions[i] + delta)
            elif self.item:
                self.item.setPos(event.pos() - self.offset)
            else:
                print("draw bounding box!")
        else:
            print("no scene associated!")

    def mouseReleaseEvent(self, event):
        self.end = event.pos()

        if self.scene():
            if self.tool == "select":
                if self.rubber_band.isVisible():
                    self.rubber_band.hide()
                    selection_rect = QtCore.QRectF(self.mapToScene(self.begin), self.mapToScene(self.end)).normalized()
                    self.selected_items = self.scene().items(selection_rect)
                    self.original_positions = [item.pos() for item in self.selected_items]
                    print("Selected items: ", self.selected_items)
            elif self.item:
                self.item.setPos(event.pos() - self.offset)
                self.item = None
            elif self.tool == "line":
                line = QtWidgets.QGraphicsLineItem(self.begin.x(), self.begin.y(), self.end.x(), self.end.y())
                line.setPen(self.pen)
                self.add_item(line)
            elif self.tool == "rectangle":
                rect = QtWidgets.QGraphicsRectItem(
                    min(self.begin.x(), self.end.x()),     # Top-left x-coordinate
                    min(self.begin.y(), self.end.y()),     # Top-left y-coordinate
                    abs(self.end.x() - self.begin.x()),    # Width
                    abs(self.end.y() - self.begin.y())     # Height
                )
                rect.setPen(self.pen)
                rect.setBrush(self.brush)
                self.add_item(rect)
            elif self.tool == "ellipse":
                ellipse = QtWidgets.QGraphicsEllipseItem(
                    min(self.begin.x(), self.end.x()),     # Top-left x-coordinate
                    min(self.begin.y(), self.end.y()),     # Top-left y-coordinate
                    abs(self.end.x() - self.begin.x()),    # Width
                    abs(self.end.y() - self.begin.y())     # Height
                )
                ellipse.setPen(self.pen)
                ellipse.setBrush(self.brush)
                self.add_item(ellipse)
            elif self.tool == "text":
                text, ok = QtWidgets.QInputDialog.getText(self, "Text Input", "Enter your text:")
                if ok:
                    text_item = QtWidgets.QGraphicsTextItem(text)
                    text_item.setPos(self.begin)
                    text_item.setDefaultTextColor(QtGui.QColor(self.pen.color()))
                    self.add_item(text_item)
            elif self.tool == "eraser":
                eraser_rect = QtCore.QRectF(self.end.x() - 5, self.end.y() - 5, 10, 10)
                items = self.scene().items(eraser_rect)  # Find items intersecting with the eraser cursor
                for item in items:
                    if isinstance(item, QtWidgets.QGraphicsItem):  # Ensure it's a graphics item
                        self.scene().removeItem(item)  # Remove the item
            else:
                print("nothing to draw!")

    def mouseDoubleClickEvent(self, event):
        if self.tool == "polygon":
            if len(self.vertices) > 2:  # Need at least 3 points to form a polygon
                polygon = QtWidgets.QGraphicsPolygonItem(QtGui.QPolygonF(self.vertices))
                polygon.setPen(self.pen)
                polygon.setBrush(self.brush)
                self.add_item(polygon)
                self.vertices = []
                self.remove_temp_polygon()

    def update_temp_polygon(self):
        if self.temp_polygon:
            self.scene().removeItem(self.temp_polygon)
        if len(self.vertices) > 1:
            self.temp_polygon = QtWidgets.QGraphicsPolygonItem(QtGui.QPolygonF(self.vertices))
            self.temp_polygon.setPen(self.pen)
            self.temp_polygon.setBrush(self.brush)
            self.scene().addItem(self.temp_polygon)

    def remove_temp_polygon(self):
        if self.temp_polygon:
            self.scene().removeItem(self.temp_polygon)
            self.temp_polygon = None

    def resizeEvent(self, event):
        print("View.resizeEvent()")
        print("width : {}, height : {}".format(self.size().width(), self.size().height()))