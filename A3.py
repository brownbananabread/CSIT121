import matplotlib.pyplot as plt
import numpy as np
import sys
import pickle
import json
import os

#Menu class (View)
class Menu:
  #Singleton Design Pattern
  __instance = None

  @staticmethod
  def getInstance():
    if Menu.__instance == None:
      Menu()
    return Menu.__instance

  #Create menu items
  def __init__(self):
    Menu.__instance = self
    self._option1 = "1. Load Saved User?"
    self._option2 = "2. Create New User?"
    self._option3 = "3. Update Saved User?"
    self._option4 = "4. Quit?"

  #Print menu items to the terminal
  def show(self):
    print()
    print("Dietary Analysis")
    print()
    print(self._option1)
    print(self._option2)
    print(self._option3)
    print(self._option4)
    print()

  #Run the program
  def run(self):
    option = input("1, 2, 3: ")
    if option == "1":
      savedUser = system.loadUser()
      if savedUser:
        current, recommend, name = system.findDetails(savedUser)
        system.createGraph(current, recommend, name)

    elif option == "2":
      savedUser = system.createUser()
      current, recommend, name = system.findDetails(savedUser)
      system.createGraph(current, recommend, name)
    
    elif option == "3":
      system.updateUser()

    else:
      print("Goodbye")
      sys.exit(0)


