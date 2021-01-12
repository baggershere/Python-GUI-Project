from utils import *
from time import sleep


class Player:
    '''The player class. When a command is called from the game menu, the position of the player will change accordingly. This will eventually be saved to the mapData.txt file to log the current position of the player'''
    def __init__ (self, pos):
        self.pos = pos

    def movement(self, command):
        if command == 'north':
            self.pos += 1

        elif command == 'south':
            self.pos -= 1
            
        elif command == 'bar' and self.pos == 2:
            self.pos = 20
        
        elif command == 'recroom' and self.pos == 2:
            self.pos = 30

        elif command == 'viperdeck' and self.pos == 3:
            self.pos = 50

        elif command == 'command' and self.pos == 3:
            self.pos = 40

        elif command == 'fortuneteller' and self.pos == 3:
            self.pos = 60
        
        elif command == 'exit' and self.pos == 20:
            self.pos = 2

        elif command == 'exit'and self.pos == 30:
            self.pos = 2

        elif command == 'exit' and self.pos == 40:
            self.pos = 3  

        elif command == 'exit' and self.pos == 50:
            self.pos = 3  

        elif command == 'exit' and self.pos == 60:
            self.pos = 3
        

        return self.pos
    
    def get_pos(self):
        return self.pos

class Character:
    '''Create a character in the world. Character is created in the room.py file.'''
    def __init__(self, name, rank, wearing, items_held, money):
        self.name = name
        self.money = money
        self.rank = rank
        self.wearing = wearing
        self.items_held = items_held
    
        self.character_speak_one = {
            'Baltar': 'Well when you put it like that, it does sound quite tempting...',
            'Roslin': 'Oh, sorry Sol, I didn\'t see you there... I was just reading the holy scriptures, trying to determine our next step in locating the Eye Of Jupiter...',
            'Lee Adama': 'Not on duty today Sol?',
            'Starbuck': 'Well well well, look what the cat dragged in',
            'Chief': 'Hey Sol, good to see you!',
            'Cally': 'Sol Ty! I loved your dance moves last night!'
        }
        self.sol_reply_one = {
            'Baltar': 'Gods dammit Baltar, who are you talking to?',
            'Roslin': 'And you\'re the one supposed to be guiding us to earth, based on a book? I\'ve never prayed before but I might have to start now!' ,
            'Lee Adama': 'The only reason you can speak to me like that is because you\'re the Admiral\'s son!',
            'Starbuck': 'Everywhere I go I just get abuse... Last time I checked I\'m still the XO of this ship!',
            'Chief': 'How\'s everything going down here?',
            'Cally': 'You didn\'t look too bad yourself last night, from what I can remember'
        }
        self.character_speak_two = {
            'Baltar': 'Sorry, I was just talking to... never mind. What can I do for you Sol?',
            'Roslin': 'I am the dying leader described in the holy scriptures Sol...',
            'Lee Adama': 'And because you probably won\'t remember this by tomorrow morning after you fnish that bottle you\'ve got in your hands',
            'Starbuck': 'Respect is earned Sol',
            'Chief': 'We are making good progress on our new Viper',
            'Cally': 'Were you watching me again? You do know I\'m married right?'
        }
        self.sol_reply_two = {
            'Baltar': 'The last thing I want is talking to your crazy ass with this killer hangover but I just wanted to say...',
            'Roslin': 'I\'m not here to talk about this anyway',
            'Lee Adama': 'I don\'t get any respect around here...',
            'Starbuck':'You should take a page out of your own book Starbuck',
            'Chief':'Good job Chief',
            'Cally': 'I know, I know...'
        }
        #compliments and inults for the insult and compliment options
        self.compliments = [f'Gods damn it {self.name}, you\'re looking great today', 'Last night was fun, it wouldn\'t have been the same without you', f'Well if it isn\'t the best {self.rank} in the fleet!']
        self.insults =[f'Looking rough there {self.name}', f'Jeez {self.name}, you look worse than me this morning', f'Gods damn it {self.name}, you\'re the last person I want to see this morning']
        #special insults for the character to say back
        self.character_insults = [f'Says the one standing half naked with a bottle of whiskey in his hand', f'Well you\'re cheerful this morning', f'You look homeless Sol']


    def return_character_options(self):
        return{
            'compliment': f'Compliment {self.name}',
            'insult': f'Insult {self.name}',
            'mission': 'Ask about your missing clothes',
            'drink': 'Ask if they have anything to drink',
            'money': 'Beg for money',
            'end': 'End the conversation'
        }
    #When you first appraoch a character, this will run.
    def approach_character(self):
        print(f'You slowly walk up to {rank} {name}, trying not to fall over')
    #print options
    def options_character(self):
        for key, value in self.return_character_options.items():
            print(value)
    #Describe the character
    def describe_character(self):
        print(f'You see {self.name} wearing ')
        print(*self.wearing, sep=', ')
        sleep(1.5)

    #Everything that happens when you choose to interact with a character

    def return_character_scene_intro(self):
        return [
            f'{self.name}: {self.character_speak_one[self.name]}. I didn\'t have you down for a {get_underwear_type()} guy. Is that a bottle of {get_drink_choice()}? Still going strong I see...',
            f'Sol: {self.sol_reply_one[self.name]}',
            f'{self.name}: {self.character_speak_two[self.name]}',
            f'Sol: {self.sol_reply_two[self.name]}'
            ]
    
    def return_compliment(self):
        return [
            f'Sol: {self.compliments[random_int(len(self.compliments) - 1)]}',
            f'{self.name}: What do you want Sol?',
            'Sol: You watch your mouth, I\'m the XO of this ship'
        ]
    
    def return_insult(self):
        return [
            f'Sol: {self.insults[random_int(len(self.insults) - 1)]}',
            f'{self.name}: {self.character_insults[random_int(len(self.character_insults) - 1)]}',

        ]
    
    def return_drink_scene(self):
        return [
            'Sol: I could use a drink, you don\'t have anything do you?',
            f'{self.name}: Is that bottle of {get_drink_choice()} in your hand not enough for you Sol?',
            'Sol: You got anything or not?',
            f'{self.name}: Here...',
            f'************ You take a shot with {self.name} *************',
            'Sol: That\'s better'
        ]
    
    def return_items_held(self):
        if self.items_held[0] in check_world_item_data():
            return True
        else:
            return False

    def return_items_scene_success(self):
        return [
            'Sol: It pains me to be the one asking you this, but I need my clothes from last night before I can return to active duty. Have you seen anything I was wearing last night?',
            f'{self.name}: Funny you mention it... I do have {self.items_held[0]}',
            f'**** You quickly try to grab {self.items_held[0]} from their hands but they pull it away teasingly ****',
            f'Sol: Gods damn it {self.name}, now is not the time for games',
            f'{self.name}: I need something Sol',
            'Sol: Here we go... ',
            f'{self.name}: I want you to admit I\'m the best {self.rank} in the fleet'
        ]
    
    def return_items_scene_fail(self):
        return [
            'Sol: It pains me to be the one asking you this, but I need my clothes from last night before I can return to active duty. Have you seen anything I was wearing last night?',
            f'{self.name}: I don\'t have anything else for you Sol\n\n'
        ]
    
    def return_add_item_scene(self):
        if self.items_held[0] not in check_item_data():
            save_item_data(self.items_held[0] + '\n')
            remove_world_data_item(self.items_held[0])
            return [
                f'Here\'s {self.items_held[0]}, you\'ve earned it Sol'
            ]
    def return_money_scene(self):
        if self.money > 0:
            current_money = get_money()
            current_money += self.money
            save_money(current_money)
            return [
                'Sol: I need some money \n\n',
                f'{self.name}: Here you go \n \n',
                f'{self.money} inter galactic dollars were added to your wallet \n \n',
            ]
        else:
            return [
                f'{self.name}: I don\'t have any money for you \n'
            ]
                        
    def return_character_money(self):
        return self.money                    
                               
     
    def run_scene(self):
            print(' ')
            self.describe_character()
            sleep(1.5)
            print(' ')
            pprint(f'{self.name}: {self.character_speak_one[self.name]}. I didn\'t have you down for a {get_underwear_type()} guy. Is that a bottle of {get_drink_choice()}? Still going strong I see...\n')
            sleep(1.5)
            print(' ')
            pprint(f'Sol : {self.sol_reply_one[self.name]}\n')
            sleep(1.5)
            print(' ')
            pprint(f'{self.name} : {self.character_speak_two[self.name]}\n')
            sleep(1.5)
            print(' ')
            pprint(f'Sol : {self.sol_reply_two[self.name]}\n')
            sleep(1.5)
            print(' ')
            sleep(2)

            flag = True
            while flag:    
                print('What would you like to do? \n')        
                self.options_character()
                print('')
                response_1 = input('Pick an option: ')
                if response_1 == 'a':
                    print(' ')
                    pprint(f'Sol: {self.compliments[random_int(len(self.compliments) - 1)]}')
                    print(' ')
                    sleep(1.5)
                    print(' ')
                    pprint(f'{self.name}: What do you want Sol? \n')
                    sleep(1.5)
                    print(' ')
                elif response_1 == 'b':
                    print(' ')
                    pprint(f'Sol: {self.insults[random_int(len(self.insults) - 1)]}\n\n')
                    sleep(1.5)
                    pprint(f'{self.name}: {self.character_insults[random_int(len(self.character_insults) - 1)]}\n\n')
                    sleep(1.5)
                    pprint('Sol: You watch your mouth, I\'m the XO of this ship\n\n')
                    sleep(1.5)
                elif response_1 == 'c':
                    print(' ')
                    pprint('Sol: It pains me to be the one asking you this, but I need my clothes from last night before I can return to active duty. Have you seen anything I was wearing last night?\n\n')
                    sleep(1.5)
                    #Check to see if you have the item already, if not then it is added to the inventory, if you do then it doesn't appear
                    if self.items_held[0] in check_world_item_data():

                        print(' ')
                        pprint(f'{self.name}: Funny you mention it... I do have {self.items_held[0]}\n\n')
                        sleep(1.5)
                        pprint(f'**** You quickly try to grab {self.items_held[0]} from their hands but they pull it away teasingly ****\n\n')
                        sleep(1.5)
                        pprint(f'Sol: Gods damn it {self.name}, now is not the time for games\n\n')
                        sleep(1.5)
                        pprint(f'{self.name}: I need something Sol\n\n')
                        sleep(1.5)
                        pprint('Sol: Here we go... \n\n')
                        sleep(1.5)
                        pprint(f'{self.name}: I want you to admit I\'m the best {self.rank} in the fleet\n\n')
                        sleep(1.5)
                        response_2 = input('Would you like to tell them that they are the best? (Y/N)').lower()  
                        if response_2 == 'y':
                            print(' ')
                            sleep(1.5)
                            print('Sol: Fine. Youre the best...\n')
                            if self.items_held[0] not in check_item_data() and self.items_held[0] in check_world_item_data():
                                pprint(f'Here\'s {self.items_held[0]}, you\'ve earned it Sol\n\n')
                                save_item_data(self.items_held[0] + '\n')
                                remove_world_data_item(self.items_held[0])
                                sleep(1.5)
                            else: 
                                print('Wait, didn\'t I give you that already?\n\n')
                                sleep(1.5)
                                
                        else:
                            print(' ')
                            pprint('Sol: I\'m the gods damn XO of this ship, don\'t tell me what to do!\n\n')
                            sleep(1.5)
                            
                    else:
                        print(' ')
                        pprint('I don\'t have anything else for you Sol\n\n')
                        sleep(1.5)
                        
                elif response_1 == 'd':
                    print(' ')
                    pprint('Sol: I could use a drink, you don\'t have anything do you?\n\n')
                    sleep(1.5)
                    pprint(f'{self.name}: Is that bottle of {get_drink_choice()} in your hand not enough for you Sol?\n\n')
                    sleep(1.5)
                    pprint('Sol: You got anything or not?\n\n')
                    sleep(1.5)
                    pprint('Here...\n\n')
                    sleep(1.5)
                    print(f'************ You take a shot with {self.name} *************\n\n')
                    sleep(1.5)
                    pprint('Sol: That\'s better\n\n')
                    sleep(1.5)

                elif response_1 == 'e':
                    if self.money > 0:
                        pprint('Sol: I need some money \n\n')
                        sleep(1.5)
                        pprint(f'{self.name}: Here you go \n \n')
                        sleep(1.5)
                        pprint(f'{self.money} inter galactic dollars were added to your wallet \n \n')
                        sleep(1.5)
                        pprint(f'You now have {get_money()} Dollars in your wallet \n\n')
                        sleep(2)
                        current_money = get_money()
                        current_money += self.money
                        save_money(current_money)
                    else:
                        pprint(f'{self.name}: I don\'t have any money for you \n')
                        sleep(1.5)

                elif response_1 == 'f':
                    flag = False
 
