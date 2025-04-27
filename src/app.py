from src.project_manager import ProjectManager

def main():
    print("Welcome to Linux Project Manager!")
    print("You can use the following commands:")
    print("1. save_setup('setupName')")
    print("2. restore_setup('setupName')")
    print("3. list_projects()")
    
    project_name = input("Enter your project name: ")

    manager = ProjectManager(project_name)

    manager.print_all_open_windows()

    while True:
        # Show a prompt for the user to enter a command
        command = input("Enter a command (save_setup, restore_setup, list_projects) or 'exit' to quit: ")

        if command == 'save_setup':
            manager.save_project()
            print(f"Project setup saved as {project_name}_setup.json")

        elif command == 'restore_setup':
            manager.restore_project()
            print(f"Project setup {project_name}_setup.json restored.")

        elif command == 'list_projects':
            manager.list_projects()

        elif command == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()
