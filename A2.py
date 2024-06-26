
#Serving class is the parent to the vegetable, fruit, grain, meat and dairy classes
class Serving:
    #Creates a new serving object which includes the age range and the serving size
    def __init__(self, range, serve):
      self._range = range
      self._serve = serve

    #returns the age range stored in the object
    def get_range(self):
        return self._range
    
    #returns the serving size stored in the object
    def get_serve(self):
        return self._serve

    #returns the object as a string so it is readable in terminal
    def __str__(self):
      return f"{self._range} {self._serve}"

    #returns the serving size as an int, based on the category, age, gender input
    @staticmethod
    def get_serving_size(category, age, gender):
        list = ""
        #firstly sorts categories by name to find which class stores the correct serving list
        if category == "V":
            #within this class, find the correct list based on the gender input and assign this list to a list variable to store directory
            if gender == "M":
                list = Vegetable.get_male_list()
            elif gender == "F":
                list = Vegetable.get_female_list()
            else:
                list = Vegetable.get_pregnant_list()

        elif category == "F":
            if gender == "M":
                list = Fruit.get_male_list()
            elif gender == "F":
                list = Fruit.get_female_list()
            else:
                list = Fruit.get_pregnant_list()
        
        elif category == "G":
            if gender == "M":
                list = Grain.get_male_list()
            elif gender == "F":
                list = Grain.get_female_list()
            else:
                list = Grain.get_pregnant_list()

        elif category == "M":
            if gender == "M":
                list = Meat.get_male_list()
            elif gender == "F":
                list = Meat.get_female_list()
            else:
                list = Meat.get_pregnant_list()

        elif category == "D":
            if gender == "M":
                list = Dairy.get_male_list()
            elif gender == "F":
                list = Dairy.get_female_list()
            else:
                list = Dairy.get_pregnant_list()

                
        #using the list calculated and store previously, use the age to determine which object has the correct attributes that match, this will return the correct serving size as int.
        if (age>=2) and (age<=3):
            for i in list:
              if i.get_range() == "2to3":
                  return(i.get_serve())
        elif (age>=4) and (age<=8):
            for i in list:
              if i.get_range() == "4to8":
                  return(i.get_serve())
        elif (age>=9) and (age<=11):
            for i in list:
              if i.get_range() == "9to11":
                  return(i.get_serve())
        elif (age>=12) and (age<=13):
            for i in list:
              if i.get_range() == "12to13":
                  return(i.get_serve())
        elif (age>=14) and (age<=18):
            for i in list:
              if i.get_range() == "14to18":
                  return(i.get_serve())
        elif (age>=19) and (age<=50):
            for i in list:
              if i.get_range() == "19to50":
                  return(i.get_serve())
        elif (age>=51) and (age<=70):
            for i in list:
              if i.get_range() == "51to70":
                  return(i.get_serve())
        else:
            for i in list:
              if i.get_range() == "70+":
                  return(i.get_serve())


    #get a string of food recommendations based on the returned serving size, calculated in get_serving_size()
    @staticmethod
    def get_reccomendation(category, serving, preference):
        if category == "V":
            x = 0.5
            y = 1.0
            if serving == "2.5":
                x*=2.5
                y*=2.5
            elif serving == "4.5":
                x*=4.5
                y*=4.5
            elif serving == "5":
                x*=5
                y*=5
            elif serving == "5.5":
                x*=5.5
                y*=5.5
            elif serving == "6":
                x*=6
                y*=6
            # depending on preferences, return a string of the food which is equavalent to that serving size
            if preference == "Broccoli":
                return(f"•{x} Cup Broccoli, Spinach, Carrots or Pumpkin")
            elif preference == "Beans":
                return(f"•{x} Cup Dried/Canned Beans, Peas or Lentils")
            elif preference == "Salad":
                return(f"•{y} Cup Leafy Greens or Raw Salad")
            elif preference == "Corn":
                return(f"•{x} Cup Sweet Corn")
            elif preference == "Potato":
                return(f"•{x} Medium Sweet Potato, Potato, Taro or Cassava")
            elif preference == "Tomato":
                return(f"•{y} Medium Tomato")
            else:
              return f'''•{x} Cup Broccoli, Spinach, Carrots or Pumpkin")
•{x} Cup Dried/Canned Beans, Peas or Lentils
•{y} Cup Leafy Greens or Raw Salad
•{x} Cup Sweet Corn
•{x} Medium Sweet Potato, Potato, Taro or Cassava
•{y} Medium Tomato'''
        elif category == "F":
            x = 1.0
            y = 2.0
            if serving == "1":
                x=x
                y=y
            elif serving == "1.5":
                x*=1.5
                y*=1.5
            elif serving == "2":
                x*=2
                y*=2
            
            if preference == "Apple":
                return(f"•{x} Medium Apple, Banana, Orange or Pear")
            elif preference == "Apricot":
                return(f"•{y} Small Apricots, Kiwi Fruit or Plums")
            elif preference == "Fruit":
                return(f"•{x} Cup Canned/Diced fruit")
            else:
                return f'''•{x} Medium Apple, Banana, Orange or Pear
•{y} Small Apricots, Kiwi Fruit or Plums
•{x} Cup Canned/Diced fruit'''
        elif category == "G":
            v = 0.25
            w = 0.5
            x = 0.5
            y = 1.0
            z = 3.0
            if serving == "1":
                v = v
                w = w
                x = x
                y = y
                z = z
            elif serving == "4":
                v*=4
                w*=4
                x*=4
                y*=4
                z*=4
            elif serving == "5":
                v*=5
                w*=5
                x*=5
                y*=5
                z*=5
            elif serving == "6":
                v*=6
                w*=6
                x*=6
                y*=6
                z*=6
            elif serving == "7":
                v*=7
                w*=7
                x*=7
                y*=7
                z*=7
            elif serving == "4.5":
                v*=4.5
                w*=4.5
                x*=4.5
                y*=4.5
                z*=4.5
            elif serving == "3":
                v*=3
                w*=3
                x*=3
                y*=3
                z*=3

            if preference == "Bread":
                return(f"•{y} Slice Bread")
            elif preference == "Pasta":
                return(f"•{w} Cup Pasta, Rice, Noodles, Buckwheat")
            elif preference == "Porridge":
                return(f"•{w} Cup Cooked Porridge")
            elif preference == "Flakes":
                return(f"•{x} Cup Wheat Cereal Flakes")
            elif preference == "Muesli":
                return(f"•{v} Cup Muesli")
            elif preference == "Crispbread":
                return(f"•{z} Crispbreads")
            elif preference == "Crumpet":
                return(f"•{y} Crumpet")
            elif preference == "Muffin":
                return(f"•{y} Small English Muffin or Scone")
            else:
                return f'''•{y} Slice Bread
•{w} Slice Flat Bread")
•{w} Cup Pasta, Rice, Noodles, Buckwheat
•{w} Cup Cooked Porridge
•{x} Cup Wheat Cereal Flakes
•{v} Cup Muesli
•{z} Crispbreads
•{y} Crumpet
•{y} Small English Muffin or Scone'''
        elif category == "M":
            t = 30
            u = 65
            v = 80
            w = 100
            x = 120
            y = 150
            z = 170
            
            if serving == "1":
                t = t
                u = u
                v = v
                w = w
                x = x
                y = y
                z = z
            elif serving == "1.5":
                t*=1.5
                u*=1.5
                v*=1.5
                w*=1.5
                x*=1.5
                y*=1.5
                z*=1.5
            elif serving == "2":
                t*=2
                u*=2
                v*=2
                w*=2
                x*=2
                y*=2
                z*=2
            elif serving == "2.5":
                t*=2.5
                u*=2.5
                v*=2.5
                w*=2.5
                x*=2.5
                y*=2.5
                z*=2.5
            elif serving == "3":
                t*=3
                u*=3
                v*=3
                w*=3
                x*=3
                y*=3
                z*=3
            elif serving == "3.5":
                t*=3.5
                u*=3.5
                v*=3.5
                w*=3.5
                x*=3.5
                y*=3.5
                z*=3.5

            if preference == "Chicken":
                return(f"•{v}g Chicken or Turkey")
            elif preference == "Fish":
                return(f"•{w}g Fish Fillet")
            elif preference == "Eggs":
                return(f"•{x}g Eggs")
            elif preference == "Beans":
                return(f"•{y}g Cooked Legumes/Beans")
            elif preference == "Tofu":
                return(f"•{z}g Tofu")
            elif preference == "Nuts":
                return(f"•{t}g Nuts, Seeds, Peanut or Almond butter")
            else:
              return f'''•{u}g Beef, Lamb, pork
•{v}g Chicken or Turkey
•{w}g Fish Fillet
•{x}g Eggs
•{y}g Cooked Legumes/Beans
•{z}g Tofu
•{t}g Nuts, Seeds, Peanut or Almond butter'''
            
        elif category == "D":
            w = 0.5
            x = 0.75
            y = 1
            z = 2
            if serving == "1":
                w = w
                x = x
                y = y
                z = z
            elif serving == "1.5":
                w*=1.5
                x*=1.5
                y*=1.5
                z*=1.5
            elif serving == "2":
                w*=2
                x*=2
                y*=2
                z*=2
            elif serving == "2.5":
                w*=2.5
                x*=2.5
                y*=2.5
                z*=2.5
            elif serving == "3.5":
                w*=3.5
                x*=3.5
                y*=3.5
                z*=3.5
            elif serving == "3":
                w*=3
                x*=3
                y*=3
                z*=3
            elif serving == "4":
                w*=4
                x*=4
                y*=4
                z*=4
            
            if preference == "Milk":
                return(f"•{y} Cup Fresh, UHT long life, Powdered milk or Buttermilk")
            elif preference == "Cheese":
                return(f"•{z} Slices Cheddar Cheese")
            elif preference == "Yoghurt":
                return(f"•{x} Cup Yoghurt")
            elif preference == "Soy":
                return(f"•{y} Cup Soy or Rice Cereal Drink")
            else:
                return f'''•{y} Cup Fresh, UHT long life, Powdered milk or Buttermilk
•{w} Cup Evaporated Milk
•{z} Slices Cheddar Cheese
•{w} Cup Ricotta cheese
•{x} Cup Yoghurt
•{y} Cup Soy or Rice Cereal Drink'''

