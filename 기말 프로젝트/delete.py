from tkinter import *

def pri():
    selection=worklist.curselection()
    print(selection[0])
    worklist.delete(selection[0])


main=Tk()
main.geometry("1000x650")

global worklist

worklist=Listbox(main,width=75,height=35,relief="solid")
worklist.pack(side=LEFT,pady=10)

worklist.insert(0,"1번 항목")
worklist.insert(1,"2번 항목")
worklist.insert(2,"3번 항목")
worklist.insert(3,"4번 항목")
worklist.insert(4,"5번 항목")

bt=Button(main,text="버튼",command=pri)
bt.pack()


main.mainloop()
