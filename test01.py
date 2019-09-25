
rewards_ball_t = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '03', '06', '07', '17', '28', '31', '10'], ['2019108', '07', '13', '19', '22', '25', '32', '13']]

my_ball_list_ex0 = [['06', '20', '26', '17', '33', '12'], ['08']]
my_ball_list_ex1 = [['02', '06' ,'15','28'],['10']]
my_ball_list_ex2 = [['12', '23', '06'], ['']]
my_ball_list_ex2 = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '03', '06', '07', '17', '28', '31', '10'], ['2019108', '07', '13', '19', '22', '25', '32', '13']]

  
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
    re_level = 0
    match_count = 0
    for i in range(0,len(my_ball)):
        for k in range(0,len(rewards_ball)):
            for j in range(0,8):
                if my_ball[0][i] == rewards_ball[k][j]:
                    red_ball += 1
                if my_ball[1][0] == rewards_ball[k][7]:
                    blue_ball = 1
    
        rewards_level(red_ball,blue_ball)
        match_count += 1

    return re_level,match_count




a = rewards_cal(rewards_ball_t,my_ball_list_ex0)

print(a)