#Vegetable, Fruit etc. are child classes of the Serving class
class Vegetable(Serving):

    #class attributes containing lists of Serving objects based on their gender
  _male_list = []
  _female_list = []
  _pregnant_list = []

  #Returns the correct list
  @staticmethod
  def get_male_list():
      return Vegetable._male_list
  @staticmethod
  def get_female_list():
      return Vegetable._female_list
  @staticmethod
  def get_pregnant_list():
      return Vegetable._pregnant_list

    #Once a vegetable object is instanciated, it will be created as a Vegetable object, using the __init__ from the Serving inheritance
  def record_male(self):
      Vegetable._male_list.append(self)

  def record_female(self):
      Vegetable._female_list.append(self)

  def record_pregnant(self):
      Vegetable._pregnant_list.append(self)

    #Creates the serving objects which store information about serving sizes and their corresponding age ranges, broken into male, female and prganant (female) categories
  @staticmethod
  def add_servings():
      Vegetable("2to3", "2.5").record_male()
      Vegetable("4to8", "4.5").record_male()
      Vegetable("9to11", "5").record_male()
      Vegetable("12to13", "5.5").record_male()
      Vegetable("14to18", "5.5").record_male()
      Vegetable("19to50", "6").record_male()
      Vegetable("51to70", "5.5").record_male()
      Vegetable("70+", "5").record_male()

      Vegetable("2to3", "2.5").record_female()
      Vegetable("4to8", "4.5").record_female()
      Vegetable("9to11", "5").record_female()
      Vegetable("12to13", "5").record_female()
      Vegetable("14to18", "5").record_female()
      Vegetable("19to50", "5").record_female()
      Vegetable("51to70", "5").record_female()
      Vegetable("70+", "5").record_female()

      Vegetable("19to50", "5").record_pregnant()

