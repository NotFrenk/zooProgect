import unittest
from unittest import TestCase
from src.zoo import Zoo, ZooKeeper, Animal, Fence

class TestiZoo(TestCase):

    def test_animal_dimension(self):
        """
        
        """
        zookeeper_1: ZooKeeper = ZooKeeper(name= 'giggio', surname='bubu', id=0)
        fence_1 :Fence =Fence(area=100, temperature=25.0, habitat='savana')
        animal_1 :Animal = Animal(name='Pluto', species='Canide', age=5, height=300.0, width=1.0, preferred_habitat='savana')
        zookeeper_1.add_animal(animal_1, fence_1)
        result :int = len(fence_1.animals)
        message: str = f'Error: the function add_animal should not add self.animal_1 into self.fence_1'

        self.assertEqual(result, 0, message)

    def test_aniaml_habitat(self):


    def test_animal(self):
    
    def





if __name__ == '__main__':
    unittest.main()