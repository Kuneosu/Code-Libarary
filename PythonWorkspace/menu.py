from tkinter import *
from tkinter import messagebox

window=Tk()

def msgbox():
    messagebox.showinfo("안내","아직 지원하지 않는 기능")
def quit():
    window.destroy()
    window.quit()

menubar=Menu(window)
f1=Menu(menubar,tearoff=0)
f1.add_command(label="새 파일",command=msgbox)
f1.add_command(label="열기",command=msgbox)
f1.add_command(label="저장",command=msgbox)
f1.add_separator()
f1.add_command(label="종료",command=quit)

menubar.add_cascade(label="Test",menu=f1)
window.config(menu=menubar)


window.mainloop()