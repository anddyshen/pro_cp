import datetime
import pymysql
from lxml import etree
import requests

backup_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
db_rewards_history_backup = 'rewards_history_backup_'+ backup_time
db_ball_history_backup = 'ball_history_backup_'+ backup_time
db_ball_detail_backup = 'ball_detail_backup_'+ backup_time


def db_backup():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp_backup', charset='utf8')
    cur = conn.cursor()
    try: #每次对比数据库最新数据
        sql0 = 'use cp'
        sql_bk_rewards_history = 'create table '+ db_rewards_history_backup +' SELECT * FROM cp.rewards_history '
        sql_bk_ball_history = 'create table '+ db_ball_history_backup +' SELECT * FROM cp.ball_history '
        sql_bk_ball_detail = 'create table '+ db_ball_detail_backup +' SELECT * FROM cp.ball_detail'
        #cur.execute(sql0)
        cur.execute(sql_bk_rewards_history)
        cur.execute(sql_bk_ball_history)
        cur.execute(sql_bk_ball_detail)
        conn.commit()

        print(f"备份当前数据库操作，成功\n\n")
    except Exception as e:
        print(e)
        print(f"备份数据库清空失败\n\n")
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def fetch_cur_page():
    for i in range(1,2):
        response = requests.get(f"https://www.17500.cn/widget/_ssq/kjlist/p/{i}.html")
        res_html = etree.HTML(response.text)
        
        tr_list = res_html.xpath('//tbody/tr/td')
        tr_ball_list = res_html.xpath('//tbody/tr/td/font')

        row_list = [] #取回后的所有元素，以一维列表形式存储
        for tr in tr_list:
            row_list.append(str(tr.text))  
        
    l_kjqh = row_list[1]

    return l_kjqh
  
a = fetch_cur_page()

print(f"最新一期是 {a} 期")

# rewards_ball_m = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '03', '06', '07', '17', '28', '31', '10'], ['2019108', '07', '13', '19', '22', '25', '32', '13']]
# rewards_ball_t1 = ['2019110', '01', '18', '22', '26', '27', '28', '08']
# rewards_ball_m1 = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '01', '18', '22', '26', '27', '30', '08'], ['2019108','01', '18', '23', '26', '27', '28', '05'], ['2019107','03', '11', '22', '26', '27', '28', '01']]


#m0 = my_ball_list_ex0 = [['06', '20', '26', '17', '33', '12'], ['08']]
# m0 = my_ball_list_ex0 = [[ '01','18','22', '26', '27', '28'], ['08']]
# m1 = my_ball_list_ex1 = [['02', '06' ,'15','28'],['10']]
# m2 = my_ball_list_ex2 = [['01', '22', '26','28'], ['']]
# m3 = my_ball_list_ex2 = [[['01', '18', '22', '26', '27', '28'], ['08']], [['12', '23', '06'], ['']], [['01', '18', '22', '26', '27', '28'], ['05']],[['01', '18', '22', '26', '27'], ['08']],[['03', '06', '07', '17', '28', '31'], ['10']], [['07', '13', '19', '22', '25', '32'], ['13']]]
# m4 = my_ball_list_ex2 = [[['01', '18', '22', '26', '27', '28'], ['08']], [['12', '23', '06'], ['']], [['01', '18', '22', '26', '27', '28'], ['05']],[['01', '18', '22', '26', '27'], ['08']],[['03', '06', '07', '17', '28', '31'], ['10']], [['07', '13', '19', '22', '25', '32'], ['13']]]
