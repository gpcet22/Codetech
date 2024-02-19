# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 15:14:46 2024

@author: Rakesh
"""

import time

def introduction():
    print("Welcome to the Interactive Story!")
    time.sleep(1)
    print("You find yourself standing at a crossroads. A mysterious adventure awaits!")
    time.sleep(1)

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def path_one():
    print("You choose the path through the dense forest.")
    time.sleep(1)
    print("As you walk deeper, you come across a magical creature.")
    time.sleep(1)

    encounter_choices = ["Approach the creature.", "Ignore the creature and continue walking."]
    encounter_choice = make_choice(encounter_choices)

    if encounter_choice == 1:
        print("The creature greets you warmly and offers guidance.")
        time.sleep(1)
        print("Congratulations! You've made a new friend.")
    else:
        print("You decide to avoid the creature and continue your journey.")
        time.sleep(1)
        print("The path becomes treacherous, but you manage to reach your destination.")

def path_two():
    print("You choose the path through the ancient ruins.")
    time.sleep(1)
    print("As you explore, you discover a hidden chamber with a mysterious artifact.")
    time.sleep(1)

    artifact_choices = ["Touch the artifact.", "Leave the artifact untouched."]
    artifact_choice = make_choice(artifact_choices)

    if artifact_choice == 1:
        print("As you touch the artifact, you feel a surge of energy.")
        time.sleep(1)
        print("The artifact grants you magical powers.")
        time.sleep(1)
        print("Congratulations! You've gained extraordinary abilities.")
    else:
        print("You decide to leave the artifact untouched and continue exploring.")
        time.sleep(1)
        print("The ruins hold many secrets, but you make it through safely.")

def main():
    introduction()

    path_choices = ["Take the path through the dense forest.", "Explore the path through the ancient ruins."]
    path_choice = make_choice(path_choices)

    if path_choice == 1:
        path_one()
    else:
        path_two()

    print("The end of the story. Thanks for playing!")

if __name__ == "__main__":
    main()