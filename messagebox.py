from PyQt5.QtWidgets import QMessageBox

def msg_about(tittle, message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle(tittle)
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        pass

def msg_error(tittle, message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setWindowTitle(tittle)
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        pass