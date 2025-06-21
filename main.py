import tkinter as tk
import os

root = tk.Tk()  # Initialize tkinter GUI
root.title("To-Do-List App")  # Set the title name

# Dimension of window and x and y position of the window ("WidthxHeight + x + y")
root.geometry("400x650+900+100")

# Disable change of window size
root.resizable(False, False)

task_list = []

# Function to add a task to the list and save it to the file
def addTask():
    task = task_entry.get()
    task_entry.delete(0, tk.END)

    if task:
        task_list.append(task)  # Add the task to the list

        # Save the updated list to the file
        with open("tasklist.txt", 'w') as taskfile:
            for t in task_list:
                taskfile.write(f"{t}\n")
        
        listbox.insert(tk.END, task)

# Function to delete a task from the list and save the updated list to the file
def deleteTask():
    global task_list
    if select_all_var.get():  # If "Select All" is checked
        task_list.clear()  # Clear all tasks
        listbox.delete(0, tk.END)
        
        # Clear the tasklist.txt file
        with open("tasklist.txt", 'w') as taskfile:
            taskfile.write("")  # Empty the file

    else:
        task = str(listbox.get(tk.ANCHOR))  # Get the selected task
        if task in task_list:
            task_list.remove(task)  # Remove the task from the list

            # Update the tasklist.txt file
            with open("tasklist.txt", 'w') as taskfile:
                for task in task_list:
                    taskfile.write(f"{task}\n")  # Write the updated list

            listbox.delete(tk.ANCHOR)  # Remove the task from the Listbox

    select_all_var.set(False)  # Reset "Select All" checkbox

# Function to open the task list from the file and display them in the Listbox
def openTaskFile():
    if os.path.exists("tasklist.txt"):  # Check if the file exists
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()  # Read all lines from the file

        for task in tasks:
            task = task.strip()  # Remove any leading/trailing whitespace
            if task:  # Ignore empty lines
                task_list.append(task)
                listbox.insert(tk.END, task)  # Add the task to the Listbox
    else:
        open("tasklist.txt", 'w').close()  # Create the file if it doesn't exist

# Function to handle "Select All" checkbox
def toggle_select_all():
    if select_all_var.get():
        listbox.select_set(0, tk.END)  # Select all tasks in the list
    else:
        listbox.select_clear(0, tk.END)  # Deselect all tasks

# Icon
appIcon = tk.PhotoImage(file="Image/task.png")
root.iconphoto(False, appIcon)  # Set icon for the root window

# Top bar
topImage = tk.PhotoImage(file="Image/topbar.png")
tk.Label(root, image=topImage).pack()

# Dock Image
dockImage = tk.PhotoImage(file="Image/dock.png")
tk.Label(root, image=dockImage, bg="#32405b", height=20, width=20).place(x=30, y=25)

# Note Icon
noteImage = tk.PhotoImage(file="Image/task.png")
tk.Label(root, image=noteImage, bg="#32405b").place(x=340, y=25)

# Heading
heading = tk.Label(root, text="TASK LIST", font="arial 20 bold", fg="white", bg="#009999")
heading.place(x=130, y=20)

# Entry Frame for adding task
frame = tk.Frame(root, width=370, height=50, bg="#E0F7FF")
frame.place(x=15, y=110)

# Checkbox for "Select All"
select_all_var = tk.BooleanVar()
checkbox_select_all = tk.Checkbutton(root, text="Select All", variable=select_all_var, command=toggle_select_all)
checkbox_select_all.place(x=10, y=200)

# Entry for task input
task_entry = tk.Entry(frame, width=20, font="arial 15", bg="#E0F7FF", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()  # Focus on task entry when the app opens

# Button to add task
button = tk.Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#009999", fg="white", bd=0, command=addTask)
button.place(x=270, y=0)

# Listbox Frame
frame1 = tk.Frame(root, width=370, height=380, bg="#E0F7FF")
frame1.pack(pady=(160, 0))

# Listbox for displaying tasks
listbox = tk.Listbox(frame1, font=('arial', 12), width=40, height=16, bg='#E0F7FF', fg="black", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

# Scrollbar for the Listbox
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

# Configure the scrollbar to work with the Listbox
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Open the task file and load tasks into the Listbox
openTaskFile()

# Delete button to remove tasks
Delete_icon = tk.PhotoImage(file="Image/delete.png")
tk.Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=tk.BOTTOM, pady=13)

# Bind the Enter key to add a task
root.bind('<Return>', lambda event: addTask())

# Run the main loop of the tkinter application
root.mainloop()