class Fruit(Serving):
  _male_list = []
  _female_list = []
  _pregnant_list = []
  
  @staticmethod
  def get_male_list():
      return Fruit._male_list
  @staticmethod
  def get_female_list():
      return Fruit._female_list
  @staticmethod
  def get_pregnant_list():
      return Fruit._pregnant_list

  def record_male(self):
      Fruit._male_list.append(self)

  def record_female(self):
      Fruit._female_list.append(self)

  def record_pregnant(self):
      Fruit._pregnant_list.append(self)

  @staticmethod
  def add_servings():
      Fruit("2to3", "1").record_male()
      Fruit("4to8", "1.5").record_male()
      Fruit("9to11", "2").record_male()
      Fruit("12to13", "2").record_male()
      Fruit("14to18", "2").record_male()
      Fruit("19to50", "2").record_male()
      Fruit("51to70", "2").record_male()
      Fruit("70+", "2").record_male()

      Fruit("2to3", "1").record_female()
      Fruit("4to8", "1.5").record_female()
      Fruit("9to11", "2").record_female()
      Fruit("12to13", "2").record_female()
      Fruit("14to18", "2").record_female()
      Fruit("19to50", "2").record_female()
      Fruit("51to70", "2").record_female()
      Fruit("70+", "2").record_female()

      Fruit("19to50", "2").record_pregnant()

