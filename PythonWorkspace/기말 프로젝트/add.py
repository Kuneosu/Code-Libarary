from tkinter import *

def add_work():
    worklist.insert("{0}                            {1}".format(workname,time))

add_screen=Tk()
add_screen.geometry("350x150")
add_screen.title("과제 추가")

workname=StringVar()
time=StringVar()

work_name=Label(add_screen,text="과제 명을 입력하시오.",font=("맑은고딕",10))
work_name.grid(row=0,pady=10)

workentry=Entry(add_screen,textvariable=workname,width=50)
workentry.grid(row=1)

end_time=Label(add_screen,text="제출 마감 일을 입력하시오.",font=("맑은고딕",10))
end_time.grid(row=2,pady=10)

timeentry=Entry(add_screen,textvariable=time,width=50)
timeentry.grid(row=4)

enter=Button(add_screen,text="등록",font="맑은고딕",command=add_work)
enter.grid(row=5,pady=5)

add_screen.mainloop()