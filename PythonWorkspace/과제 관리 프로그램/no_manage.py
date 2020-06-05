from tkinter import *
from tkinter import messagebox
from datetime import datetime,timedelta
import datetime
import webbrowser
import os

def main_account_screen():                              # 메인 창 함수 
    global main_account_screen
    main_account_screen = Tk() # 윈도우 창 생성
    main_account_screen.geometry("300x250") # 윈도우 창 크기 설정
    main_account_screen.title("회원가입") # 윈도우 창 제목 설정

# 첫 화면 글자 설정

    Label(text="과제 관리 프로그램",bg="blue",width="300",height="2",font=("맑은 고딕",13)).pack()
    Label(text="").pack()

# 로그인 버튼 생성

    Button(text="로그인",height="2",width="30",command=login).pack()
    Label(text="").pack()

# 회원가입 버튼 생성

    Button(text="회원가입",height="2",width="30",command=register).pack()

    main_account_screen.mainloop() # 윈도우창 실행

def register(): # 회원가입 창 함수

    global register_screen
    register_screen = Toplevel(main_account_screen)
    register_screen.title("회원가입")
    register_screen.geometry("300x250")

#텍스트 변수 설정

    global username
    global password
    username=StringVar()
    password=StringVar()

# 유저가 볼 레이블 설정

    Label(register_screen, text="자세한 정보를 아래에 적어 주세요",bg="blue").pack()
    Label(register_screen,text="").pack()

# 아이디 레이블 설정

    username_lable=Label(register_screen, text="아이디 *")
    username_lable.pack()

# 아이디 입력 설정

    global username_entry
    global password_entry
    username_entry=Entry(register_screen, textvariable=username)
    username_entry.pack()

# 비밀번호 레이블 설정 

    password_lable=Label(register_screen, text="비밀번호 *")
    password_lable.pack()

# 비밀번호 입력 설정

    password_entry=Entry(register_screen, textvariable=password)
    password_entry.pack()

    Label(register_screen, text="").pack()

# 회원가입 버튼 설정

    Button(register_screen, text="회원가입",width=10,height=1,bg="blue",command=register_user).pack()
    
def register_user():        # 회원 정보 기록 함수

    # 아이디와 비밀번호 가져옴
    global username_info
    global password_info
    username_info=username.get()
    password_info=password.get()

    # 회원 정보 기록 파일 생성

    file_list=os.listdir()
    n=0
    for i in range(0,len(file_list)):
        if file_list[i] in username_info:
            n+=1
    if n==0:
        register_success()
    else:
        register_fail()
            
def register_success():
    file = open(username_info,"w") # 파일에 아이디 비밀번호 기록
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    wf=open("{0} work.txt".format(username_info),"w")
    tf=open("{0} time.txt".format(username_info),"w")
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    wf.close()
    tf.close()
    register_screen.destroy()
    messagebox.showinfo("회원가입","회원가입에 성공하였습니다.")    # 회원가입 성공 레이블 설정
def register_fail():
    messagebox.showerror("회원가입","이미 존재하는 아이디 입니다.")
    register_screen.destroy()  
def login():            # 로그인 창 함수
    
    global login_screen
    login_screen=Toplevel(main_account_screen)
    login_screen.title("로그인")
    login_screen.geometry("300x250")
    Label(login_screen, text="회원 정보를 아래에 입력해주십시오.").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify=StringVar()
    password_verify=StringVar()

    global username_login_entry
    Label(login_screen, text="아이디 *").pack()
    username_login_entry=Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()

    global password_login_entry
    Label(login_screen, text="비밀번호 *").pack()
    password_login_entry=Entry(login_screen, textvariable=password_verify,show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen,text="로그인",width=10,height=1,command=login_verify).pack()
    

def login_verify():             # 로그인 검증 함수

#아이디 비밀번호 받아옴
    global username1
    username1=username_verify.get()
    password1=password_verify.get()

# 로그인 버튼을 누를시 항목 삭제
 
    username_login_entry.delete(0,END)
    password_login_entry.delete(0,END)

# listdir() 메소드로 지정된 경로에서 항목의 이름을 포함하는 목록을 반환

    list_of_files=os.listdir()
    global verify
    verify = 0
    
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify=file1.read().splitlines()
        if password1 in verify:
            login_success()             
        else:                       # 비밀번호를 틀렸을 경우
            password_not_recognized()
    else:                           # 아이디를 틀렸을 경우
        user_not_found()
        



def login_success():            # 로그인 성공 창 함수
   
    messagebox.showinfo("로그인","로그인에 성공하였습니다.")
    global id
    id="{0}".format(username1)
    login_screen.destroy()
    main_account_screen.destroy()
    mains()

def password_not_recognized():      # 비밀번호 오류 창 함수

    messagebox.showwarning("로그인","잘못된 비밀번호 입력입니다.")

        
def user_not_found():                   # 아이디 오류 창 함수

    messagebox.showwarning("로그인","존재하지 않는 아이디입니다.")

def door():
    webbrowser.open_new("http://door.deu.ac.kr")
def quit():                         # 종료 함수
    wf=open("{0} work.txt".format(username1),"w")
    tf=open("{0} time.txt".format(username1),"w")
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
    main_screen.geometry("1000x600")
    main_screen.title("과제 관리 프로그램")

    main_screen.resizable(width=0,height=0) 

    work=Label(main_screen,text=" 과제 LIST                                                                                                   User name: {0}".format(username1),font=("맑은고딕",17,"bold"))   
    work.pack(anchor=NW,pady=10,padx=10)

    global worklist
    worklist=Listbox(main_screen,width=75,height=32,relief="solid")
    worklist.pack(side=LEFT,pady=10)
    global timelist
    timelist=Listbox(main_screen,width=25,height=32,relief="solid")
    timelist.pack(side=LEFT,pady=10)

    wf=open("{0} work.txt".format(username1),"r")
    tf=open("{0} time.txt".format(username1),"r")

    user_works=wf.readlines()
    user_times=tf.readlines()

    length=len(user_works)

    for i in range(0,length):
        if user_works[i]!='\n':
            worklist.insert(i,user_works[i])
            timelist.insert(i,user_times[i])
    wf.close()
    tf.close()

    
    add_button=Button(main_screen,text="과제 추가",width=15,height=2,font=("맑은고딕",20,"bold"),command=add)
    add_button.pack()

    work_button=Button(main_screen,text="과제 삭제",width=15,height=2,font=("맑은고딕",20,"bold"),command=delete)
    work_button.pack(pady=10)

    check_button=Button(main_screen,text="DOOR",width=15,height=2,font=("맑은고딕",20,"bold"),command=door)
    check_button.pack(pady=10)

    door_button=Button(main_screen,text="정렬",width=15,height=2,font=("맑은고딕",20,"bold"),command=sort)
    door_button.pack(pady=10)

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

    print("m={0}, d={1}, entry_date={2}, dif_m={3},dif_days={4},now ={5}".format(m,d,entry_date,dif_month,dif_days,now))
    if dif_month==0:
        if dif_days>0:
            if dif_days<10:
                worklist.insert(0,"{0} 일 남음. {1}".format(dif_days,work))
                if d<10:
                    timelist.insert(0,"{0} 월 {1} 일 까지 제출".format(m,d))
                else:
                    timelist.insert(0,"9+) {0} 월 {1} 일 까지 제출".format(m,d))
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


def delete():
    selection=worklist.curselection()
    worklist.delete(selection[0])
    timelist.delete(selection[0])



def main():
    main_account_screen()

if __name__=="__main__":
    main()