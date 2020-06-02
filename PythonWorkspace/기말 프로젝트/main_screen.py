from tkinter import *

main_screen=Tk()
main_screen.geometry("1000x600")
main_screen.title("과제 관리 프로그램")

main_screen.resizable(width=0,height=0)
n=8
name="김권수"
work=Label(main_screen,text=("  과제 List                                                 \
                     ( 남은 과제 : {0} 개 )             User : {1}".format(n,name)) \
                             ,font=("맑은고딕",16,"bold"))
work.pack(anchor=NW,pady=10,padx=10)

worklist=Listbox(main_screen,width=100,height=35)
worklist.pack(side=LEFT,pady=10)

work_button=Button(main_screen,text="과제 관리",width=15,height=2,font=("맑은고딕",20,"bold"))
work_button.pack(pady=10)

check_button=Button(main_screen,text="전체 과제 현황",width=15,height=2,font=("맑은고딕",20,"bold"))
check_button.pack(pady=10)

door_button=Button(main_screen,text="DOOR",width=15,height=2,font=("맑은고딕",20,"bold"))
door_button.pack(pady=10)

set_button=Button(main_screen,text="설정",width=15,height=2,font=("맑은고딕",20,"bold"))
set_button.pack(pady=10)

exit_button=Button(main_screen,text="종료",width=15,height=2,font=("맑은고딕",20,"bold"))
exit_button.pack(pady=10)

main_screen.mainloop()