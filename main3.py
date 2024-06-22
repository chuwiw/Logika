from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, 

app = QApplication([])

main_wind = QWidget()
main_wind.setWindowTitle("Конкурс від Crazy People")
main_wind.resize(400,200)

question = QLabel("Коли придумали Python 3000?")

btn1 = QRadioButton("2005")
btn2 = QRadioButton("2010")
btn3 = QRadioButton("2015")
btn4 = QRadioButton("2003")

main_layout = QVBoxLayout()

layoutH1 = QVBoxLayout()
layoutH2 = QVBoxLayout()
layoutH3 = QVBoxLayout()


layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn4, alignment=Qt.AlignCenter)

main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)

main_wind.setLayout(main_layout)
main_wind.show()
app.exec_()
