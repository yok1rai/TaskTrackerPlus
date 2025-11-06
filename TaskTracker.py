import json
import os
from time import sleep as sl

os.chdir(os.path.dirname(os.path.abspath(__file__)))

FILE = "task.json"

def load_task():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_task(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False, separators=(",", ": "))


def add_task(task):
    tasks = load_task()
    tasks.append({"task": task, "done": False})
    save_task(tasks)
    print(f"✅ Added: {task}")

def view_task():
    tasks = load_task()
    if not tasks:
        print("📪 No tasks yet")
        return
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} [{status}]")

def mark_done(index):
    tasks = load_task()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_task(tasks)
        print(f"✅ Marked '{tasks[index]['task']}' as done")
    else:
        print("❌ Invalid task number")

def delete_task(index):
    tasks = load_task()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_task(tasks)
        print(f"🗑️ Deleted: {removed['task']}")
    else:
        print("❌ Invalid task number")

def main():
    while True:
        print("\n=== TaskTracer+ ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        try:
            choice = int(input("Select: "))

            if choice == 1:
                view_task()
            elif choice == 2:
                add_task(input("Enter a new task: "))
            elif choice == 3:
                view_task()
                mark_done(int(input("Task number: ")) - 1)
            elif choice == 4:
                view_task()
                delete_task(int(input("Task number: ")) - 1)
            elif choice == 5:
                print("Goodbye!")
                sl(0.5)
                break
            else:
                raise ValueError

            sl(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')

        except ValueError:
            print("Enter a valid value")

if __name__ == "__main__":
    main()
