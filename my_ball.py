import datetime
import pymysql

class MyBall(object):
    

    def __init__(self):
        self.MyBall = ""

    """
    def isInt(num):
        try:
            num = int(str(num))
            return isinstance(num, int)
        except:
            return False

    """

    def isredok(self,num):
        try:
            num = int(str(num))
            return isinstance(num, int) and num < 34 and num >0
        except:
            return False

    def isrepeat(self,num,lst):
        try:
            for i in range(0,len(lst)):
                if int(num) == int(lst[i]):
                    return  True
        except:
            return False

    def isblueok(self,num):
        try:
            num = int(str(num))
            return isinstance(num, int) and num <= 16 and num >0
        except:
            return False



    def input_my_ball(self):
        red_ball = []
        x = 1
        cs =20 #尝试次数

        for i in range(1,20):
            a = input(f"请输入第{x}个红球号码:")

            if MyBall.isredok(self,a)== True or a == "":
                if MyBall.isrepeat(self,a,red_ball) == True:
                    print("与之前的输入数字有重复,重新输入")
                else:
                    red_ball.append(a)
                    x += 1
            else:
                print("请输入1-33之间的数字,重新输入")

            if  len(red_ball) >= 6 or i == cs:
                if i == cs:
                    print(f"输入次数超过{cs}次，退出")
                break

        print(f"你输入的红球号码是：{red_ball}")


        blue_ball = []
        for i in range(1,6):
            blue_ball_t = input(f"请输入一个蓝球号码：")
            if MyBall.isblueok(self,blue_ball_t) == True or blue_ball_t == "":
                blue_ball.append(blue_ball_t)
                print(f"蓝球号码为{blue_ball}")
                break
            else:
                print("请输入1-16之间的数字,重新输入")
                x += 1

                if x == cs: 
                    print(f"输入次数超过{cs}次，退出")
                    break


        for i in range(len(red_ball)-1, 0, -1):
            if red_ball[i] == "":
                red_ball.pop(i)
            else:
                pass


        my_all_ball = []

        my_all_ball.append(red_ball)
        my_all_ball.append(blue_ball)

        print(f"你最终输入的红+蓝球号码是：{my_all_ball}")

        my_input = my_all_ball
        return my_all_ball

    
if __name__ == "__main__":
    my_ball_run = MyBall()
    my_ball_run.input_my_ball()