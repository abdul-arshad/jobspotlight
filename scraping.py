from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

job_id = []
job_title = []
company_name = []
date = []
job_link = []

def linkedin(keyword,loc):
    driver = webdriver.Chrome(r"C:\Users\aarsh\PycharmProjects\telebot\venv\Lib\chromedriver.exe")
    driver.get("https://in.linkedin.com/jobs/search?keywords=&location=&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    time.sleep(5)

    search_keyword = driver.find_element_by_name("keywords")
    search_keyword.clear()
    search_keyword.send_keys(keyword)
    search_location = driver.find_element_by_name("location")
    search_location.clear()
    search_location.send_keys(loc)
    search_location.send_keys(Keys.RETURN)
    job_lists = driver.find_element_by_class_name('jobs-search__results-list')
    jobsl = job_lists.find_elements_by_tag_name('li') # return a list

    for job in jobsl:
        job_id0 = job.get_attribute('data - id')
        job_id.append(job_id0)

        job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
        job_title.append(job_title0)

        company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
        company_name.append(company_name0)

        date0 = job.find_element_by_css_selector('div > div > time').get_attribute('datetime')
        date.append(date0)

        job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
        job_link.append(job_link0)
