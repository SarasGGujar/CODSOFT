# To-Do List

def main():
    tasks = []

    while True:
        print("===== Your To-Do List =====")
        print("1. Add New Tasks")
        print("2. View All Tasks")
        print("3. Mark Task as Done")
        print("4. Update Tasks")
        print("5. Exit")

        choice = input("Choose option Between (1-5): ")

        if choice == '1':
            print("Adding Tasks Window:")
            total_tasks = int(input("How many tasks would you like to add? "))
            
            for i in range(total_tasks):
                print("Enter task", i + 1, ": ", end="")
                task = input()
                tasks.append({"task": task, "done": False})
                print("Your Task of'" + task + "' has been added!")

        elif choice == '2':
            if tasks:
                print("Your All tasks Window:")
                for index, task in enumerate(tasks):
                    status = "Completed" if task["done"] else "Pending"
                    print(str(index + 1) + ". " + task["task"] + " - " + status)
            else:
                print("No tasks in your list till. You might need to add some tasks first!")

        elif choice == '3':
            print("Marking Task as Completed Window:")
            task_number = int(input("Enter the number of the task you have completed: ")) - 1
            if 0 <= task_number < len(tasks):
                tasks[task_number]["done"] = True
                print("Your Task of '" + tasks[task_number]['task'] + "' marked as completed!")
            else:
                print("Invalid task number. Please Retry.")

        elif choice == '4':
            print("Updating Task Window:")
            task_number = int(input("Enter the number of the tasks you wanted to update: ")) - 1
            if 0 <= task_number < len(tasks):
                new_task = input("Enter the new Task Description: ")
                tasks[task_number]["task"] = new_task
                print("Your Task has been updated to: '" + new_task + "'")
            else:
                print("Invalid task number. Please Retry.")

        elif choice == '5':
            print("Thank you for using the To-Do List. Have a Nice Day Again!")
            break

        else:
            print("Invalid selection. Please choose number between 1 and 5.")

if __name__ == "__main__":
    main()
