from world import *
from utils import *
from room import *
from characters import *
import pathlib

path = pathlib.Path(__file__).parent.absolute()

import tkinter as tk
from PIL import Image, ImageTk

WORLD = World('locationData.txt', 'itemData.txt', 'mapData.txt')

# Rooms in game
BAR = Room('bar', ['Starbuck', 'Lee Adama'], ['a bottle of whiskey', 'a mysterious key', 'a stained shirt'])
RECROOM = Room('recroom', ['Roslin', 'Baltar'], ['a pair of old shoes', 'a copy of the Galactic Daily'])
HALLWAY = Hallway('Hallway', [])
VIPERDECK = Room('viperdeck', ['Chief', 'Cally'], ['a skrew driver', 'a military jacket'])
COMMAND = Command('command', ['Admiral Adama', 'Gaydar'])
FORTUNETELLERROOM = Room('fortuneteller', ['Fortune teller'], [])

#Characters in game
STARBUCK = Character('Starbuck', 'Viper Pilot', ['a long and beautiful black dress', 'a pair of 8 inch Stilletos', 'and a red blouse'], ['a tie'], 5)
LEEADAMA = Character('Lee Adama', 'Captain', ['a black jacket', 'a pair of army trousers', 'and a pair of long socks'], ['a cap'], 0)
ROSLIN = Character('Roslin', 'President', ['a religious gown', 'a pair of sandals'], ['a pair of trousers'], 0)
BALTAR = Character('Baltar', 'Vice President', ['a holy symbol', 'a pair of sandals', 'a bandanna'], ['a pair of gloves'], 0)
CHIEF = Character('Chief', 'Mechanic', ['an oily jump suit', 'a beanie hat', 'a pair of dirty gloves'], ['an eye patch'], 5)
CALLY = Character('Cally', 'Deckhand', ['an oily jump suit', 'a beanie hat', 'a pair of dirty gloves'], ['a pair of glasses'], 0)
FORTUNETELLER = Character('Fortune teller', 'fortune teller', ['a red gown', 'a pendent', 'bangels'], ['a military pin'], 0)
PLAYER = Player(WORLD.get_map_data())

class Map():
    def __init__(self, root):
        self.root = root
        self.position = str(get_map_data())
        self.mapFrame = tk.Frame(root, borderwidth = 0, highlightthickness = 0)

        self.mapFrame.image1 = ImageTk.PhotoImage(Image.open(path / "image/map1.png").resize((400, 350), Image.ANTIALIAS))
        self.mapFrame.image2 = ImageTk.PhotoImage(Image.open(path / "image/map2.png").resize((400, 350), Image.ANTIALIAS))
        self.mapFrame.image3 = ImageTk.PhotoImage(Image.open(path / "image/map3.png").resize((400, 350), Image.ANTIALIAS))
        self.mapFrame.image20 = ImageTk.PhotoImage(Image.open(path / "image/map20.png").resize((400, 350), Image.ANTIALIAS))
        self.mapFrame.image30 = ImageTk.PhotoImage(Image.open(path / "image/map30.png").resize((400, 350), Image.ANTIALIAS))
        self.mapFrame.image40 = ImageTk.PhotoImage(Image.open(path / "image/map40.png").resize((400, 350), Image.ANTIALIAS))
        self.mapFrame.image50 = ImageTk.PhotoImage(Image.open(path / "image/map50.png").resize((400, 350), Image.ANTIALIAS))
        self.mapFrame.image60 = ImageTk.PhotoImage(Image.open(path / "image/map60.png").resize((400, 350), Image.ANTIALIAS))

        self.mapFrame.grid(column = 2, row = 0)

    def onclick(self):
        text = '''Move around the map and talk to characters to obtain all the items needed to enter the command room. Enter the command room once you have collected all the items needed.\n\n
        Your player position, money and items will be saved as you play.
        '''
        self.instructions_window = tk.Toplevel(self.root)
        self.instructions_window.geometry('500x300')
        tk.Label(self.instructions_window, text = text, wraplength = 400).pack()

    def display_map(self):
        self.position = str(get_map_data())
        self.map_label = tk.Label(self.mapFrame, width = 400, borderwidth = 0, highlightthickness = 0, image = eval('self.mapFrame.image' + str(self.position)))
        self.map_label.config(height = 350, width = 400)
        self.map_label.grid(row = 0, column = 2)

        button = tk.Button(self.mapFrame, text = 'Game Instructions', command = self.onclick)
        button.place(relx = 0.67, rely = 0.05)
        

