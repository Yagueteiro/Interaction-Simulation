import pyautogui
import random
import time
import argparse
import sys

# defines user input via. cli
parser = argparse.ArgumentParser()
parser.add_argument("--mode", type=str, default="vol", help="Define mode to run - you can choose between vol (volume), "
                                                            "mouse (mouse movements) and comb (combined which is both"
                                                            "mouse movement and volume simulation)")
parser.add_argument("--duration_min", type=str, default=1, help="Min. duration for the mouse to move from a to b")
parser.add_argument("--duration_max", type=str, default=10, help="Max. duration for the mouse to move from a to b")
parser.add_argument("--sleep_min", type=str, default=5, help="Min. time to wait until next action")
parser.add_argument("--sleep_max", type=str, default=5, help="Max. time to wait until next action")
args = parser.parse_args()

# defines the duration it should take to move mouse from a to b -> Gets choosen randomly between the min and max value
duration_range = (args.duration_min, args.duration_max)

# defines the min/max duration the script should pause between mouse moves
sleep_range = (args.sleep_min, args.sleep_max)

# get screen dimensions
display_width, display_height = pyautogui.size()


def exit_prompt() -> str:
    """Exit prompt to check if user wants to exit"""
    print("Simulation has been interrupted!")
    resp = input('To exit Press "E" for continuing the simulation press "C" and confirm with Enter.')
    return resp.lower()


def simulate_mouse(width=display_width, height=display_height, duration=duration_range, sleep=sleep_range,
                   one_move=False):
    """simulate mouse movement randomly across the screen"""
    while True:
        # adjust screen - 10% padding
        pyautogui.moveTo(random.randint(width*0.1, width*0.9),
                         random.randint(height*0.1, height*0.9),
                         random.randint(duration[0], duration[1])/10)
        time.sleep(random.randint(sleep[0], sleep[1]))
        if one_move:
            break


def simulate_keys_volume(sleep=sleep_range, one_move=False):
    """simulate key presses"""

    while True:

        # increase volume and then decrease it to get original value
        pyautogui.press('volumeup')
        time.sleep(1)
        pyautogui.press('volumedown')

        # make random break until next volume changement
        time.sleep(random.randint(sleep[0], sleep[1]))
        if one_move:
            break


def simulate_combined(width=display_width, height=display_height, duration=duration_range, sleep=sleep_range):
    """Simulates mouse and volume in combination - via. random choice"""
    while True:
        rand_choice = random.choice(["vol", "mouse"])
        if rand_choice == "vol":
            simulate_keys_volume(sleep, one_move=True)
        elif rand_choice == "mouse":
            simulate_mouse(width, height, duration, sleep, one_move=True)


def simulate(argu=args):
    """Simulation program that runs the simulation based on the arguments"""
    try:
        if argu.mode.lower() == "vol":
            simulate_keys_volume()
        elif argu.mode.lower() == "mouse":
            simulate_mouse()
        elif argu.mode.lower() == "comb":
            simulate_combined()

    except KeyboardInterrupt:
        resp = exit_prompt()
        while (len(resp) != 1) & (resp not in ["e", "c"]):
            resp = exit()

        if resp == "e":
            sys.exit()
        elif resp == "c":
            simulate()


if __name__ == "__main__":
    simulate()