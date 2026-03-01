import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.get_choices(options)
    choices = {"player": player_choice, "computer": computer_choice}
    
