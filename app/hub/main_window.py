from pathlib import Path

from PySide6.QtWidgets import QMainWindow

from app.hub.navigation import Navigation


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("STEM Project")
        self.resize(1200, 750)
        self.setMinimumSize(800, 600)

        self.navigation = Navigation()
        self.setCentralWidget(self.navigation)

        self.theme = "light"
        self.apply_styles()

    def apply_styles(self, theme: str | None = None):
        selected_theme = self.theme if theme is None else theme
        if not selected_theme or Path(selected_theme).name != selected_theme:
            raise ValueError("Theme must be a filename without a path.")

        themes_dir = Path(__file__).resolve().parent.parent / "ui" / "themes"
        stylesheet_path = themes_dir / f"{selected_theme}.qss"
        stylesheet = stylesheet_path.read_text(encoding="utf-8")
        self.setStyleSheet(stylesheet)
        self.theme = selected_theme
