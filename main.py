import time
import deps

def main() -> None:
    
    deps.run_command_in_cmd()
    time.sleep(2)
    controller = deps.get_facebook_controller()
    sex = int(input("press 1 for male \npress 0 for female "))
    video = int(input("press 1 if it's reel \npress 0 if it's not "))
    
    if (sex != 1 and sex != 0):
        print("Error with the value of sex")
        exit(1)
    if (video !=1 and video!=0):
        print("Error with video")
        exit(1)
    controller.open_web()
    time.sleep(5)
    controller.share_post(sex,video)
    controller.driver.quit()
    print("Done!")

if __name__ == "__main__":
    main()
