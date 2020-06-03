from tkinter import *
from tkinter import messagebox
from datetime import datetime,timedelta

def sort():
    t_sortlist=[]
    w_sortlist=[]
    t_many=timelist.size()
    t_thing=timelist.get(0,t_many)
    w_thing=worklist.get(0,t_many)
    for i in range(0,t_many):
        t_value=t_thing[i]
        w_value=w_thing[i]
        t_sortlist.append(t_value)
        w_sortlist.append(w_value)
    t_sortlist.sort()
    w_sortlist.sort()
    worklist.delete(0,t_many)
    timelist.delete(0,t_many)
    for i in range(0,t_many):
        timelist.insert(i,t_sortlist[i])
        worklist.insert(i,w_sortlist[i])     

def add_work():
    work=workentry.get()
    now=datetime.datetime.now()
    m=int(month_entry.get())
    d=int(days_entry.get())
    entry_date=datetime.date(2020,m,d)
    dif_month=m-now.month
    dif_days=d-now.day
    if dif_month==1:
        d_month="한"
    elif dif_month==2:
        d_month="두"

    print("m={0}, d={1}, entry_date={2}, dif_m={3},dif_days={4},now ={5}".format(m,d,entry_date,dif_month,dif_days,now))
    if dif_month==0:
        if dif_days>0:
            if dif_days<10:
                worklist.insert(0,"{0} 일 남음. {1}".format(dif_days,work))
                timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))
            else:
                worklist.insert(0,"9+) {0} 일 남음. {1}".format(dif_days,work))
                timelist.insert(0,"9+) {0} 월 {1} 일 까지 제출".format(m,d))
        elif dif_days==0:
            worklist.insert(0,"{0} 일 남음(오늘 제출). {1}".format(dif_days,work))
            timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))
        else:
            worklist.insert(0,"{0} 일 남음(제출일 지남). {1}".format(dif_days,work))
            timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))
            
    elif dif_month>0:
        worklist.insert(0,"9++) {0} 달 {1} 일 남음. {2}".format(dif_month,dif_days,work))
        timelist.insert(0,"9++) {0} 월 {1} 일 까지 제출".format(m,d))    
    else:
        worklist.insert(0,"{0} 달 {1} 일 남음(제출일 지남). {2}".format(dif_month,dif_days,work))
        timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))    
    messagebox.showinfo("등록 성공","과제가 등록되었습니다.")
    add_screen.destroy()
    

def adds():

    global add_screen
    add_screen=Tk()
    add_screen.geometry("350x150")
    add_screen.title("과제 추가")

    global workname
    global month
    global days
    workname=StringVar()
    month=StringVar()
    days=StringVar()

    work_name=Label(add_screen,text="과제 명을 입력하시오.",font=("맑은고딕",10))
    work_name.grid(row=0,pady=10)

    global workentry
    workentry=Entry(add_screen,textvariable=workname,width=50)
    workentry.grid(row=1)

    end_time=Label(add_screen,text="제출 마감 일을 입력하시오. ( 월, 일 순서 )",font=("맑은고딕",10))
    end_time.grid(row=2,pady=10)

    global month_entry
    global days_entry
    month_entry=Entry(add_screen,textvariable=month,width=23)
    month_entry.grid(row=4,sticky=W)
    days_entry=Entry(add_screen,textvariable=days,width=23)
    days_entry.grid(row=4,sticky=E)

    b1=Button(add_screen,text="등록",command=add_work,font="맑은고딕")
    b1.grid(row=5)

    add_screen.mainloop()