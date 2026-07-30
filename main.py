import sys

from PySide6.QtWidgets import QApplication

from app.hub.main_window import MainWindow

def main():
    # Initialize App
    app = QApplication(sys.argv)
    
    # Create and display the main window
    window = MainWindow()
    window.show()
    
    # Start app event loop
    sys.exit(app.exec())
    
    
if __name__ == "__main__":
    main()