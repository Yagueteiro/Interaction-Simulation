import pyautogui
import random
import time
import argparse

# defines user input via. cli
parser = argparse.ArgumentParser()
parser.add_argument("--mode", type=str, default="vol", help="Define mode to run - you can choose between vol (volume), "
                                                            "mouse (mouse movements) and comb (combined which is both"
                                                            "mouse movement and volume simulation)")
parser.add_argument("--duration_min", type=str, default=1, help="Min. duartion for the mouse to move from a to b")
parser.add_argument("--duration_max", type=str, default=10, help="Max. duartion for the mouse to move from a to b")
parser.add_argument("--sleep_min", type=str, default=5, help="Min. time to wait until next action")
parser.add_argument("--sleep_max", type=str, default=5, help="Max. time to wait until next action")
args = parser.parse_args()

# defines the duration it should take to move mouse from a to b -> Gets choosen randomly between the min and max value
duration_range = (args.duration_min, args.duration_max)

# defines the min/max duration the script should pause between mouse moves
sleep_range = (args.sleep_min, args.sleep_max)

# get screen dimensions
display_width, display_height = pyautogui.size()


def simulate_mouse(width=display_width, height=display_height, duration=duration_range, sleep=sleep_range):
    """simulate mouse movement randomly across the screen"""
    while True:
        # adjust screen - 10% padding
        pyautogui.moveTo(random.randint(width*0.1, width*0.9),
                         random.randint(height*0.1, height*0.9),
                         random.randint(duration[0], duration[1])/10)
        time.sleep(random.randint(sleep[0], sleep[1]))


def simulate_keys_volume(sleep=sleep_range):
    """simulate key presses"""
    while True:

        # increase volume and then decrease it to get original value
        pyautogui.press('volumeup')
        time.sleep(1)
        pyautogui.press('volumedown')

        # make random break until next volume changement
        time.sleep(random.randint(sleep[0], sleep[1]))


def simulate_combined(width=display_width, height=display_height, duration=duration_range, sleep=sleep_range):
    """Simulates mouse and volume in combination - via. random choice"""
    while True:
        if random.choice(["vol", "mouse"]) == "vol":
            simulate_keys_volume(sleep)
        elif random.choice["vol", "mouse"] == "mouse":
            simulate_mouse(width, display_width, height, duration, sleep)


if __name__ == "__main__":

    if args.mode.lower() == "vol":
        simulate_keys_volume()
    elif args.mode.lower() == "mouse":
        simulate_mouse()
    elif args.mode.lower() == "comb":
        simulate_mouse()
