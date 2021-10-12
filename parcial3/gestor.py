import os

import tkinter as tk
  


def gettask():
    matriz_tasks = []
    pids = []
    a = os.popen("tasklist").readlines()
    for task_array in a:
        try:
            tasks = task_array[0:77]
            tasks = tasks.split(" ")
            tasks = tuple([ele for ele in tasks if ele.strip()])
            matriz_tasks.append(tasks)
            
        except Exception:
            pass
    return matriz_tasks
    
def endtask():
    pids = []
    a = os.popen("tasklist").readlines()
    i = 0
    print(t_pid.get())
    for x in a:
        try:
            t10 = x[0:77]
            t10 = t10.split(" ")
            t10 = [ele for ele in t10 if ele.strip()]
            
            if(t10[1] == t_pid.get()):
                pid = t10[1]
                os.system("taskkill /pid "+str(pid))
                print(t10)
                break
        except Exception:
            pass
    

lst = gettask()
lst.pop(0)
lst.pop(0) 
lst.pop(0) 
lst.pop(0) 
print(lst)

 


class Table:
      
    def __init__(self,root):
        self.sb = tk.Scrollbar(root)  
        self.sb.pack(side = tk.RIGHT, fill = tk.Y)  
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                  
                self.e = tk.Entry(root,yscrollcommand = self.sb.set, width=20, fg='blue',
                               font=('Arial',10,'bold'))
                  
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, lst[i][j])
  
# take the data
lst = lst
   
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
   
# create root window
root = tk.Tk() 
t = Table(root)


tk.Label(root, text="PID").grid(row=0)
t_pid = tk.Entry(root)
t_pid.grid(row=0, column=1)

tk.Button(root, text='Cerrar tarea', command=endtask).grid(row=3, column=1, sticky=tk.W, pady=4)
root.mainloop()