import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import PyQt5.QtCore as core
from PyQt5.QtGui import QFont,QIcon
from eediter import Ui_Form
from cryptography.fernet import Fernet
import base64
import hashlib

class Eediter(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		saveFile = QAction("Save File", self)
		saveFile.setShortcut("Ctrl+S")
		saveFile.triggered.connect(self.slot1_save)
		self.addAction(saveFile)
		loadFile = QAction("Load File", self)
		loadFile.setShortcut("Ctrl+O")
		loadFile.triggered.connect(self.slot2_load)
		self.addAction(loadFile)
		if len(sys.argv) >= 2:
			self.load(sys.argv[1])
		self.setWindowIcon(QIcon('lib/icon.png'))
		self.show()

	def load(self, filename):
		if filename == "":
			return
		elif filename.split(".")[-1] != "iml":
			err = QMessageBox()
			err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .iml file)")
			return
		f = open(filename, 'rb')
		data = f.read()
		try:
			data = decrypt(data)
		except:
			err = QMessageBox()
			err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .iml file)")
			return
		f.close()
		self.edit.clear()
		self.edit.setPlainText(data)
		self.setWindowTitle("IML Encryption Editor - " + filename)

	def wheelEvent(self, e):
		modifiers = QApplication.keyboardModifiers()
		if modifiers == core.Qt.ControlModifier:
			if e.angleDelta().y() > 0:
				self.edit.zoomIn()
			else:
				self.edit.zoomOut()

	@pyqtSlot()
	def slot1_save(self):
		txt = self.edit.toPlainText()
		txt = encrypt(txt)
		if self.windowTitle().split(" ")[-1] == "New":
			filename = QFileDialog.getSaveFileName(self,"Save File","*.iml",\
			"Ecrypted File (*.iml)")
			if filename[0] == "":
				return
		else:
			filename = [self.windowTitle().split(" ")[-1], None]
		f= open(filename[0],'wb')
		f.write(txt)
		f.close()
		self.setWindowTitle("IML Encryption Editor - " + filename[0])

	@pyqtSlot()
	def slot2_load(self):
		filename = QFileDialog.getOpenFileName()
		if filename[0] == "":
			return
		elif filename[0].split(".")[-1] != "iml":
			err = QMessageBox()
			err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .iml file)")
			return
		f = open(filename[0], 'rb')
		data = f.read()
		try:
			data = decrypt(data)
		except:
			err = QMessageBox()
			err.about(self, "Load Error", "열 수 없는 파일 포맷입니다.(only .iml file)")
			return
		f.close()
		self.edit.clear()
		self.edit.setPlainText(data)
		self.setWindowTitle("IML Encryption Editor - " + filename[0])
		
def encrypt(txt):
	m = hashlib.sha256()
	m.update(b"It's My Life gAAAAABcFrn86Xex6rnweeNcI4iTcocmBpqBqpUS_pd7trjHMlUWxNYEWGokEZNrafqDqTZFBWTzHj4f49U5pH-sfak_edLFYg==")
	key = base64.urlsafe_b64encode(m.digest())
	txt = bytes(txt, 'utf-8')
	cipher_suite = Fernet(key)
	return cipher_suite.encrypt(txt)

def decrypt(enc):
	m = hashlib.sha256()
	m.update(b"It's My Life gAAAAABcFrn86Xex6rnweeNcI4iTcocmBpqBqpUS_pd7trjHMlUWxNYEWGokEZNrafqDqTZFBWTzHj4f49U5pH-sfak_edLFYg==")
	key = base64.urlsafe_b64encode(m.digest())
	cipher_suite = Fernet(key)
	decoded_text = cipher_suite.decrypt(enc)
	return decoded_text.decode('utf-8')

app = QApplication(sys.argv)
ex = Eediter()
sys.exit(app.exec_())
