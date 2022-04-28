from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# 创建一个参数对象，用来控制chrome以无界面模式打开
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver= Chrome('D:\py\chromedriver_win32\chromedriver.exe',chrome_options=chrome_options)
driver= Chrome('D:\py\chromedriver_win32\chromedriver.exe')
# web.implicitly_wait(5)
#
# web.get('https://www.lagou.com')
# web.maximize_window()
# web.find_element(By.XPATH,'//*[@id="cboxClose"]').click()
#
# # element=WebDriverWait(web,5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search_input"]')))
#
# web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python")
# #
# # element.send_keys("python")
def test():
    driver.implicitly_wait(5)

    driver.get('https://www.lagou.com')
    driver.maximize_window()
    sleep(1)
    driver.find_element(By.XPATH,'//*[@id="cboxClose"]').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="search_input"]').send_keys('RPA',Keys.ENTER)
    alts = driver.find_elements(By.CLASS_NAME,'p-top__1F7CL')
    for a in range(0,len(alts)):
        alts = driver.find_elements(By.CLASS_NAME, 'p-top__1F7CL')
        alts[a].find_element(By.TAG_NAME,'a').click()
        driver.switch_to.window(driver.window_handles[-1])
        text = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]').text
        print(text)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
if __name__ == "__main__":
    test()
