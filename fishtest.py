import unittest
from FishProblem import pond, Fish, Fisher

class Testpond(unittest.TestCase):  

     def test_init(self):
          self.pond = pond("naile", 10)
          self.assertEqual(self.pond.name, "naile")
          self.assertEqual(self.pond.capacity, 10)


     def test_fishreduce(self):
          self.pond = pond("naile", 10)
          self.Pike = Fish("Pike",10)
          self.Tuna = Fish("Tuna",10)
          self.Goldie = Fish("Goldie",10)
          self.pond.__addfish__(self.Pike)
          self.values = ("Pike",10)
          self.assertEqual(self.pond.fishreduce(self.values),[])
          

     def test_catchfish(self):
          self.Pike = Fish("Pike",18)
          self.pond = pond("naile", 10)
          self.pond.__addfish__(self.Pike)
          self.fisher = Fisher()
          self.assertEqual(self.fisher.catchfish(self.pond),('Pike', 18))
          

     def test_catchfish(self):
          self.Pike = Fish("Pike", 9)
          self.pond = pond("naile", 10)
          self.pond.__addfish__(self.Pike)
          self.fisher = Fisher()
          self.assertEqual(self.fisher.catchfish(self.pond), 'there is no fishes of your expected size')


if __name__ == '__main__':
     unittest.main()


