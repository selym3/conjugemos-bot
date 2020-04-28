from conjug_wrapper import Conjug
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class SeleniumTest:

    email = "mpasetsky30@stuy.edu"
    password = "kanye!banana!sauce!3"

    max_correct = 70

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\mp3bl\Desktop\conjug\chromedriver\chromedriver")
        self.conjugator = Conjug()
        pass

    def start(self):
        self.driver.get("https://conjuguemos.com/student/activities")

        main_page = self.driver.current_window_handle

        # open google sign in frame
        option = self.driver.find_element_by_xpath("/html/body/div[3]/form/div[1]/div/div/div")
        option.click()

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)


        # switch to google sign in frame
        login = self.driver.find_element_by_id("identifierId")
        login.send_keys(SeleniumTest.email)
        login.send_keys(Keys.RETURN)

        time.sleep(5)

        password = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        password.send_keys(SeleniumTest.password)
        password.send_keys(Keys.RETURN)

        time.sleep(5)

        self.driver.switch_to.window(main_page)

        time.sleep(5)

        # click on lesson with pretirite
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[1]/div/a").click()
        #self.driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[7]/div/a").click()
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[6]/div/a").click()

        self.driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/a[1]").click()

        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]").click()

        time.sleep(2)

        counter = 0

        while counter < SeleniumTest.max_correct:
            time.sleep(0.05)

            counter += 1

            pronoun = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div[3]").text
            verb = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div[4]").text

            pronoun_parts = pronoun.split(" ")

            # input box
            i = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[2]/div/input")

            if pronoun == "yo":
                i.send_keys(self.conjugator.get(Conjug.first_singular,verb))
                i.send_keys(Keys.RETURN)
            elif pronoun == "tú":
                i.send_keys(self.conjugator.get(Conjug.second_singular,verb))
                i.send_keys(Keys.RETURN)
            elif pronoun in ["él","ella","usted"]:
                i.send_keys(self.conjugator.get(Conjug.third_singular,verb))
                i.send_keys(Keys.RETURN)
            elif pronoun == "nosotros":
                i.send_keys(self.conjugator.get(Conjug.first_plural,verb))
                i.send_keys(Keys.RETURN)
            elif pronoun == "vosotros":
                i.send_keys(self.conjugator.get(Conjug.second_plural,verb))
                i.send_keys(Keys.RETURN)
            elif pronoun in ["ellos","ellas","ustedes"]:
                i.send_keys(self.conjugator.get(Conjug.third_plural,verb))
                i.send_keys(Keys.RETURN)
            elif len(pronoun_parts) == 3:
                if pronoun_parts[2] == "yo":
                    i.send_keys(self.conjugator.get(Conjug.first_plural,verb))
                    i.send_keys(Keys.RETURN)
                else:
                    i.send_keys(self.conjugator.get(Conjug.third_plural,verb))
                    i.send_keys(Keys.RETURN)
            elif len(pronoun_parts) == 1:
                i.send_keys(self.conjugator.get(Conjug.third_singular,verb))
                i.send_keys(Keys.RETURN)
            else:
                counter -= 1
                pass
        self.stop()

    def stop(self):
        self.driver.close()



test = SeleniumTest()

test.start()