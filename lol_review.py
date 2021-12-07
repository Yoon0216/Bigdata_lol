import re, csv
import pandas as pd
import numpy as np
from pandas._config.config import set_option
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

def re_place(rate):
    rate = float(re.sub("%",' ', (rate)))

lane = input('포지션을 입력해주세요. : ')
champ = input('원하는 챔피언을 입력해 주세요. : ')

# fieldnames=['position', 'name', 'win_rate', 'pick_rate', 'ban_rate', 'champ_rank', 'hard_champ', 'easy_champ']
pd.set_option('display.max_columns', None)

df1 = pd.read_csv("/Users/yoonyoungho/Documents/bigdata/lolps.csv", encoding='euc-kr')

# df2 = pd.read_csv("/Users/yoonyoungho/Documents/bigdata/opGG/opgg1.csv", encoding='euc-kr', error_bad_lines=False)
# df3 = pd.read_csv("/Users/yoonyoungho/Documents/bigdata/opGG/opgg2.csv", encoding='euc-kr', error_bad_lines=False)
# df4 = pd.read_csv("/Users/yoonyoungho/Documents/bigdata/opGG/opgg3.csv", encoding='euc-kr', error_bad_lines=False)
df1.columns = ['position', 'name', 'win_rate', 'pick_rate', 'ban_rate', 'champ_rank', 'hard_champ', 'easy_champ']


for i in range(0, len(df1)):
    if df1.position[i] == str(lane) and df1.name[i] == str(champ):
        print(df1.loc[i])




    
