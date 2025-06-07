import turtle as t
import random

hungry = 2 # 0 ~ 4 까지. 0 = 매우 배고픔, 4 = 매우 배부름
feeling = 0 # -2 ~ 2 까지. -2 = 매우 나쁨, 2 = 매우 좋음
speed = 1.0

# text 업데이트를 위한 함수
def UpdateText(text = None): # 처음으로 메서드가 실행될 때 create_text 를 실행하기 위해서 디폴트 값을 설정
    global hungry
    global feeling
    global speed

    x = -570 # 초기화 상태(hunger = 보통, mood = 보통)때 텍스트가 좌 상단에 위치하기 위한 x 좌표
    y = -490 # 텍스트가 좌 상단에 위치하기 위한 y 좌표
    if hungry == 0 or hungry == 4: # 표기되는 텍스트가 조금 길어져서 좌 상단에 위치하기 위해서 x 좌표 조정
        x = -545
    elif feeling == -2 or feeling == 2 or hungry == 1 or hungry == 3: # 표기되는 텍스트가 조금 길어져서 좌 상단에 위치하기 위해서 x 좌표 조정
        x = -555
    
    screen = t.Screen()
    canvas = screen.getcanvas()
    if text == None: # 처음 실행하면 text 를 만듬.
        text = canvas.create_text(x,y,text = '',font = ("Arial", 14))

    # 배고픔에 따라서 표기되는 상태를 다르게 함.
    if hungry == 0:
        hunger = "매우 배고픔"
    elif hungry == 1:
        hunger = "배고픔"
    elif hungry == 2:
        hunger = "보통"
    elif hungry == 3:
        hunger = "배부름"
    elif hungry == 4:
        hunger = "매우 배부름"
    
    # 기분에 따라서 표기되는 상태를 다르게 함.
    if feeling == -2:
        mood = "매우 나쁨"
    elif feeling == -1:
        mood = "나쁨"
    elif feeling == 0:
        mood = "보통"
    elif feeling == 1:
        mood = "좋음"
    elif feeling == 2:
        mood = "매우 좋음"

    canvas.coords(text,x,y) # 바꾼 x,y 좌표를 반영
    canvas.itemconfig(
        text,
        text = f'허기 : {hunger}\n기분 : {mood}\n속도 : {speed}'
        # 바뀐 hunger, mood, speed 값을 반영.
    )

    return text # text 를 반환해서 처음 이후론 text를 매개변수로 줄 수 있도록 함.

def Menu():
    print("1.밥먹기")
    print("2.운동하기")
    print("3.산책가기")
    print("4.대회")
    n = int(input())
    return n

# feeling 관련 함수
def Better(): # 기분 +1
    global feeling
    if feeling != 2: # 기분이 최대치면 더는 올리지 않음.
        feeling += 1
def Worse(): # 기분 -1
    global feeling
    if feeling != -2: # 기분이 최저값이면 더는 내리지 않음.
        feeling -= 1


# 밥먹기
def Eat():
    global hungry
    
    if 0 <= hungry <= 1: # 배고플때 밥을 먹으면 배고픔 +1, 기분 +1
        hungry += 1
        print("밥을 매우 맛있게 먹었습니다.")
        Better()
        
    elif 2 <= hungry <= 3: # 보통 or 배부름 상태일 땐 배고픔 +1
        hungry += 1
    else: # 배고픔이 최대값일 때 먹으면 배고픔 값은 그대로, 기분 -1
        print("너무 배부릅니다.")
        Worse()

# 운동하기
def Exercise():
    global hungry
    global speed
    global feeling

    if hungry == 0: # 배고픔이 0이면 운동 x, 기분 -1
        print("운동을 할 힘이 없습니다.")
        Worse()
        return
    
    if feeling == -2: # 기분이 최저면 운동 x
        print("거북이가 운동을 하고싶어하지 않습니다.")
        return
    
    n = random.randint(1,6) # 랜덤 이벤트를 위한 n
    
    if n == 1: # 1/6 확률로 속도 +1, 기분 +1, 배고픔 -1
        print("완벽한 운동을 해냈습니다")
        speed += 1
        hungry -= 1
        Better()
    else: # 속도 +0.5, 기분 -1, 배고픔 -1
        print("열심히 운동을 했습니다.")
        speed += 0.5
        hungry -= 1
        Worse()

# 산책가기
def Walk(player):
    n = random.randint(1,10) # 랜덤 이벤트를 위한 n

    # 플레이어가 해당 이벤트를 한 적이 없고 n == 1 이면 특수 이벤트 발생.
    # 거북이 색이 gold 로 바뀌고 기분 +2
    if n == 1 and player.fillcolor() == 'black':
        print("산책 중에 보물을 발견했습니다!")
        print("거북이의 몸에 변화가 생깁니다.")
        player.fillcolor('gold')
        Better()
        Better()
    else: # 기분 +1
        print("즐겁게 산책을 마쳤습니다.")
        Better()
        

# def end():

player = t.Turtle()
player.shape('turtle')
text = UpdateText() # 첫 실행이므로 매개변수로 아무것도 전달하지 않음.


while True:
    text = UpdateText(text) # 첫 실행이 아니므로 text 값을 전달해서 업데이트 하도록 함.
    n = Menu()

    if n == 1:
        Eat()
    elif n == 2:
        Exercise()
    elif n == 3:
        Walk(player)