from tkinter import *
from tkinter import messagebox

def msgbox():
    messagebox.showinfo("안내","아직 지원하지 않습니다.")
def quit():
    root.destroy()
    root.quit()

def area():
    
    def circle():           # 원의 넓이를 구하여 출력하는 함수
        radius=e1.get()
        if not radius.isdigit():    # radius가 숫자가 아닐 경우
            messagebox.showerror("입력 실패","반지름을 입력하세요.")
        else:
            radius=float(radius) # 입력받은 e1.get()값을 float으로 형변환
            cir=radius**2*3.14     # 원의 넓이를 구하여 cir에 저장 
            e2.insert(0,str(cir))  # str로 형변환한 cir값을 e2에 추가

    def reset():            # 초기화를 위한 reset()함수
        e1.delete(0,END)
        e2.delete(0,END)    # e1과 e2의 엔트리 값을 모두 초기화

    def close():            # 종료 함수
        window.destroy()

    window=Tk()
    rad=Label(window,text="원의 반지름")
    res=Label(window,text="원의 넓이")
    rad.grid(row=0)
    res.grid(row=1)

    e1=Entry(window)
    e2=Entry(window)

    e1.grid(row=0,column=1,columnspan=2) # 반지름 입력 칸 출력
    e2.grid(row=1,column=1,columnspan=2) # 넓이 출력 칸 출력

    b1=Button(window,text='원 넓이 계산', command=circle) # 버튼 클릭 시 circle() 함수 실행
    b1.grid(row=2,column=0,sticky=W)    # 원 넓이 계산 버튼 출력

    b2=Button(window,text='초기화', command=reset) # 버튼 클릭 시 reset() 함수 실행
    b2.grid(row=2,column=1,sticky=N)    # 초기화 버튼 출력

    b3=Button(window,text='종료',command=close)
    b3.grid(row=2,column=2)

    window.mainloop()

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

