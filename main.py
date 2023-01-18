from selenium import webdriver

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

def main():
  driver = get_driver()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
  #to get the actual text in the console, "element.text" is required
  return element.text
  
print(main())

