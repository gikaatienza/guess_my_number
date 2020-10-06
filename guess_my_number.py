#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 08:55:09 2020

@author: Angelika
"""

import random


MIN = 0
MAX = 1000

class GuessMachine():
    
    def __init__(self):
        
        self._number_to_guess = random.randint(MIN, MAX)
        self.number_of_attempt = 0
        
    def guess(self, num):
        
        self.number_of_attempt +=1
        if num < self._number_to_guess:
            return 'too low'
        elif num > self._number_to_guess:
            return 'too high'
        else: 
            return 'found'
        

if __name__ == '__main__':
    guess_machine = GuessMachine()
    print('Hey! Try to guess a number between %d  and %d!' %(MIN, MAX))

    while True:
        user_input = input('Your guess?')
        try:
            user_attempt = int(user_input)
            result = guess_machine.guess(user_attempt)
            if result == 'found':
                print(
                    'Fantastic, you find'
                    'the number I had in mind'
                    'in %d attempts!' % guess_machine.number_of_attempt)
                break
            else:
                print(result)
        except ValueError:
            print('You joker...that was not an integer!')
