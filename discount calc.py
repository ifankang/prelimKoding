from PySide6.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowTitle("Discount Calculator")

price_input = QLineEdit()
discount_input = QLineEdit()

result_label = QLabel("Final Price: ")

button = QPushButton("Calculate")

def calculate():
    price = float(price_input.text())
    discount = float(discount_input.text())

    final_price = price * (1 - discount / 100)

    result_label.setText(
        f"Final Price: Rp {final_price:,.0f}"
    )

button.clicked.connect(calculate)

layout = QVBoxLayout()

layout.addWidget(QLabel("Price"))
layout.addWidget(price_input)

layout.addWidget(QLabel("Discount (%)"))
layout.addWidget(discount_input)

layout.addWidget(button)
layout.addWidget(result_label)

window.setLayout(layout)

window.show()

app.exec()