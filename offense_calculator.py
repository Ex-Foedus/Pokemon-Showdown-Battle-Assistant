"""Given the type(s) of a Pokemen, this program will answer:
* what types can/can't the Pokemon beat up ?

It prints the following information to the user:
* Strong against: {formatted_result}
* Weak against: {formatted_result}
* Ineffective against: {formatted_result}"""
def offense_calculator(pokemon_type1, pokemon_type2):
    """This function will calculate the offensive multiplier for the pokemon's type(s)"""

    pokemon_types = [pokemon_type1, pokemon_type2]

    # Dictionary for the offensive multipliers for each of the types below:
    offense_multiplier_dict = {
        "normal": {
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "dragon", "dark", "steel", "fairy", "none"],
            0: ["ghost"]
        },
        "fire": {
            2: ["grass", "ice", "bug", "steel"],
            1: ["normal", "electric", "fighting", "poison", "ground", "flying", "psychic", "ghost", "dark", "fairy", "none"],
            0.5: ["fire", "water", "rock", "dragon"]
        },
        "water": {
            2: ["fire", "ground", "rock"],
            1: ["normal", "electric", "ice", "fighting", "poison", "flying", "psychic", "bug", "ghost", "dark", "steel", "fairy", "none"],
            0.5: ["water", "grass", "dragon"]
        },
        "electric": {
            2: ["water", "flying"],
            1: ["normal", "fire", "ice", "fighting", "poison", "psychic", "bug", "rock", "dark", "steel", "fairy", "none"],
            0.5: ["electric", "grass", "dragon", "ground"],
            0: ["ground"]
        },
        "grass": {
            2: ["water", "ground", "rock"],
            1: ["normal", "electric", "ice", "fighting", "psychic", "ghost", "dark", "fairy", "none"],
            0.5: ["fire", "grass", "poison", "flying", "bug", "dragon", "steel"]
        },
        "ice": {
            2: ["grass", "ground", "flying", "dragon"],
            1: ["normal", "electric", "fighting", "poison", "psychic", "bug", "rock", "ghost", "dark", "fairy", "none"],
            0.5: ["fire", "water", "ice", "steel"]
        },
        "fighting": {
            2: ["normal", "ice", "rock", "dark", "steel"],
            1: ["fire", "water", "electric", "grass", "fighting", "ground", "dragon", "none"],
            0.5: ["poison", "flying", "psychic", "bug", "fairy"],
            0: ["ghost"]
        },
        "poison": {
            2: ["grass", "fairy"],
            1: ["normal", "fire", "water", "electric", "ice", "fighting", "flying", "psychic", "bug", "dragon", "none"],
            0.5: ["poison", "ground", "rock", "ghost"],
            0: ["steel"]
        },
        "ground": {
            2: ["fire", "electric", "poison", "rock", "steel"],
            1: ["normal", "water", "ice", "fighting", "ground", "psychic", "ghost", "dragon", "dark", "fairy", "none"],
            0.5: ["grass", "bug"],
            0: ["flying"]
        },
        "flying": {
            2: ["grass", "fighting", "bug"],
            1: ["normal", "fire", "water", "ice", "poison", "ground", "flying", "psychic", "ghost", "dragon", "dark", "fairy", "none"],
            0.5: ["electric", "rock", "steel"],
            0: ["ground"]
        },
        "psychic": {
            2: ["fighting", "poison"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "ground", "flying", "bug", "rock", "dragon", "fairy", "none"],
            0.5: ["psychic", "steel"],
            0: ["dark"]
        },
        "bug": {
            2: ["grass", "psychic", "dark"],
            1: ["normal", "water", "electric", "ice", "ground", "bug", "rock", "dragon", "none"],
            0.5: ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"]
        },
        "rock": {
            2: ["fire", "ice", "flying", "bug"],
            1: ["normal", "water", "electric", "grass", "fighting", "psychic", "rock", "ghost", "dragon", "dark", "fairy", "none"],
            0.5: ["fighting", "ground", "steel"]
        },
        "ghost": {
            2: ["psychic", "ghost"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "bug", "rock", "dragon", "steel", "fairy", "none"],
            0.5: ["dark"],
            0: ["normal"]
        },
        "dragon": {
            2: ["dragon"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "dark", "none"],
            0.5: ["steel"],
            0: ["fairy"]
        },
        "dark": {
            2: ["psychic", "ghost"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "bug", "rock", "dragon", "steel", "none"],
            0.5: ["fighting", "dark", "fairy"]
        },
        "steel": {
            2: ["ice", "rock", "fairy"],
            1: ["normal", "grass", "fighting", "poison", "ground", "flying", "psychic", "bug", "ghost", "dragon", "dark", "none"],
            0.5: ["fire", "water", "electric", "steel"]
        },
        "fairy": {
            2: ["fighting", "dragon", "dark"],
            1: ["normal", "water", "electric", "grass", "ice", "ground", "flying", "psychic", "bug", "rock", "ghost", "fairy", "none"],
            0.5: ["fire", "poison", "steel"]
        },
        "none": {
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "dragon", "dark", "steel", "fairy"]
        }
    }
    
    offense_analysis = {}

    # Look up pokemon's types in offense_multiplier_dict and populate offense_analysis with its values
    offense_analysis[pokemon_type1] = offense_multiplier_dict[pokemon_type1]
    if pokemon_type2 != "none":
        offense_analysis[pokemon_type2] = offense_multiplier_dict[pokemon_type2]

    # Create a formal format for printing both user-given types e.g. ["normal", "ice"]-> "Normal & Ice":
    formal_types = ([pokemon_type1[0].upper() + pokemon_type1[1:], pokemon_type2[0].upper() + pokemon_type2[1:]])
    non_list_of_formal_types = " & ".join(formal_types)

    # Print offense_analysis in a clean format
    print(f"\nHere's the offensive analysis (what types {non_list_of_formal_types} can/can't beat up):")
    for type in offense_analysis:
        # Create a formal format for each given type (e.g. "normal" -> "Normal"):
        formal_type = type[0].upper() + type[1:]

        print(f"\n{formal_type} is ~~~")

        for multiplier in offense_analysis[type]:
            # Create a clean format use in output
            formatted_result = str(multiplier) + "x " + "=> " + str(offense_analysis[type][multiplier])
            
            # Return strong matchups
            if multiplier == 2:
                print(f"Strong against: {formatted_result}")

            # Return weak matchups
            if multiplier == 0.5:
                print(f"\nWeak against: {formatted_result}")

            # Return matchups with no effect
            if multiplier == 0:
                print(f"\nIneffective against: {formatted_result}:")
    
    return
