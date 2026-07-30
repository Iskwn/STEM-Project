from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QWidget,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("STEM Project")
        self.resize(1200, 750)
        self.setMinimumSize(800, 600)
        
        # Create central widget
        central_widget = QWidget()
        
        # Place central widget in window
        self.setCentralWidget(central_widget)
        
        # Main Vertical Layout
        main_layout = QVBoxLayout(central_widget)
        
        main_layout.setContentsMargins(40, 30, 40, 40)
        main_layout.setSpacing(25)
        
        # ----- HEADER -----
        
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
        
        # ----- Project Cards -----
        project_grid = QGridLayout()
        project_grid.setSpacing(20)
        
        gravity_card = self.create_project_card(
            title = "Gravity Simulation",
            description = (
                "Explore gravity, orbital mechanics, "
                "and astrophysics through interactive simulations."
            ),
            button_text = "Open Gravity Simulation",
            callback = self.open_gravity_simulation
        )
        
        calculator_card = self.create_project_card(
            title = "Calculator",
            description = (
                "Perform complex mathematical operations including calculus, linear algebra, "
                "physics, unit conversions, and more."
            ),
            button_text = "Open Calculator",
            callback = self.open_calculator
        )

        coming_soon_card = self.create_project_card(
            title = "Coming Soon",
            description = (
                "Additional simulations and interactive "
                "tools will appear here."
            ),
            button_text = "Learn More",
            callback = None
        )
        
        project_grid.addWidget(gravity_card, 0, 0)
        project_grid.addWidget(calculator_card, 0, 1)
        project_grid.addWidget(coming_soon_card, 1, 0, 1, 2)
        
        main_layout.addLayout(project_grid)
        
        # Pushes the cards toward the top instead of stretching them across the window
        main_layout.addStretch()
        
        # Temp stylesheet
        self.apply_styles()
    
    def create_project_card(
        self,
        title: str,
        description: str,
        button_text: str,
        callback
    ) -> QFrame:
        '''
        Creates and returns a project card.
        '''
        
        card = QFrame()
        card.setObjectName("projectCard")

        # Card layout
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(25, 25, 25, 25)
        card_layout.setSpacing(12)

        # Card title
        card_title = QLabel(title)
        card_title.setObjectName("cardTitle")
        card_title.setWordWrap(True)

        # Card description
        card_description = QLabel(description)
        card_description.setObjectName("cardDescription")
        card_description.setWordWrap(True)

        # Card button
        card_button = QPushButton(button_text)
        card_button.setObjectName("card_button")
        if callback:
            card_button.clicked.connect(callback)
        else:
            card_button.setEnabled(False)
            
        # Add widgets to card layout
        card_layout.addWidget(card_title)
        card_layout.addWidget(card_description)
        card_layout.addStretch()
        card_layout.addWidget(card_button)

        return card
    
    def open_gravity_simulation(self):
        '''
        Placeholder
        Will later open the gravity simulation.
        '''
        print("Opening gravity simulation...")

    def open_calculator(self):
        '''
        Placeholder
        Will later open the calculator.
        '''
        print("Opening calculator...")
    
    def apply_styles(self):
        '''
        Temp application styling
        Will later be moved into app/ui/themes/dark.qss
        '''
        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #15171c;
            }
            
            QLabel {
                color: #e8eaf0;
            }
            
            QLabel#title {
                font-size: 42px;
                font-weight: 700;
            }
            
            QLabel#subtitle {
                color: #a9afbb;
                font-size: 17px;
            }
            
            QFrame#projectCard {
                background-color: #20242c;
                border: 1px solid #343a46;
                border-radius: 14px;
            }
            
            QFrame#projectCard:hover {
                border: 1px solid #5d78c7;
            }
            
            QLabel#cardTitle {
                font-size: 24px;
                font-weight: 600;
            }
            
            QLabel#cardDescription {
                color: #aeb5c2;
                font-size: 14px;
            }
            
            QPushButton {
                background-color: #3d5fa8;
                border: none;
                border-radius: 8px;
                color: white;
                font-size: 14px;
                font-weight: 600;
                padding: 11px 16px;
            }
            
            QPushButton:hover {
                background-color: #4b70bf;
            }
            
            QPushButton:pressed {
                background-color: #304c87;
            }
            
            QPushButton:disabled {
                background-color: #343842;
                color: #777d89;
            }
            """
        )
        