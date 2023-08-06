from selenium import webdriver



class WebDriver():
    def __init__(self) -> None:
        options = webdriver.ChromeOptions()  # create options var
        # run this command below on cmd where chrome.exe is and than run this function (only need to be done once)
        # chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:9222")  # make chrome to not close
        self.driver = webdriver.Chrome(options)  # install required chrome

    def get_driver(self):
        return self.driver
