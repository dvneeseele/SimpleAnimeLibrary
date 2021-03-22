import sys
from PyQt5.QtWidgets import QApplication
from sal import SAL_app

application = QApplication(sys.argv)
#application.setStyleSheet(open("qss/app.qss", "r").read())
application.setStyle('fusion')
SAL = SAL_app()
sys.exit(application.exec_())