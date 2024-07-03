import unittest
from character import Character
from ship import Ship

class TestCharacter(unittest.TestCase):
    
    def setUp(self):
        self.character= Character(name='NPC_NamE', hp=1_000, position=[100, 100])
    
    def test_character_creation(self):
        self.assertEqual(self.character.name, 'NPC_NamE')
        self.assertEqual(self.character.hp, 1_000)
        self.assertEqual(self.character.position, [100, 100])
        self.assertEqual(self.character.alive, True)
        self.assertEqual(self.character.can_take_dmg, True)
    
    def test_move(self):
        self.character.move([100, 100])
        self.assertEqual(self.character.position, [200, 200])
        self.character.move([-200, -300])
        self.assertEqual(self.character.position, [0, -100])

    def test_take_dmg(self):
        self.character.take_dmg(900)
        self.assertEqual(self.character.hp, 100)
        self.assertEqual(self.character.alive, True)
        self.character.take_dmg(100)
        self.assertEqual(self.character.hp, 0)
        self.assertEqual(self.character.alive, False)
        
    def test_cannot_take_dmg(self):
        self.character.can_take_dmg = False
        self.assertEqual(self.character.can_take_dmg, False)
        self.character.take_dmg(900)
        self.assertEqual(self.character.hp, 1_000)
        self.assertEqual(self.character.alive, True)
        self.character.take_dmg(100)
        self.assertEqual(self.character.hp, 1_000)
        self.assertEqual(self.character.alive, True)
        # even when hp drop to 0, character have to be alive
        self.character.hp = 0
        self.assertEqual(self.character.alive, True)


class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship('The Blachbeard', 100, [20, 30], speed_max=12.1, momentum=5.2, course=270, canons_max=120, canons=100, canons_range=300)
    
    def test_ship_creation(self):
        self.assertEqual(self.ship.speed_max, 12.1)
        self.assertEqual(self.ship.speed, 0)
        self.assertEqual(self.ship.momentum, 5.2)
        self.assertEqual(self.ship.course, 270)
        self.assertEqual(self.ship.canons_max, 120)
        self.assertEqual(self.ship.canons, 100)
        self.assertEqual(self.ship.canons_range, 300)


if __name__ == '__main__':
    unittest.main()