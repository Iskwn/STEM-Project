from collections.abc import Callable

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class HomePage(QWidget):
    gravity_requested = Signal()
    calculator_requested = Signal()

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(40, 30, 40, 40)
        main_layout.setSpacing(25)

        title = QLabel("STEM Project")
        title.setObjectName("title")

        subtitle = QLabel(
            "Interactive tools and visualizations for math, "
            "science, engineering, and more."
        )
        subtitle.setObjectName("subtitle")
        subtitle.setWordWrap(True)

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        project_grid = QGridLayout()
        project_grid.setSpacing(20)
        project_grid.addWidget(
            self.create_project_card(
                "Gravity Simulation",
                "Explore gravity, orbital mechanics, and astrophysics "
                "through interactive simulations.",
                "Open Gravity Simulation",
                self.gravity_requested.emit,
            ),
            0,
            0,
        )
        project_grid.addWidget(
            self.create_project_card(
                "Calculator",
                "Perform complex mathematical operations including calculus, "
                "linear algebra, physics, unit conversions, and more.",
                "Open Calculator",
                self.calculator_requested.emit,
            ),
            0,
            1,
        )
        project_grid.addWidget(
            self.create_project_card(
                "Coming Soon",
                "Additional simulations and interactive tools will appear here.",
                "Learn More",
                None,
            ),
            1,
            0,
            1,
            2,
        )

        main_layout.addLayout(project_grid)
        main_layout.addStretch()

    @staticmethod
    def create_project_card(
        title: str,
        description: str,
        button_text: str,
        callback: Callable[[], None] | None,
    ) -> QFrame:
        card = QFrame()
        card.setObjectName("projectCard")
        card.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(25, 25, 25, 25)
        card_layout.setSpacing(12)

        card_title = QLabel(title)
        card_title.setObjectName("cardTitle")
        card_title.setWordWrap(True)

        card_description = QLabel(description)
        card_description.setObjectName("cardDescription")
        card_description.setWordWrap(True)

        card_button = QPushButton(button_text)
        card_button.setObjectName("card_button")
        if callback is None:
            card_button.setEnabled(False)
        else:
            card_button.clicked.connect(callback)

        card_layout.addWidget(card_title)
        card_layout.addWidget(card_description)
        card_layout.addStretch()
        card_layout.addWidget(card_button)
        return card
