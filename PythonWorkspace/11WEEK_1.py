from tkinter import *
from tkinter import messagebox

root=Tk()

def click():
    pt=et.get()
    print(pt)
    lb['fg']=pt
    et.delete(0,END)

    messagebox.showinfo("제목",pt+"(으)로 색을 변경합니다.")

root.title("버튼 이벤트 만들기")
lb = Label(root,text="아래 빈칸에 텍스트를 입력하세요",width=40)
et=Entry(root,width=40)
bt=Button(root,text="   확  인  ",width=40,bg="pink",command=click)
lb.pack()
et.pack()
bt.pack()

root.mainloop()
