import os, csv, re
import pandas as pd
from bs4 import BeautifulSoup

def re_place(tag):
    for i in tag:
        pattern = re.compile(r'\s+')
        sentence = re.sub(pattern,'', i)
    return sentence

def pick_sort(rate):
    rate = float(re.sub("%",' ', (rate)))
    if rate >= 1:
        return rate
    else:
        return False

def sort_data():
    for i in range(1,4):
        path_dir = "/Users/yoonyoungho/Documents/bigdata/lolpsData_v11.2"+str(i)
        file_list = os.listdir(path_dir)
        for j in file_list:
            page = open(path_dir+'/'+j, 'rb', encoding='euc-kr').read()
            soup = BeautifulSoup(page, 'html.parser')
            for i in range(0,5):
                try:
                    lane = soup.select('div.radio-container input')[i]['checked']
                    select_rate = soup.select('div.radio-container b')[i].text
                    sort_rate = pick_sort(select_rate)
                    if (sort_rate == False):
                        print(select_rate)
                        os.remove(path_dir+'/'+j)
                except:
                    continue


#lol.ps에서 수집한 데이터 가공.
def ps_data():
    for i in range(1,4):
        path_dir = "/Users/yoonyoungho/Documents/bigdata/lolpsData_v11.2"+str(i)
        file_list = os.listdir(path_dir)
        list1=[]
        # df = pd.DataFrame(incolumns=['name', 'position', 'win_rate', 'pick_rate', 'ban_rate', 'champ_rank', 'hard_champ', 'easy_champ'])
        for j in file_list:
            try:
                page = open(path_dir+'/'+j, 'rb').read()
                soup = BeautifulSoup(page, 'html.parser')
                name = re_place(soup.select('div.header h3')[0])
                # print(name)
        
                for r in range(0,5):
                    if str(r) in j :
                        if r==0: position = '탑'
                        elif r==1: position = '정글'
                        elif r==2: position = '미드'
                        elif r==3: position = '원딜'
                        else: position = '서폿'
                
                percent = soup.select('div.percent p')
                
                win_rate = re_place(percent[0])
                pick_rate = re_place(percent[1])
                ban_rate = re_place(percent[2])
                champ_rank = re_place(soup.select('div.ranking b')[1])
                hard_info = soup.select('div.versus-difficult div.champ-info')
                
                easy_info = soup.select('div.versus-easy div.champ-info')
                hard_champ = []
                easy_champ = []
                for s in range(0,len(hard_info)):
                    sort_hard = hard_info[s].get_text().strip()
                    sort_easy = easy_info[s].get_text().strip()
                    hard_champ.append(sort_hard)
                    easy_champ.append(sort_easy)
                fieldnames=['position', 'name', 'win_rate', 'pick_rate', 'ban_rate', 'champ_rank', 'hard_champ', 'easy_champ']
                list1=[position, name, win_rate, pick_rate, ban_rate, champ_rank, hard_champ, easy_champ]
                # print(l)
                # df = pd.DataFrame(data =, columns=fieldnames)
                # df.to_csv("/Users/yoonyoungho/Documents/bigdata/lolps.csv", 'a', encoding='euc-kr')
                with open("/Users/yoonyoungho/Documents/bigdata/lolps.csv", 'a', encoding='utf-8') as f:
                    write = csv.writer(f)
                    write.writerow(list1)
            except:
                continue
            
def gg_data():
    path_dir = "/Users/yoonyoungho/Documents/bigdata/opggData/"
    file_list = os.listdir(path_dir)
    for x in file_list:
        try:
            with open("/Users/yoonyoungho/Documents/bigdata/opggData/"+x, "r", encoding='utf-8') as f:
                datas = [l.strip() for l in f.readlines()]
            data = []         
            list1 = []
            cnt = 0
            for i in datas:
                if i == '솔랭':
                    if cnt != 1:
                        data.append(i)
                        cnt = 1
                    else: 
                        list1.append(data) 
                        data = []
                        data.append(i)
                elif (i == '일반' or i == '무작위 총력전' or i == '단일 챔피언' or  i == '자유 5:5 랭크' or 
                    i == '우르프' or i == '격전' or i == 'AI 상대 대전'):
                    if cnt == 1:
                        list1.append(data)
                        data = []
                        cnt = -1
                else:
                    if cnt == 1: 
                        data.append(i)
            
            with open("/Users/yoonyoungho/Documents/bigdata/opggCsv/opgg.csv", 'a', encoding='euc-kr') as f:
                write = csv.writer(f)
                for j in list1:
                    write.writerow(j)
        except:
            continue

def dup_sort():
    with open("/Users/yoonyoungho/Documents/bigdata/opggCsv/opgg.csv", "r", encoding='euc-kr') as f:
        read = csv.reader(f)
        data = list(read)
    idx=0
    for x in data:
        for y in data:
            idx+=1
            if x[37:98] == y[37:98] or x[37:98] == y[106:167]:
                if x == y:
                    continue
                else:
                    del data[idx-1]
        idx=0
    with open("/Users/yoonyoungho/Documents/bigdata/opGG/opgg.csv", 'a', encoding='euc-kr') as f:
            write = csv.writer(f)
            for i in data:
                write.writerow(i[0:170])

def opgg_process1():
    with open("/Users/yoonyoungho/Documents/bigdata/opGG/opgg.csv", 'a', encoding='euc-kr') as f:
            write = csv.writer(f)
            for i in data:
                write.writerow(i[0:170])

def opgg_process():
    with open("/Users/yoonyoungho/Documents/bigdata/opggCsv/opgg.csv", "r", encoding='euc-kr') as f:
            read = csv.reader(f)
            data = list(read)
    list1=[]
    list2=[]
    list3=[]

    for x in data:
        try:
            if "패배" in x[37] or "승리" in x[37]:
                # x = re_place(x)
                list1.append(x)
            elif "etc" in x[37]:
                list2.append(x)
            else:
                list3.append(x)
        except:
            continue

    with open("/Users/yoonyoungho/Documents/bigdata/opGG/opgg1.csv", 'a', encoding='euc-kr') as f:
        write = csv.writer(f)
        for i in list1:
            write.writerow(i[0:168])
        

    with open("/Users/yoonyoungho/Documents/bigdata/opGG/opgg2.csv", 'a', encoding='euc-kr') as f:
        write = csv.writer(f)
        for i in list2:
            write.writerow(i[0:168]) 

    with open("/Users/yoonyoungho/Documents/bigdata/opGG/opgg3.csv", 'a', encoding='euc-kr') as f:
        write = csv.writer(f)
        for i in list3:
            write.writerow(i[0:168]) 


               
