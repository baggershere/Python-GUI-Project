from utils import *
from characters import *
import collections

#Instansiate characters which will be placed in each room. Arguments consist of their name, rank, clothes worn and items held
 
class Room:
    '''General room functions and interactions'''
    def __init__(self, room, people, loot):
        self.room = room
        self.people = people
        self.loot = loot
    
    def enter_room(self):
        print(f'You enter the {self.room}...')
    
    def describe_room(self):
        print(f'You are in the {self.room}')
    
    def search_characters(self):
        '''Search for which characters are in the room that you are in and list them'''
        print('You have a look around and notice...')
        for person in self.people:
            print(person)
        response = input('Who would you like to talk to? ')

    def list_room_loot(self):
        '''Print loot in room'''
        room_loot = {}
        for i, item in enumerate(self.loot):
            if item in check_world_item_data():
                room_loot[i + 1] = item
        return room_loot

    def save_item_data(self, data):
        '''Add an item to your inventory'''
        file = open('itemData.txt', 'a')
        file.write(str(data))
        file.close()
    
    def get_item_data(self):
        '''Check and list current items in player inventory'''
        file = open('itemData.txt', 'r')
        lines = [line.strip() for line in file.readlines()]
        file.close()
        return lines

    def return_room_options(self):
        options_room = {
            "1": "Look around the room for people",
            "2": "Look around the room for some potential clothing",
            "3": "Exit Room"
        }
        return options_room
    
    def return_room_instruction_1(self):
        return f'Youre now in the {self.room}, what would you like to do?'

    def options(self):
        '''options available to player in each room when you first enter'''
    
    def return_people_dict(self):
        people = {}
        for i in range(len(self.people)):
            people[str(i + 1)] = self.people[i]
        people['exit'] = 'Go Back'
        return people
    
    def return_fortune_teller_intro(self):
        return [
            'Fortune teller: Hello Sol, the frequency of your visits is starting to get weird...',
            'Sol: Well I\'m not here for your fairy tales today... I\'m looking for for my military pin',
            'Fortune teller: Does the Admiral know that you are one of the five Cylon models?',
            'Sol: Watch your mouth... Last I checked I\'m still the XO of this ship!'
        ] 
            
    
    # print()
    # flag = True
    # while flag:
    #     '''Start main room loop. Call the map variable from utils.py using the name of the current room in the room class'''
    #     for line in globals()['map_' + self.room]:
    #         print(line)
    #     print('\n')
    #     # Print players options for room
    #     for key in options_room.keys():
    #         print(options_room[key] + '\n')
    #     print('\n')
    #     response = input('What would you like to do? ').lower().replace(' ', '')
    #     # Conditional statements based on the response to main player options.
    #     if response == 'a':
    #         '''Next loop to deal with the '(a) Look around for people' response to main options'''
    #             # list the people in the room and choose who you want to speak to
    #         for person in self.people:
    #             print(f'({person}) {person} \n') 
    #         print('(Back) Go Back\n')
    #         print('\n')
    #         approach_response = input('Who would you like to talk to? ').lower().replace(' ', '')
    #         # call the scene the relates to the option chosen. The scene can be called for each character that was declared at the top of the file.
    #         if approach_response == 'back':
    #             flag2 = False                    
    #         elif approach_response == self.people[0].lower().replace(' ', ''):
    #             globals()[self.people[0].upper().replace(' ', '')].run_scene()
    #         elif len(self.people) > 1: 
    #             if approach_response == self.people[1].lower().replace(' ', ''):
    #                 globals()[self.people[1].upper().replace(' ', '')].run_scene()
    #         # elif approach_response == 'back':
    #         #     flag2 = False          
    #     elif response == 'b':
    #         '''(b) Look around the room option for items. List items.'''
    #         flag3 = True
    #         while flag3:
    #             if not set(self.loot).issubset(check_item_data()):          
    #                 print(' ')
    #                 print(f'You look around the room and notice a few things lying around...')
    #                 print(' ')
    #                 for i in range(len(self.loot)):
    #                     if self.loot[i] not in check_item_data():
    #                         print(' ')
    #                         print(letter_options[i] + self.loot[i])
    #                         print(' ')
    #                 print(' ')
    #                 print(' (Back) Go back')
    #                 print(' ')
    #                 response = input('What would you like to take? ').lower()
    #                 # If items listed, check whether or not the items has been taken already. If not, don't list the item.
    #                 if response == 'a' and self.loot[0] not in check_item_data() and self.loot[0] in check_world_item_data():
    #                     save_item_data(self.loot[0] + '\n')
    #                     remove_world_data_item(self.loot[0])
    #                     print(' ')
    #                     print('\n')
    #                     print(f'************You add {self.loot[0]} to your inventory***********\n')
    #                     print(' ')
    #                     sleep(2)
    #                 elif response == 'b' and self.loot[1] not in check_item_data() and self.loot[1] in check_world_item_data():
    #                     save_item_data(self.loot[1] + '\n')
    #                     remove_world_data_item(self.loot[1])
    #                     print('\n')
    #                     print(f'***************You add {self.loot[1]} to your inventory***************\n')   
    #                     print(' ')
    #                     sleep(2)
    #                 elif response == 'c' and self.loot[2] not in check_item_data() and self.loot[2] in check_world_item_data():
    #                     self.save_item_data(self.loot[2] + '\n')
    #                     remove_world_data_item(self.loot[2])
    #                     print(' ')
    #                     print(f'You put on the {self.loot[2]}')
    #                     print(' ')
    #                 elif response == 'back':
    #                     flag3 = False
    #             else:
    #                 print(' ')
    #                 print('You can\'t seem to find any items')
    #                 print(' ')
    #                 flag3 = False
    #                 sleep(2)
    #     elif response == 'c':
    #         print_inventory()
    #     elif response == 'd':
    #         for line in globals()['map_' + self.room]:
    #             print(line)
    #     elif response == 'e':
    #         print(' ')
    #         print('You leave the ' + self.room)
    #         print(' ')
    #         if get_map_data() == 20 or get_map_data() == 30:
    #             save_map_data(2)
    #         elif get_map_data() == 50 or get_map_data() == 60:
    #             save_map_data(3)
    #         flag = False

