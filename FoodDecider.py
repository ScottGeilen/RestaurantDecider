#!/usr/bin/env python
# coding: utf-8
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *

root = Tk()
root.geometry('500x150')

myLabel = Label(root, text="Tucson, AZ Restaurant Decider ")
myLabel.pack()
    
def suggestFood():
    doorDash = ["Popeyes"
                  "It's Just Wings",
                  "Raising Cane's",
                  "McDonald's",
                  "Riliberto's Fresh Mexican Food",
                  "Five Guys",
                  "Wendy's",
                  "Burger King",
                  "Taco Bell",
                  "MOD Pizza",
                  "Smashburger",
                  "Jack in the Box",
                  "Carl's Jr.",
                  "Baskin Robins",
                  "Arby's",
                  "Wienerschnitzel",
                  "El Beto Mexican Food",
                  "Subway",
                  "El Pollo Loco",
                  "Jersey Mike's Subs",
                  "Jimmy John's Sandwiches",
                  "Panera Bread",
                  "Lucky Wishbone",
                  "Panda Express",
                  "Blake's Lotaburger",
                  "Freddy's Frozen Custard & Steakburgers",
                  "Firehouse Subs",
                  "Dairy Queen",
                  "Sarku Japan",
                  "Charleys Philly Steaks",
                  "KFC",
                  "No Anchovies",
                  "IHOP",
                  "Trident Pizza Pub",
                  "Eegee's",
                  "Jason's Deli",
                  "Hooters",
                  "Applebee's Grill & Bar",
                  "Viva Burrito",
                  "Cheba Hut",
                  "The Cheesecake Factory",
                  "Beyond Bread",
                  "Famous Dave's",
                  "The Oink Cafe",
                  "Claim Jumper",
                  "Red Robin Gourmet Burgers and Brews",
                  "Los Betos",
                  "Denny's",
                  "Black Bear Diner",
                  "Chili's Grill & Bar",
                  "Buffalo Wild Wings",
                  "The Habit Burger",
                  "Craft Republic",
                  "Salty Dawg II",
                  "The Buffalo Spot",
                  "Chipotle",
                  "Wingstop",
                  "Sauce Pizza & Wine",
                  "Pita Jungle",
                  "Guilin Chinese Restaurant",
                  "Truland Burgers & Greens",
                  "Schlotzsky's Austin Eatery",
                  "Brooklyn Pizza Company",
                  "Empire Pizza",
                  "North Italia",
                  "Oregano's",
                  "Piezanos Rustic Pizza and Wine",
                  "Postino",
                  "Carrabba's",
                  "Renee's Organic Oven",
                  "Guiseppe's",
                  "Piazza Gavi",
                  "Romano's Lunch Express",
                  "Green Things",
                  "Kenney D's",
                  "Humble Pie",
                  "Southwest Grillers",
                  "Native Grill & Wings",
                  "BJ's Restaurant * Brewhouse",
                  "Pizza Patron",
                  "Magpies Gourmet Pizza",
                  "Fired Pie",
                  "Scordato's Pizzeria",
                  "Frog & Firkin",
                  "Golden Corral",]
    choice = random.choice(doorDash)
    myLabel = Label(root, text='You should consider ordering '+str(choice)+'!')
    myLabel.pack()
btn = Button(root, text='Where should I eat?', bd='5', command=suggestFood)
btn.pack()
root.mainloop()