import time, pandas as pd
from selenium import webdriver # will be used to launch and operate browser
from selenium.webdriver.support.ui import WebDriverWait #Element may not yet be on the screen at the time of the operation.
from selenium.common.exceptions import NoSuchElementException

gecko_path = '/bin/geckodriver' #for linux

i_job_title = 'html'
url = 'https://www.naukri.com/'+i_job_title+'-jobs?k='+i_job_title

job_links = []
headings = []
companies = []

options = webdriver.firefox.options.Options()
options.headless = False # without gui if true
driver = webdriver.Firefox(options = options, executable_path= gecko_path)


try:
    driver.get(url)
    time.sleep(5)
    error = driver.find_element_by_xpath("//span[@class = 'saveSpn fs12']")
    #wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'filterOptns')))
    #WebDriverWait(driver, 5)
    #more = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,"//div[@class ='mt-8 fw500']"))).click()
    
    links = driver.find_elements_by_xpath("//a[@class='title fw500 ellipsis']")
    comp_name = driver.find_elements_by_xpath("//a[@class='subTitle ellipsis fleft']")
    exper_no = driver.find_elements_by_xpath("//span[@class='fleft fw500']")
    
    # Extract links,titles and companies name
    for link in links:
        job_links.append(link.get_attribute('href'))
        headings.append(link.get_attribute('title'))

    for comp in comp_name:
        companies.append(comp.get_attribute('title'))

   # for exper in exper_no:
    #    exper.append(exper.text)   

    fieldnames = {'Headings': headings, 'Comapny Name': companies, 'Links': job_links}
    df = pd.DataFrame(fieldnames)
    df.to_csv('output.csv' ,index = False)

except NoSuchElementException:
    print('Did you enter wrong spelling of any word?')
    #print(e)
finally:
    time.sleep(2)
    driver.quit()
#print(driver.page_source)
#driver.quit()
