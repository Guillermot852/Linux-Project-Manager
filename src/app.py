from src.project_manager import ProjectManager
from src.ui import UserInterface

def main():
    print("Welcome to Linux Project Manager!")
    manager = ProjectManager()
    ui = UserInterface(manager)
    ui.start()

if __name__ == "__main__":
    main()
