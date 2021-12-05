
from selenium import webdriver
import time

chromedriver = '/Users/yoonyoungho/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)

# 모든 챔피언의 이름을 얻기 위해 실행. 'allChampName.txt'파일에 저장하는 방식.
def get_champion():
    driver.get('https://www.op.gg/champion/statistics')

    allChamps = driver.find_elements_by_xpath(
        "//div[contains(@class,'champion-item__name')]")
    time.sleep(2)
    for i in allChamps:
        with open("allChampName.txt", "a") as f:
            f.write(i.text+'\n')




def get_lolps():
    driver.get('https://lol.ps/')
    
    with open("allChampName.txt", "r") as f:
        allnames= f.readlines()

    for i in allnames:
        name= i.strip('\n')
        time.sleep(1)
        driver.find_element_by_name('q').send_keys(name)
        enter = driver.find_element_by_css_selector(
            ".searchbar > button")
        enter.click()
        for j in range(0,5):
            lane = driver.find_element_by_id('lane_input_'+str(j))
            lane.click()
            content = driver.page_source
            with open("./lolpsData/"+str(name)+str(j)+ ".html", 'a') as f:
                f.write(content)
            time.sleep(1)

def get_prevLolps():
    driver.get('https://lol.ps/')
    
    with open("allChampName.txt", "r") as f:
        allnames= f.readlines()

    for i in allnames:
        name= i.strip('\n')
        time.sleep(1)
        driver.find_element_by_name('q').send_keys(name)
        enter = driver.find_element_by_css_selector(
            ".searchbar > button")
        enter.click()
        time.sleep(1)
        option = driver.find_element_by_css_selector(
            "#menu-scroll > div > form > div.d-inline-block.select-patch.mr-sm-1 > span > span.selection > span > span.select2-selection__arrow")
        option.click()
        time.sleep(1)
        versions = driver.find_element_by_xpath("//span[contains(@class,'33')]")
        versions.click() 
        for j in range(0,5):
            lane = driver.find_element_by_id('lane_input_'+str(j))
            lane.click()
            content = driver.page_source
            with open("./lolpsData_v11.22/"+str(name)+str(j), 'a') as f:
                f.write(content)

# get_champion()
# get_lolps()
# get_prevLolps()