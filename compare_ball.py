# -*- coding:utf-8 -*-

import my_ball
import history_data_load
import datetime
import pymysql

def compare_ball():

    a = ""
    #输入自己的号码
    my_input = my_ball.MyBall.input_my_ball(a)#class 中 self的参数传递尚未搞清楚，先用为空的a作为参数传入，日后修改，暂时使用无问题
    #取得需要的开奖期数的号码
    rewards_ball_list = history_data_load.LoadSsqEngine.load_history(a)#同上


    awards_level = ""
    cal_r = ""
    match_count = 0
    awards_count = 0
    
    def rewards_level(red_ball,blue_ball):#奖项对比
        rewards_level = 0

        if red_ball == 6 and blue_ball == 1:
            rewards_level = 1
        else:
            if red_ball == 6 and blue_ball == 0:
                rewards_level = 2
            else:
                if red_ball == 5 and blue_ball == 1:
                    rewards_level = 3
                else:
                    if red_ball == 5 and blue_ball == 0:
                        rewards_level = 4
                    else: 
                        if red_ball == 4 and blue_ball == 1:
                            rewards_level = 4
                        else:
                            if red_ball == 4 and blue_ball == 0:
                                rewards_level = 5
                            else:
                                if red_ball == 3 and blue_ball == 1:
                                    rewards_level = 5
                                else:
                                    if red_ball < 4 and blue_ball == 1:
                                        rewards_level = 6


        return rewards_level

    def rewards_cal(rewards_ball,my_ball):#单期对奖，取本人选择号码与对应奖期对奖，得到奖结果
        red_ball = 0
        blue_ball = 0
        sNo = ""
        award_results = ""

        for i in range(0,len(my_ball[0])):
            for j in range(1,len((rewards_ball))):
                if my_ball[0][i] == rewards_ball[j-1]:
                    red_ball += 1
                if my_ball[1][0] == rewards_ball[7]:
                    blue_ball = 1
                    
        if red_ball >= 4 or blue_ball == 1 :
            sNo = rewards_ball[0]
        else:
            sNo = "no award"

        award_results = [red_ball,blue_ball,sNo]
            
        return award_results


    award_results_t = []

    for k in range(0,len(rewards_ball_list)):#计算统计一个号码与多期对比中奖结果
        rewards_r = rewards_cal(rewards_ball_list[k],my_input)
        awards_level = rewards_level(rewards_r[0],rewards_r[1])
        if awards_level > 0 :
            awards_count += 1
        x = [rewards_r[2],awards_level]
        award_results_t.append(x)

    print_r = ""
    y = 0
    max_awards = 6
    max_awards_num = 0
    v = 0
    for u in range(0,len(award_results_t)):
        if award_results_t[u][1] > 0 :
            if award_results_t[u][1] <= max_awards :
                max_awards = award_results_t[u][1]
                max_awards_num += 1
                if max_awards < award_results_t[v][1]:
                    max_awards_num = 1
                v = u

            print_r = print_r + "\n 第 " + str(award_results_t[u][0]) + " 期 1 注 " + str(award_results_t[u][1]) +" 等奖；  "
            y += 1

    if awards_count == 0:
        print(f"很遗憾你的号码没有中奖\n\n")
    else:
        print(f" 恭喜 , 你中了 {print_r} \n  共  {y} 注奖项，最大奖项为 {max_awards} 等奖 共中得 {max_awards_num} 注\n\n")



if __name__ == "__main__":
    compare_ball()
    r = input("请输入quit退出，其他任意键继续核对下一条彩票 :>>")
    if r == "quit":
        exit()
    else:    
        compare_ball()
