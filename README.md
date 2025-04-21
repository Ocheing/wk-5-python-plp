# wk-5-python-plp
🦸‍♂️ Superhero and Polymorphism OOP Example 🦸‍♀️
This repository contains two Python programming assignments that demonstrate key concepts of Object-Oriented Programming (OOP) using Superheroes 🦸‍♂️ and Polymorphism 🎭.

🏗️ Assignment 1: Superhero Class with Inheritance
This assignment involves creating a Superhero class with attributes such as name, alter ego, and superpower. The class uses inheritance to extend from a parent class called Superpower. The Superhero class overrides the use_power() method to implement specific behaviors for each superhero.

🦸‍♂️ Superhero Class Example
The Superhero class has:

Attributes: name, alter_ego, power_name

Methods:

use_power(): Each superhero uses their unique superpower.

display_info(): Displays the superhero's name, alter ego, and power.

Example Usage:

hero1 = Superhero("Superman", "Super Strength", "Clark Kent")
hero1.display_info()
hero1.use_power()
🚗 Activity 2: Polymorphism Challenge with Vehicles ✈️
This activity demonstrates polymorphism by creating different vehicle classes (e.g., Car, Plane, Bike) that implement the same move() method differently. Each class overrides the move() method to define how the vehicle moves.

🚗 Vehicle Classes:
Car: move() prints "Driving 🚗"

Plane: move() prints "Flying ✈️"

Bike: move() prints "Cycling 🚲"

Example Usage:

vehicles = [Car(), Plane(), Bike()]

for vehicle in vehicles:
    vehicle.move()  # Demonstrates polymorphism with different outputs
⚙️ How to Run the Code
1. Clone the repository:

git clone https://github.com/yourusername/repository-name.git

2. Navigate to the project folder:

cd repository-name

3.Run the Python files directly from your terminal:

python SuperheroClassInheritance.py  # To run the superhero class example
python Vehicle_Polymorphism.py  # To run the polymorphism example

