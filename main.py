from selenium import webdriver

#import time module because whenever the browser is loaded it wont load immediately the dynamic variables
import time
from datetime import datetime as dt

#step 1:
def get_driver():

  #set options to make the browsing easier
  options = webdriver.ChromeOptions()
  #to disable the info bars so that they wont interrupt script processing
  options.add_argument("disable-infobars")
  
  # to start the browser maximized
  options.add_argument("start-maximized")
  
  # to disable certain parameters on linux machine
  options.add_argument("disable-dev-shm-usage")
  
  # to have more previlages and sandboxes are disabled
  options.add_argument("no-sandbox")
  
  # to exclude switches and enable automation
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  
  # to exclude blink features
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com")
  return driver

#step 3:
# to cleant the text and get the value of only the number in output
def clean_text(text):
  """Extract only yhe temperature value from text"""
  output = float(text.split(": ")[1])
  return output

#step 4:
#to write input text into a text file
def write_file(text):
  """Write Input text into a text file"""
  #Define file name such that it gives the current date time and hence here 
  #'dt.now().strftime('Y-%m-%d.%H-%M-%S')' has been used
  filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"

  with open (filename, 'w') as file:
    file.write(text)
    
  
#step 2:
def main():
  driver = get_driver()

  #As we need to get the temperature value multiple times we need to put it 
  #inside  a while loop
  while True:
    
    #whenever the browser is loaded it wont load immediately the dynamic 
    #variables, hence use time.sleep(2)
    time.sleep(2)
  
    #find element by xpath is not supported and hence here find element has been 
    #used with "by" and "value" arguments. In Google chrome, then select the 
    #particular text then right click and give inspect. Then select the 
    #highlighted code in the developer window again right click then select 'copy 
    #full xpath', then paste the copied value in "value"
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    #to get the actual text in the console, "element.text" is required
    text = str(clean_text(element.text))
    write_file(text)
    
print(main())

