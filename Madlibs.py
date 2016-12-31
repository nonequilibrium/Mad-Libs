#""""""Madlibs python"""""""

print ("Mad Libs has started!")

name = input("Enter a name: ")
adj1 = input("Enter an adjective: ")
adj2 = input("Enter a second adjective: ")
adj3 = input("Enter a third adjective: ")

verb1 = input("Enter a verb: ")
verb2 = input("Enter a second verb: ")
verb3 = input("Enter a third verb: ")

noun1 = input("Enter a noun: ")
noun2 = input("Enter a second noun: ")
noun3 = input("Enter a third noun: ")
noun4 = input("Enter a fourth noun: ")

animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
number = input("Enter a number: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")


#story#
STORY = ("This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %s very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %ss. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world.")

print (STORY %(adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4))
