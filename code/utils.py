from time import sleep
import sys
import random

def random_int(num):
    return random.randint(0, num)

letter_options = [' (a) ', ' (b) ', ' (c) ', ' (d) ']


def save_item_data(data):
    #Open the .txt file that you want to save your item/inventory data to. Use 'a' to add to the file instead of overwriting it
    file = open('itemData.txt', 'a')
    file.write(str(data))
    file.close()

def check_item_data(): #get all the items from the .txt file 
    #open the item data file in 'r' (read) mode
    file = open('itemData.txt', 'r')
    #Get each item (line) from the file using .readlines by using a for loop on the lines. Remove whitespace and '\n' using strip
    lines = [line.strip() for line in file.readlines()]
    #close file
    file.close()
    #return the lines which are now the items in your inventory. Call print(check_item_data) to print the lines
    return lines

def get_map_data():
    file = open('mapData.txt', 'r')
    #Get the current coordinates of the player from the file
    coordinate = file.read()
    file.close()
    #return the coordinates as an integer
    return int(coordinate)

def check_world_item_data():
    #get a list of the items that haven't yet been collected from the world. Remove the '/n' by using strip()
    file = open('world_item_data.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    file.close()
    return lines

def count_items_left():
    player_items = str(len(check_item_data()))
    world_items = str(len(check_world_item_data()))
    return player_items 
    

def save_map_data(data):
    #Save current player position to the .txt file
    file = open('mapData.txt', 'w')
    file.write(str(data))
    file.close()

def remove_world_data_item(item):
    #Remove an item from the current list of uncollected items left in the world. Rewrite the list without the removed item.
    items = check_world_item_data()
    file = open('world_item_data.txt', 'w')
    items.remove(item)
    for item in items:
        file.write(item + '\n')    
    file.close()  

def room_description(room):
    #print a description of the room
    if room == 'bar':
        print(f'{room} desc')
    elif room == 'viperdeck':
        print(f'{room} desc')
    elif room == 'Bar':
        print(f'{room} desc')
    elif room == 'Bar':
        print(f'{room} desc')
    elif room == 'Bar':
        print(f'{room} desc')
    elif room == 'Bar':
        print(f'{room} desc')

def generate_dialogue(name):
    if name == 'Starbuck':
        print('Starbuck Dialogue')

def pprint(text):
    #letter spacing typewriter style function. REFERENCE FROM STACK OVERFLOW 
    for i in text:
        sleep(0.02)
        print(i, end='', flush=True) 

def get_drink_choice():
    # Get the drink that was chosen during character creation
    file = open('drink_choice.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    file.close()
    return lines[0]

def get_underwear_type():
    #Get the type of underwear that was input during the character creation
    file = open('clothing_choice.txt', 'r')
    lines = [line.strip() for line in file.readlines()]
    file.close()
    return lines[0]    

def game_intro():
    print('Welcome to the game blah blah blah intro and OBJ')
    print('Would you like to: ')
    print('(a) View map')

def moving_desc(direction):
    #print this when moving from one coordinate to another based on the direction moved
    print('')
    print('')
    print('')
    print(f'*********** You stagger {direction} **************')
    print('')
    print('')
    print('')

def print_inventory():
    #print current inventory containing items that you have already collected
    print(' ')
    print('********** YOUR CURRENT INVENTORY *************\n')
    print('----------------------------')
    for item in check_item_data():
        print(item)
    print('----------------------------\n')
    sleep(2)

def get_money():
    # Check how much money is currently in your wallet
    file = open('money.txt', 'r')
    money = file.read()
    file.close()
    return int(money)

def save_money(money):
    # Save money to your wallet
    file = open('money.txt', 'w')
    file.write(str(money))
    file.close()


#list of map variables for each coordinate

map_one =[ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______      ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command                Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     | Rec room       |                 '],
    ['          |   Bar                                   |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |  x  |                                  ']
]
map_two =[ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______      ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command                Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     | Rec room       |                 '],
    ['          |   Bar               x                   |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  ']
]
map_three =[ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______      ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command       x        Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     | Rec room       |                 '],
    ['          |   Bar                                   |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  ']
]

map_bar =[ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______      ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command                Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     | Rec room       |                 '],
    ['          |   Bar           x                       |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  ']
]
map_recroom =[ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______      ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command                Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     |                |                 '],
    ['          |     Bar                 x    Rec room   |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  ']
]
map_command =[ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______      ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command   x            Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     |                |                 '],
    ['          |     Bar                      Rec room   |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  ']
]
map_viperdeck =[ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______      ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command           x    Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     |                |                 '],
    ['          |     Bar                      Rec room   |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  ']
]
map_fortuneteller = [ 
    ['                        _________________                             '],
    ['                       |                |                             '],
    ['                       |    fortune     |                             '],
    ['                       |    teller      |                             '],
    ['                       |                |                             '],
    ['                       |______  x   ____|                             '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['               ______________|     |_____________                     '],
    ['              |              |     |             |                    '],
    ['              |   Command                Viper   |                    '],
    ['              |              |     |      deck   |                    '],
    ['              |______________|     |_____________|                    '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['          ___________________|     |________________                  '],
    ['          |                  |     |                |                 '],
    ['          |                  |     |                |                 '],
    ['          |     Bar                      Rec room   |                 '],
    ['          |                  |     |                |                 '],
    ['          |__________________|     |________________|                 '],
    ['                             |     |                                  '],
    ['                             |     |                                  '],
    ['                             |     |                                  ']
]