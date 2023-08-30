def find_types():
    """This function determines the pokemon's type(s) and return them to the main function"""
    
    # List of all acceptable types to be checked against the user's input:
    acceptable_types = ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground",
                        "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "steel", "fairy"]
    
    # Ask for first type and ensure type is valid:
    while True:
        pokemon_type1 = input("\nWhat is the pokemon's first type? > ").lower()
        if pokemon_type1 in acceptable_types:
            break
        else:
            print(f"\nHere is a list of all acceptable types: {acceptable_types}")
            print(f"\nYou entered: {pokemon_type1}")
            print("\nPlease enter a valid type.")
  
    # Ask for second type and ensure type is valid (in acceptable_types AND not the same as pokemon_type1)
    # If the second type is "none", then the pokemon only has one type and the program will continue:
    while True:
        pokemon_type2 = input("\nWhat is the pokemon's second type? (Enter 'none' if the pokemon only has one type) > ").lower()
        if pokemon_type2 in acceptable_types and pokemon_type2 != pokemon_type1:
            break
        elif pokemon_type2 == "none":
            break
        else:
            print(f"\nHere is a list of all acceptable types: {acceptable_types}")
            print(f"\nYou entered: {pokemon_type2}")
            
            # Double check that the user didn't enter the same type as the first type:
            if pokemon_type2 == pokemon_type1:
                print("\nYou entered the same type as the first type.") 
            print("\nPlease enter a valid type or 'none'.")
    
    return pokemon_type1, pokemon_type2
