import pandas as pd
from tqdm import tqdm
from selenium import webdriver
import time
import os

def Team_Runner():

    df_total = pd.DataFrame()

    for num in tqdm([str(i) for i in range(1,21)]):

        url = 'https://www.koreabaseball.com/Record/Team/Runner/Basic.aspx'

        driver = webdriver.Chrome('./chromedriver')

        driver.get(url=url)

        year = driver.find_element_by_xpath(
                '//*[@id="cphContents_cphContents_cphContents_ddlSeason_ddlSeason"]/option['+num+']')
        year.click()

        time.sleep(1)

        table = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table')

        file = open('./tmp.txt', 'w')
        file.write(table.text)
        file.close()

        df = pd.read_csv('./tmp.txt', sep = ' ')

        df['연도'] = 2000 + int(num)

        df = df[['연도']+df.columns.to_list()[:-1]]

        df = df.dropna()

        df_total = pd.concat([df_total,df],axis=0)

        driver.close()

    os.remove('./tmp.txt')

    del df_total['순위']

    df_total.to_csv('./Data/Team_Runner.csv', index=False, encoding='EUC-KR')

    return df_total

if __name__ == "__main__":
    Team_Runner()