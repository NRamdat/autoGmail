from selenium import webdriver
import time, random, string


def randomPass(strlen=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strlen))


firstName = "newFirstName"
lastName = "newLastName"
gntel = "gntel"
mobile = "0612345678"

url = "https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp"

driver = webdriver.Chrome("chromedriver") # https://chromedriver.storage.googleapis.com/index.html?path=2.38/
driver.get(url)

time.sleep(0.5)
driver.find_element_by_id("firstName").send_keys(firstName)
time.sleep(0.5)
driver.find_element_by_id("lastName").send_keys(lastName)
time.sleep(0.5)
driver.find_element_by_id("username").send_keys(firstName[0]+"."+lastName+"."+gntel)
time.sleep(0.5)

password = randomPass()
print("Do not forget to change your password!!\n" + password) # password

driver.find_element_by_name("Passwd").send_keys(password)
time.sleep(0.5)
driver.find_element_by_name("ConfirmPasswd").send_keys(password)


driver.find_element_by_class_name("CwaK9").click() # Click next
time.sleep(2)

driver.find_element_by_id("phoneNumberId").send_keys(mobile)

time.sleep(0.5)
driver.find_element_by_class_name("CwaK9").click()  # Click next
time.sleep(2)
driver.find_element_by_class_name("uBOgn").click()  # Call the mobile number to verify