#System class (Controller)
class System:

  #Singleton Design Pattern
  __instance = None

  @staticmethod
  def getInstance():
    if System.__instance == None:
      System()
    return System.__instance
  
  def __init__(self):
    System.__instance = self

  #If file, load file
  def loadUser(self):
    filename = input("Enter file name: ")
    try:
      current_directory = os.getcwd()
      file_path = os.path.join(current_directory, filename)
      
      with open(file_path, "rb") as file:
        savedUser = pickle.load(file)
        return savedUser
    except FileNotFoundError:
      print("File does not exist, please try again.")

  #Create Person object, dump in pickle file, return Person object
  def createUser(self):
    try:
      name = input("Enter Username: ")
      age = int(input("Enter Age (2-150): "))
      if age < 2 or age > 150:
        raise ValueError("Age must be between 2 and 150.")
      gender = input("Enter Gender (Male or Female): ")
      if gender != "Male" and gender != "Female":
        raise ValueError("Gender must be Male or Female.")
      vegetable_intake = int(input("Enter Daily Vegetable Serving: "))
      if vegetable_intake < 0 or vegetable_intake > 20:
        raise ValueError("Intake must be between 0 and 20 Servings.")
      fruit_intake = int(input("Enter Daily Fruit Serving: "))
      if fruit_intake < 0 or fruit_intake > 20:
        raise ValueError("Intake must be between 0 and 20 Servings.")
      grain_intake = int(input("Enter Daily Grain Serving: "))
      if grain_intake < 0 or grain_intake > 20:
        raise ValueError("Intake must be between 0 and 20 Servings.")
      meat_intake = int(input("Enter Daily Meat Serving: "))
      if meat_intake < 0 or meat_intake > 20:
        raise ValueError("Intake must be between 0 and 20 Servings.")
      dairy_intake = int(input("Enter Dairy Grain Serving: "))
      if dairy_intake < 0 or dairy_intake > 20:
        raise ValueError("Intake must be between 0 and 20 Servings.")
      savedUser = Person(name, age, gender, vegetable_intake, fruit_intake, grain_intake, meat_intake, dairy_intake)
      
      current_directory = os.getcwd()
      file_path = os.path.join(current_directory, f"{name}'s Diet")
      
      with open(file_path, "wb") as file:
        pickle.dump(savedUser, file)
      
      return savedUser
    
    except ValueError as e:
      print(e)
      sys.exit(0)

  #If file, update Person attributes and dump into same file
  def updateUser(self):
    filename = input("Enter file name: ")
    try:
      current_directory = os.getcwd()
      file_path = os.path.join(current_directory, filename)
      
      with open(file_path, "rb") as file:
        savedUser = pickle.load(file)

        name = input("Enter Username: ")
        age = int(input("Enter Age (2-150): "))
        if age < 2 or age > 150:
          raise ValueError("Age must be between 2 and 150.")
        
        gender = input("Enter Gender (Male or Female): ")
        if gender != "Male" and gender != "Female":
          raise ValueError("Gender must be Male or Female.")
        
        vegetable_intake = int(input("Enter Daily Vegetable Serving: "))
        if vegetable_intake < 0 or vegetable_intake > 20:
          raise ValueError("Intake must be between 0 and 20 Servings.")
        
        fruit_intake = int(input("Enter Daily Fruit Serving: "))
        if fruit_intake < 0 or fruit_intake > 20:
          raise ValueError("Intake must be between 0 and 20 Servings.")
        
        grain_intake = int(input("Enter Daily Grain Serving: "))
        if grain_intake < 0 or grain_intake > 20:
          raise ValueError("Intake must be between 0 and 20 Servings.")
        
        meat_intake = int(input("Enter Daily Meat Serving: "))
        if meat_intake < 0 or meat_intake > 20:
          raise ValueError("Intake must be between 0 and 20 Servings.")
        
        dairy_intake = int(input("Enter Dairy Grain Serving: "))
        if dairy_intake < 0 or dairy_intake > 20:
          raise ValueError("Intake must be between 0 and 20 Servings.")
        
        savedUser = Person(name, age, gender, vegetable_intake, fruit_intake, grain_intake, meat_intake, dairy_intake)
        
        with open(filename, "wb") as file:
          pickle.dump(savedUser, file)
        
    except FileNotFoundError:
      print("File does not exist, please try again.")

    except ValueError as e:
      print(e)
      sys.exit(0)

  #Use Person object from either createUser() or loadUser(), calculate recommended dietary requirements, return username, current diet and recommended diet.
  def findDetails(self, savedUser):
    name = savedUser.get_name()
    age = int(savedUser.get_age())
    gender = savedUser.get_gender()
    veg_current = savedUser.get_veg_current()
    fruit_current = savedUser.get_fruit_current()
    grain_current = savedUser.get_grain_current()
    meat_current = savedUser.get_meat_current()
    dairy_current = savedUser.get_dairy_current()

    if (age>=2) and (age<=3):
      age = "2to3"
    elif (age>=4) and (age<=8):
      age = "4to8"
    elif (age>=9) and (age<=11):
      age = "9to11"
    elif (age>=12) and (age<=13):
      age = "12to13"
    elif (age>=14) and (age<=18):
      age = "14to18"
    elif (age>=19) and (age<=50):
      age = "19to50"
    elif (age>=51) and (age<=70):
      age = "51to70"
    else:
      age = "70plus"
    
    #Sort servings.JSON by category, gender, age for the recommended dietary recommendations

    # Open the file and load JSON data
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'servings.json')
    with open(file_path, 'r') as f:
        serving = json.load(f)

    veg_recommended = serving['Vegetable List'][gender][age]
    fruit_recommended = serving['Fruit List'][gender][age]
    grain_recommended = serving['Grain List'][gender][age]
    meat_recommended = serving['Meat List'][gender][age]
    dairy_recommended = serving['Dairy List'][gender][age]

    current = [float(veg_current), float(fruit_current), float(grain_current), float(meat_current), float(dairy_current)]
    
    recommend = [float(veg_recommended), float(fruit_recommended), float(grain_recommended), float(meat_recommended), float(dairy_recommended)]
    return current, recommend, name


  #Use returned data from findDetails() to create matplotlib graph
  def createGraph(self, current, recommend, name):

    labels = ["Vegetables", "Fruit", "Grain", "Meat", "Dairy"]
    
    # Plotting the pie charts
    plt.subplot(2, 2, 1)
    plt.pie(recommend, labels=labels, autopct='%1.1f%%')
    plt.title("Recommended Daily Intake")
    plt.subplot(2, 2, 2)
    plt.pie(current, labels=labels, autopct='%1.1f%%')
    plt.title(f"{name}'s Daily Intake")
    
    # Plotting the line graph
    plt.subplot(2, 2, 3)
    plt.plot(labels, current, labels, recommend)
    plt.title(f"{name}'s vs Recommended Intake")

    # Plotting the dual bar graph
    plt.subplot(2, 2, 4)
    X_axis = np.arange(len(labels)) 
    plt.bar(X_axis - 0.2, recommend, 0.4, label='Recommend', color="darkorange")
    plt.bar(X_axis + 0.2, current, 0.4, label='Current', color="#3776ab")
    plt.xticks(X_axis, labels) 
    plt.legend() 
    plt.title(f"{name}'s vs Recommended Intake")
    plt.show()

#Person class (Model)
class Person:
  #Create Person object
  def __init__(self, name, age, gender, vegetable_intake, fruit_intake, grain_intake, meat_intake, dairy_intake):
        self._name = name
        self._age = age
        self._gender = gender
        self._vegetable_intake = vegetable_intake
        self._fruit_intake = fruit_intake
        self._grain_intake = grain_intake
        self._meat_intake = meat_intake
        self._dairy_intake = dairy_intake
  
  #Return private attributes
  def get_name(self):
    return self._name
  def get_age(self):
    return self._age
  def get_gender(self):
    return self._gender
  def get_veg_current(self):
    return self._vegetable_intake
  def get_fruit_current(self):
    return self._fruit_intake
  def get_grain_current(self):
    return self._grain_intake
  def get_meat_current(self):
    return self._meat_intake
  def get_dairy_current(self):
    return self._dairy_intake

if __name__ == "__main__":
  menu = Menu.getInstance()
  system = System.getInstance()

  menu.show()
  menu.run()



  
