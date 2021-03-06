#!/usr/bin/env python
# coding: utf-8
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *

root = Tk()
root.geometry('3000x1300')
root['background'] = '#841818'

myLabel = Label(root, text="Tucson, AZ Restaurant Decider", bg='#841818', fg='white')
myLabel.config(font=("Courier", 32))
myLabel.pack()
    
def suggestDoorDash():
    doorDash = [
                "Popeyes",
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
                "Golden Corral",
                ]
    choice = random.choice(doorDash)
    myLabel = Label(root, text='You should order '+str(choice)+' on DoorDash!', bg='#841818', fg='white')
    myLabel['background'] = '#841818'
    myLabel.pack()
def suggestFastFood():
    fastFood = [
                "Five Guys",
                "Raising Cane's",
                "KFC",
                "Subway",
                "Smashburger",
                "Jack in the Box",
                "Carl's Jr.",
                "Arby's",
                "Five Guys",
                "Wendy's",
                "Burger King",
                "Taco Bell",
                "Chipotle",
                "Firehouse Subs",
                "Dairy Queen",
                "Popeyes",
                "McDonald's",
                "What-a-burger"
                ]
    choice = random.choice(fastFood)
    myLabel = Label(root, text='You should order '+str(choice)+'!', bg='#841818', fg='white')
    myLabel['background'] = '#841818'
    myLabel.pack()
def suggestDineIn():
    dineIn = [
                "Popeyes",
                "It's Just Wings",
                "McDonald's",
                "Riliberto's Fresh Mexican Food",
                "MOD Pizza",
                "Baskin Robins",
                "Wienerschnitzel",
                "El Beto Mexican Food",
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
                "Golden Corral",
                ]
    choice = random.choice(dineIn)
    myLabel = Label(root, text='You should order '+str(choice)+' for dine in!', bg='#841818', fg='white')
    myLabel['background'] = '#841818'
    myLabel.pack()
DD = Button(root, text='DoorDash?', bd='5', bg='#9A1818', fg='white', borderwidth=1, command=suggestDoorDash)
FF = Button(root, text='Fast food?', bd='5', bg='#9A1818', fg='white', borderwidth=1,  command=suggestFastFood)
DI = Button(root, text='Dine in?', bd='5', bg='#9A1818', fg='white', borderwidth=1,  command=suggestDineIn)
DD.pack()
DD.config(font=("Courier", 12))
DD.pack(pady=8)
FF.pack()
FF.config(font=("Courier", 12))
FF.pack(pady=8)
DI.pack()
DI.config(font=("Courier", 12))
DI.pack(pady=8)
root.mainloop()