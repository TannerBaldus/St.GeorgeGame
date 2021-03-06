import random

import places
import persons
import actions
import options
from character import Character
from multiple_choice import MultipleChoice

def lords_victory(character):
    if not persons.lord_arthur.alive and \
       not persons.lord_bartholomew.alive and \
       not persons.lord_carlos.alive and \
       not persons.lord_daniel.alive:
        character.alone = False
        print("You have destroyed the establishment and brought about "
              "a uptopian anarchy... more or less.")
        print("You win!")

def pyro_victory(character):
    if len(places.burned) > 8:  # increase this number for each new 
                                # burnable place we add
        character.alone = False  # might need to add a master_pryo 
                                 # boolean for the character instead 
                                 # of using .alone (which makes no sense)
        print(random.choice(["Some people just like to watch the world "
                             "burn. You are one of them.",
                             "You are satisfied with how everything has "
                             "been burned.",
                             ]))
        print("You win!")

def main():
    """
    The goal is to have the main function operate as follows:
        Set up the initial state
        Display the initial message
        Display the initial options
        Choose an action
        Get an outcome
        Display results of the outcomes
        Outcome changes game state
    """
    character = Character(place=places.tavern)
    choices = MultipleChoice()
    options.set_initial_actions(choices)
    print("\n---The St. George Game---\n")
    print("You are in a tavern. The local assassins hate you.")
    while character.alive and character.alone and not character.lose:
        action = choices.choose_action()
        if not character.threatened or action.combat_action:
            outcome = action.get_outcome(character)
        else:
            outcome = actions.Attack(character.person).get_outcome(character)
        outcome.execute()
        options.add_actions(choices, character, outcome)
        choices.generate_actions(character)
        lords_victory(character)
        pyro_victory(character)
        
if __name__ == "__main__":
    main()
