from selenium import webdriver
import time

chromedriver = '/Users/yoonyoungho/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)


def get_summoner(): 
    for i in range(1,10001):
        driver.get("https://www.op.gg/ranking/ladder/page="+str(i))
        allSummonersName = driver.find_elements_by_css_selector(
        'body > div.l-wrap.l-wrap--ranking > div.l-container > div.LadderRankingLayoutWrap > div > div > div > table > tbody > tr')
        for item in allSummonersName:
            nick = item.find_element_by_tag_name("span").text
            with open("lolData2.txt","a") as f:
                f.write(nick+'\n')

def get_opgg():
    with open('lolData.txt',"r") as f:
        read = f.readlines()
    for i in read:
        newNick = i.strip('\n')
        with open("nick.txt","r") as f:
            preNick = f.read()
        if i not in preNick:
            with open("nick.txt","a") as f:
                f.write(i)
            driver.get("https://www.op.gg/summoner/userName="+str(i))
            while True:
                try:
                    morebtn = driver.find_element_by_class_name("GameMoreButton").click()
                    time.sleep(1)
                except:
                    break
            details = driver.find_elements_by_xpath("//div[contains(@class,'StatsButton')]")
            for i in details:
                i.click()
                time.sleep(2)
            try:    
                data = driver.find_elements_by_css_selector(
                    "#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.RealContent > div > div.Content > div.GameItemList")
                name = driver.find_element_by_css_selector(
                    "body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header > div.Profile > div.Information > span").text
                for i in data:
                    with open("./opggData/"+ str(name) + ".txt", 'a') as f:
                        f.write(i.text)              
                driver.back()
                time.sleep(2)
            except:
                continue



# get_summoner()
# get_opgg()