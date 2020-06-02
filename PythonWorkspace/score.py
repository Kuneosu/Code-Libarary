def main(): # 메뉴 선택 및 함수호출을 위한 메인함수
    
    rows=3 # 행 값 3으로 지정
    cols=5 # 열 값 5로 지정
    
    kor_score=[]   #
    math_score=[]  #  과목별 점수를 담아두기 위한 리스트
    eng_score=[]   #
 
    midterm_score=[kor_score,math_score,eng_score]      # 모든 점수를 담아두기 위한 리스트
    midterm_score=[([0]*cols)for rows in range(rows)]   # 리스트의 2차원 배열 크기 지정, 리스트 초기화
    
    student_score=[0,0,0,0,0]   # 평균 값을 담아두기 위한 리스트       

    menu = 0 # 메뉴 선택을 위한 변수

    while True: # 종료 (9) 를 입력하기 전까지 반복하는 반복문
        print("-----------------")
        print("1. 성적입력")               # 
        print("2. 평균계산")               #     메뉴 선택 화면
        print("3. 전체성적출력")           #   
        print("9. 종료")                   #
        menu=int(input("메뉴를 선택하시오: "))  # 선택 값을 입력받음
        if menu==1: # 1을 입력받은 경우
            kor_score,math_score,eng_score,midterm_score=add(kor_score,math_score,eng_score,midterm_score)
            # add 함수를 불러와 return 값으로 각 과목별 성적과 모든 점수를 담은 리스트값을 반환받음
        elif menu==2: # 2를 입력받은 경우
            student_score=avg(midterm_score) # avg 함수에 앞에서 반환받은 점수 리스트를 대입하여 호출. 평균값을 반환받음
            print(student_score)    # 평균값 출력
        elif menu==3: # 3을 입력받은 경우
            print(midterm_score) # 모든 점수 출력
        elif menu==9: # 9를 입력받은경우
            print("프로그램을 종료합니다.") 
            break  # 반복 루프 탈출, 프로그램 종료
        else: # 이외의 값을 입력받은 경우
            print("잘못된 입력입니다.") 
            
def avg(a): # 평균값을 계산하는 함수, 인수로 전체 점수 사용

    rows=5 # 행 값 5로 지정
    cols=3 # 열 값 3으로 지정
    s=[0,0,0,0,0] # 점수의 합을 담아두기 위한 리스트
    average=[0,0,0,0,0] # 평균값을 담아두기 위한 리스트

    for i in range(rows):      #
        for j in range(cols):  # 반복문을 통해 점수 리스트에서
            value=a[j][i]      # 필요한 점수들을 불러와 합하여
            s[i]+=value        # s 리스트에 저장.
        val=s[i]/3             # 저장된 s 리스트의 합을 3으로 나누어 구한
        average[i]+=val        # 평균값을 average에 저장
        
    return average # 평균값 반환

def add(k,m,e,a): # 성적을 입력하는 함수
    k=[] # 
    m=[] # 과목별 성적을 담아두는 리스트
    e=[] #
    a=[k,m,e] # 전체 성적을 담아두는 리스트
    t=['국어','수학','영어'] # 성적을 입력받을 때 출력할 과목명 리스트

    for i in range(3):                      #
        print(t[i])                         # 주기별로 과목명 출력
        for j in range(5):                  #
            print("성적 [",j,end="")        # 
            value=int(input(" ] 입력:"))    # 성적 입력받음
            a[i].append(value)              # 입력받은 성적을 a리스트에 저장
        print("")                           # 줄바꿈을 위한 공백 출력

    return k,m,e,a # 과목별 성적 리스트와 전체 성적 리스트를 반환



if __name__=="__main__":
    main()            # 메인함수 호출