class Grain(Serving):
  _male_list = []
  _female_list = []
  _pregnant_list = []
  
  @staticmethod
  def get_male_list():
      return Grain._male_list
  @staticmethod
  def get_female_list():
      return Grain._female_list
  @staticmethod
  def get_pregnant_list():
      return Grain._pregnant_list

  def record_male(self):
      Grain._male_list.append(self)

  def record_female(self):
      Grain._female_list.append(self)

  def record_pregnant(self):
      Grain._pregnant_list.append(self)

  @staticmethod
  def add_servings():
      Grain("2to3", "4").record_male()
      Grain("4to8", "4").record_male()
      Grain("9to11", "5").record_male()
      Grain("12to13", "6").record_male()
      Grain("14to18", "7").record_male()
      Grain("19to50", "6").record_male()
      Grain("51to70", "6").record_male()
      Grain("70+", "4.5").record_male()

      Grain("2to3", "4").record_female()
      Grain("4to8", "4").record_female()
      Grain("9to11", "4").record_female()
      Grain("12to13", "5").record_female()
      Grain("14to18", "7").record_female()
      Grain("19to50", "6").record_female()
      Grain("51to70", "4").record_female()
      Grain("70+", "3").record_female()

      Grain("19to50", "8.5").record_pregnant()
     
class Meat(Serving):
  _male_list = []
  _female_list = []
  _pregnant_list = []
  
  @staticmethod
  def get_male_list():
      return Meat._male_list
  @staticmethod
  def get_female_list():
      return Meat._female_list
  @staticmethod
  def get_pregnant_list():
      return Meat._pregnant_list

  def record_male(self):
      Meat._male_list.append(self)

  def record_female(self):
      Meat._female_list.append(self)

  def record_pregnant(self):
      Meat._pregnant_list.append(self)

  @staticmethod
  def add_servings():
      Meat("2to3", "1").record_male()
      Meat("4to8", "1.5").record_male()
      Meat("9to11", "2.5").record_male()
      Meat("12to13", "2.5").record_male()
      Meat("14to18", "2.5").record_male()
      Meat("19to50", "3").record_male()
      Meat("51to70", "2.5").record_male()
      Meat("70+", "2.5").record_male()

      Meat("2to3", "1").record_female()
      Meat("4to8", "1.5").record_female()
      Meat("9to11", "2.5").record_female()
      Meat("12to13", "2.5").record_female()
      Meat("14to18", "2.5").record_female()
      Meat("19to50", "2.5").record_female()
      Meat("51to70", "2").record_female()
      Meat("70+", "2").record_female()

      Meat("19to50", "3.5").record_pregnant()

class Dairy(Serving):
  _male_list = []
  _female_list = []
  _pregnant_list = []
  
  @staticmethod
  def get_male_list():
      return Dairy._male_list
  @staticmethod
  def get_female_list():
      return Dairy._female_list
  @staticmethod
  def get_pregnant_list():
      return Dairy._pregnant_list

  def record_male(self):
      Dairy._male_list.append(self)

  def record_female(self):
      Dairy._female_list.append(self)

  def record_pregnant(self):
      Dairy._pregnant_list.append(self)

  @staticmethod
  def add_servings():
      Dairy("2to3", "1.5").record_male()
      Dairy("4to8", "2").record_male()
      Dairy("9to11", "2.5").record_male()
      Dairy("12to13", "3.5").record_male()
      Dairy("14to18", "3.5").record_male()
      Dairy("19to50", "2.5").record_male()
      Dairy("51to70", "2.5").record_male()
      Dairy("70+", "3.5").record_male()

      Dairy("2to3", "1.5").record_female()
      Dairy("4to8", "1.5").record_female()
      Dairy("9to11", "3").record_female()
      Dairy("12to13", "3.5").record_female()
      Dairy("14to18", "3.5").record_female()
      Dairy("19to50", "2.5").record_female()
      Dairy("51to70", "4").record_female()
      Dairy("70+", "4").record_female()

      Dairy("19to50", "2.5").record_pregnant()


