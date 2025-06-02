import turtle as t

hungry = 0 # 0 ~ 5 까지. 0 = 매우 배고픔, 5 = 매우 배부름
feeling = 0 # -2 ~ 2 까지. -2 = 매우 나쁨, 2 = 매우 좋음
speed = 1.0

def Menu():
    print("1.밥먹기")
    print("2.운동하기")
    print("3.산책가기")
    print("4.대회")
    n = int(input())
    return n

t.shape('turtle')

while True:
    n = Menu()
    t.forward(10)
    
    






