import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from pol import *
import numpy as np

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()


def pol_coz():
    a = int(ui.lineEdit.text())
    b = int(ui.lineEdit_4.text())
    c = int(ui.lineEdit_7.text())
    d = int(ui.lineEdit_10.text())
    e = int(ui.lineEdit_2.text())
    f = int(ui.lineEdit_5.text())
    g = int(ui.lineEdit_8.text())
    h = int(ui.lineEdit_11.text())
    i = int(ui.lineEdit_3.text())
    j = int(ui.lineEdit_6.text())
    k = int(ui.lineEdit_9.text())
    m = int(ui.lineEdit_12.text())

    x = np.array([[a, b, c], [e, f, g], [i, j, k]])
    y = np.array([d, h, m])
    z = np.linalg.solve(x, y)
    ui.lineEdit_13.setText("x0 =  " + str(z[0]) + "   x1 = " + str(z[1]) + "   x2 =  " + str(z[2]))



ui.pushButton.clicked.connect(pol_coz)

sys.exit(app.exec_())
