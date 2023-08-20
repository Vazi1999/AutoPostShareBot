import time
import deps

def main() -> None:
    
    deps.run_command_in_cmd()
    time.sleep(1)
    controller = deps.get_facebook_controller()
    video = int(input("press 1 if it's reel \npress 0 if it's not "))
    if (video !=1 and video!=0):
        print("Error with video")
        exit(1)
    controller.open_web()
    time.sleep(6)
    controller.share_post(video)
    controller.driver.quit()
    print("Done!")

if __name__ == "__main__":
    main()
