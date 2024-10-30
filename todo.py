import argparse
import os

def create_parse():
    parser = argparse.ArgumentParser(description="Welcome to todo-cli app" , epilog="For more help visit")

    parser.add_argument('-a' ,'--add' , metavar="" , help="add a item")
    parser.add_argument('-l' , '--list' , action="store_true" , help="lists all items")
    parser.add_argument('-r' , '--rem' , metavar="" , help="remove an item")
    return parser


def add_task(task):
    with open("tasks.txt" , "a") as file:
        file.write(task + '\n')

def list_task():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt" , 'r') as file:
            tasks = file.readlines();
            for index , task in enumerate(tasks , start =1):
                print(f"{index}. {task}")
    else:
        print("No tasks found")

def remove_task(index):
    if os.path.exists("tasks.txt"):
        with open("tasks.txt" , "r") as file:
            tasks = file.readlines();
        with open("tasks.txt" , 'w') as file:
            for i ,task in enumerate(tasks , start =1):
                if i != index:
                    file.write(task)
        print("Task deleted")
    else:
        print("No tasks found")

def main():
    parser = create_parse()
    args = parser.parse_args()
    if args.add :
        add_task(args.add)
    elif args.list:
        list_task()
    elif args.rem:
        remove_task(int(args.rem))
    else:
        parser.print_help()
    
if __name__ == "__main__" :
    main()