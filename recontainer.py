import os
import sys
from subprocess import call
from PyQt5.QtCore import QFileInfo
from ffmpy3 import FFmpeg
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog, QMessageBox, QDesktopWidget, \
    QApplication


class Recontainer(QWidget):

    def __init__(self):
        super().__init__()

        self.default_dir = os.path.expanduser('~/Movies')

        self.setWindowTitle('Recontainer')
        self.setWindowIcon(QIcon('web.png'))
        self.setMinimumSize(700, 150)
        self.center()

        input_file_label = QLabel("<b>Input file:</b>", self)
        self.input_file_path_label = QLabel("", self)
        btn_input_file = QPushButton("Select .mov", self)
        btn_input_file.clicked.connect(self.open_file_dialog)

        output_file_label = QLabel("<b>Output file:</b>", self)
        self.output_file_path_label = QLabel("", self)
        btn_output_file = QPushButton("Select output .mp4", self)
        btn_output_file.clicked.connect(self.save_file_dialog)

        btn_recontain = QPushButton('Recontain', self)
        btn_recontain.clicked.connect(self.check_existing_then_recontain)

        layout = QGridLayout()

        layout.addWidget(input_file_label, 0, 0)
        layout.addWidget(self.input_file_path_label, 1, 0)
        layout.addWidget(btn_input_file, 2, 0)

        layout.addWidget(output_file_label, 0, 1)
        layout.addWidget(self.output_file_path_label, 1, 1)
        layout.addWidget(btn_output_file, 2, 1)

        layout.addWidget(btn_recontain, 3, 0, 1, 2)

        self.setLayout(layout)
        self.show()

    def open_file_dialog(self):
        filename = QFileDialog.getOpenFileName(self, "Select .mov", self.default_dir, 'Movie Files (*.mov)')
        if filename:
            self.input_file_path_label.setText(filename[0])  # filename path
            self.output_file_path_label.setText(self.change_extension(filename[0], 'mp4'))

    def save_file_dialog(self):
        # set default file
        if self.input_file_path_label.text() is not '':
            self.default_dir = self.change_extension(self.input_file_path_label.text(), 'mp4')

        filename = QFileDialog.getSaveFileName(self, "Select .mp4", self.default_dir, 'MP4 Files (*.mp4)')
        if filename:
            self.output_file_path_label.setText(filename[0])

    @staticmethod
    def change_extension(input_text, extension):
        extension_index = 0
        for i in range(0, len(input_text) - 1):  # find the . in the file path
            if input_text[i] == '.':
                extension_index = i
                break
        return input_text[:extension_index] + '.' + extension

    @staticmethod
    def get_parent_directory(input_text):
        slash_index = 0
        for i in range(len(input_text) - 1, 0, -1):  # find the last slash in the file path
            if input_text[i] == '/':
                slash_index = i
                break
        return input_text[:slash_index]

    def recontain(self):
        ff = FFmpeg(
            inputs={self.input_file_path_label.text(): '-y'},
            outputs={self.output_file_path_label.text(): '-c copy'}
        )
        ff.run_async()
        call(['open', self.get_parent_directory(self.output_file_path_label.text())])
        call(['open', self.output_file_path_label.text()])

    def check_existing_then_recontain(self):
        if not QFileInfo.exists(self.output_file_path_label.text()):
            self.recontain()
        else:
            result = QMessageBox.warning(self, "File exists",
                                         self.output_file_path_label.text() + " already exists. Overwrite?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                self.recontain()
            else:
                return

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Recontainer()

    sys.exit(app.exec_())