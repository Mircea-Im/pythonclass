# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.
# 입력 시간은 24시간 표현을 사용한다.
# 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

while True:
    real_time = [0,0]
    alarm_time = [0,0]
    input_hour = int(input("HOUR : "))
    if input_hour > 23 :
        print("잘못 입력하셨습니다! - 프로그램 종료")
        break
    input_min = int(input("MINUTE : "))
    if input_min > 59 :
        print("잘못 입력하셨습니다! - 프로그램 종료")
        break
    real_time[0]= input_hour
    real_time[1] = input_min
    print(f"입력 시간 = {real_time[0]}:{real_time[1]}")
    if (real_time[1] - 45) < 0 :
        alarm_time[0] = real_time[0] - 1
        if alarm_time[0] < 0 :
            alarm_time[0] = alarm_time[0] + 24
        alarm_time[1] = real_time[1] + 15
    elif real_time[1] - 45 == 0:
        alarm_time[0] = real_time[0]+
        alarm_time[1] = 0
    else :
        alarm_time[0] = real_time[0]
        alarm_time[1] = real_time[1] - 45
    print(f"알람 설정 = {alarm_time[0]}:{alarm_time[1]}")

