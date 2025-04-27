import Xlib
import Xlib.display
import json

class ProjectManager:
    def __init__(self, project_name):
        self.project_name = project_name
        self.window_data = []

    def get_open_windows(self):
        """Get details of all open windows using Xlib."""
        # Connect to the X server
        display = Xlib.display.Display()
        root = display.screen().root

        # Get a list of all windows on the display
        windows = root.query_tree().children
        self.window_data = []  # Clear the window data before appending new data
        for window in windows:
            # Get the window properties (title, position, size)
            window_info = {}
            try:
                app_name = window.get_wm_name()  # Window title
                # Filter out irrelevant windows (e.g., null or empty app names, system windows)
                if app_name and app_name not in []:
                    geometry = window.get_geometry()
                    window_info['app'] = app_name
                    window_info['position'] = {
                        'x': geometry.x,
                        'y': geometry.y,
                        'width': geometry.width,
                        'height': geometry.height
                    }
                    self.window_data.append(window_info)
            except Xlib.error.XError:
                continue  # Skip windows that cannot be accessed

        display.close()

    # temporary
    def print_all_open_windows(self):
        """Print all open windows detected by Xlib."""
        self.get_open_windows()  # Get the open windows
        for window in self.window_data:
            print(f"App: {window['app']}, Position: {window['position']}")

    def save_project(self):
        """Save the project setup, including window positions, to a JSON file."""
        # Get the current open windows and their positions
        self.get_open_windows()

        # Prepare the data for saving
        project_data = {
            'project_name': self.project_name,
            'windows': self.window_data
        }

        # Save the setup to a JSON file
        filename = f"{self.project_name}_setup.json"
        with open(filename, 'w') as json_file:
            json.dump(project_data, json_file, indent=4)

        print(f"Project '{self.project_name}' setup saved as {filename}")

    def restore_project(self):
        """Restore a project setup from a JSON file."""
        filename = f"{self.project_name}_setup.json"
        try:
            with open(filename, 'r') as json_file:
                project_data = json.load(json_file)
            print(f"Restored project: {project_data}")
        except FileNotFoundError:
            print(f"Project file '{filename}' not found.")

    def list_projects(self):
        """List all saved project setups."""
        import os
        for filename in os.listdir("."):
            if filename.endswith("_setup.json"):
                print(filename)
