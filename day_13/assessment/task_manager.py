class TaskNode:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.status = "Pending"
        self.next = None


class TaskManager:
    def __init__(self):
        self.head = None

    # Add task at the end
    def add_task(self, name, priority):
        new_task = TaskNode(name, priority)
        if self.head is None:
            self.head = new_task
            print(f"Task '{name}' added successfully!")
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_task
        print(f"Task '{name}' added successfully!")

    # Display all tasks
    def display_tasks(self):
        if self.head is None:
            print("No tasks available.")
            return

        curr = self.head
        print("\n Task List:")
        while curr:
            print(f"Task: {curr.name} | Priority: {curr.priority} | Status: {curr.status}")
            curr = curr.next

    # Delete a task by name
    def delete_task(self, name):
        curr = self.head
        prev = None

        # Case 1: Empty list
        if not curr:
            print("No tasks to delete.")
            return

        # Case 2: First node matches
        if curr and curr.name == name:
            self.head = curr.next
            print(f"Task '{name}' deleted successfully!")
            return

        # Case 3: Search through list
        while curr and curr.name != name:
            prev = curr
            curr = curr.next

        if curr is None:
            print(f"Task '{name}' not found.")
            return

        prev.next = curr.next
        print(f"Task '{name}' deleted successfully!")

    # Mark a task as completed
    def mark_completed(self, name):
        curr = self.head
        while curr:
            if curr.name == name:
                if curr.status == "Completed":
                    print(f"Task '{name}' is already completed!")
                    return
                curr.status = "Completed"
                print(f"Task '{name}' marked as completed!")
                return
            curr = curr.next
        print(f"Task '{name}' not found.")

    # Count pending tasks
    def count_pending(self):
        curr = self.head
        count = 0
        while curr:
            if curr.status == "Pending":
                count += 1
            curr = curr.next
        return count


if __name__ == "__main__":
    manager = TaskManager()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Show Pending Task Count")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ")
            manager.add_task(name, priority)

        elif choice == "2":
            manager.display_tasks()

        elif choice == "3":
            name = input("Enter task name to delete: ")
            manager.delete_task(name)

        elif choice == "4":
            name = input("Enter task name to mark completed: ")
            manager.mark_completed(name)

        elif choice == "5":
            print(f"Pending tasks: {manager.count_pending()}")

        elif choice == "6":
            print("Exiting Task Manager...")
            break

        else:
            print("Invalid choice. Try again.")
