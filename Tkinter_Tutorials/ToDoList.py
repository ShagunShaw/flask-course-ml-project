import tkinter as tk
import tkinter.messagebox as tmsg
import os
import datetime
root=tk.Tk()
root.geometry("850x502")
root.title("My Program")
root.configure(background="grey")
f1=tk.Frame(root,height=2)
tk.Label(f1, text="To Do List", font="comicsansms 19 bold",background="blue").pack(anchor="center")
f1.pack(side="top",fill="y")

title=""
for files in os.listdir():
    if files.endswith(".txt"):     
        title=files   
if title=="":
    with open(".txt","w") as f:
        title=".txt"
        f.close()        

def getfoldername():
    s1=os.path.abspath(title)
    bs=s1[2]
    index=0
    count=0
    for i in range(len(s1)-1,0,-1):
        if s1[i]==bs:
            if count==1:
                s=""
                for j in range(i+1,index):
                    s=s+s1[j]
                return s    
            elif count==0:
                count+=1
                index=i

f2=tk.Frame(root, background="yellow")
tk.Label(f2,text="Title:", font="comicsansms 19 bold",background="yellow").pack(side="left")
t2=tk.Text(f2,width=30,height=2,font="17")

def saveTitle():
    titletext=t2.get("1.0", "end-1c")          # to get the text written in tk.Text()
    titletext+=".txt"
    os.rename(title,titletext)   
    t2.configure(state="disabled") 
    return titletext  

t2.insert("1.0",title[:-4])
t2.configure(state="disabled")

def writeTitle():
    t2.configure(state="normal")

t2.pack(side="left",pady=5)

t3=tk.Text(f2,width=30,height=2,font="17" )
t3.insert("1.0",getfoldername())
t3.pack(side="right",pady=5)
tk.Label(f2,text="Folder Name:", font="comicsansms 19 bold",background="yellow").pack(side="right")
f2.pack(side="top")

f4=tk.Frame(root)
scrollbar=tk.Scrollbar(f4)
t1=tk.Text(f4,width=100, height=20, yscrollcommand=scrollbar.set)
def save():
    global title
    title=saveTitle()
    t=t1.get("1.0", "end-1c")          # to get the text written in tk.Text()
    with open(title,"w") as f:
        f.write(t)
    t1.configure(state="disabled")    

def write():
    writeTitle()
    t1.configure(state="normal")

def delete():
    ans=tmsg.askquestion("Confirm delete", "Are you sure you want to delete this file?")
    if ans=="yes":
        tmsg.showinfo("File deleted","Your file have been deletd successfully.")
        os.remove(title)
        quit()        

def info():
    created=os.path.getctime(title)                     # To get the time of file creation
    create_datetime=datetime.datetime.fromtimestamp(created)

    modified=os.path.getmtime(title)                   # To get the time of last modification
    modify_datetime=datetime.datetime.fromtimestamp(modified)

    details=f"File Path: {os.path.abspath(title)}\n\nFile Size: {os.path.getsize(title)} Kb \n\nFile Created: {create_datetime} \n\nLast Modified: {modify_datetime}\n\nFile Type: .txt"
      # also relate the file name with the 'title'
    tmsg.showinfo("Details",details)

with open(title,"r") as  f:
    t1.insert("1.0", f.read())           # to insert some text in tk.Text()
    t1.configure(state="disabled")
    t1.pack(side="left", pady=10,padx=10)  
    scrollbar.config(command=t1.yview)
    scrollbar.pack(side="right",fill="y")
    f4.pack(side="top")

mymenu=tk.Menu(root)
m1=tk.Menu(mymenu,tearoff=0)
m1.add_command(label="File 1")
m1.add_command(label="File 2")
m1.add_separator()
m1.add_command(label="File 3")
m1.add_command(label="File 4")
m1.add_separator()
m1.add_command(label="File 5")
mymenu.add_cascade(label="File",menu=m1)

m1=tk.Menu(mymenu,tearoff=0)
m1.add_command(label="Edit 1")
m1.add_command(label="Edit 2")
m1.add_separator()
m1.add_command(label="Edit 3")
mymenu.add_cascade(menu=m1, label="Edit")

mymenu.add_command(label="Print")

m1=tk.Menu(mymenu,tearoff=0)
m2=tk.Menu(m1,tearoff=0)
m2.add_command(label="Help 5")
m2.add_separator()
m2.add_command(label="help 6")
m1.add_cascade(menu=m2,label="Help 1")
m1.add_separator()
m1.add_command(label="Help 2")
m1.add_command(label="Help 3")
m1.add_command(label="Help 4")
mymenu.add_cascade(menu=m1, label="Help")
root.configure(menu=mymenu)

f3=tk.Frame(root)
tk.Button(f3, text="Write", width=10, height=2, font="comicsansms 10 bold", relief="raised" ,padx=40, command=write).pack(side="left")
tk.Button(f3, text="Save", height=2, font="comicsansms 10 bold", relief="raised" ,padx=40, command=save).pack(side="left")
tk.Button(f3, text="Delete", width=10, height=2, font="comicsansms 10 bold", relief="raised", padx=40, command=delete).pack(side="left")
tk.Button(f3, text="Info", width=10, height=2, font="comicsansms 10 bold", relief="raised" ,padx=40, command=info).pack(side="left")
f3.pack(side="top")

tk.Button(text="EXIT", font="comicsansms 10 bold",padx=20,pady=5,command=quit).pack(side="bottom")
# print(os.path.abspath(title))

root.mainloop()


# +------------------------------------+
# |            To-Do List             |
# +------------------------------------+
# | [Input Field          ] [Add Button]|
# +------------------------------------+
# | [ ] Task 1                          |
# | [ ] Task 2                          |
# | [ ] Task 3                          |
# |                                    |
# |                                    |
# |                                    |
# +------------------------------------+
# | [Complete] [Delete] [Save] [Load]  |
# +------------------------------------+
# |            [Exit]                  |
# +------------------------------------+
