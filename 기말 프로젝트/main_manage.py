from tkinter import *
from tkinter import messagebox
from datetime import datetime,timedelta
import datetime
import webbrowser

global name
name="김권수"

def door():
    webbrowser.open_new("http://door.deu.ac.kr")
def quit():                         # 종료 함수
    wf=open("{0} work.txt".format(name),"w")
    tf=open("{0} time.txt".format(name),"w")
    many=worklist.size()
    user_work=worklist.get(0,many)
    user_time=timelist.get(0,many)
    for i in range(0,many):
        wf.write(user_work[i]+"\n")
        tf.write(user_time[i]+"\n")
    wf.close()
    tf.close()
    main_screen.destroy()
    main_screen.quit()

def mains():                        # 메인 스크린 함수
    global main_screen
    main_screen=Tk()
    main_screen.geometry("1000x650")
    main_screen.title("과제 관리 프로그램")

    main_screen.resizable(width=0,height=0) 

    work=Label(main_screen,text=" 과제 LIST                                                                                                   User name: {0}".format(name),font=("맑은고딕",16,"bold"))   
    work.pack(anchor=NW,pady=10,padx=10)

    global worklist
    worklist=Listbox(main_screen,width=75,height=35,relief="solid")
    worklist.pack(side=LEFT,pady=10)
    global timelist
    timelist=Listbox(main_screen,width=25,height=35,relief="solid")
    timelist.pack(side=LEFT,pady=10)

    wf=open("{0} work.txt".format(name),"r")
    tf=open("{0} time.txt".format(name),"r")

    user_works=wf.readlines()
    user_times=tf.readlines()

    length=len(user_works)

    for i in range(0,length):
        worklist.insert(i,user_works[i])
        timelist.insert(i,user_times[i])
    wf.close()
    tf.close()

    add_button=Button(main_screen,text="과제 추가",command=add)
    add_button.pack()

    work_button=Button(main_screen,text="과제 관리",width=15,height=2,font=("맑은고딕",20,"bold"),command=manager)
    work_button.pack(pady=10)

    check_button=Button(main_screen,text="DOOR",width=15,height=2,font=("맑은고딕",20,"bold"),command=door)
    check_button.pack(pady=10)

    door_button=Button(main_screen,text="정렬",width=15,height=2,font=("맑은고딕",20,"bold"),command=sort)
    door_button.pack(pady=10)

    set_button=Button(main_screen,text="설정",width=15,height=2,font=("맑은고딕",20,"bold"))
    set_button.pack(pady=10)

    exit_button=Button(main_screen,text="종료",width=15,height=2,font=("맑은고딕",20,"bold"),command=quit)
    exit_button.pack(pady=10)

    main_screen.mainloop()

def sort():             # 리스트 정렬 함수
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

def add_work():                     # 과제 추가 알고리즘
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
    

def add():                         # 과제 추가 창

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

def sort_manage():             # 리스트 정렬 함수
    mt_sortlist=[]
    mw_sortlist=[]
    mt_many=m_timelist.size()
    mt_thing=m_timelist.get(0,mt_many)
    mw_thing=managelist.get(0,mt_many)
    for i in range(0,mt_many):
        mt_value=mt_thing[i]
        mw_value=mw_thing[i]
        mt_sortlist.append(mt_value)
        mw_sortlist.append(mw_value)
    mt_sortlist.sort()
    mw_sortlist.sort()
    managelist.delete(0,mt_many)
    m_timelist.delete(0,mt_many)
    for i in range(0,mt_many):
        m_timelist.insert(i,mt_sortlist[i])
        managelist.insert(i,mw_sortlist[i]) 
    sort()  

