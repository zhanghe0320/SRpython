from PyQt5.Qt import * #刚开始学习可以这样一下导入
import sys
#1,创建app
app  = QApplication(sys.argv)


#2，控件的操作：
#创建控件
window = QWidget()

#设置控件
window.setWindowTitle("光标")
window.resize(500,500)

lineEdit = QLineEdit(window)
lineEdit.move(100,100)
lineEdit.resize(200,100)

lineEdit.setStyleSheet("background-color:cyan;")

#水平靠右  垂直靠下
lineEdit.setAlignment(Qt.AlignRight|Qt.AlignBottom)
lineEdit.setTextMargins(0,0,5,5)  #配合使用   让它不太靠角落

def btn_clicked_slot():
      lineEdit.setFocus()

btn = QPushButton(window)
btn.setText("按钮")
btn.move(0,300)
btn.clicked.connect(btn_clicked_slot)

#展示控件
window.show()

#3,进入消息循环
sys.exit(app.exec_())