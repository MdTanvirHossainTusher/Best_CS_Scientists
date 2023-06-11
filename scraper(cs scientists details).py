from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

columns = ['World Rank','National Rank','Name','Image Urls','Affiliation','Country','D-Index','Citations','#DBLP']

def get_scholar_details(row):

    details = row.text.split('\n')
    contents = {}
    contents['World Rank'] = details[0]
    contents['National Rank'] = details[1]
    contents['Name'] = details[2]
    contents['Image Urls'] = row.find_element(By.CLASS_NAME,'lazyload').get_attribute('src')
    contents['Affiliation'] = details[3].split(',')[0]
    contents['Country'] = details[3].split(',')[1].strip()
    contents['D-Index'] = details[4]
    contents['Citations'] = details[5].replace(',','')
    contents['#DBLP'] = details[6].replace(',','')

    return contents

def main():

    webdriver_path = "J:\chromedriver_win32"
    driver = webdriver.Chrome(webdriver_path);

    scholar_details = []

    for page_no in range(1,11):

        url = f"https://research.com/scientists-rankings/computer-science?page={page_no}"
        driver.get(url)
        rows = driver.find_elements(By.XPATH,"//div[@id='rankingItems']//div[contains(@class,'rankings-content__item')]")

        for idx, row in enumerate(rows):
            scholar_details.append(get_scholar_details(row))

    print(len(scholar_details))
    driver.quit()
    
    df = pd.DataFrame(data=scholar_details, columns=columns)
    df.to_csv('best_cs_scientist_details.csv', index=False)

    return


if __name__ == "__main__":
    main()