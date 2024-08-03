import tkinter as tk
  
root=tk.Tk()
root.title("Internet Speed Checker")

root.geometry("800x500")
root.maxsize(800,500)

root.configure(background="yellow")

tk.Label(text="Uploading Speed", background="red", font="comicsans 19 bold").place(x=290,y=40,height=50,width=250)
l1=tk.Label(text="00",font="comicsans 19 bold")

tk.Label(text="Downloading Speed", background="red", font="comicsans 19 bold").place(x=290,y=240,height=50,width=250)
l2=tk.Label(text="00",font="comicsans 19 bold")

def check():
    import speedtest
    sp=speedtest.Speedtest()
    down= str(round(sp.download()/(10**6),3)) + " Mbps"
    up= str(round(sp.upload()/(10**6),3)) + " Mbps"
    l1.config(text=up)
    l2.config(text=down)

l1.place(x=290,y=90,height=50,width=250)    
l2.place(x=290,y=290,height=50,width=250)    

tk.Button(text="CHECK", background="grey", font="Arial 25 bold", command=check, relief="raised").place(x=325,y=390,height=30,width=170)

root.tk.mainloop()