from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver =  webdriver.Chrome()
courseLinkId = "ctl00_ContentPlaceHolder1_lstCourse_ctrl1_btnCourseWebsite"
nextLessionId = "ctl00_ContentPlaceHolder1_lbtnNextLessonTop"
previousLessonId = "ctl00_ContentPlaceHolder1_lbtnPreviousLessonTop"
videoLinkId= "ctl00_ContentPlaceHolder1_lstCourseCalender_ctrl3_gvCourseCalender_ctl06_lbtnLesson"
weekNumberId = "Week_04"


def login(url,username,password,submit_button):
   driver.get(url)
   driver.find_element_by_id(username).send_keys("username")
   driver.find_element_by_id(password).send_keys("password")
   driver.find_element_by_id(submit_button).click()
   driver.implicitly_wait(7)
   driver.maximize_window()

def scrollDown(height=200):
    driver.implicitly_wait(3)
    driver.execute_script("window.scrollTo(0,%s)" %height)

def toggleWeekNumber():
    driver.implicitly_wait(3)
    driver.find_element_by_id(weekNumberId).click()

def clickOnCourseLink():
    driver.implicitly_wait(3)
    driver.find_element_by_id(courseLinkId).click()

def clickOnVideoLink():
    driver.find_element_by_id(videoLinkId).click()
    driver.implicitly_wait(5)

def clickNextTopic():
    driver.implicitly_wait(3)
    driver.find_element_by_id(nextLessionId).click()

def clickPreviousTopic():
    driver.implicitly_wait(3)
    driver.find_element_by_id(previousLessonId).click()

def watchVideos(num=0):
    for i in range(num,0,-1):
        print("printing, ",i)
        WebDriverWait(driver,120).until(EC.element_to_be_clickable((By.CLASS_NAME,"text-green"))).click()
        clickNextTopic()


login("login-url","txtStudentId","txtNewPassword","btnLogin")
clickOnCourseLink()
scrollDown(200)
toggleWeekNumber()
scrollDown(500)
clickOnVideoLink()
watchVideos(150)
