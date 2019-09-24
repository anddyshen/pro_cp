def isok(num):
    try:
        num = int(str(num))
        return isinstance(num, int) and num < 34 and num >0
    except:
        return False

def isrepeat(num,lst):
    try:
        for i in range(0,len(lst)):
            if int(num) == int(lst[i]):
                return  True
    except:
        return False



my_ball = []
x = 1
cs =20 #尝试次数

for i in range(1,20):
    a = input(f"请输入第{x}个篮球号码:")

    if isok(a)== True:
        if isrepeat(a,my_ball) == True:
            print("与之前的输入数字有重复,重新输入")
        else:
            my_ball.append(int(a))
            x += 1
    else:
        print("错误的输入类型,重新输入")

    


    if  len(my_ball) >= 6 or i == cs:
        if i == cs:
            print(f"输入次数超过{cs}次，退出")
        break
    
print(f"你输入的号码是：{my_ball}")