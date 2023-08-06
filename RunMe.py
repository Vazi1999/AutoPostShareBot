# This needs to be run before the main script is executed , for cookies on port 9222 .
import subprocess
from selenium import webdriver
import os

original_dir = os.getcwd()
try:
    # Change the working directory to the Chrome application directory
    os.chdir(r'C:\Program Files\Google\Chrome\Application')
    
    # Construct the command and arguments
    command = 'chrome.exe'
    arguments = ['--remote-debugging-port=9222', '--user-data-dir=C:\\selenium\\ChromeProfile']
    
    # Execute the desired command using subprocess.Popen
    subprocess.Popen([command] + arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Change the working directory back to the original directory
    os.chdir(original_dir)
    
options = webdriver.ChromeOptions()  # create options var
# run this command below on cmd where chrome.exe is and than run this function (only need to be done once)
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
options.add_experimental_option("debuggerAddress", f"127.0.0.1:9222")  # make chrome to not close
driver = webdriver.Chrome(options)  # install required chrome

driver.get("https://www.facebook.com")
driver.quit()
print("Please login to facebook.")