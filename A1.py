class Item:
    def __init__(self, name, protein, fat, carb, energy, calcium):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carb = carb
        self.energy = energy
        self.calcium = calcium
    
    def __str__(self):
        productName = self.name if self.name else "Empty"
        productProtein = self.protein if self.protein else "Empty"
        productFat = self.fat if self.fat else "Empty"
        productCarb = self.carb if self.carb else "Empty"
        productEnergy = self.energy if self.energy else "Empty"
        productCalcium = self.calcium if self.calcium else "Empty"
        return f"| Name: {productName} | Protein(g): {productProtein} | Fat(g): {productFat} | Carbohydrates(g): {productCarb} | Energy(Kj): {productEnergy} | Calcium(mg): {productCalcium} |"
    

class Milk(Item):
    def __init__(self, name, protein, fat, carb, energy, calcium):
        super().__init__(name, protein, fat, carb, energy, calcium)

class Cheese(Item):
    def __init__(self, name, protein, fat, carb, energy, calcium):
        super().__init__(name, protein, fat, carb, energy, calcium)

class Butter(Item):
    def __init__(self, name, protein, fat, carb, energy, calcium):
        super().__init__(name, protein, fat, carb, energy, calcium)

class Cream(Item):
    def __init__(self, name, protein, fat, carb, energy, calcium):
        super().__init__(name, protein, fat, carb, energy, calcium)

class Custard(Item):
    def __init__(self, name, protein, fat, carb, energy, calcium):
        super().__init__(name, protein, fat, carb, energy, calcium)

class Icecream(Item):
    def __init__(self, name, protein, fat, carb, energy, calcium):
        super().__init__(name, protein, fat, carb, energy, calcium)

class Yoghurt(Item):
    def __init__(self, name, protein, fat, carb, energy, calcium):
        super().__init__(name, protein, fat, carb, energy, calcium)


class System:
    def __init__(self):
        self.milk_list = []
        self.cheese_list = []
        self.butter_list = []
        self.cream_list = []
        self.custard_list = []
        self.icecream_list = []
        self.yoghurt_list = []

    def create_product(self, category, name, protein, fat, carb, energy, calcium):
        if category == "Milk":
            newProduct = Milk(name, protein, fat, carb, energy, calcium)
            self.milk_list.append(newProduct)
        elif category == "Cheese":
            newProduct = Cheese(name, protein, fat, carb, energy, calcium)
            self.cheese_list.append(newProduct)
        elif category == "Butter":
            newProduct = Butter(name, protein, fat, carb, energy, calcium)
            self.butter_list.append(newProduct)
        elif category == "Cream":
            newProduct = Cream(name, protein, fat, carb, energy, calcium)
            self.cream_list.append(newProduct)
        elif category == "Custard":
            newProduct = Custard(name, protein, fat, carb, energy, calcium)
            self.custard_list.append(newProduct)
        elif category == "Icecream":
            newProduct = Icecream(name, protein, fat, carb, energy, calcium)
            self.icecream_list.append(newProduct)
        elif category == "Yoghurt":
            newProduct = Yoghurt(name, protein, fat, carb, energy, calcium)
            self.yoghurt_list.append(newProduct)
        else:
            print("Error")
        
    def search_by_type(self, category):
        if category == "Milk":
            found = False
            for i in self.milk_list:
                print("   •" + str(i))
                found = True
            if found == False:
                print("No Milk Items Recorded...")
        elif category == "Cheese":
            found = False
            for i in self.cheese_list:
                print("   •" + str(i))
                found = True
            if found == False:
                print("No Cheese Items Recorded...")            
        elif category == "Butter":
            found = False
            for i in self.butter_list:
                print("   •" + str(i))
                found = True
            if found == False:
                print("No Butter Items Recorded...")            
        elif category == "Cream":
            found = False
            for i in self.cream_list:
                print("   •" + str(i))
                found = True
            if found == False:
                print("No Cream Items Recorded...")            
        elif category == "Custard":
            found = False
            for i in self.custard_list:
                print("   •" + str(i))
                found = True
            if found == False:
                print("No Custard Items Recorded...")            
        elif category == "Icecream":
            found = False
            for i in self.icecream_list:
                print("   •" + str(i))
                found = True
            if found == False:
                print("No Icecream Items Recorded...")
        elif category == "Yoghurt":
            found = False
            for i in self.yoghurt_list:
                print("   •" + str(i))
                found = True
            if found == False:
                print("No Yoghurt Items Recorded...") 
        else:
            print("Error")
        print()
        
    def show_all_list(self):
        print("Milk Products:")
        found = False
        for i in self.milk_list:
            print("   •" + str(i.name))
            found = True
        if found == False:
            print("   No Milk Items Recorded...")

        print("Cheese Products:")
        found = False
        for i in self.cheese_list:
            print("   •" + str(i.name))
            found = True
        if found == False:
            print("   No Cheese Items Recorded...")

        print("Butter Products:")
        found = False
        for i in self.butter_list:
            print("   •" + str(i.name))
            found = True
        if found == False:
            print("   No Butter Items Recorded...")

        print("Cream Products:")
        found = False
        for i in self.cream_list:
            print("   •" + str(i.name))
            found = True
        if found == False:
            print("   No Cream Items Recorded...")

        print("Custard Products:")
        found = False
        for i in self.custard_list:
            print("   •" + str(i.name))
            found = True
        if found == False:
            print("   No Custard Items Recorded...")

        print("Icecream Products:")
        found = False
        for i in self.icecream_list:
            print("   •" + str(i.name))
            found = True
        if found == False:
            print("   No Icecream Items Recorded...")

        print("Yoghurt Products:")
        found = False
        for i in self.yoghurt_list:
            print("   •" + str(i.name))
            found = True
        if found == False:
            print("   No Yoghurt Items Recorded...") 

        print()

