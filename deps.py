from controller import WebDriver, FacebookController
import os
import subprocess


def get_facebook_controller():
    web_driver = WebDriver()
    url = input("Enter the url of the facebook post: ")
    facebook_controller = FacebookController(url , web_driver.get_driver())
    return facebook_controller


def run_command_in_cmd() -> None:
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

