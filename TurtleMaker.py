import turtle as t
import random

hungry = 2 # 0 ~ 4 까지. 0 = 매우 배고픔, 4 = 매우 배부름
feeling = 0 # -2 ~ 2 까지. -2 = 매우 나쁨, 2 = 매우 좋음
speed = 1.0

def Menu():
    print("1.밥먹기")
    print("2.운동하기")
    print("3.산책가기")
    print("4.대회")
    n = int(input())
    return n

def Better():
    global feeling
    if feeling != 2:
        print("기분이 좋아집니다.")
        feeling += 1
def Worse():
    global feeling
    if feeling != -2:
        print("기분이 나빠집니다.")
        feeling -= 1


def Eat():
    global hungry
    
    if 0 <= hungry <= 1:
        hungry += 1
        Better()
        
    elif 2 <= hungry <= 3:
        hungry += 1
    else:
        print("너무 배부릅니다.")
        Worse()

def Exercise():
    global hungry
    global speed

    if hungry == 0:
        print("운동을 할 힘이 없습니다.")
        Worse()
        return
    
    n = random.randint(1,6)
    
    if n == 1:
        print("완벽한 운동을 해냈습니다")
        speed += 1
        hungry -= 1
    else:
        print("열심히 운동을 했습니다.")
        speed += 0.5
        hungry -= 1

def walk():
    n = random.randint(1,6)

# def end():

t.shape('turtle')

while True:
    n = Menu()
    
    if n == 1:
        Eat()
    elif n == 2:
        Exercise()
    
    
    

    
    
    






