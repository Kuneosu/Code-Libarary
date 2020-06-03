from tkinter import *
from tkinter import messagebox

global manager_screen
manager_screen=Tk()
manager_screen.geometry("1000x650")
manager_screen.title("과제 관리")

manager_screen.resizable(width=0,height=0)

name="김권수"
work=Label(manager_screen,text=" 과제 LIST                                                                                                   User name: {0}".format(name),font=("맑은고딕",16,"bold"))   
work.pack(anchor=NW,pady=10,padx=10)

worklist=Listbox(manager_screen,width=75,height=35,relief="solid")
worklist.pack(side=LEFT,pady=10)

timelist=Listbox(manager_screen,width=25,height=35,relief="solid")
timelist.pack(side=LEFT,pady=10)

adds_button=Button(manager_screen,text="과제 추가",width=300,height=4,font=("맑은고딕",16,"bold"))
adds_button.pack(anchor=E,pady=20)

modify_button=Button(manager_screen,text="과제 수정",width=300,height=4,font=("맑은고딕",16,"bold"))
modify_button.pack(anchor=E,pady=20)

del_button=Button(manager_screen,text="과제 삭제",width=300,height=4,font=("맑은고딕",16,"bold"))
del_button.pack(anchor=E,pady=20)

exit_button=Button(manager_screen,text="나가기",width=300,height=4,font=("맑은고딕",16,"bold"))
exit_button.pack(anchor=E,pady=20)

manager_screen.mainloop()

