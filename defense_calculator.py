"""Given the type(s) of a Pokemen, this program will answer:
* what types can/can't beat it up ?

It prints the following information to the user:
todo: MAKE FMT"""

def defense_calculator(pokemon_type1, pokemon_type2):
    # Dictionary for the final defensive multipliers based on each of the types:
    defense_multiplier_dict = {
        "normal": {
            2: ["fighting"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "psychic", "bug", "rock", "dragon", "dark", "steel", "fairy"],
            0: ["ghost"]
        },
        "fire": {
            2: ["water", "ground", "rock"],
            1: ["normal", "electric", "fighting", "poison", "flying", "psychic", "ghost", "dragon", "dark"],
            0.5: ["fire", "grass", "ice", "bug", "steel", "fairy"]
        },
        "water": {
            2: ["electric", "grass"],
            1: ["normal", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["fire", "water", "ice", "steel"]
        },
        "electric": {
            2: ["ground"],
            1: ["normal", "fire", "water", "ice", "fighting", "poison", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["electric", "flying", "steel"]
        },
        "grass": {
            2: ["fire", "ice", "poison", "flying", "bug"],
            1: ["normal", "fighting", "psychic", "rock", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["water", "electric", "grass", "ground"]
        },
        "ice": {
            2: ["fire", "fighting", "rock", "steel"],
            1: ["normal", "water", "electric", "grass", "poison", "ground", "flying", "psychic", "bug", "ghost", "dragon", "dark", "fairy"],
            0.5: ["ice"]
        },
        "fighting": {
            2: ["flying", "psychic", "fairy"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "fighting", "poison", "ground", "ghost", "dragon", "steel"],
            0.5: ["bug", "rock", "dark"]
        },
        "poison": {
            2: ["ground", "psychic"],
            1: ["normal", "fire", "water", "electric", "ice", "flying", "rock", "ghost", "dragon", "dark", "steel"],
            0.5: ["grass", "fighting", "poison", "bug", "fairy"]
        },
        "ground": {
            2: ["water", "grass", "ice"],
            1: ["normal", "fire", "fighting", "ground", "flying", "psychic", "bug", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["poison", "rock"],
            0: ["electric"]
        },
        "flying": {
            2: ["electric", "ice", "rock"],
            1: ["normal", "fire", "water", "poison", "flying", "psychic", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["grass", "fighting", "bug"],
            0: ["ground"]
        },
        "psychic": {
            2: ["bug", "ghost", "dark"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "rock", "dragon", "steel", "fairy"],
            0.5: ["fighting", "psychic"]
        },
        "bug": {
            2: ["fire", "flying", "rock"],
            1: ["normal", "water", "electric", "ice", "poison", "psychic", "bug", "ghost", "dragon", "dark", "steel", "fairy"],
            0.5: ["grass", "fighting", "ground"]
        },
        "rock": {
            2: ["water", "grass", "fighting", "ground", "steel"],
            1: ["electric", "ice", "psychic", "bug", "rock", "ghost", "dragon", "dark", "fairy"],
            0.5: ["normal", "fire", "poison", "flying"]
        },
        "ghost": {
            2: ["ghost", "dark"],
            1: ["fire", "water", "electric", "grass", "ice", "ground", "flying", "psychic", "rock", "dragon", "steel", "fairy"],
            0.5: ["poison", "bug"],
            0: ["normal", "fighting"]
        },
        "dragon": {
            2: ["ice", "dragon", "fairy"],
            1: ["normal", "fighting", "poison", "ground", "flying", "psychic", "bug", "rock", "ghost", "dark", "steel"],
            0.5: ["fire", "water", "electric", "grass"]
        },
        "dark": {
            2: ["fighting", "bug", "fairy"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "poison", "ground", "flying", "rock", "dragon", "steel"],
            0.5: ["ghost", "dark"],
            0: ["psychic"]
        },
        "steel": {
            2: ["fire", "fighting", "ground"],
            1: ["water", "electric", "ghost", "dark"],
            0.5: ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"],
            0: ["poison"]
        },
        "fairy": {
            2: ["poison", "steel"],
            1: ["normal", "fire", "water", "electric", "grass", "ice", "ground", "flying", "psychic", "rock", "ghost", "fairy"],
            0.5: ["fighting", "bug", "dark"],
            0: ["dragon"]
        }
    }

    # The final result that's returned to the user will populate here
    defense_analysis = {
        4: [],
        2: [],
        1: [],
        0.5: [],
        0.25: [],
        0: []
    }

    # Placeholder dictionary to help determine the final multiplier, given some type(s)
    calc_final_multiplier_dict = {
        # E.g. "normal": 1
    }

    # Append the first type to multiplier_dict to determine final multiplier:
    for multiplier in defense_multiplier_dict[pokemon_type1]:
        for defense_dict_type in defense_multiplier_dict[pokemon_type1][multiplier]:
            calc_final_multiplier_dict[defense_dict_type] = multiplier
    
    # Repeat for second type && compare its multiplier to determine final one:
    if pokemon_type2 != "none":
        for multiplier in defense_multiplier_dict[pokemon_type2]:
            for defense_dict_type in defense_multiplier_dict[pokemon_type2][multiplier]:
                # Compare the multipliers and multiply them to determine the new multiplier for that type:
                if defense_dict_type in calc_final_multiplier_dict:
                    calc_final_multiplier_dict[defense_dict_type] *= multiplier
    
    # Insert data into defense_analysis in a clean format
    for type in calc_final_multiplier_dict:
        # Insert the type into the correct list in defense_analysis
        defense_analysis[calc_final_multiplier_dict[type]].append(type)
    
    # Analysis prompts dictionary
    analysis_prompts = {
        4: "VERY strong against",
        2: "strong against",
        1: "weak against",
        0.5: "VERY weak against",
        0.25: "VERY weak against",
        0: "NO EFFECT against"
    }

    # Create a formal format for the output e.g. "normal" -> "Normal":
    formal_types = ([pokemon_type1[0].upper() + pokemon_type1[1:], pokemon_type2[0].upper() + pokemon_type2[1:]])
    print(f"\nHere's the defensive analysis (what types are strong/weak against {formal_types}):")   
    
    for multiplier in defense_analysis:
        formal_multiplier = str(multiplier) + "x"
        if defense_analysis[multiplier] != []:
            print(f"\nThe following types are {analysis_prompts[multiplier]} {formal_multiplier} {defense_analysis[multiplier]}:")
    

    # if defense_analysis[4] != []:
    #     print(f"\nThe following types are VERY strong against your given type(s): {defense_analysis[4]}")
    # if defense_analysis[2] != []:
    #     print(f"\nThe following types are strong against your given type(s): {defense_analysis[2]}")
    # if defense_analysis[0.5] != []:
    #     print(f"\nThe following types are weak against your given type(s): {defense_analysis[0.5]}")
    # if defense_analysis[0.25] != []:
    #     print(f"\nThe following types are VERY weak against your given type(s): {defense_analysis[0.25]}")
    # if defense_analysis[0] != []:
    #     print(f"\nThe following types have NO EFFECT against your given type(s): {defense_analysis[0]}")

    
    
    print(f"\nPokemon types: {formal_types[0]}, {formal_types[1]}")
    print(f"\nHere's the defense analysis after both types were analyzed: \n{defense_analysis}")
    
    return
