import sys
from unicodedata import name
from PyQt5.QtCore import*
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit
import pyperclip


class yxhscq(QWidget):
    def __init__(self):
        super(yxhscq,self).__init__()
        self.initUi()

    def initUi(self):

        global JieGuoLabel
        self.setWindowTitle("营销号生成器")
        layout = QGridLayout()
        self.setGeometry(500, 200, 900, 800)


        ZhuTiLabel = QLabel("事件")
        self.ZhuTi = QLineEdit("")
        YuanYinLabel = QLabel("原因")
        self.YuanYin = QLineEdit("")
        JieGuoLabel = QLineEdit("结果")
        JieGuoLabel.setText('结果将输出在这里')
        FuZhi = QPushButton('复制')
        yes_btn = QPushButton('确定')
        no_btn = QPushButton('关闭')

        layout.addWidget(ZhuTiLabel,1,0)
        layout.addWidget(self.ZhuTi,1,1)
        layout.addWidget(YuanYinLabel, 2, 0)
        layout.addWidget(self.YuanYin, 2, 1)
        layout.addWidget(FuZhi,3,0)
        layout.addWidget(JieGuoLabel,3,1)
        layout.setColumnStretch(1, 10)


        #链接单击各按钮后的函数
        no_btn.clicked.connect(QCoreApplication.quit)
        yes_btn.clicked.connect(self.QueDing)
        FuZhi.clicked.connect(self.Copy)
        
        layout.addWidget(yes_btn)
        layout.addWidget(no_btn)
        self.setLayout(layout)

    def QueDing(self):
        global a
        ZhuTi = self.ZhuTi.text()
        YuanYin = self.YuanYin.text()
        # print('%s到底是怎么回事呢？%s相信大家都很震惊，但是%s到底是怎么回事呢，下面就让小编带大家一起了解吧。%s，其实就是%s，大家可能会很惊讶%s。但事实就是这样，小编也感到非常惊讶。这就是关于%s的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'%(ZhuTi,ZhuTi,ZhuTi,ZhuTi,YuanYin,ZhuTi,ZhuTi))
        a = '%s到底是怎么回事呢？%s相信大家都很震惊，但是%s到底是怎么回事呢，下面就让小编带大家一起了解吧。%s，其实就是%s，大家可能会很惊讶%s。但事实就是这样，小编也感到非常惊讶。这就是关于%s的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'%(ZhuTi,ZhuTi,ZhuTi,ZhuTi,YuanYin,ZhuTi,ZhuTi)
        # print(a)
        
        JieGuoLabel.setText(a)
    def Copy(self):
        pyperclip.copy(a)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = yxhscq()
    win.show()
    sys.exit(app.exec_())