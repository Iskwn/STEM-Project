from PySide6.QtCore import Signal
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class GravityPage(QWidget):
    back_requested = Signal()

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 40)
        layout.setSpacing(20)

        title = QLabel("Gravity Simulation")
        title.setObjectName("title")
        description = QLabel(
            "Explore gravity, orbital mechanics, and astrophysics through "
            "interactive simulations."
        )
        description.setObjectName("subtitle")
        description.setWordWrap(True)

        back_button = QPushButton("Back to projects")
        back_button.clicked.connect(self.back_requested.emit)

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()
        layout.addWidget(back_button)