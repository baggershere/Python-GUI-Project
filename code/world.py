from utils import *
#from room import *
#from characters import *
import os
#from time import sleep
#from player import *

class World:
    '''A class refering to the main functions that need to take place in the world'''
    def __init__ (self, location_data, item_data, map_data):
        self.location_data = location_data
        self.item_data = item_data
        self.map_data = map_data

    def get_item_data(self):
        '''Get all the items in your inventory from a itemData.txt file'''
        file = open(self.item_data, 'r')
        #separate each  in the .txt file 
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines

    def get_map_data(self):
        '''A function that calls the players current coordinates from mapData.txt'''
        file = open(self.map_data, 'r')
        coordinate = file.read()
        file.close()
        return int(coordinate)

    def save_map_data(self, data):
        '''Updates the players current position in the mapData.txt which will be saved'''
        file = open(self.map_data, 'w')
        file.write(str(data))
        file.close()

    def print_map(self):
        '''Prints the map if in the hallway of the world. Takes the current coordinates and calls the variable linked to the correct map in utils.py based on the cooridnates '''
        maps = [map_one, map_two, map_three]
        for map in maps[self.get_map_data() - 1]:
            print(map)
    
    def game_started(self):
        '''Saves 'True' to the game_state.txt file which will stop the intro from running in the game'''
        file = open('game_state.txt', 'w')
        file.write('True')
        file.close()

    def save_clothing(self, clothing):
        file = open('clothing_choice.txt', 'w')
        file.write(clothing)
        file.close

    def save_drink(self, drink):
        file = open('drink_choice.txt', 'w')
        file.write(drink)
        file.close
    
    def game_end(self):
        '''Saves 'False' to game_state.txt which means that the next time you run the game, the intro will run.
        All the items from the players inventory (intemData.txt) will be removed so that it is empty. 
        All items will be rewritten to world_item_data.txt to reset the game for next time'''
        file = open('game_state.txt', 'w')
        file.write('False')
        file.close() 
        inven_file = open('itemData.txt', 'w')
        inven_file.write('')
        inven_file.close()
        world_inven_file = open('world_item_data.txt', 'w+')
        world_inven_file.write('a mysterious key\n')
        world_inven_file.write('a bottle of whiskey\n')
        world_inven_file.write('a stained shirt\n')
        world_inven_file.write('a pair of gloves\n')
        world_inven_file.write('an eye patch\n')
        world_inven_file.write('a pair of glasses\n')
        world_inven_file.write('a skrew driver\n')
        world_inven_file.write('a military jacket\n')
        world_inven_file.write('a tie\n')
        world_inven_file.write('a cap\n')
        world_inven_file.write('a pair of trousers\n')
        world_inven_file.write('a pair of old shoes\n')
        world_inven_file.write('a copy of the Galactic Daily\n')
        world_inven_file.write('a military pin')
        world_inven_file.close()
        save_money(0)

        character_creation = open('character_creation.txt', 'r+')
        character_creation.truncate(0)
        character_creation.close()

        self.save_map_data(1)

    def check_game_state(self):
        '''Checks whether the game is currently being played or not. This is saved so that the player can come back and continue playing'''
        file = open('game_state.txt', 'r')
        line = file.read()
        file.close()
        return line   
