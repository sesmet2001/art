import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class PixelValueViewer(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        self.image_path = image_path

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Pixel Value Viewer')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        self.pixel_value_label = QLabel(self)
        layout.addWidget(self.pixel_value_label)

        central_widget.setLayout(layout)

        self.load_image()

    def load_image(self):
        pixmap = QPixmap(self.image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignTop)

        self.image = pixmap.toImage()

    def mouseMoveEvent(self, event):
        if event.x() < 0 or event.y() < 0 or event.x() >= self.image.width() or event.y() >= self.image.height():
            return

        pixel_color = self.image.pixelColor(event.x(), event.y())
        pixel_value_int = round((pixel_color.red() + pixel_color.green() + pixel_color.blue()) / 3, 0)
        pixel_value = f"RGB: " + str(pixel_value_int)
        #pixel_value = f"RGB: ({pixel_color.red()}, {pixel_color.green()}, {pixel_color.blue()})"
        self.pixel_value_label.setText(pixel_value)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python pixel_value_viewer.py image_path")
        sys.exit(1)

    image_path = sys.argv[1]

    app = QApplication(sys.argv)
    viewer = PixelValueViewer("pepe.png")
    viewer.show()
    sys.exit(app.exec_())