class GameImage():
    def __init__(self, root):
        self.root = root
        self.position = str(get_map_data())
        self.image_frame = tk.Frame(root, borderwidth = 0, highlightthickness = 0)

        self.image_frame.image1 = ImageTk.PhotoImage(Image.open(path / "image/battlestar_hallway.jpg").resize((400, 350), Image.ANTIALIAS))
        self.image_frame.image2 = ImageTk.PhotoImage(Image.open(path / "image/battlestar_hallway.jpg").resize((400, 350), Image.ANTIALIAS))
        self.image_frame.image3 = ImageTk.PhotoImage(Image.open(path / "image/battlestar_hallway.jpg").resize((400, 350), Image.ANTIALIAS))
        self.image_frame.image20 = ImageTk.PhotoImage(Image.open(path / "image/battlestar_bar.jpg").resize((400, 350), Image.ANTIALIAS))
        self.image_frame.image50 = ImageTk.PhotoImage(Image.open(path / "image/battlestar_viperdeck.jpg").resize((400, 350), Image.ANTIALIAS))
        self.image_frame.image30 = ImageTk.PhotoImage(Image.open(path / "image/battlestar_recroom.jpg").resize((400, 350), Image.ANTIALIAS))
        self.image_frame.image60 = ImageTk.PhotoImage(Image.open(path / "image/battlestar_fortuneteller.jpg").resize((400, 350), Image.ANTIALIAS))

        self.image_frame.grid(column = 1, row = 0)

    def display_image(self):
        self.position = str(get_map_data())
        self.image_label = tk.Label(self.image_frame, width = 400, borderwidth = 0, highlightthickness = 0, image = eval('self.image_frame.image' + str(self.position)))
        self.image_label.config(height = 350, width = 400)
        self.image_label.grid(row = 0, column = 1)

class Inven():
    def __init__(self, root):
        self.player_items = check_item_data()
        self.items_left = count_items_left()
        self.player_money = str(get_money())

        self.inven_frame = tk.Frame(root, width = 400, height = 350, borderwidth = 0, highlightthickness = 0)
        self.inven_frame.grid(column = 0, row = 0)
        self.inven_frame.grid_propagate(0)

    def display_inven(self):
        self.drink_choice = get_drink_choice()
        self.underwear_choice = get_underwear_type()
        self.player_items = check_item_data()
        self.items_left = count_items_left()
        self.player_money = str(get_money())
        self.inven_frame.destroy()
        self.inven_frame = tk.Frame(root, width = 400, height = 350, borderwidth = 0, highlightthickness = 0, bg = '#CAA472')
        self.inven_frame.grid(column = 0, row = 0)
        self.inven_frame.grid_propagate(0)

        self.money_label = tk.Label(self.inven_frame, text = 'MONEY: \n You have $' + self.player_money, padx = 20, pady = 10)
        self.money_label.config(bg = '#CAA472')
        self.money_label.grid(column = 0, row = 0, sticky = 'w')

        self.money_label = tk.Label(self.inven_frame, text = 'INVENTORY:' , padx = 20, pady = 10)
        self.money_label.config(bg = '#CAA472')
        self.money_label.grid(column = 0, sticky = 'w')

        for item in self.player_items:
            item_label = tk.Label(self.inven_frame, text = item, padx = 20)
            item_label.config(bg = '#CAA472')
            item_label.grid(column = 0, sticky = 'w')
            

        self.items_left_label = tk.Label(self.inven_frame, text = self.items_left + '/14 Items Collected', padx = 20)
        self.items_left_label.config(bg = '#CAA472')
        self.items_left_label.grid(column = 1, row = 0)
        self.drink_choice_label = tk.Label(self.inven_frame, text = f'YOUR CHARACTER:\n{self.drink_choice}')
        self.drink_choice_label.config(bg = '#CAA472')
        self.drink_choice_label.grid(column = 1, row = 1)
        self.underwear_choice_label = tk.Label(self.inven_frame, text = self.underwear_choice)
        self.underwear_choice_label.config(bg = '#CAA472')
        self.underwear_choice_label.grid(column = 1, row = 2)

choice = 0
dia_flag = False

