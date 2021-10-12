from tkinter import *
from  tkinter import ttk
import os


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


ws  = Tk()
ws.title('PythonGuides')
ws.geometry('1000x1000')
ws['bg'] = '#AC99F2'

game_frame = Frame(ws)
game_frame.pack()

button1 = Button(ws, text='Cerar tarea',command=endtask)
button1.place(x=0, y=80)

L1 = Label(ws, text="Ingrese PID")
L1.place(x=0,y=50)
t_pid = Entry(ws, text="Ingrese el PID")
t_pid.place(x=65,y=50)


game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame,orient='horizontal')
game_scroll.pack(side= BOTTOM,fill=X)

my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set,height=1000)


my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)


 
my_game['columns'] = ('Nombre_de_la_imagen', 'PID', 'Nombr_de_sesion', 'Num_de_ses', 'Uso_de_memoria','unidad')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("Nombre_de_la_imagen",anchor=CENTER, width=100)
my_game.column("PID",anchor=CENTER,width=100)
my_game.column("Nombr_de_sesion",anchor=CENTER,width=100)
my_game.column("Num_de_ses",anchor=CENTER,width=100)
my_game.column("Uso_de_memoria",anchor=CENTER,width=100)
my_game.column("unidad",anchor=CENTER,width=100)


my_game.heading("#0",text="",anchor=CENTER) 
my_game.heading("Nombre_de_la_imagen",text="Nombre de la imagen",anchor=CENTER)
my_game.heading("PID",text="PID",anchor=CENTER)
my_game.heading("Nombr_de_sesion",text="Nombre de la sesion",anchor=CENTER)
my_game.heading("Num_de_ses",text="Num de ses",anchor=CENTER)
my_game.heading("Uso_de_memoria",text="Uso de la memoria",anchor=CENTER)
my_game.heading("unidad",text="Unidad",anchor=CENTER)



for i in range(len(lst)):
    print(i)
    my_game.insert(parent='',index='end',iid=i,text='',
    values=lst[i])

my_game.pack()



ws.mainloop()