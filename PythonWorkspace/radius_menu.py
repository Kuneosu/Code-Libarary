from tkinter import *
from tkinter import messagebox
from radius import *

def msgbox():
    messagebox.showinfo("안내","아직 지원하지 않습니다.")
def quit():
    root.destroy()
    root.quit()

root=Tk()

menubar=Menu(root)
f1=Menu(menubar,tearoff=0)
f1.add_command(label="원넓이계산",command=area)
f1.add_command(label="열기",command=msgbox)
f1.add_command(label="저장",command=msgbox)
f1.add_separator()
f1.add_command(label="Exit",command=quit)

menubar.add_cascade(label="File",menu=f1)
root.config(menu=menubar)
root.mainloop()