class GameArea():
    def __init__(self, root):
        
        self.game_area_frame1 = tk.Frame(root, width = 600, height = 350, borderwidth = 0, highlightthickness = 0, bg = '#CAA472')
        self.game_area_frame1.grid(column = 0, row = 1, columnspan = 2)

        self.game_area_frame2 = tk.Frame(root, width = 600, height = 350, borderwidth = 0, highlightthickness = 0, bg = '#CAA472')

        self.game_area_frame2.grid(column = 1, row = 1, columnspan = 2)

    def display_instruction(self, text):
        self.game_area_frame1.destroy()
        self.game_area_frame1 = tk.Frame(root, width = 600, height = 350, borderwidth = 0, highlightthickness = 0, bg = '#CAA472')
        self.game_area_frame1.grid(column = 0, row = 1, columnspan = 2)
        self.instruction = tk.StringVar()

        instruction_label = tk.Label(self.game_area_frame1, textvariable = self.instruction, wraplength = 500, justify = 'center')
        instruction_label.config(bg = '#CAA472', font = ("Courier", 14))
        instruction_label.grid(column = 0, row = 0)
        self.instruction.set(text)

    def display_dialogue(self, dialogue_list, instructions = None):
        self.game_area_frame1.destroy()
        self.game_area_frame1 = tk.Frame(root, width = 600, height = 350, borderwidth = 0, highlightthickness = 0, bg = '#CAA472')
        self.game_area_frame1.grid(column = 0, row = 1, columnspan = 2)

        for i, line in enumerate(dialogue_list):
            self.instruction = tk.StringVar()

            instruction_label = tk.Label(self.game_area_frame1, textvariable = self.instruction, wraplength = 500, justify = 'left', anchor = 'e')
            instruction_label.config(bg = '#CAA472', font = ("Courier", 11))
            instruction_label.grid(column = 0, row = i, sticky = 'W')
            self.instruction.set(line)
        
        if instructions:
            self.instruction = tk.StringVar()
            instruction_label = tk.Label(self.game_area_frame1, textvariable = self.instruction, wraplength = 800, justify = 'center')
            instruction_label.config(bg = '#CAA472')
            instruction_label.grid(column = 0)
            self.instruction.set(instructions)
    
    def display_input(self, options_dict):
        self.game_area_frame2.destroy()
        self.game_area_frame2 = tk.Frame(root, width = 600, height = 350, bg = '#CAA472')
        self.game_area_frame2.grid(column = 1, row = 1, columnspan = 2)
        global choice
        choice = 0
        self.v = tk.StringVar()
        self.v.set('1')
        self.btnVar = tk.StringVar()
        self.btnVar.set("")

        def onclick(btn):
            btn.config(state = tk.NORMAL)

        for (text, value) in options_dict.items(): 
            button_new = tk.Radiobutton(self.game_area_frame2, text = value, variable = self.v, value = value, command = lambda: onclick(self.btn))
            button_new.config(bg = '#CAA472')
            button_new.grid(column = 0, ipady = 0)

        self.btn = tk.Button(self.game_area_frame2, text = 'click me', command = lambda: self.btnVar.set(self.v.get()))
        self.btn.config(state = tk.DISABLED)
        self.btn.grid(column = 0)

        self.btn.wait_variable(self.btnVar)
        
        choice = self.btnVar.get()

    def return_choice(self):
        return choice


