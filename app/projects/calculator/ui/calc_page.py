from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class CalculatorPage(QWidget):
    back_requested = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 40)
        layout.setSpacing(20)

        title = QLabel("Calculator")
        title.setObjectName("title")
        description = QLabel(
            "Perform mathematical operations including calculus, linear algebra, "
            "physics, and unit conversions."
        )
        description.setObjectName("subtitle")
        description.setWordWrap(True)

        back_button = QPushButton("Back to projects")
        back_button.clicked.connect(self.back_requested.emit)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()
        layout.addWidget(back_button)