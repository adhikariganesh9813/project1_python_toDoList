import tkinter as tk

root = tk.Tk() #initialize tkinter GUI
root.title("To-Do-List App")  #Set the title name

# Dimension of window and x and y position of the window ("WidthxHeight + x + y")
root.geometry("400x650+1150+100")

# Disable change of window size
root.resizable(False, False)

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0,tk.END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(tk.END, task)

def deleteTask():

    global task_list
    if select_all_var.get():
        task_list.clear()
        listbox.delete(0, tk.END)

        with open("tasklist.txt", 'w') as taskfile:
            taskfile.write("")
    else:
        task = str(listbox.get(tk.ANCHOR))
        if task in task_list:
            task_list.remove(task)
            with open ("tasklist.txt", 'w') as taskfile:
                for task in task_list:
                    taskfile.write(task+"\n")

            listbox.delete(tk.ANCHOR)
    select_all_var.set(False)

def openTaskFile():

    try:
        with open("p1_to_do_list/tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(tk.END, task)

    except:
        file = open('tasklist.txt', 'w')
        file.close()

def toggle_select_all():
    if select_all_var.get():
        listbox.select_set(0, tk.END)
    else:
        listbox.select_clear(0, tk.END)

#icon
appIcon = tk.PhotoImage(file="p1_to_do_list/Image/task.png") #Step 1 for icon setup
root.iconphoto(False, appIcon) # Step 2 to setup icon, here false means set icon only for root window

#top bar
topImage = tk.PhotoImage(file="p1_to_do_list/Image/topbar.png")
tk.Label(root, image= topImage).pack() #Label is a widget and pack automatically adjusts label image in the root window

dockImage = tk.PhotoImage(file="p1_to_do_list/Image/dock.png")
tk.Label(root, image= dockImage, bg = "#32405b", height=20, width=20).place(x=30, y=25)

noteImage = tk.PhotoImage(file="p1_to_do_list/Image/task.png")
tk.Label(root, image=noteImage, bg = "#32405b").place(x=340,y=25)

heading = tk.Label(root, text= "ALL TASK", font = "arial 20 bold", fg = "white", bg = "#32405b")
heading.place(x=130, y=20)

# Corrected frame configuration
frame = tk.Frame(root, width=370, height=50, bg="#ffffe6")  # Increased width to match window
frame.place(x=15, y=110)  # Adjusted placement

# frame_select_all = Frame(root, width=185, height=20, bg="#ffffe6")  # Increased width to match window
# frame_select_all.place(x=10, y=220)  # Adjusted placement
select_all_var = tk.BooleanVar()
checkbox_select_all = tk.Checkbutton(root,text= "Select All", variable= select_all_var, command = toggle_select_all)
checkbox_select_all.place(x=10, y=200)

task = tk.StringVar()
task_entry = tk.Entry(frame, width=30, font="arial 15", bg= "#ffffe6" ,bd=0)  # Increased width
task_entry.place(x=10, y=7)
task_entry.focus() #when app opens, it directly focus on task_entry element, blinks type symbol

button = tk.Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#32405b", fg="white", bd=0, command = addTask)
button.place(x=270, y=0)

#listbox
frame1 = tk.Frame(root,width=370, height=380,bg= "#ffffe6")
frame1.pack(pady=(160,0))

listbox = tk.Listbox(frame1,font=('arial',12),width=40, height=16,bg='#32405b',fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=tk.LEFT,fill=tk.BOTH, padx=2)
scrollbar = tk.Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command= listbox.yview)


openTaskFile()
#delete
Delete_icon = tk.PhotoImage(file = "p1_to_do_list/Image/delete.png")
tk.Button(root,image=Delete_icon,bd=0, command = deleteTask).pack(side=tk.BOTTOM,pady=13)

root.bind('<Return>', lambda event: addTask())

root.mainloop()