class Menu:
    @staticmethod
    def run():
        #instantiate serving objects in child classes
        Vegetable.add_servings()
        Fruit.add_servings()
        Grain.add_servings()
        Meat.add_servings()
        Dairy.add_servings()

        #run methods to get age, gender and show the different dietary recommendations
        age = Menu.get_age()
        gender = Menu.get_gender(age)
        veg_recommendation = Menu.show_veg(age, gender)
        fruit_recommendation = Menu.show_fruit(age, gender)
        grain_recommendation = Menu.show_grain(age, gender)
        meat_recommendation = Menu.show_meat(age, gender)
        dairy_recommendation = Menu.show_dairy(age, gender)
        Menu.import_export(veg_recommendation, fruit_recommendation, grain_recommendation, meat_recommendation, dairy_recommendation)

        
    #Get age method with exception handling
    @staticmethod
    def get_age():
        while True:
            try: 
                age = int(input("Enter Age (2-150): "))
                if age not in range(2, 151):
                        raise ValueError
                return age
                break

            except:
                print("Invalid input. Please enter a new choice again.")


    #Get gender method with exception handling
    @staticmethod
    def get_gender(age):
        #If gender is female AND age is between 19 to 50, prompt pregnant?, if yes, update gender to pregnant
        while True:
            try: 
                gender = input("Enter Gender (M or F): ")
                if (gender != "M") and (gender != "F"):
                    raise ValueError
                else:
                    if gender =="F":
                        if (age>=19) and (age<=50):
                            pregnant = input("Enter Pregnant (Y or N): ")
                            if ((pregnant != "Y") and (pregnant != "N")):
                                raise ValueError
                            else:
                                if pregnant =="Y":
                                    gender = "P"
                                    return gender
                                else:
                                    return gender
                    else:
                        return gender
            except:
                print("Invalid input. Please enter a new choice again.")

    #Get show dietary recommendations based on age, gender and food category, this includes preference handling
    @staticmethod
    def show_veg(age, gender):
        print(f"Dietary Recommendations Age: {age} Gender: {gender}")
        print()
        veg_serve = Serving.get_serving_size("V", age, gender)
        print(f"{veg_serve} serves of Vegetables")
        veg_preference = input("Enter Prefernece (Click Enter for all): ")

        veg_recommendation = Serving.get_reccomendation("V", veg_serve, veg_preference)
        print(veg_recommendation)
        print()
        return veg_recommendation

    @staticmethod
    def show_fruit(age, gender):
        fruit_serve = Serving.get_serving_size("F", age, gender)
        print(f"{fruit_serve} serves of Fruit")
        fruit_preference = input("Enter Prefernece (Click Enter for all): ")
        fruit_recommendation = Serving.get_reccomendation("F", fruit_serve, fruit_preference)
        print(fruit_recommendation)
        print()
        return fruit_recommendation

    @staticmethod
    def show_grain(age, gender):
        grain_serve = Serving.get_serving_size("G", age, gender)
        print(f"{grain_serve} serves of Grain")
        grain_preference = input("Enter Prefernece (Click Enter for all): ")
        grain_recommendation = Serving.get_reccomendation("G", grain_serve, grain_preference)
        print(grain_recommendation)
        print()
        return grain_recommendation

    @staticmethod
    def show_meat(age, gender):
        meat_serve = Serving.get_serving_size("M", age, gender)
        print(f"{meat_serve} serves of Meat")
        meat_preference = input("Enter Prefernece (Click Enter for all): ")
        meat_recommendation = Serving.get_reccomendation("M", meat_serve, meat_preference)
        print(meat_recommendation)
        print()
        return meat_recommendation

    @staticmethod
    def show_dairy(age, gender):
        dairy_serve = Serving.get_serving_size("D", age, gender)
        print(f"{dairy_serve} serves of Dairy")
        dairy_preference = input("Enter Prefernece (Click Enter for all): ")
        dairy_recommendation = Serving.get_reccomendation("D", dairy_serve, dairy_preference)
        print(dairy_recommendation)
        print()
        return dairy_recommendation

    @staticmethod
    def import_export(veg_recommendation, fruit_recommendation, grain_recommendation, meat_recommendation, dairy_recommendation):
        while True:
            try: 
                export_ = input("Would you like to export file (Y or N): ")
                if (export_ != "Y") and (export_ != "N"):
                    raise ValueError
                else:
                    if export_ == "Y":
                        with open('/Users/jacobbrown/Desktop/Dietary Info.txt', 'w') as file:
                            file.write(veg_recommendation)
                            file.write("\n \n")
                            file.write(fruit_recommendation)
                            file.write("\n \n")
                            file.write(grain_recommendation)
                            file.write("\n \n")
                            file.write(meat_recommendation)
                            file.write("\n \n")
                            file.write(dairy_recommendation)
                            file.write("\n \n")
                            break
                    else:
                        break
            except:
                print("Invalid input. Please enter a new choice again.")


        while True:
            try: 
                import_ = input("Would you like to import file (Y or N): ")
                if (import_ != "Y") and (import_ != "N"):
                    raise ValueError
                else:
                    if import_ == "Y":
                        with open('/Users/jacobbrown/Desktop/Dietary Info.txt', "r") as file:
                            contents = file.read()
                            print()
                            print(contents)
                            break
                    else:
                        break
            except:
                print("Invalid input. Please enter a new choice again.")
            

if __name__ == "__main__":
    Menu.run()

