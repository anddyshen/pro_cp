# -*- coding:utf-8 -*-

#自动随机生成双色球号码
import random
from textwrap import dedent


class GenEngine(object):
    

    def __init__(self):
        self.GenEngine = ""
        
    def gen_ball(self):   
        print(dedent("""\n
        ==========================
            """))
        print("\n红球")
        list1 = []
        while True:
            a= random.randint(1,34)
            if a not in list1:
                list1.append(a)
                if len(list1) == 6:
                    print(list1)
                    break
        print("\n==========================")
        print("蓝球")
        b = random.randint(1,17)
        print(f"[{b}]")
        print("==========================")

if __name__ == "__main__":
    a_ball=GenEngine()
    a_ball.gen_ball()

