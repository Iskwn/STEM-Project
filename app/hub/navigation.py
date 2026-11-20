from PySide6.QtWidgets import QStackedWidget

from app.hub.home_page import HomePage
from app.projects.calculator.ui.calc_page import CalculatorPage
from app.projects.gravity.ui.grav_page import GravityPage


class Navigation(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.home_page = HomePage()
        self.gravity_page = GravityPage()
        self.calculator_page = CalculatorPage()

        self.addWidget(self.home_page)
        self.addWidget(self.gravity_page)
        self.addWidget(self.calculator_page)
        self.setCurrentWidget(self.home_page)

        self.home_page.gravity_requested.connect(self.show_gravity)
        self.home_page.calculator_requested.connect(self.show_calculator)
        self.gravity_page.back_requested.connect(self.show_home)
        self.calculator_page.back_requested.connect(self.show_home)

    def show_home(self):
        self.setCurrentWidget(self.home_page)

    def show_gravity(self):
        self.setCurrentWidget(self.gravity_page)

    def show_calculator(self):
        self.setCurrentWidget(self.calculator_page)