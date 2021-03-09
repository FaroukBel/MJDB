import matplotlib
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.ticker import (
    FuncFormatter,
)

matplotlib.use('Qt5Agg')


class MplCanvas(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MplCanvas, self).__init__(parent)
        self.figure = plt.figure(1)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.x = plt
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.yaxis.set_major_formatter(FuncFormatter(lambda x, p: format(x / 1000000) + 'M'))
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # creating a window object
    main = MplCanvas()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
