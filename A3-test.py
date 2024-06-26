import unittest
from matplot2 import System, Person

class TestServing(unittest.TestCase):
    def test_find_details(self):
        system = System()  # Create an instance of the System class
        
        self.assertEqual(system.findDetails(Person("Jacob", 2, "Male", 2, 2, 2, 2, 2))[1], ([2.5, 1, 4, 1, 1.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 4, "Male", 2, 2, 2, 2, 2))[1], ([4.5, 2, 4, 1.5, 2]))
        self.assertEqual(system.findDetails(Person("Jacob", 9, "Male", 2, 2, 2, 2, 2))[1], ([5, 2, 5, 2.5, 2.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 12, "Male", 2, 2, 2, 2, 2))[1], ([5.5, 2, 6, 2.5, 3.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 14, "Male", 2, 2, 2, 2, 2))[1], ([5.5, 2, 7, 2.5, 3.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 19, "Male", 2, 2, 2, 2, 2))[1], ([6, 2, 6, 3, 2.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 51, "Male", 2, 2, 2, 2, 2))[1], ([5.5, 2, 6, 2.5, 2.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 71, "Male", 2, 2, 2, 2, 2))[1], ([5, 2, 4.5, 2.5, 3.5]))

        self.assertEqual(system.findDetails(Person("Jacob", 2, "Female", 2, 2, 2, 2, 2))[1], ([2.5, 1, 4, 1, 1.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 4, "Female", 2, 2, 2, 2, 2))[1], ([4.5, 1.5, 4, 1.5, 1.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 9, "Female", 2, 2, 2, 2, 2))[1], ([5, 2, 4, 2.5, 3]))
        self.assertEqual(system.findDetails(Person("Jacob", 12, "Female", 2, 2, 2, 2, 2))[1], ([5, 2, 5, 2.5, 3.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 14, "Female", 2, 2, 2, 2, 2))[1], ([5, 2, 7, 2.5, 3.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 19, "Female", 2, 2, 2, 2, 2))[1], ([5, 2, 6, 2.5, 2.5]))
        self.assertEqual(system.findDetails(Person("Jacob", 51, "Female", 2, 2, 2, 2, 2))[1], ([5, 2, 4, 2, 4]))
        self.assertEqual(system.findDetails(Person("Jacob", 71, "Female", 2, 2, 2, 2, 2))[1], ([5, 2, 3, 2, 4]))


if __name__ == "__main__":
    unittest.main()


'''To perform code coverage report, type the following in terminal:
python3 -m coverage run -m unittest
python3 -m coverage report
'''


