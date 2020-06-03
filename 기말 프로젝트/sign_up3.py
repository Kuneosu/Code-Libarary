from tkinter import *
from tkinter import messagebox
import os

def main_account_screen():                              # 메인 창 함수 
    global main_screen
    main_screen = Tk() # 윈도우 창 생성
    main_screen.geometry("300x250") # 윈도우 창 크기 설정
    main_screen.title("회원가입") # 윈도우 창 제목 설정

# 첫 화면 글자 설정

    Label(text="과제 관리 프로그램",bg="blue",width="300",height="2",font=("맑은 고딕",13)).pack()
    Label(text="").pack()

# 로그인 버튼 생성

    Button(text="로그인",height="2",width="30",command=login).pack()
    Label(text="").pack()

# 회원가입 버튼 생성

    Button(text="회원가입",height="2",width="30",command=register).pack()

    main_screen.mainloop() # 윈도우창 실행

def register(): # 회원가입 창 함수

    global register_screen
    register_screen = Toplevel(main_screen)
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
    
    username_info=username.get()
    password_info=password.get()

    # 회원 정보 기록 파일 생성

    file_list=os.listdir()
    for i in range(0,len(file_list)):
        if file_list[i] in username_info:
            messagebox.showerror("회원가입","이미 존재하는 아이디 입니다.")
            register_screen.destroy()
        else:
            file = open(username_info,"w")

            # 파일에 아이디 비밀번호 기록

            file.write(username_info+"\n")
            file.write(password_info)
            file.close()

            username_entry.delete(0,END)
            password_entry.delete(0,END)

            register_screen.destroy()

            # 회원가입 성공 레이블 설정

            messagebox.showinfo("회원가입","회원가입에 성공하였습니다.")

def login():            # 로그인 창 함수
    
    global login_screen
    login_screen=Toplevel(main_screen)
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
    login_screen.destroy()

def password_not_recognized():      # 비밀번호 오류 창 함수

    messagebox.showwarning("로그인","잘못된 비밀번호 입력입니다.")

        
def user_not_found():                   # 아이디 오류 창 함수

    messagebox.showwarning("로그인","존재하지 않는 아이디입니다.")
   

def main():
    main_account_screen()

if __name__=="__main__":
    main()