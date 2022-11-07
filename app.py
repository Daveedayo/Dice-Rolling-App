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

DICE_HEIGHT = 5
DICE_WIDTH = 11

def generate_dice_faces_diagram(dice_values):

    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)

    # Generate header with the word "RESULTS" centered

    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "_")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)

    return dice_faces_diagram

def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])

    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    for row_idx in range(DICE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = " ".join(row_components)
        dice_faces_rows.append(row_string) 

    return dice_faces_rows

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

# Generate the ASCII diagram of dice faces
dice_faces_diagram = generate_dice_faces_diagram(roll_results)

# Display the diagram
print(f"\n{dice_faces_diagram}")

#Test the result with this line of code to see how it works
#print(roll_results)
