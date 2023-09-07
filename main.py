# -*- coding: utf-8 -*-
# import the other files
from type_input import find_types
from offense_calculator import offense_calculator
from defense_calculator import defense_calculator

"""This function call a function for the offensive stats and another for the defensive ones.
Both return a list of  multipliers for each type, given respective weaknesses and resistances"""
def main():
    # Program's name:
    battle_assistant = "べろべろ"

    # Welcome the user and explain the program:
    print("Welcome to the Pokemon Showdown Battle Assistant!")
    print("\nThis program will answer the following:")
    print("""Given the type(s) of a Pokemen, what:
          *can it/can't it beat up
          *can/can't beat it up""")
    print(f"\nI'm BeroBero ({battle_assistant}) or Bero for short; I'll be your battle assistant!")

    # Call function to determine the pokemon's type(s):
    pokemon_type1, pokemon_type2 = find_types()

    # Call function to determine pokemon's offensive multipliers for each type:
    offensive_analysis = offense_calculator(pokemon_type1, pokemon_type2)
    


    
    return


main()
