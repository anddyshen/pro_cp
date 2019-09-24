import datetime
import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
cur = conn.cursor()

"""
def isInt(num):
    try:
        num = int(str(num))
        return isinstance(num, int)
    except:
        return False

"""

def isredok(num):
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

def isblueok(num):
    try:
        num = int(str(num))
        return isinstance(num, int) and num < 16 and num >0
    except:
        return False


red_ball = []
x = 1
cs =20 #尝试次数

for i in range(1,20):
    a = input(f"请输入第{x}个红球号码:")

    if isredok(a)== True or a == "":
        if isrepeat(a,red_ball) == True:
            print("与之前的输入数字有重复,重新输入")
        else:
            red_ball.append(a)
            x += 1
    else:
        print("错误的输入类型,重新输入")

    if  len(red_ball) >= 6 or i == cs:
        if i == cs:
            print(f"输入次数超过{cs}次，退出")
        break

print(f"你输入的红球号码是：{red_ball}")


blue_ball = []
for i in range(1,6):
    blue_ball_t = int(input(f"请输入一个蓝球号码："))    
    if isblueok(blue_ball_t) == True:
        blue_ball.append(blue_ball_t)
        print(f"蓝球号码为{blue_ball}")
        break
    else:
        print("错误的输入类型,重新输入")
        x += 1

        if x == cs: 
            print(f"输入次数超过{cs}次，退出")
            break

all_ball = []

all_ball.append(red_ball)
all_ball.append(blue_ball)

print(f"你输入的红+蓝球号码是：{all_ball}")



try:
    sql = 'select * from ball_detail where kjqh = 0000'
    cur.execute(sql)
    conn.commit()
    print(f"读取了所有确认的期号号码的数据\n\n")
except Exception as e:
    print(e)
    print(f"读取数据库失败\n\n")
    conn.rollback()
finally:
    cur.close()
    conn.close()