import unittest

from PySide6.QtWidgets import QApplication, QPushButton

from app.hub.navigation import Navigation


class NavigationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.application = QApplication.instance() or QApplication([])

    def setUp(self):
        self.navigation = Navigation()

    def test_project_cards_open_pages_and_back_buttons_return_home(self):
        self.assertIs(self.navigation.currentWidget(), self.navigation.home_page)
        self.assertEqual(self.navigation.count(), 3)

        gravity_button = next(
            button
            for button in self.navigation.home_page.findChildren(QPushButton)
            if button.text() == "Open Gravity Simulation"
        )
        gravity_button.click()
        self.assertIs(self.navigation.currentWidget(), self.navigation.gravity_page)

        self.navigation.gravity_page.findChild(QPushButton).click()
        self.assertIs(self.navigation.currentWidget(), self.navigation.home_page)

        calculator_button = next(
            button
            for button in self.navigation.home_page.findChildren(QPushButton)
            if button.text() == "Open Calculator"
        )
        calculator_button.click()
        self.assertIs(
            self.navigation.currentWidget(), self.navigation.calculator_page
        )

        self.navigation.calculator_page.findChild(QPushButton).click()
        self.assertIs(self.navigation.currentWidget(), self.navigation.home_page)