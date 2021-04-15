import pandas as pd
from tqdm import tqdm
from selenium import webdriver
import time
import os

def Player_Hitter():

    df_total_1 = pd.DataFrame()

    for num in tqdm([str(i) for i in range(21,40)]):

        url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'

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

                file = open('./tmp.txt', 'w')
                file.write(table.text)
                file.close()

                df = pd.read_csv('./tmp.txt', sep = ' ')

                df['연도'] = 1981 + int(num)

                df = df[['연도']+df.columns.to_list()[:-1]]

                df_total_1 = pd.concat([df_total_1,df],axis=0)

            try:
                next_button = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ucPager_btnNext"]')
                next_button.click()
                time.sleep(1)
            except:
                break

        driver.close()

    df_total_2 = pd.DataFrame()

    for num in tqdm([str(i) for i in range(21,40)]):

        url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Basic2.aspx'

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

                file = open('./tmp.txt', 'w')
                file.write(table.text)
                file.close()

                df = pd.read_csv('./tmp.txt', sep = ' ')

                df['연도'] = 1981 + int(num)

                df = df[['연도']+df.columns.to_list()[:-1]]

                df_total_2 = pd.concat([df_total_2,df],axis=0)

            try:
                next_button = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ucPager_btnNext"]')
                next_button.click()
                time.sleep(1)
            except:
                break

        driver.close()

    df_total_3 = pd.DataFrame()

    for num in tqdm([str(i) for i in range(21,40)]):

        url = 'https://www.koreabaseball.com/Record/Player/HitterBasic/Detail1.aspx'

        driver = webdriver.Chrome('./chromedriver')

        driver.get(url=url)

        year = driver.find_element_by_xpath(
                '//*[@id="cphContents_cphContents_cphContents_ddlSeason_ddlSeason"]/option['+num+']')
        year.click()

        time.sleep(1)

        while True:

            pages = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_udpContent"]/div[3]/div')

            pages = pages.text.split(' ')

            for page in range(1,len(pages)+1):
                page_button = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ucPager_btnNo'+str(page)+'"]')
                page_button.click()

                time.sleep(1)

                table = driver.find_element_by_css_selector('#cphContents_cphContents_cphContents_udpContent > div.record_result > table')

                tmp = [i.split(' ') for i in table.text.split('\n')]

                tmp[0][8] = tmp[0][8] + '_' + tmp[0][9]

                del tmp[0][9]

                for i in range(len(tmp)):
                    tmp[i] = ' '.join(tmp[i])

                tmp = '\n'.join(tmp)

                file = open('./tmp.txt', 'w')
                file.write(tmp)
                file.close()

                df = pd.read_csv('./tmp.txt', sep = ' ')

                df['연도'] = 1981 + int(num)

                df = df[['연도']+df.columns.to_list()[:-1]]

                df_total_3 = pd.concat([df_total_3,df],axis=0)

            try:
                next_button = driver.find_element_by_xpath('//*[@id="cphContents_cphContents_cphContents_ucPager_btnNext"]')
                next_button.click()
                time.sleep(1)
            except:
                break

        driver.close()

    os.remove('./tmp.txt')

    del df_total_1['순위']
    del df_total_2['순위']
    del df_total_2['선수명']
    del df_total_2['팀명']
    del df_total_2['AVG']
    del df_total_2['연도']
    del df_total_3['순위']
    del df_total_3['선수명']
    del df_total_3['팀명']
    del df_total_3['AVG']
    del df_total_3['연도']

    df_total = pd.concat([df_total_1.reset_index(drop=True), df_total_2.reset_index(drop=True), df_total_3.reset_index(drop=True)], axis=1)

    df_total.to_csv('./Data/Player_Hitter.csv', index=False, encoding='EUC-KR')

    return df_total

if __name__ == "__main__":
    Player_Hitter()