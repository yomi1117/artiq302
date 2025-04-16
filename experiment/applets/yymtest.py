import sys
import random
import time
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class RandomSequenceDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.stop_flag = False
        self.display_thread = threading.Thread(target=self.display_random_sequence)
        self.display_thread.start()

    def initUI(self):
        self.label = QLabel("等待随机序列...", self)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('随机序列显示')
        self.show()

    def display_random_sequence(self):
        while not self.stop_flag:
            random_num = random.randint(1, 100)
            self.label.setText(str(random_num))
            QApplication.processEvents()
            time.sleep(1)

    def closeEvent(self, event):
        self.stop_flag = True
        self.display_thread.join()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RandomSequenceDisplay()
    sys.exit(app.exec_())
    