from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from yahoo_csv import *

COMPANIES = ['PD', 'ZUO', 'PINS', 'ZM', 'PVTL', 'DOCU', 'CLDR', 'RUN']
URL = 'https://finance.yahoo.com/'

class YahooCompanies:

    driver = webdriver.Firefox()
    driver.get(URL)

    def parse(self, company):
        search = self.driver.find_element_by_xpath('//input[@id="yfin-usr-qry"]')
        self.driver.implicitly_wait(5)
        search.send_keys(company)
        time.sleep(2)
        search.send_keys(Keys.ENTER)
        time.sleep(4)
        if company is 'PVTL':
            summary = self.driver.find_element_by_xpath('//u[@data-reactid="54"]').click()
        else:
            summary = self.driver.find_element_by_xpath('//h3[@class="Mb(5px)"]').click()
        title = self.driver.find_element_by_xpath('//header[@class="canvas-header"]').text
        return {
            'title': title,
            'link': self.driver.current_url
        }
        time.sleep(2)
        self.driver.quit()


def main():
    yahoo = YahooCompanies()
    for company in COMPANIES:
        file = CSVFile(company + '.csv')
        file.write([yahoo.parse(company)])

if __name__ == '__main__':
    main() 
