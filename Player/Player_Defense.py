import pandas as pd
from tqdm import tqdm
from selenium import webdriver
import time
import os

def Player_Defense():

    df_total = pd.DataFrame()

    for num in tqdm([str(i) for i in range(2,21)]):

        url = 'https://www.koreabaseball.com/Record/Player/Defense/Basic.aspx'

        driver = webdriver.Chrome('./chromedriver')

        driver.get(url=url)

        year = driver.find_element_by_xpath(
                '//*[@id="cphContents_cphContents_cphContents_ddlSeason_ddlSeason"]/option['+num+']')
        year.click()

        time.sleep(1)

        while True:

            pages = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpContent"]/div[2]/div')

            pages = pages.text.split(' ')

            for page in range(1,len(pages)+1):
                page_button = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ucPager_btnNo'+str(page)+'"]')
                page_button.click()

                time.sleep(1)

                table = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table')

                tmp = [i.split(' ') for i in table.text.split('\n')]

                for i in range(len(tmp)):
                    if len(tmp[i]) == 18:
                        if '1/3' in tmp[i]:
                            tmp[i] = ' '.join(tmp[i]).replace(' 1/3', '+1/3')
                        if '2/3' in tmp[i]:
                            tmp[i] = ' '.join(tmp[i]).replace(' 2/3', '+2/3')
                    else:
                        tmp[i] = ' '.join(tmp[i])

                tmp = '\n'.join(tmp)

                file = open('./tmp.txt', 'w')
                file.write(tmp)
                file.close()

                df = pd.read_csv('./tmp.txt', sep = ' ')

                df['연도'] = 2000 + int(num)

                df = df[['연도']+df.columns.to_list()[:-1]]

                df_total = pd.concat([df_total,df],axis=0)

            try:
                next_button = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ucPager_btnNext"]')
                next_button.click()
                time.sleep(1)
            except:
                break

        driver.close()

    os.remove('./tmp.txt')

    del df_total['순위']

    df_total.to_csv('./Data/Player_Defense.csv', index=False, encoding='EUC-KR')

    return df_total

if __name__ == "__main__":
    Player_Defense()