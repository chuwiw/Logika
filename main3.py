from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox, QHBoxLayout


def win():
    victory_win = QMessageBox()
    victory_win.setText("Ти вгадав")
    victory_win.exec_()

def lose():
    loose = QMessageBox()
    loose.setText("Ти не вгадав")
    loose.exec_()


app = QApplication([])

main_wind = QWidget()
main_wind.setWindowTitle("Конкурс від BuzzFeed")
main_wind.resize(400,200)

question = QLabel("Коли створили гру Genshin Impact")

btn1 = QRadioButton("2018")
btn2 = QRadioButton("2019")
btn3 = QRadioButton("2020")
btn4 = QRadioButton("2021")

main_layout = QVBoxLayout()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()


layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn4, alignment=Qt.AlignCenter)

main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)

btn1.clicked.connect(lose)
btn2.clicked.connect(lose)
btn3.clicked.connect(win)
btn4.clicked.connect(lose)


main_wind.setLayout(main_layout)
main_wind.show()
app.exec_()
