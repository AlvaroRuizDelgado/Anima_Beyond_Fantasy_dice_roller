#!/usr/local/bin/python3
# Last edited: 19/05/08

import sys
import math
from random import randint

# Constants
FUMBLE_THRESHOLD = 3
EXPLODE_THRESHOLD = 90
INHUMAN_THRESHOLD = 320
ZEN_THRESHOLD = 440

def roll(argv):
    if (len(argv) == 0 or "--help" in argv or "-h" in argv):
        print_help()
        sys.exit(0)

    # Roll characteristics
    die_range = 100
    modifier = 0
    difficulty = 0
    fail_modifier = 0
    explode_value = EXPLODE_THRESHOLD

    # Get the arguments
    roll_type = argv.pop(0)
    if (roll_type == "d100"):
        die_range = 100
    elif (roll_type == "d10"):
        die_range = 10
    else:
        print("Error: The accepted values are 'd100' and 'd10'")
        print_help()
        sys.exit(1)

    while len(argv) > 0:
        if (argv[0] == "--difficulty" or argv[0] == "-d"):
            argv.pop(0)
            difficulty = int(argv.pop(0))
        elif (argv[0] == "--master" or argv[0] == "-m"):
            argv.pop(0)
            fail_modifier = -1
        elif (argv[0] == "--resistance" or argv[0] == "-r"):
            argv.pop(0)
            explode_value = die_range+1     # No explosion
        else:
            modifier = int(argv.pop(0))
    print("Roll type:", roll_type, "/ Modifier:", modifier, "/ Difficulty:", difficulty, "/ Fail modifier:", fail_modifier)

    # Show results
    class bcolors:
        PURPLE = '\033[95m'
        GREY = '\033[92m'
        ORANGE = '\033[91m'
        LIGHT_RED = '\033[35m'
        YELLOW = '\033[0;32m'
        BLUE = '\033[0;34m'
        TEST = '\033[0;36m'

    # Find the result and print it out
    if (roll_type == "d100"):
        single_roll = randint(1,die_range)
        die_roll = single_roll
        while (single_roll > explode_value):
            single_roll = randint(1,die_range)
            die_roll = die_roll + single_roll
            explode_value = explode_value + 1
        
        roll_result = "not assigned"
        success_level = 0

        if (die_roll <= FUMBLE_THRESHOLD+fail_modifier):
            font_roll_color = bcolors.GREY
            font_result_color = bcolors.PURPLE
            success_level = randint(1,100)
            if (success_level >= 96):
                roll_result = "TRAGIC FUMBLE!!"
            elif (success_level >= 51):
                roll_result = "BAD FUMBLE!!"
            else:
                roll_result = "FUMBLE!!"
        else:
            die_roll = die_roll + modifier
            if (difficulty != 0):
                success_level = die_roll - difficulty
            if (difficulty != 0 and die_roll < difficulty):
                font_roll_color = bcolors.GREY
                font_result_color = bcolors.BLUE
                roll_result  = "FAIL!"
            else:
                font_roll_color = bcolors.YELLOW
                font_result_color = bcolors.ORANGE
                if (success_level >= 80):
                    roll_result = "ABSOLUTE SUCCESS"
                elif (success_level >= 40):
                    roll_result = "GREAT SUCCESS"
                else:
                    roll_result = "SUCCESS"
        print(font_roll_color, die_roll, bcolors.LIGHT_RED, "-->", font_result_color, roll_result, "(level "+str(success_level)+")", bcolors.GREY)
        return(
                  {
                    'die_range': die_range,
                    'die_roll': die_roll,
                    'roll_result': roll_result
                  }
              )

    elif (roll_type == "d10"):
        die_roll = randint(1,die_range)
        if (die_roll == 10):
            die_roll = 12
        die_roll = die_roll + modifier
        roll_result = "not assigned"
        if (difficulty == 0):
            difficulty = 10
        success_level = die_roll - difficulty

        if (die_roll < difficulty):
            font_roll_color = bcolors.GREY
            font_result_color = bcolors.BLUE
            roll_result  = "FAIL!"
        else:
            font_roll_color = bcolors.YELLOW
            font_result_color = bcolors.ORANGE
            roll_result = "SUCCESS"
        print(font_roll_color, die_roll, bcolors.LIGHT_RED, "-->", font_result_color, roll_result, "(level "+str(success_level)+")", bcolors.GREY)
        return(
                  {
                    'die_range': die_range,
                    'die_roll': die_roll,
                    'roll_result': roll_result
                  }
              )

def print_help():
    print("Usage: pass the type of die to roll, followed by the modifier in the d100 case and other options")
    print("  - d100 +modifier")
    print("  - d10")
    print("Options:")
    print("  -d, --difficulty, sets the difficulty")
    print("  -m, --master, fumble threshold is reduced by 1 (i.e. '3' is not a fumble)")
    print("  -r, --resistance, resistance check, does not use open roll")
    print("Examples:")
    print("  ./roll d100 +30 -d 120")
    print("  ./roll d100 +15 -d 80 -m")
    print("  ./roll d100 -20")
    print("  ./roll d100")
    print("  ./roll d10")

if __name__ == "__main__":
   roll(sys.argv[1:])