def m_add_work():                     # 과제 추가 알고리즘
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
                managelist.insert(0,"{0} 일 남음. {1}".format(dif_days,work))
                m_timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))
            else:
                managelist.insert(0,"9+) {0} 일 남음. {1}".format(dif_days,work))
                m_timelist.insert(0,"9+) {0} 월 {1} 일 까지 제출".format(m,d))
        elif dif_days==0:
            managelist.insert(0,"{0} 일 남음(오늘 제출). {1}".format(dif_days,work))
            m_timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))
        else:
            managelist.insert(0,"{0} 일 남음(제출일 지남). {1}".format(dif_days,work))
            m_timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))
            
    elif dif_month>0:
        managelist.insert(0,"9++) {0} 달 {1} 일 남음. {2}".format(dif_month,dif_days,work))
        m_timelist.insert(0,"9++) {0} 월 {1} 일 까지 제출".format(m,d))    
    else:
        managelist.insert(0,"{0} 달 {1} 일 남음(제출일 지남). {2}".format(dif_month,dif_days,work))
        m_timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))    
    add_work()  

def m_add():     # 관리 / 과제 추가 창

    global m_add_screen
    m_add_screen=Tk()
    m_add_screen.geometry("350x150")
    m_add_screen.title("과제 추가")

    global workname
    global month
    global days
    workname=StringVar()
    month=StringVar()
    days=StringVar()

    work_name=Label(m_add_screen,text="과제 명을 입력하시오.",font=("맑은고딕",10))
    work_name.grid(row=0,pady=10)

    global workentry
    workentry=Entry(m_add_screen,textvariable=workname,width=50)
    workentry.grid(row=1)

    end_time=Label(m_add_screen,text="제출 마감 일을 입력하시오. ( 월, 일 순서 )",font=("맑은고딕",10))
    end_time.grid(row=2,pady=10)

    global month_entry
    global days_entry

    month_entry=Entry(m_add_screen,textvariable=month,width=23)
    month_entry.grid(row=4,sticky=W)
    days_entry=Entry(m_add_screen,textvariable=days,width=23)
    days_entry.grid(row=4,sticky=E)

    b1=Button(m_add_screen,text="등록",command=m_add_work,font="맑은고딕")
    b1.grid(row=5)   

    m_add_screen.mainloop()

def m_delete():
    selection=managelist.curselection()
    worklist.delete(selection[0])
    managelist.delete(selection[0])
    timelist.delete(selection[0])
    m_timelist.delete(selection[0])

def m_quit():
    manager_screen.destroy()
    manager_screen.quit()

def manager():      # 과제 관리 창
    global manager_screen
    manager_screen=Tk()
    manager_screen.geometry("1000x650")
    manager_screen.title("과제 관리")

    manager_screen.resizable(width=0,height=0)

    name="김권수"
    work=Label(manager_screen,text=" 과제 LIST                                                                                                   User name: {0}".format(name),font=("맑은고딕",16,"bold"))   
    work.pack(anchor=NW,pady=10,padx=10)

    global managelist
    managelist=Listbox(manager_screen,width=75,height=35,relief="solid")
    managelist.pack(side=LEFT,pady=10)

    global m_timelist
    m_timelist=Listbox(manager_screen,width=25,height=35,relief="solid")
    m_timelist.pack(side=LEFT,pady=10)

    m_list=[]
    mt_list=[]
    l=worklist.size()
    m_list=worklist.get(0,l)
    mt_list=timelist.get(0,l)
    managelist.delete(0,l)
    m_timelist.delete(0,l)
    for i in range(0,l):
        managelist.insert(i,m_list[i])
        m_timelist.insert(i,mt_list[i]) # main_screen 에서 과제 목록을 받아옴

    adds_button=Button(manager_screen,text="과제 추가",width=300,height=4,font=("맑은고딕",16,"bold"),command=m_add)
    adds_button.pack(anchor=E,pady=20)

    delete_button=Button(manager_screen,text="과제 삭제",width=300,height=4,font=("맑은고딕",16,"bold"),command=m_delete)
    delete_button.pack(anchor=E,pady=20)

    del_button=Button(manager_screen,text="과제 정렬",width=300,height=4,font=("맑은고딕",16,"bold"),command=sort_manage)
    del_button.pack(anchor=E,pady=20)

    exit_button=Button(manager_screen,text="나가기",width=300,height=4,font=("맑은고딕",16,"bold"),command=m_quit)
    exit_button.pack(anchor=E,pady=20)

    manager_screen.mainloop()


mains()