class FortuneTeller(Character):
    def __init__(self, name, rank, wearing, items_held, money):
        super().__init__(name, rank, wearing, items_held, money)


    def run_scene(self):
        pprint('Fortune teller: Hello Sol, the frequency of your visits is starting to get weird... \n\n')
        sleep(1)
        pprint('Sol: Well I\'m not here for your fairy tales today... I\'m looking for for my military pin \n\n')
        sleep(1)
        pprint('Fortune teller: Does the Admiral know that you are one of the five Cylon models? \n\n')
        sleep(1)
        pprint('Sol: Watch your mouth... Last I checked I\'m still the XO of this ship! \n\n')
       
        if get_money() >= 40 and 'a military pin' not in check_item_data():
            pprint('Fortune teller: I do have this Military pin actually... but it\'s going to cost you 60 Galactic Dollars \n\n')
            sleep(1)
            pprint('Sol: I expected nothing less from a scam artist like yourself...\n\n')
            sleep(1)
            pprint('****** The Fortune teller gives you your military pin *********\n\n')
            sleep(1)
            save_item_data('a military pin\n')
            remove_world_data_item('a military pin')
        elif 'a military pin' in check_item_data():
            pprint('Fortune teller: I\'ve already given you your stupid pin!\n\n')
            sleep(1)
        elif get_money() < 40:
            pprint('Fortune teller: I do have this Military pin actually... but it\'s going to cost you 40 Galactic Dollars \n\n')
            sleep(1)
            pprint('I expected nothing less from a scam artist like yourself...\n\n')
            sleep(1)
            pprint(f'Oh no! I only have {get_money()}... The cost is 40 Dollars. You might want to ask some of your colloeagues on the ship \n\n')
            sleep(1)


        



    
    

    
            
        



    




