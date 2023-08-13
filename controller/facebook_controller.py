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
    

    def share_post(self , sex , video):
        # click on the share button
        if(video == 1): #video post
            share_button_xpath = '//div[@aria-label="שיתוף"]'
        else: # text post
            if(sex == 1): # male
                share_button_xpath = '//span[contains(text(), "שתף")]'
            else: # female
                share_button_xpath = '//span[contains(text(), "שתפי")]'
        share_button = self.driver.find_element(By.XPATH, share_button_xpath)
        share_button.click()
        time.sleep(1.1)
        # click on share to group button
        group_share_button_xpath = '//span[contains(text(), "שיתוף בקבוצה")]'
        group_share_button = self.driver.find_element(By.XPATH, group_share_button_xpath)
        group_share_button.click()
        time.sleep(1.2)
        #click on the group
        groups_divs = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]') # all the groups
        self.groups_count = len(groups_divs)
        group_div = groups_divs[0] # the first group

        for i in range(0,self.groups_count,1):
            if i == 0:
                # needs to continue from this starting point
                group = group_div.find_elements(By.TAG_NAME, "i")
                group[0].click()
                time.sleep(uniform(1,2))
                if(sex==1): # male
                    post_button_xpath = '//span[contains(text(), "פרסם")]'
                else:
                    post_button_xpath = '//span[contains(text(), "פרסמי")]'
                post_button = self.driver.find_element(By.XPATH, post_button_xpath)
                post_button.click()
                time.sleep(uniform(5,7))
                continue
            # all the process all over again.
            if(video == 1): #video post
                share_button_xpath = '//div[@aria-label="שיתוף"]'
            else: # text post
                if(sex == 1): # male
                    share_button_xpath = '//span[contains(text(), "שתף")]'
                else: # female
                    share_button_xpath = '//span[contains(text(), "שתפי")]'
            share_button = self.driver.find_element(By.XPATH, share_button_xpath)
            share_button.click()
            time.sleep(1.1)
            # click on share to group button
            group_share_button_xpath = '//span[contains(text(), "שיתוף בקבוצה")]'
            group_share_button = self.driver.find_element(By.XPATH, group_share_button_xpath)
            group_share_button.click()
            time.sleep(1.2)
            time.sleep(uniform(1,2))
            group_div = self.driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')[i]
            group =  group_div.find_elements(By.TAG_NAME, "i")
            group[0].click()
            time.sleep(uniform(1,2))
            if(sex==1): # male
                post_button_xpath = '//span[contains(text(), "פרסם")]'
            else: # female
                post_button_xpath = '//span[contains(text(), "פרסמי")]'

            post_button = self.driver.find_element(By.XPATH, post_button_xpath)
            post_button.click()
            time.sleep(uniform(5,7))



