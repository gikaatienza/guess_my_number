#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:14:57 2020

@author: Angelika
"""

import random 

from guess_my_number import MIN, MAX, GuessMachine

if __name__ == '__main__':
    guess_machine = GuessMachine()
    while True: 
        attempt = random.randint(MIN, MAX)
        result = guess_machine.guess(attempt)
        print('tried %d : %s' % (attempt, result))
        if result == 'found':
            print('Finished in %d attempts.' % guess_machine.number_of_attempt)
            break