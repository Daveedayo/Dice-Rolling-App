import random 

DICE_ART = {
    1: (
        
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),

    2: (

        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),

    3: (

        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),

    4: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),

    5: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘", 
    ),

    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘", 
    )

}

DICE_HEIGHT = len(DICE_ART[1])
DICE_WIDTH = len(DICE_ART[1][0])
DICE_FACE_SEPERATOR = " "

def generate_dice_faces_diagram(dice_values):
    pass 

def roll_dice(num_dice):
    roll_results = []

    for _ in range(num_dice):
        #print(_)
        roll = random.randint(1, 6)
        roll_results.append(roll)

    return roll_results

def parse_input(input_string):
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)

# App's main code block 

# Get and validate user's input

num_dice_input = input("How many dice do you want to roll? [1-6]: ")
num_dice = parse_input(num_dice_input)

#Roll the dice
roll_results = roll_dice(num_dice)

#Test the result with this line of code to see how it works
print(roll_results)
