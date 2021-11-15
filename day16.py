from selenium import webdriver
import time

jd=webdriver.Chrome()
jd.get("https://www.jd.com/")

jd.find_element_by_xpath("//*[@id='key']").send_keys("华为")

jd.find_element_by_xpath("//*[@id='search']/div/div[2]/button").click()

time.sleep(30)

tianjia = jd.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[2]/div/div[1]/a/img")
tianjia.click()

time.sleep(30)

jd.find_element_by_xpath("/html/body/div[6]/div/div[2]/div[5]/div[18]/a[1]").click()

jd.quit()





# from selenium import webdriver
# import time
#
# bili=webdriver.Chrome()
#
# bili.maximize_window()
#
# bili.get("https://www.bilibili.com/")
#
# time.sleep(5)
#
# sousu= bili.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div/form/input")
# sousu.click()
# sousu.send_keys("鬼畜")
#
# time.sleep(3)
#
# bili.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div/div/div[1]").click()
#
# time.sleep(3)
#
# bili.quit()