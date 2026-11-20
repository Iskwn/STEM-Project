# Application UI

`app/hub/main_window.py` provides the top-level window and hosts the `Navigation`
stack. `app/hub/navigation.py` registers the home page and project pages and
switches between them.

Each page owns its UI in a separate module:

- `app/hub/home_page.py` contains the project launcher.
- `app/projects/gravity/ui/grav_page.py` contains the gravity page.
- `app/projects/calculator/ui/calc_page.py` contains the calculator page.

Project pages signal when the user requests navigation; the navigation stack
handles page switching and returning to the home page.