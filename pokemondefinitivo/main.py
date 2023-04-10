#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Francisco Hernando Gallego (francisco.hernandogallego@ceu.es)
           Ruben Juarez Cadiz (ruben.juarezcadiz@ceu.es)

@version :  0.0.1, 08 November 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.



def get_data_from_user(name_file):
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------
      [ ] = get_data_from_user(name_file)

    Parameters
    ----------
      name_file str Name of the CSV file.

    Returns
    -------
      list_pokemons List of Pokemons obtained from CSV .

    Example
    -------
      >>> list_pokemons = get_data_from_user("file.csv")
    """
        list_pokemons = []
        weapon_map = {"headbutt": WeaponType.HEADBUTT, "punch": WeaponType.PUNCH,
                      "kick": WeaponType.KICK, "elbow": WeaponType.ELBOW}

        with open(name_file, "r") as file:
            reader = csv.reader(file)
            for line in reader:
                weapon_type = weapon_map[line[2]]
                pokemon = Pokemon(int(line[0]), str(line[1]), weapon_type, int(line[3]), int(line[4]), int(line[5]))
                list_pokemons.append(pokemon)

        return list_pokemons


def get_pokemon_in_a_list_of_pokemons(pokemons):
    """Ask user to select a pokemon from a list of available pokemons."""
    while True:
        try:
            print("Available Pokemons:")
            for i, pokemon in enumerate(pokemons):
                print(f"{i + 1}. {pokemon.name} (HP: {pokemon.hp})")
            choice = int(input("Select a Pokemon (1-3): "))
            if choice not in range(1, 4):
                raise ValueError("Invalid choice, please select a number between 1 and 3.")
            elif pokemons[choice-1].hp <= 0:
                raise ValueError("That Pokemon is already defeated, please select another one.")
            return pokemons[choice - 1]
        except ValueError as e:
            print(e)


def coach_is_undefeated(coach):
    """Check if the coach has any undefeated Pokemon left."""
    return any(pokemon.hp > 0 for pokemon in coach.pokemons)



def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    coach1 = get_data_from_user("coach_1_pokemons.csv")
    print(coach1)

    # Get configuration for Game User 2.
    coach2 = get_data_from_user("coach_2_pokemons.csv")
    for i in coach2:
        print(i)


    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of pokemons:
    entrenadores_pokemon = [coach1, coach2]
    print(entrenadores_pokemon)

    # Choose first pokemons
    pokemons1 = get_pokemon_in_a_list_of_pokemons("coach1", coach1)
    pokemons2 = get_pokemon_in_a_list_of_pokemons("coach2", coach2)

    # Main loop.
    while coach_is_undefeated(coach1) and coach_is_undefeated(coach2):
        # escoger al azar quién empieza
        player_turn = random.randint(1, 2)
        if player_turn == 1:
            current_player = coach1
            other_player = coach2
        else:
            current_player = coach2
            other_player = coach1

        print("Jugador {} comienza".format(player_turn))

        # esocgicion de pokemons
        current_pokemon = current_player.choose_pokemon()
        other_pokemon = other_player.choose_pokemon()
        print("Jugador {} escoge a {}".format(player_turn, current_pokemon.pokemon_name))
        print("Jugador {} escoge a {}".format(3 - player_turn, other_pokemon.pokemon_name))


        while current_pokemon.health_points > 0 and other_pokemon.health_points > 0:
            print("Jugador {} ataca".format(player_turn))
            current_pokemon.fight_attack(other_pokemon)
            print("{} realiza {} puntos de daño".format(current_pokemon.pokemon_name,
                                                        current_pokemon.attack_rating - other_pokemon.defense_rating))


            if other_pokemon.health_points <= 0:
                other_player.remove_pokemon(other_pokemon)
                if coach_is_undefeated(coach1) == False or coach_is_undefeated(coach2) == False:
                    break
                else:
                    other_pokemon = other_player.choose_pokemon()
                    print("Jugador {} escoge a {}".format(3 - player_turn, other_pokemon.pokemon_name))


            print("Jugador {} ataca".format(3 - player_turn))
            other_pokemon.fight_attack(current_pokemon)
            print("{} realiza {} puntos de daño".format(other_pokemon.pokemon_name,
                                                        other_pokemon.attack_rating - current_pokemon.defense_rating))

            if current_pokemon.health_points <= 0:
                current_player.remove_pokemon(current_pokemon)
                if coach_is_undefeated(coach1) == False or coach_is_undefeated(coach2) == False:
                    break
                else:
                    current_pokemon = current_player.choose_pokemon()
                    print("Jugador {} escoge a {}".format(player_turn, current_pokemon.pokemon_name))

        # determinar ganador
        if len(coach1) == 0:
            print("Jugador 2 gana la partida")
            break
        elif len(coach2) == 0:
            print("Jugador 1 gana la partida")
            break

    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")


    print("Game User 2:")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
