import time
from random import uniform
from selenium.webdriver.common.by import By


class FacebookController:
    def __init__(self, web_base_url , driver):
        self.web_base_url = web_base_url
        self.driver = driver
        self.groups_count = None

    
    def open_web(self):
        self.driver.get(self.web_base_url)
    

    def scroll_groups(self):
        groups_divs_xpath = '//span[contains(text(), "ציבורית")]'
        js_code = "arguments[0].scrollIntoView();"
        self.groups_count = -1
        groups_divs = []
        while self.groups_count != len(groups_divs):
            self.groups_count = len(groups_divs)
            groups_divs = self.driver.find_elements(By.XPATH, groups_divs_xpath)
            element = groups_divs[-1]
            js_code = "arguments[0].scrollIntoView();"
            self.driver.execute_script(js_code, element)
            time.sleep(uniform(4,5))
        element = groups_divs[0]
        self.driver.execute_script(js_code, element)
        return groups_divs
            

    def share_post(self , video):
        # click on the share button
        if(video == 1): #video post
            share_button_xpath = '//div[@aria-label="שיתוף"]'
        else: # text post
            share_button_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[3]/div/div[1]'
        share_button = self.driver.find_element(By.XPATH, share_button_xpath)
        share_button.click()
        time.sleep(uniform(1.1,1.5))
        # click on share to group button
        group_share_button_xpath = '//span[contains(text(), "שיתוף בקבוצה")]'
        group_share_button = self.driver.find_element(By.XPATH, group_share_button_xpath)
        group_share_button.click()
        time.sleep(uniform(1.1,1.5))
        groups_divs = self.scroll_groups()
        print(len(groups_divs))
        group_div = groups_divs[0] # the first group
        for i in range(0,self.groups_count,1):
            if i == 0:
                # needs to continue from this starting point
                group_div.click()
                time.sleep(uniform(1.1,1.5))
                if(video == 0):
                    post_button_xpath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div'
                else:
                    post_button_xpath = '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/form/div/div[1]/div/div/div[1]/div/div[3]/div[3]/div/div/div'
                post_button = self.driver.find_element(By.XPATH, post_button_xpath)
                post_button.click()
                time.sleep(uniform(5,7))
                continue
            # all the process all over again.
            share_button = self.driver.find_element(By.XPATH, share_button_xpath)
            share_button.click()
            time.sleep(uniform(1.1,1.5))
            # click on share to group button
            group_share_button = self.driver.find_element(By.XPATH, group_share_button_xpath)
            group_share_button.click()
            time.sleep(uniform(1.1,1.5))
            time.sleep(uniform(1.1,1.5))
            groups_divs_xpath = '//span[contains(text(), "ציבורית")]'
            group_div = self.driver.find_elements(By.XPATH, groups_divs_xpath)[i]
            group_div.click()
            time.sleep(uniform(1,2))
            post_button = self.driver.find_element(By.XPATH, post_button_xpath)
            post_button.click()
            time.sleep(uniform(5,7))



