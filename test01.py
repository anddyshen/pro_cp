
rewards_ball_t = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '03', '06', '07', '17', '28', '31', '10'], ['2019108', '07', '13', '19', '22', '25', '32', '13']]

m0 = my_ball_list_ex0 = [['06', '20', '26', '17', '33', '12'], ['08']]
m1 = my_ball_list_ex1 = [['02', '06' ,'15','28'],['10']]
m2 = my_ball_list_ex2 = [['12', '23', '06'], ['']]
m3 = my_ball_list_ex2 = [['01', '18', '22', '26', '27', '28'], ['08']], [['12', '23', '06'], ['']], [['01', '18', '22', '26', '27', '28'], ['05']],[['01', '18', '22', '26', '27'], ['08']],[['03', '06', '07', '17', '28', '31'], ['10']], [['07', '13', '19', '22', '25', '32'], ['13']]

  
def rewards_level(red_ball,blue_ball):
    rewards_level = 0
    if red_ball <= 2 and blue_ball == 1:
        rewards_level = 6
    if red_ball == 3 and blue_ball == 1:
        rewards_level = 5
    if red_ball == 4 and blue_ball == 0:
        rewards_level = 5
    if red_ball == 4 and blue_ball == 1:
        rewards_level = 4
    if red_ball == 5 and blue_ball == 0:
        rewards_level = 4
    if red_ball == 5 and blue_ball == 1:
        rewards_level = 3
    if red_ball == 6 and blue_ball == 0:
        rewards_level = 2
    if red_ball == 6 and blue_ball == 1:
        rewards_level = 1
    
    return rewards_level


def rewards_cal(rewards_ball,my_ball):
    red_ball = 0
    blue_ball = 0
    award_results = []
    match_count = 0
    awards_count = 0
    sNo = ""
    award_results = []
    award_results_t = []
    award_results_t1 = []
    for i in range(0,len(rewards_ball)):#总选择的中奖历史号码的注数，每一注都是标准，每个号码都去对一遍
        award_results_t1 = rewards_ball_t[i]
        for j in range(0,len(my_ball)):#总输入的所有号码注数，有几注对几次 
            my_ball_t = my_ball[j]
            #for k in range(0,len(my_ball_t)):#取出第j(一注)标准答案，分割这个标注答案
            #my_ball_split = my_ball_t[1]
            for m in range(0,len(my_ball_t[0])):#分拆当前自选注
                if my_ball_t[0][m] == award_results_t1[m+1]:
                    red_ball += 1
                if my_ball_t[1][0] == award_results_t1[7]:
                    blue_ball = 1
                
                if red_ball >= 4 or blue_ball == 1:
                    sNo = award_results_t1[0]

                a = rewards_level(red_ball,blue_ball)
                awards_count += 1
            red_ball = 0
            blue_ball = 0

            award_results_t.append(sNo)
            award_results_t.append(a)
    
        award_results.append(award_results_t)

#match_count += 1    

    return award_results 
    



a = rewards_cal(rewards_ball_t,m3)

print(f"中奖结果列表：{a} \n\n")

print(f"你所选的号码在过去的 {len(rewards_ball_t)} 期中，")#中了 {a[0]} 注 {a[1]} 等奖")