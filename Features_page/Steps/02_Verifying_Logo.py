from behave import *
from datetime import datetime

@then('Verify that the logo present on page')
def Logo_verification(context):
   logo_text = context.driver.find_element_by_xpath("//img[@alt='company-branding']").is_displayed()
   print(logo_text)
   dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   context.driver.save_screenshot(f"C:\\NSR_Python_Projects\\Python_Project_Version2\\7_NSR_HRM_Project_Behave_Framework\\Features_page\\Screenshots\\login_page_logo{dt}.png")

   assert logo_text is True



@then('close browser')
def Close_Browesr(context):
    context.driver.close()
