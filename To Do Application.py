# To-Do List Application
import os

def clear_screen():
    # Clear the console screen for better readability
    os.system('cls' if os.name == 'nt' else 'clear')
    
def display_menu():
    print("\nWelcome to Lee's To-Do List Application!")
    print("Please choose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
#display_menu()
def add_task(task_list):
    """Adds a new task to the task list."""
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"Task added: {task}")
#    input("\nPress Enter to return to menu...")
def view_tasks(task_list):
    if not task_list:
        print("No tasks available to view.")
    else:
        print("Current Tasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
#    input("\nPress Enter to return to menu...")
def delete_task(task_list):
    """Deletes a task from the task list based on user input."""
    view_tasks(task_list)
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if task_index < 0 or task_index >= len(task_list):
            raise IndexError
    except ValueError:
        print("Invalid input. Please enter a number.")
    except IndexError:
        print("Task not found.")
    else:
        removed_task = task_list.pop(task_index)
        print(f"Task deleted: {removed_task}")
    finally:
        input("\nPress Enter to return to menu...")
# Main function to run the To-Do List Application
def main():
    tasks = []
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            delete_task(tasks)
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
#        input("\nPress Enter to return to menu...")
if __name__ == "__main__":
    main()