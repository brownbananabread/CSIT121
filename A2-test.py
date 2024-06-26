import unittest
from main import Serving, Vegetable, Fruit, Grain, Meat, Dairy, Menu

#Create a unnitest class to assess the input and output of each function
class TestServing(unittest.TestCase):
    #this function will be called when unittest.main() called and will
    #assess wether the input ie. Serving.get_serv... returns a "2.5"

    def test_get_serving_size(self):
        #Testing range of Vegetable Class
        self.assertEqual(Serving.get_serving_size("V", 3, "M"), "2.5")
        self.assertEqual(Serving.get_serving_size("V", 9, "M"), "5")
        self.assertEqual(Serving.get_serving_size("V", 19, "M"), "6")
        self.assertEqual(Serving.get_serving_size("V", 100, "M"), "5")
        self.assertEqual(Serving.get_serving_size("V", 3, "F"), "2.5")
        self.assertEqual(Serving.get_serving_size("V", 9, "F"), "5")
        self.assertEqual(Serving.get_serving_size("V", 19, "F"), "5")
        self.assertEqual(Serving.get_serving_size("V", 100, "F"), "5")
        self.assertEqual(Serving.get_serving_size("V", 19, "P"), "5")

        #Testing range of Fruit Class
        self.assertEqual(Serving.get_serving_size("F", 3, "M"), "1")
        self.assertEqual(Serving.get_serving_size("F", 9, "M"), "2")
        self.assertEqual(Serving.get_serving_size("F", 19, "M"), "2")
        self.assertEqual(Serving.get_serving_size("F", 100, "M"), "2")
        self.assertEqual(Serving.get_serving_size("F", 3, "F"), "1")
        self.assertEqual(Serving.get_serving_size("F", 9, "F"), "2")
        self.assertEqual(Serving.get_serving_size("F", 19, "F"), "2")
        self.assertEqual(Serving.get_serving_size("F", 100, "F"), "2")
        self.assertEqual(Serving.get_serving_size("F", 19, "P"), "2")

        #Testing range of Grain Class
        self.assertEqual(Serving.get_serving_size("G", 3, "M"), "4")
        self.assertEqual(Serving.get_serving_size("G", 9, "M"), "5")
        self.assertEqual(Serving.get_serving_size("G", 19, "M"), "6")
        self.assertEqual(Serving.get_serving_size("G", 100, "M"), "4.5")
        self.assertEqual(Serving.get_serving_size("G", 3, "F"), "4")
        self.assertEqual(Serving.get_serving_size("G", 9, "F"), "4")
        self.assertEqual(Serving.get_serving_size("G", 19, "F"), "6")
        self.assertEqual(Serving.get_serving_size("G", 100, "F"), "3")
        self.assertEqual(Serving.get_serving_size("G", 19, "P"), "8.5")

        #Testing range of Meat Class
        self.assertEqual(Serving.get_serving_size("M", 3, "M"), "1")
        self.assertEqual(Serving.get_serving_size("M", 9, "M"), "2.5")
        self.assertEqual(Serving.get_serving_size("M", 19, "M"), "3")
        self.assertEqual(Serving.get_serving_size("M", 100, "M"), "2.5")
        self.assertEqual(Serving.get_serving_size("M", 3, "F"), "1")
        self.assertEqual(Serving.get_serving_size("M", 9, "F"), "2.5")
        self.assertEqual(Serving.get_serving_size("M", 19, "F"), "2.5")
        self.assertEqual(Serving.get_serving_size("M", 100, "F"), "2")
        self.assertEqual(Serving.get_serving_size("M", 19, "P"), "3.5")

        #Testing range of Dairy Class
        self.assertEqual(Serving.get_serving_size("D", 3, "M"), "1.5")
        self.assertEqual(Serving.get_serving_size("D", 9, "M"), "2.5")
        self.assertEqual(Serving.get_serving_size("D", 19, "M"), "2.5")
        self.assertEqual(Serving.get_serving_size("D", 100, "M"), "3.5")
        self.assertEqual(Serving.get_serving_size("D", 3, "F"), "1.5")
        self.assertEqual(Serving.get_serving_size("D", 9, "F"), "3")
        self.assertEqual(Serving.get_serving_size("D", 19, "F"), "2.5")
        self.assertEqual(Serving.get_serving_size("D", 100, "F"), "4")
        self.assertEqual(Serving.get_serving_size("D", 19, "P"), "2.5")
        
if __name__ == "__main__":
    Vegetable.add_servings()
    Fruit.add_servings()
    Grain.add_servings()
    Meat.add_servings()
    Dairy.add_servings()

    unittest.main()




