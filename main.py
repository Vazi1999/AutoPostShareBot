import time
import deps

def main() -> None:
    
    deps.run_command_in_cmd()
    time.sleep(2)
    controller = deps.get_facebook_controller()
    controller.open_web()
    time.sleep(5)
    controller.share_post()
    controller.driver.quit()
    print("Done!")

if __name__ == "__main__":
    main()