class Hallway(Room):
    '''Special options for hallway'''
    def __init__(self, room, people):
        super().__init__(self, room, people)
        self.room = room
        self.people = people
    
    def main_options_menu(self, options_required):
        options = {
            'question': 'What would you like to do? ',
            'north': 'Move North',
            'east': 'Move East',
            'south': 'Move South',
            'west': 'Move West',
            'bar': 'Enter Bar',
            'fortuneteller': 'Enter the Fortune teller\'s room',
            'recroom': 'Enter Rec room',
            'command': 'Enter the command room',
            'viperdeck': 'Enter the Viper Deck',
            'searchforpeople': 'Look around the room for people',
            'searchforloot': 'Look around the room for items',
        }
        required_options = {}
        for item_key in options_required:
            required_options[item_key] = options.get(item_key)

        return required_options


class Command(Room):
    '''Special options for the command'''
    def __init__(self, room, people):
        super().__init__(self, room, people)
        self.room = room
        self.people = people

    def run_command_scene(self):
        return [
            '*** You stroll into the command center trying not to look too hungover... ***',
            'Admiral Adama: Where have you been Sol?',
            'Sol: I had a few errands to run this morning',
            'Admiral Adama: Good to have you back Sol',
            'Sol: How are we doing with the settlement on New Caprica?',
            '********* Alarm signs start ***********',
            'Gaydar: Enemy contact! 3 Cylon Base ships just jumped into orbit',
            'Sol: Fire up the FTL drives',
            'Admiral Adama: Let\'s get the hell out of here',
            '******* This has happened before and it will happen again *********'
        ]

class Fortune_Teller_Room(Room):
    def __init__ (self, room, people, loot):
        super().__init__(room, people, loot)
        self.room = room
        self.people = people
    
    def test(self):
        print(self.people)