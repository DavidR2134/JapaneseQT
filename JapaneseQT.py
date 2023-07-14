import sys
import random
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QLabel, QPushButton, QGridLayout, QWidget, QAction, QLineEdit
from PyQt5.QtCore import QTimer, Qt, pyqtSlot
from PyQt5.QtGui import QIcon, QFont

#Global Variables
HIRAGANA = ['わ','ら','や','ま','は','な','た','さ','か','あ','り','み','ひ','に','ち','し','き','い'
            ,'る','ゆ','む','ふ','ぬ','つ','す','く','う','ん','れ','め','へ','ね','て','せ','け','え'
            ,'を','ろ','よ','も','ほ','の','と','そ','こ','お','ぱ','ば','だ','ざ','が','ぴ','び','ぢ','じ','ぎ'
            ,'ぷ','ぶ','づ','ず','ぐ','ぺ','べ','で','ぜ','げ','ぽ','ぼ','ど','ぞ','ご']

KATAKANA = ['ワ','ラ','ヤ','マ','ハ','ナ','タ','サ','カ','ア','リ','ミ','ヒ','ニ','チ','シ','キ','イ'
            ,'ル','ユ','ム','フ','ヌ','ツ','ス','ク','ウ','ン','レ','メ','ヘ','ネ','テ','セ','ケ','エ'
            ,'ヲ','ロ','ヨ','モ','ホ','ノ','ト','ソ','コ','オ','パ','バ','ダ','ザ','ガ','ピ','ビ','ヂ','ジ','ギ'
            ,'プ','ブ','ヅ','ズ','グ','ペ','ベ','デ','ゼ','ゲ','ポ','ボ','ド','ゾ','ゴ']

SOUNDS = ['wa','ra','ya','ma','ha','na','ta','sa','ka','a','ri','mi','hi','ni','chi','shi','ki','i'
            ,'ru','yu','mu','fu/hu','nu','tsu','su','ku','u','n','re','me','he','ne','te','se','ke','e'
            ,'wo','ro','yo','mo','ho','no','to','so','ko','o','pa','ba','da','za','ga','pi','bi','dzi','ji','gi'
            ,'pu','bu','dzu','zu','gu','pe','be','de','ze','ge','po','bo','do','zo','go']




class JapaneseLesson(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Learn Japanese!! - こにちわ！！")
        self.setGeometry(1500,500,400,200)
        self.hiragana = HIRAGANA
        self.katakana = KATAKANA
        self.sounds = SOUNDS
        self.counter = 0
        self.correct = 0
        self.incorrect = 0



        #Create Hiragana / Katakana label
        self.index = random.randint(0, len(self.hiragana) - 1)
        self.japanese_label = QLabel(self.hiragana[self.index], self)
        print(self.sounds[self.index])
        self.japanese_label.setStyleSheet("border: 1px solid black;")
        self.japanese_label.setFont(QFont('Arial', 24))
        self.japanese_label.setAlignment(Qt.AlignCenter)

        self.correct_label = QLabel("Correct: " + str(self.correct), self)
        self.correct_label.setFont(QFont('Arial', 12))
        
        self.incorrect_label = QLabel("Incorrect: " + str(self.incorrect), self)
        self.incorrect_label.setFont(QFont('Arial', 12))


        #Create Text Box
        self.textbox = QLineEdit(self)

        #Create Button
        self.button = QPushButton('Show Answer', self)
        self.button.setFont(QFont('Arial', 11))

        #Connect button to function on_click
        self.button.clicked.connect(self.on_click)

        layout = QGridLayout()
        layout.addWidget(self.correct_label, 0, 0)
        layout.addWidget(self.incorrect_label, 1, 0)
        layout.addWidget(self.japanese_label, 0, 1)
        layout.addWidget(self.textbox, 1, 1)
        layout.addWidget(self.button, 2, 1)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_labels(self):
        self.correct_label.setText(f"Correct: {str(self.correct)}")
        self.incorrect_label.setText(f"Incorrect: {str(self.incorrect)}")

    def on_click(self):
        textboxValue = self.textbox.text()
        
        if textboxValue.lower() == self.sounds[self.index]:    
            self.japanese_label.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
            QMessageBox.question(self, 'Correct!', "You're Right!", QMessageBox.Ok)
            self.textbox.setText("")
            self.japanese_label.setStyleSheet("border: 1px solid black;")
            self.correct += 1
            self.counter += 1
            self.change_character()

        elif textboxValue.lower() != self.sounds[self.index] and textboxValue != "":
            self.japanese_label.setStyleSheet("background-color: lightcoral; border: 1px solid black;")
            QMessageBox.question(self, "Wrong!", f"You got it wrong you ding dong! The correct answer was '{self.sounds[self.index]}'", QMessageBox.Ok)
            self.textbox.setText("")
            self.japanese_label.setStyleSheet("border: 1px solid black;")
            self.incorrect += 1
            self.counter += 1
            self.change_character()
        else:
            self.japanese_label.setStyleSheet("background-color: aqua; border: 1px solid black;")
            QMessageBox.information(self,"Invalid Input", "Please enter a valid sound.", QMessageBox.Ok)
            self.japanese_label.setStyleSheet("border: 1px solid black;")

        self.update_labels()

        print(f"Correct: {self.correct}\nIncorrect: {self.incorrect}\nCounter: {self.counter}")


    def change_character(self):
        character_set = random.randint(0,1)
        self.index = random.randint(0, len(self.hiragana) - 1)
        
        if character_set == 1:
            self.japanese_label.setText(self.katakana[self.index])
        else:
            self.japanese_label.setText(self.hiragana[self.index])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JapaneseLesson()
    window.show()
    sys.exit(app.exec_())