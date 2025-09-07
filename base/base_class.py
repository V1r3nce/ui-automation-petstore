import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver


    # METHOD ASSERT WORD

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    # METHOD GET CURRENT URL

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    # METHOD SCREENSHOT

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
        name_screenshot = "screenshot " + now_date + ".png"
        self.driver.save_screenshot(f"C:\\Users\\Andrey\\PycharmProjects\\TotalProjectHomeWork\\screen\\{name_screenshot}")