class Menu:
    def run():
        #instantiate an instance of the system
        system = System()
        #load the default products to the lists... (optional)
        preset_milk1 = system.create_product("Milk", "Regular", 3.5, 3.5, 6.3, 293, 107)
        preset_milk2 = system.create_product("Milk", "Long-Life", 3.6, 3.8, 4.6, 277, 117)
        preset_milk3 = system.create_product("Milk", "Reduced-Fat", 3.8, 1.2, 6.1, 212, 109)
        preset_milk4 = system.create_product("Milk", "Skim", 3.7, 0.1, 5, 147, 121)
        preset_cheese1 = system.create_product("Cheese", "Blue Vein", 20.3, 32.4, 0.1, 1570, 510)
        preset_cheese2 = system.create_product("Cheese", "Camembert", 18.6, 30.3, 0.1, 1465, 464)
        preset_cheese3 = system.create_product("Cheese", "Cheddar", 24.6, 32.8, 0.5, 1663, 763)
        preset_cheese4 = system.create_product("Cheese", "Cream Cheese", 3.7, 0.1, 5.0, 1384, 82)
        preset_cheese5 = system.create_product("Cheese", "Mozzarella", 26.9, 33.3, 0.1, 1300, 817)
        preset_cheese6 = system.create_product("Cheese", "Parmesan", 40.6, 33.3, 0.1, 1949, 1121)
        preset_cheese7 = system.create_product("Cheese", "Ricotta", 10.1, 8.7, 2.0, 551, 230)
        preset_butter1 = system.create_product("Butter", "Butter Salted", 1.1, 81.5, 0, 3036, 776)
        preset_butter2 = system.create_product("Butter", "Reduced Salt", 1.1, 81.5, 0, 3036, 350)
        preset_butter3 = system.create_product("Butter", "Unsalted", 1.1, 81.5, 0, 3036, 10)
        preset_cream1 = system.create_product("Cream", "Pure", 2.3, 35.9, 1.8, 1397, 61)
        preset_cream2 = system.create_product("Cream", "Reduced-fat", 2.8, 26.6, 3.7, 1085, 91)
        preset_cream3 = system.create_product("Cream", "Thickened", 2.3, 36.8, 3.1, 1461, 62)
        preset_cream4 = system.create_product("Cream", "UHT Thickened", 2.3, 37.2, 3.4, 1470, 72)
        preset_cream5 = system.create_product("Cream", "Rich or Double", 1.7, 49.4, 1.7, 1882, 60)
        preset_cream6 = system.create_product("Cream", "Whipped, Aerosol", 0.9, 7.6, 1.3, 317, 28)
        preset_cream7 = system.create_product("Cream", "Sour Cream", 2.4, 39.1, 2.5, 1534, 69)
        preset_custard1 = system.create_product("Custard", "Standard Vanilla", 3.5, 3.1, 14.5, 407, 120)
        preset_custard2 = system.create_product("Custard", "Premium Vanilla", 3.9, 0.9, 15.4, 359, 127)
        preset_icecream1 = system.create_product("Icecream", "Standard Vanilla", 2.1, 5.9, 11.5, 447, 52)
        preset_icecream2 = system.create_product("Icecream", "Reduced-Fat Vanilla", 1.9, 1.5, 16.0, 351, 51)
        preset_icecream3 = system.create_product("Icecream", "Gelato", 2.2, 2.6, 26.9, 570, 36)
        preset_yoghurt1 = system.create_product("Yoghurt", "Regular", 6.0, 4.4, 5.0, 367, 193)
        preset_yoghurt2 = system.create_product("Yoghurt", "Low-fat", 6.8, 0.3, 6.2, 249, 244)
        preset_yoghurt3 = system.create_product("Yoghurt", "Vanilla regular", 5.1, 3.0, 10.2, 404, 177)
        preset_yoghurt4 = system.create_product("Yoghurt", "Vanilla low-fat", 6.1, 0.5, 14.5, 382, 174)
        preset_yoghurt5 = system.create_product("Yoghurt", "Regular frozen", 6.3, 6.0, 33.9, 871, 214)

        #load menu interface
        while True:
            print("Dairy System")
            print()
            print("1. Record new product")
            print("2. Search all products")
            print("3. Search by category")
            print("4. Quit")
            print()
            menuItem = input("Enter an option: ")

            if menuItem == "1":
                #create new product
                category = input("What type of product (Milk, Cheese, Butter, Cream, Icecream, Custard, Yoghurt): ")
                name = input("Name: ")
                protein = input("Protein: ")
                fat = input("Fat: ")
                carb = input("Carb: ")
                energy = input("Energy: ")
                calcium = input("Calcium: ")                    
                system.create_product(category, name, protein, fat, carb, energy, calcium)    
                    
            elif menuItem == "2":
                #search all products
                system.show_all_list()
                
            elif menuItem == "3":
                #search by category
                category = input("What type of product (Milk, Cheese, Butter, Cream, Icecream, Custard, Yoghurt): ")
                print("Nutritional Information per 100g")
                system.search_by_type(category)
                
            elif menuItem == "4":
                #quit
                print("Goodbye!")
                break

            else:
                print("Error")

#run the program
if __name__ == "__main__":
    Menu.run()