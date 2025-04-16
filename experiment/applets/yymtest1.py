import sys
import random
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class RandomSequenceLineChart(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = []
        self.stop_flag = False
        self.display_thread = threading.Thread(target=self.generate_random_sequence)
        self.display_thread.start()

    def initUI(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('随机序列折线图显示')
        self.show()

    def generate_random_sequence(self):
        while not self.stop_flag:
            random_num = random.randint(1, 100)
            self.data.append(random_num)
            self.update_plot()
            time.sleep(1)

    def update_plot(self):
        self.ax.clear()
        self.ax.plot(self.data)
        self.ax.set_xlabel('时间点')
        self.ax.set_ylabel('随机数')
        self.ax.set_title('随机序列折线图')
        self.canvas.draw()

    def closeEvent(self, event):
        self.stop_flag = True
        self.display_thread.join()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomSequenceLineChart()
    sys.exit(app.exec_())
    