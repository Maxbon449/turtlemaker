import turtle as t
import random

hungry = 2 # 0 ~ 4 까지. 0 = 매우 배고픔, 4 = 매우 배부름
feeling = 0 # -2 ~ 2 까지. -2 = 매우 나쁨, 2 = 매우 좋음
speed = 1.0

# 대회에서 경쟁할 거북이를 만드는 함수.
def MakeEnemy():
    t1 = t.Turtle()
    t2 = t.Turtle()
    t3 = t.Turtle()
    t4 = t.Turtle()

    arr = (t1,t2,t3,t4) # 만든 거북이를 배열에 담음.
    t.colormode(255)

    for i in range(4):
        arr[i].hideturtle() # 거북이가 보이지 않게함.
        arr[i].shape('turtle')
        arr[i].penup() # 거북이가 선을 그리지 않게함.
        arr[i].color(random.randint(0,255),random.randint(0,255),random.randint(0,255)) # 거북이마다 랜덤한 색깔
    return arr # 거북이를 담은 배열을 반환

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
        
# 대회 나가기
def end(arr):
    global speed
    global feeling
    
    arrSpeed = [0,0,0,0] # 경쟁 거북이들의 속도를 담음.
    # 경쟁 거북이들과 주인공 거북이를 출발점에 놓음
    arr[0].goto(-500,40)
    arr[1].goto(-500,20)
    arr[2].goto(-500,-20)
    arr[3].goto(-500,-40)
    
    player.goto(-500,0)
    # 경쟁 거북이들의 속도를 랜덤하게 결정 및 거북이들을 보이게 만듬.
    for i in range(4):
        arrSpeed[i] = random.randint(10,20)
        arr[i].showturtle()
    
    while True:
        player.forward(speed+feeling*2) # speed + feeling * 2 만큼 앞으로 나감.
        if(player.xcor() >= 400): # 주인공 거북이가 먼저 목표한 위치에 도달하면 승리
            print("축하합니다! 대회에서 우승했습니다!")
            return -1 # 승리를 알리기 위해 -1 반환
        
        for i in range(4):
            arr[i].forward(arrSpeed[i])
            if(arr[i].xcor() >= 400): # 경쟁 거북이들중 한 마리라도 먼저 도착하면 패배.
                print("아쉽습니다. 다음에 다시 도전해보세요.")
                for j in range(4): # 경쟁 거북이들을 다시 숨김
                    arr[j].hideturtle()
                player.goto(0,0) # 플레이어를 다시 원점에 가져다 놓음.
                return 0 # 패배를 알리기 위해 0 반환

player = t.Turtle() # 주인공 거북이 생성
player.shape('turtle')
player.penup() 
text = UpdateText() # 첫 실행이므로 매개변수로 아무것도 전달하지 않음.
arr = MakeEnemy() # 경쟁 할 거북이들이 담긴 배열

while True:
    text = UpdateText(text) # 첫 실행이 아니므로 text 값을 전달해서 업데이트 하도록 함.
    n = Menu()

    if n == 1:
        Eat()
    elif n == 2:
        Exercise()
    elif n == 3:
        Walk(player)
    elif n == 4:
        x = end(arr) # 승리를 감지하기 위한 변수 x
        if x == -1: # 만약 승리했다면 while 문을 종료함. 아니면 계속 반복.
            break