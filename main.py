import sys
from PyQt5 import QtCore,QtGui,QtWidgets

from view import View
from window import Window

print(QtCore.QT_VERSION_STR)
app=QtWidgets.QApplication(sys.argv)

position=0,0
dimension=5000,1000
mw=Window(position,dimension)
mw.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowFullscreenButtonHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowStaysOnTopHint)
mw.show()

sys.exit(app.exec_())
