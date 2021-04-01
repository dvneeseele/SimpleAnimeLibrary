import sys
from PyQt5.QtWidgets import QApplication
from sal import SAL_app

application = QApplication(sys.argv)
application.setStyleSheet(open("qss/SyNet/SyNet.qss", "r").read())
# application.setStyleSheet(open("qss/Obit/Obit.qss", "r").read())
# application.setStyleSheet(open("qss/DeepBox/DeepBox.qss", "r").read())
# application.setStyleSheet(open("qss/Combinear/Combinear.qss", "r").read())
application.setStyle('fusion')
SAL = SAL_app()
sys.exit(application.exec_())