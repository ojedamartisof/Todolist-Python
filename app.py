import csv

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    todos.append(title)

def print_list():
    if len(todos) > 0:
        for x in range(0, len(todos)):
            print(str(x + 1) + ". " + todos[x])
    else:
        print("Empty list")


def delete_task(number_to_delete):
    # your code here
    if len(todos) > 0:
        for x in range(0, len(todos)):
            if(int(number_to_delete) == int(x+1)):
                todos.remove(todos[x])
    else:
        print("Empty list")

def save_todos():
    # your code here
    todos_as_csv = ','.join(todos) # convert the list into a string
    file = open('todos.csv', 'w+') # open the file for writing 'w', create if it doesn't exist
    file.write(todos_as_csv) # write the content
    file.close()

    
def load_todos():
    # your code here
    file = open("todos.csv") 
    file_content = csv.reader(file)
    for row in file_content:
        for x in row:
            todos.append(x)
        

    

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")