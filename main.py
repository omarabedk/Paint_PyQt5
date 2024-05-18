import sys
from PyQt5 import QtCore,QtGui,QtWidgets

from view import View
from window import Window

print(QtCore.QT_VERSION_STR)
app=QtWidgets.QApplication(sys.argv)

position=0,0
dimension=8000,5000
mw=Window(position,dimension)

mw.show()

sys.exit(app.exec_())
