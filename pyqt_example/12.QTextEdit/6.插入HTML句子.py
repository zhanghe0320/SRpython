from PyQt5.Qt import *  # 刚开始学习可以这样一下导入
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit的学习")
        self.resize(400, 400)
        self.set_ui()

    def set_ui(self):
        self.textEdit = QTextEdit(self)
        self.textEdit.move(50, 50)
        self.textEdit.resize(300, 300)
        self.textEdit.setStyleSheet("background-color:cyan;")

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(0, 300)
        self.setup_conent()
        self.cursor_object()

    def setup_conent(self):
        # self.textEdit.setText("hhhhhhhh")
        # self.textEdit.append("Hello world")
        pass

    ############################文本光标对象方法之插入句子###############################
    def cursor_object(self):
        # QTextCursor   #它的对象方法，编辑器不能很好识别，需要我们自己点进去去找
        QTextCursor
        cursor_obj = self.textEdit.textCursor()

        ############################QTextDocumentFragment 的使用###############################
        textDocumentFragment = QTextDocumentFragment.fromHtml("<h1>hello</h1>")
        # 这里要注意的是，虽然 fromHtml 的说明中是个self 但是它是个类方法，直接可以用类名调用

        # textDocumentFragment = QTextDocumentFragment.fromPlainText("<h1>hello</h1>")
        ############################QTextDocumentFragment 的使用###############################

        cursor_obj.insertFragment(textDocumentFragment)

    ############################文本光标对象方法之插入句子###############################


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())