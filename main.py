from conjug_wrapper import Conjug
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import env

class SeleniumTest:

    max_correct = 250
    target_time = 1 * 60

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=env.path)
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
        login.send_keys(env.email)
        login.send_keys(Keys.RETURN)

        time.sleep(5)

        password = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        password.send_keys(env.password)
        password.send_keys(Keys.RETURN)

        time.sleep(5)

        self.driver.switch_to.window(main_page)

        time.sleep(5)

        # click on lesson with pretirite
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[1]/div/a").click()
        # self.driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[7]/div/a").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[2]/div[6]/div/a").click()

        self.driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/div[1]/a[1]").click()

        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]").click()

        counter = 0

        while counter < SeleniumTest.max_correct:
            try:
                time.sleep(SeleniumTest.target_time / (SeleniumTest.max_correct))

                pronoun = self.driver.execute_script('return document.getElementById("pronoun-input").innerHTML')

                pronoun_parts = pronoun.split()

                tense = ""

                if pronoun[0] == 'y': #yo comparison
                    tense = Conjug.first_singular
                elif pronoun[0] == "t": #tu comparison
                    tense = Conjug.second_singular
                elif pronoun[0] == "n": # nosotros
                    tense = Conjug.first_plural
                elif pronoun[0] == "v": # vosotros
                    tense = Conjug.second_plural
                elif len(pronoun_parts) == 3:
                    if pronoun_parts[2][0] == "y": # check for last yo
                        tense = Conjug.first_plural 
                    else:
                        tense = Conjug.third_plural
                elif pronoun[len(pronoun)-1] == 's': # ellas, ellas, ustedes
                    tense = Conjug.third_plural
                elif len(pronoun_parts) == 1:
                    tense = Conjug.third_singular
                else:
                    #print(pronoun + " " + verb)
                    continue
                
                verb = self.driver.execute_script('return document.getElementById("verb-input").innerHTML')    

                self.sendToInput(self.conjugator.get(tense,verb))

                counter += 1

            except Exception as e:
                print(e)

    def stop(self):
        self.driver.close()

    def sendToInput(self, inp: str):
        self.driver.execute_script('document.getElementById("answer-input").value="{}";'.format(inp))
        self.driver.execute_script('document.getElementById("check-button").click();')
        
test = SeleniumTest()

test.start()