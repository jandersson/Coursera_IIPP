__author__ = 'Jonas'
##Assignment 1

##Name to number assignments
#0 — rock
#1 — Spock
#2 — paper
#3 — lizard
#4 — scissors

import random

def name_to_number(name):
    '''
    Takes a name and returns a corresponding number
    '''
    if name == 'rock':
        return 0
    if name == 'Spock':
        return 1
    if name == 'paper':
        return 2
    if name == 'lizard':
        return 3
    if name == 'scissors':
        return 4
    else:
        print 'Thats an invalid choice!'

def number_to_name(number):
    '''
    Takes a number and returns its corresponding name.
    '''
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        print 'Invalid number!'

def rpsls(player_choice):
    print "\nYou chose", player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_name = number_to_name(comp_number)
    print "Computer chose", comp_name
    diff = (player_number - comp_number) % 5
    if diff == 0:
        print 'Draw!'
    elif diff == 1:
        print 'Player wins!'
    elif diff == 2:
        print 'Player wins!'
    elif diff > 2:
        print 'Computer wins!'

rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')