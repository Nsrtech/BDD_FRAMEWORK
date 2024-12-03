from behave import *
from selenium import webdriver
import time
from datetime import datetime

# Global Variables
LOGIN_URL = "https://opensource-demo.orangehrmlive.com/"

@given('Launch Chrome Browser')
def Open_Browser_Login(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\Lenovo\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    context.driver.maximize_window()

@when('Open OrangeHRM websites')
def Launching_Website(context):
    context.driver.get(LOGIN_URL)
    time.sleep(10)

@when('Enter User "{Username}" and Password "{Password}"')
def Enter_User_Pwd(context, Username, Password):
    context.driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys(Username)
    context.driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys(Password)

@then('Click on Login')
def Login_Buttion(context):
    Login_Button = context.driver.find_element_by_xpath("//button[normalize-space()='Login']")
    Login_Button.click()
    time.sleep(5)
    dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    context.driver.save_screenshot(f"C:\\NSR_Python_Projects\\Python_Project_Version2\\7_NSR_HRM_Project_Behave_Framework\\Features_page\\Screenshots\\login_page_{dt}.png")
    time.sleep(5)