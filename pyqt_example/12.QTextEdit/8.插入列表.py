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

    ############################文本光标对象方法之插入列表###############################
    def cursor_object(self):
        # QTextCursor   #它的对象方法，编辑器不能很好识别，需要我们自己点进去去找
        QTextCursor
        cursor_obj = self.textEdit.textCursor()

        QTextListFormat
        textListFormat = QTextListFormat()
        ############################QTextListFormat  的设置###############################
        textListFormat.setIndent(3)  # 缩进三个tab

        textListFormat.setStyle(QTextListFormat.ListDecimal)  # 数字
        textListFormat.setNumberPrefix("<")  # 前缀  注：前缀和后缀是配合数字使用的，其他样式不行
        textListFormat.setNumberSuffix(">")  # 后缀

        ############################QTextListFormat  的设置###############################

        cursor_obj.createList(textListFormat)

    ############################文本光标对象方法之插入列表###############################


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())