
rewards_ball_m = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '03', '06', '07', '17', '28', '31', '10'], ['2019108', '07', '13', '19', '22', '25', '32', '13']]
rewards_ball_t1 = ['2019095', '02', '05', '14', '19', '21', '28', '01']
rewards_ball_m1 = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '01', '18', '22', '26', '27', '30', '08'], ['2019108','01', '18', '23', '26', '27', '28', '05'], ['2019107','03', '11', '22', '26', '27', '28', '01']]


#m0 = my_ball_list_ex0 = [['06', '20', '26', '17', '33', '12'], ['08']]
m0 = my_ball_list_ex0 = [[ '01','02','03', '04', '05', '06'], ['01']]
m1 = my_ball_list_ex1 = [['02', '06' ,'15','28'],['10']]
m2 = my_ball_list_ex2 = [['01', '22', '26','28'], ['']]
m3 = my_ball_list_ex2 = [[['01', '18', '22', '26', '27', '28'], ['08']], [['12', '23', '06'], ['']], [['01', '18', '22', '26', '27', '28'], ['05']],[['01', '18', '22', '26', '27'], ['08']],[['03', '06', '07', '17', '28', '31'], ['10']], [['07', '13', '19', '22', '25', '32'], ['13']]]
m4 = my_ball_list_ex2 = [[['01', '18', '22', '26', '27', '28'], ['08']], [['12', '23', '06'], ['']], [['01', '18', '22', '26', '27', '28'], ['05']],[['01', '18', '22', '26', '27'], ['08']],[['03', '06', '07', '17', '28', '31'], ['10']], [['07', '13', '19', '22', '25', '32'], ['13']]]

awards_level = ""
cal_r = ""
match_count = 0
awards_count = 0
  
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

my_ball_input = m0
award_results_t = []

for k in range(0,len(rewards_ball_t1)):#计算统计一个号码与多期对比中奖结果
    rewards_r = rewards_cal(rewards_ball_t1,my_ball_input)
    awards_level = rewards_level(rewards_r[0],rewards_r[1])
    if awards_level > 0 :
        awards_count += 1
    x = [rewards_r[2],awards_level]
    award_results_t.append(x)

print_r = ""
for u in range(0,len(award_results_t)):
    if award_results_t[u][1] != 0 :
        print_r = print_r + "第 " + str(award_results_t[u][0]) + " 期 1 注 " + str(award_results_t[u][1]) +" 等奖； "

if awards_count == 0:
    print(f"很遗憾你的号码没有中奖\n\n")
else:
    print(f"恭喜,你中了{print_r}\n\n")
