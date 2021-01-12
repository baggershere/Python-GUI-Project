import unittest
import characters
import world
import utils
import tkinter_project

class TestMovement(unittest.TestCase):
    def setUp(self):
        # Create a player instance for each possible location
        self.game_coordinates = [characters.Player(1), characters.Player(2), characters.Player(3), characters.Player(20), characters.Player(30), characters.Player(50), characters.Player(60)]

class TestMovement(TestMovement):
    def test_movement(self):
        # Iterate through the player locations list 
        for coordinate in self.game_coordinates:   
            #For each location, run the player movement function and check if the new coordinate is correct
            if coordinate == 1:
                self.assertEqual(coordinate.movement('north'), 2)

            elif coordinate == 2:
                self.assertEqual(coordinate.movement('north'), 3)
                self.assertEqual(coordinate.movement('south'), 2)
                self.assertEqual(coordinate.movement('bar'), 20)
                self.assertEqual(coordinate.movement('recroom'), 30)
            
            elif coordinate == 3:
                self.assertEqual(coordinate.movement('south'), 2)
                self.assertEqual(coordinate.movement('fortuneteller'), 60)
                self.assertEqual(coordinate.movement('viperdeck'), 50)
            
            elif coordinate == 20 or coordinate == 30:
                self.assertEqual(coordinate.movement('exit'), 2)
            
            elif coordinate == 50 or coordinate == 60:
                self.assertEqual(coordinate.movement('exit'), 3)




class TestDataType(unittest.TestCase):
    def setUp(self):
        # Get the current money
        self.get_money = utils.get_money()

class TestType(TestDataType):
    def test_data_type(self):
        # Check that the data type is equal to an integer
        self.assertIsInstance(self.get_money, int)

if __name__ == '__main__':
    unittest.main()


        
