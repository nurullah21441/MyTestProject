import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout, 
                           QHBoxLayout, QWidget, QPushButton, QFileDialog, QLabel,
                           QMessageBox, QStatusBar)
from PyQt6.QtGui import QIcon, QFont, QPalette, QColor
from PyQt6.QtCore import Qt
import os

class GitignoreEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Ana pencere ayarları
        self.setWindowTitle('.gitignore Editor')
        self.setGeometry(100, 100, 800, 600)
        # Uygulama ikonu
        if os.path.exists('icon.ico'):
            self.setWindowIcon(QIcon('icon.ico'))
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QTextEdit {
                background-color: #1e1e1e;
                color: #ffffff;
                border: 1px solid #3c3c3c;
                border-radius: 5px;
                padding: 5px;
                font-family: 'Consolas';
                font-size: 12px;
            }
            QPushButton {
                background-color: #0d47a1;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 4px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton:hover {
                background-color: #1565c0;
            }
            QLabel {
                color: #ffffff;
                font-size: 14px;
            }
            QStatusBar {
                color: #ffffff;
                background-color: #1e1e1e;
            }
        """)

        # Ana widget ve layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Başlık
        title_label = QLabel('.gitignore Editor', self)
        title_label.setStyleSheet('font-size: 24px; font-weight: bold; margin: 10px;')
        layout.addWidget(title_label)

        # Buton container
        button_layout = QHBoxLayout()
        
        # Dosya açma butonu
        self.open_btn = QPushButton('Dosya Aç', self)
        self.open_btn.clicked.connect(self.open_file)
        button_layout.addWidget(self.open_btn)
        
        # Kaydetme butonu
        self.save_btn = QPushButton('Kaydet', self)
        self.save_btn.clicked.connect(self.save_file)
        button_layout.addWidget(self.save_btn)
        
        # Yeni dosya butonu
        self.new_btn = QPushButton('Yeni', self)
        self.new_btn.clicked.connect(self.new_file)
        button_layout.addWidget(self.new_btn)
        
        layout.addLayout(button_layout)
        
        # Metin editörü
        self.editor = QTextEdit()
        self.editor.setPlaceholderText("# .gitignore dosyanızı buraya yazın...")
        layout.addWidget(self.editor)
        
        # Durum çubuğu
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage('Hazır')
        
        self.current_file = None
        
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Dosya Aç', '', 
                                                 '.gitignore Files (*.gitignore);;All Files (*)')
        
        if file_name:
            try:
                with open(file_name, 'r') as f:
                    self.editor.setText(f.read())
                self.current_file = file_name
                self.statusBar.showMessage(f'Dosya açıldı: {file_name}')
            except Exception as e:
                QMessageBox.critical(self, 'Hata', f'Dosya açılırken hata oluştu: {str(e)}')
                
    def save_file(self):
        if not self.current_file:
            file_name, _ = QFileDialog.getSaveFileName(self, 'Dosyayı Kaydet', '', 
                                                     '.gitignore Files (*.gitignore);;All Files (*)')
            if not file_name:
                return
            self.current_file = file_name
            
        try:
            with open(self.current_file, 'w') as f:
                f.write(self.editor.toPlainText())
            self.statusBar.showMessage(f'Dosya kaydedildi: {self.current_file}')
        except Exception as e:
            QMessageBox.critical(self, 'Hata', f'Dosya kaydedilirken hata oluştu: {str(e)}')
            
    def new_file(self):
        if self.editor.toPlainText().strip():
            reply = QMessageBox.question(self, 'Yeni Dosya',
                                       'Mevcut içerik kaybolacak. Devam etmek istiyor musunuz?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                return
                
        self.editor.clear()
        self.current_file = None
        self.statusBar.showMessage('Yeni dosya oluşturuldu')

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern görünüm
    editor = GitignoreEditor()
    editor.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main() 