import random

answer = random.randint(1,10)
temp = input("轻输入一个数字：")
guess = int(temp)
if guess>answer:
    print("大了")
else:
    if guess < answer:
        print("小了")
    else:
        print("猜对了")   
while guess != answer:
    temp = input("错了，轻重新输入：")
    guess = int(temp)
    if guess>answer:
        print("大了")
    else:
        if guess < answer:
            print("小了")
        else:
            print("猜对了")          
print("游戏结束")                    
                    
                    
