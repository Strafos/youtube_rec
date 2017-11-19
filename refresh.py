from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import config

def cycle():
    try:
        # Google acc info. Create your own config file
        usr = config.usr 
        pw = config.pw

        #Log in to google account
        driver = webdriver.Chrome()
        driver.get('https://youtube.com')
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="text"]').click()
        time.sleep(1)
        elem = driver.find_element_by_id('identifierId')
        elem.send_keys(usr + Keys.ENTER)
        time.sleep(1)
        elem = driver.find_element_by_name('password')
        elem.send_keys(pw + Keys.ENTER)

        time.sleep(3)

        # When a video thumbnail is hovered over, a button appears which allows you to indicate 
        # "Not Interested" to delete that video from your recommendations
        # This function finds that element
        def tiny():
            elems = driver.find_elements_by_xpath('//*[@id="button"]/yt-icon')
            for elem in elems:
                if "ytd-menu-renderer" in elem.get_attribute('class') and elem.size['height'] != 0:
                    return elem

        def cycle2():
            # Get all thumbnail elements
            thumbnails = driver.find_elements_by_xpath('//*[@id="img"]')

            for i in range(1,9):
                elems = driver.find_elements_by_xpath('//*[@id="button"]/yt-icon')
                ActionChains(driver).move_to_element(thumbnails[i]).move_to_element(tiny()).click().perform()
                time.sleep(.2)
                driver.find_element_by_xpath('//*[@id="items"]/div/ytd-menu-service-item-renderer[1]/yt-formatted-string').click()

        for i in range(10):
            cycle2()
            driver.get('https://youtube.com')

        driver.quit()

    except:
        driver.quit()

for i in range(100):
    cycle()