class Main():
    def __init__(self, parent):
        self.parent = parent
        self.map = Map(self.parent)
        self.inven = Inven(self.parent)
        self.game_area = GameArea(self.parent)
        self.map.display_map()
        self.inven.display_inven()
        self.image = GameImage(self.parent)
        self.image.display_image()

    def game_intro(self):
        #'''Main game loop. This is linked to the current position in mapData.txt. Depending on the position, different things will happen. Every time the player moves, the loop will re-run using the new player position.'''
        if WORLD.check_game_state() == 'False':
            #If the game_state is false, the game has not yet been started, So the introcution will run 
            self.game_area.display_instruction('''You wake up in the hallway of the BattleStar Galactics spaceship. Your name is Sol Ty, the second in command of the ship. After the Cylons destroyed the human occupied planet of Caprica 4 months ago, the Battlestar Galactica and several civilian ships have been on the run from the Cylon army. You are the only humans left in the universe. You are expected to report in the command center for duty, but after a long night of drinking you wake up with a killer hangover and only wearing your underwear. What happened to your clothes? If you want to report for duty, you must be wearing your uniform. YOUR MISSION: Search the ship for your missing clothes. Use the map to help you. Enter the command room when you have everything you need. HINT: There may be one extra item you need to find. To select an option, write what you see in the brackets () e.g. write 'map' to access the command '(Map) Open map'. What drink is Sol drinking now?''')

            self.game_area.display_input({"1" : 'Vodka', "2" : 'Whiskey', "3" : 'Rum'})

            if self.game_area.return_choice() == 'Vodka':
                WORLD.save_drink('Vodka')
                print('vods')
            elif self.game_area.return_choice() == 'Whiskey':
                WORLD.save_drink('Whiskey')
                print('whiskey')
            elif self.game_area.return_choice() == 'Rum':
                WORLD.save_drink('Rum')
                print('Rum')
            
            self.inven.display_inven()

            self.game_area.display_instruction('What type of underwear is Sol wearing?')
            self.game_area.display_input({"1" : 'Boxers', "2" : 'Briefs', "3" : 'Bikini'})

            if self.game_area.return_choice() == 'Boxers':
                WORLD.save_clothing('Boxers')
                print('Boxers')
            elif self.game_area.return_choice() == 'Briefs':
                WORLD.save_clothing('Briefs')
                print('Briefs')
            elif self.game_area.return_choice() == 'Bikini':
                WORLD.save_clothing('Bikini')
                print('Bikini')
            
            self.inven.display_inven()
            self.game_area.display_instruction(' ')
            WORLD.game_started()
            self.run_current_room()
        else:
            pass

    def run_character_scene(self, person):
        self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_character_scene_intro(), 'What would you like to do?')
        self.game_area.display_input(globals()[person.replace(' ', '').upper()].return_character_options())

        if self.game_area.return_choice() == f'Compliment {person}':
            self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_compliment(), 'Choose an option')
            self.game_area.display_input({'continue':'Continue'})
            if self.game_area.return_choice() == 'Continue':
                self.run_character_scene(person)

        elif self.game_area.return_choice() == f'Insult {person}':
            self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_insult(), 'Choose an option')
            self.game_area.display_input({'continue':'Continue'})
            if self.game_area.return_choice() == 'Continue':
                self.run_character_scene(person)

        elif self.game_area.return_choice() == f'Ask if they have anything to drink':
            self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_drink_scene(), 'Choose an option')
            self.game_area.display_input({'continue':'Continue'})
            if self.game_area.return_choice() == 'Continue':
                self.run_character_scene(person)

        elif self.game_area.return_choice() == f'Ask about your missing clothes':
            if globals()[person.replace(' ', '').upper()].return_items_held() == True:
                self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_items_scene_success(), 'Choose an option')
                self.game_area.display_input({'yes':'Yes', 'no': 'No'})
                if self.game_area.return_choice() == 'Yes':
                    self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_add_item_scene(), 'Choose an option')
                    self.game_area.display_input({'continue': 'Continue'})
                    if self.game_area.return_choice() == 'Continue':
                        self.inven.display_inven()
                        self.run_character_scene(person)
                elif self.game_area.return_choice() == 'No':
                    self.run_character_scene(person)
            else:
                self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_items_scene_fail(), 'Choose an option')
                self.game_area.display_input({'continue': 'Continue'})
                if self.game_area.return_choice() == 'Continue':
                    self.run_character_scene(person)
        
        elif self.game_area.return_choice() == f'Beg for money':
            self.inven.display_inven()
            self.game_area.display_dialogue(globals()[person.replace(' ', '').upper()].return_money_scene(), 'Choose an option')
            self.game_area.display_input({'continue': 'Continue'})
            self.inven.display_inven()
            if self.game_area.return_choice() == 'Continue':
                self.run_character_scene(person)
        
        elif self.game_area.return_choice() == 'End the conversation':
            self.run_current_room()

    def run_standard_room(self, room):
        self.game_area.display_instruction(room.return_room_instruction_1())
        self.game_area.display_input(room.return_room_options())

        if self.game_area.return_choice() == 'Exit Room':
                new_pos = PLAYER.movement('exit')
                WORLD.save_map_data(new_pos)
                self.run_current_room()
        
        elif self.game_area.return_choice() == 'Look around the room for people':
            self.game_area.display_instruction('You look around the room for people and see: ')
            self.game_area.display_input(room.return_people_dict())

            self.return_choice = self.game_area.return_choice()

            for value, person in room.return_people_dict().items():
                if self.game_area.return_choice() == 'Go Back':
                    self.run_standard_room(room)
                if self.game_area.return_choice() == person:
                    self.run_character_scene(person)
                else:
                    print('exit')
        
        elif self.game_area.return_choice() == 'Look around the room for some potential clothing':
            if len(room.list_room_loot()) > 0:
                self.game_area.display_instruction('You see some items in the room, which one would you like to take?')
                self.game_area.display_input(room.list_room_loot())
                item = self.game_area.return_choice()
                if item:
                    save_item_data(item + '\n')
                    remove_world_data_item(item)
                    self.inven.display_inven()
                    self.run_current_room()
            else:
                self.game_area.display_instruction('There are no items left in the room, you have already collected them!')
                self.game_area.display_input({'continue': 'Continue'})
                if self.game_area.return_choice() == 'Continue':
                    self.run_current_room()

    
    def run_fortune_teller_room(self, room):
        self.game_area.display_dialogue(room.return_fortune_teller_intro(), 'What would you like to do?')
        self.game_area.display_input(room.return_room_options())

        if self.game_area.return_choice() == 'Exit Room':
                new_pos = PLAYER.movement('exit')
                WORLD.save_map_data(new_pos)
                self.run_current_room()

        if self.game_area.return_choice() == 'Look around the room for people':
            self.game_area.display_instruction('You look around the room for people and see: ')
            self.game_area.display_input(room.return_people_dict())

            self.return_choice = self.game_area.return_choice()

            for value, person in room.return_people_dict().items():
                if self.game_area.return_choice() == person:
                    self.run_fortune_teller_scene(person)
                    
                else:
                    print('exit')
    
    def run_fortune_teller_scene(self, person):
        self.game_area.display_instruction('What would you like to do?')
        self.game_area.display_input({'1':'Ask the Fortune Teller about missing clothes', '2':'Exit the room'})
        
        if self.game_area.return_choice() == 'Ask the Fortune Teller about missing clothes':
            if get_money() >= 40 and 'a military pin' not in check_item_data():
                self.game_area.display_dialogue(
                    [
                        'Fortune teller: I do have this Military pin actually... but it\'s going to cost you 60 Galactic Dollars',
                        'Sol: I expected nothing less from a scam artist like yourself...',
                        '****** The Fortune teller gives you your military pin *********'
                    ],
                    'Choose an option'
                )

                save_item_data('a military pin\n')
                remove_world_data_item('a military pin')
                self.game_area.display_input({'continue': 'Continue'})
                if self.game_area.return_choice() == 'Continue':
                    self.run_current_room()

            elif 'a military pin' in check_item_data():
                self.game_area.display_dialogue([
                    'Fortune teller: I\'ve already given you your stupid pin!'
                ], 'Choose an option')
                self.game_area.display_input({'continue': 'Continue'})
                if self.game_area.return_choice() == 'Continue':
                    self.run_current_room()

            elif get_money() < 40:
                self.game_area.display_dialogue([
                    'Fortune teller: I do have this Military pin actually... but it\'s going to cost you 40 Galactic Dollars',
                    'Sol: I expected nothing less from a scam artist like yourself...',
                    f'Oh no! I only have {get_money()}... The cost is 40 Dollars. You might want to ask some of your colloeagues on the ship'
                ],  'Choose an option')
                self.game_area.display_input({'continue': 'Continue'})
                if self.game_area.return_choice() == 'Continue':
                    self.run_current_room()
    
    def run_command_room(self):
        item_data = check_item_data()
        
        if not set(['a stained shirt', 'a tie', 'a cap', 'a pair of trousers', 'a pair of old shoes', 'a pair of gloves', 'an eye patch', 'a pair of glasses']).issubset(set(item_data)):
            self.game_area.display_dialogue([
                'You haven\'t found all your clothes yet, keep looking!'
            ], 'Press continue')
            self.game_area.display_input({'continue': 'Continue'})
            if self.game_area.return_choice() == 'Continue':
                save_map_data(PLAYER.movement('exit'))
                self.run_current_room()

        elif set(['a stained shirt', 'a tie', 'a cap', 'a pair of trousers', 'a pair of old shoes', 'a pair of gloves', 'an eye patch', 'a pair of glasses']).issubset(set(item_data)) and 'a mysterious key' not in item_data:
            self.game_area.display_dialogue([
               'You have all the clothes you need but you are unable to unlock the door, perhaps a key is needed'
            ], 'Press continue')
            self.game_area.display_input({'continue': 'Continue'})
            if self.return_choice() == 'Continue':
                save_map_data(PLAYER.movement('exit'))
                self.run_current_room()
            
        
        elif set(['a stained shirt', 'a tie', 'a cap', 'a pair of trousers', 'a pair of old shoes', 'a pair of gloves', 'an eye patch', 'a pair of glasses']).issubset(set(item_data)) and 'a mysterious key' in item_data:
            WORLD.save_map_data(40)
            self.game_area.display_dialogue(COMMAND.run_command_scene(), 'Game complete!')  
            self.game_area.display_input({'continue': 'Continue'})
            if self.game_area.return_choice() == 'Continue':
                self.game_area.display_instruction('Congratulations! You have completed the game')
                self.game_area.display_input({'continue': 'Continue'})
                if self.game_area.return_choice() == 'Continue':
                    self.parent.destroy()

    def run_current_room(self):
        self.inven.display_inven()
        self.map.display_map()
        
        if WORLD.get_map_data() == 1:
            self.inven.display_inven()
            self.map.display_map()
            self.image.display_image()

            self.game_area.display_instruction('''What would you like to do?''')
            self.game_area.display_input({'north': 'Move North'})

            if self.game_area.return_choice() == 'Move North':
                new_pos = PLAYER.movement('north')
                WORLD.save_map_data(new_pos)
                
            self.run_current_room()
            
        elif WORLD.get_map_data() == 2:
            self.inven.display_inven()
            self.map.display_map()
            self.image.display_image()
            
            options = HALLWAY.main_options_menu(['north', 'south', 'bar', 'recroom'])
            self.game_area.display_instruction('''What would you like to do?''')
            self.game_area.display_input(options)

            if self.game_area.return_choice() == 'Move North':
                new_pos = PLAYER.movement('north')
                WORLD.save_map_data(new_pos)
            elif self.game_area.return_choice() == 'Move South':
                new_pos = PLAYER.movement('south')
                WORLD.save_map_data(new_pos)
            elif self.game_area.return_choice() == 'Enter Bar':
                new_pos = PLAYER.movement('bar')
                WORLD.save_map_data(new_pos)
            elif self.game_area.return_choice() == 'Enter Rec room':
                new_pos = PLAYER.movement('recroom')
                WORLD.save_map_data(new_pos)
            
            self.run_current_room()
        
        elif WORLD.get_map_data() == 3:
            self.inven.display_inven()
            self.map.display_map()
            self.image.display_image()
            
            options = HALLWAY.main_options_menu(['fortuneteller', 'south', 'command', 'viperdeck'])
            self.game_area.display_instruction('''What would you like to do?''')
            self.game_area.display_input(options)

            if self.game_area.return_choice() == 'Move South':
                new_pos = PLAYER.movement('south')
                WORLD.save_map_data(new_pos)
            elif self.game_area.return_choice() == 'Enter the Viper Deck':
                new_pos = PLAYER.movement('viperdeck')
                WORLD.save_map_data(new_pos)
            elif self.game_area.return_choice() == 'Enter the Fortune teller\'s room':
                new_pos = PLAYER.movement('fortuneteller')
                WORLD.save_map_data(new_pos)
            elif self.game_area.return_choice() == 'Enter the command room':
                new_pos = PLAYER.movement('command')
                WORLD.save_map_data(new_pos)
            
            self.run_current_room()
        
        elif WORLD.get_map_data() == 20:
            self.inven.display_inven()
            self.map.display_map()
            self.image.display_image()
            self.run_standard_room(BAR)

        elif WORLD.get_map_data() == 30:
            self.inven.display_inven()
            self.map.display_map()
            self.image.display_image()
            self.run_standard_room(RECROOM)

        elif WORLD.get_map_data() == 40:
            self.inven.display_inven()
            self.map.display_map()
            self.run_command_room()

        elif WORLD.get_map_data() == 50:
            self.inven.display_inven()
            self.map.display_map()
            self.image.display_image()
            self.run_standard_room(VIPERDECK)
        
        elif WORLD.get_map_data() == 60:
            self.inven.display_inven()
            self.map.display_map()
            self.image.display_image()
            self.run_fortune_teller_room(FORTUNETELLERROOM)

            
if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background = 'black')
    root.geometry('1200x700')
    Main(root)
    Main(root).game_intro()
    Main(root).run_current_room()
    root.mainloop()

# Fix padding issues and add an instructions button
