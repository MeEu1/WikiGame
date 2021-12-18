import sys
import time
import random

import keyboard
import wikipediaapi as wiki

stoptime = ''

def countdown(t):
    original_t = t
    while t:
        mins, secs = divmod(t, 60) # gets seconds and minutes
        timer = '{:02d}:{:02d}'.format(mins, secs)#formats the time
        print(timer, end='\r')#makes the cursor go back to the initial position at the console so it will keep rewriting itself
        time.sleep(1) #waits one second
        t -= 1

        if keyboard.is_pressed('space'):
            spent_mins, spent_secs = divmod(original_t - t, 60)
            print('Coungratulations!\nYou stopped at {:02d}:{:02d}\nAnd it took you {:02d}:{:02d}!'.format(mins, secs, spent_mins, spent_secs))
            break#breaks the function if the player wins
            #note: must holf for a few seconds 
        elif t == 0 or keyboard.is_pressed('d'):#in case you loose
            print('Maybe next time...')
            break


categories = ['Places', 'Physics', 'Technology', 'Biology', 'Objects', 'Religion', 'Chemistry', 'History', 'Geography', 'Mathematics', 'Literature', 'Languages']

time_ = int(sys.argv[1])#time given in seconds
objective = sys.argv[2]#page you'll need to stop at

#design purpose
rules_separator = '-' * 20
controls_separator = '*' * 20

print(f'{rules_separator}\nRULES:\nYou\' get a random category.\nThen you\'ll chose a link in this category.\nFinally, you will try to reach the page {objective}.\nIf you find it, press space for at least 2 seconds\n{rules_separator}')
print(f'{controls_separator}\nControls:\nSPACE: stop the timer(meaning you won)\nD: used if you want to give up{controls_separator}')
print('NOTES:\n\t+the game will start in 8 seconds\n\t+you have to copy the link')

#wikipedia api
wikipedia = wiki.Wikipedia('en')
chosen_category = random.choice(categories)#gets the category you'll start at in wikipedia
page = wikipedia.page(f'Category:{chosen_category}\n')
print(chosen_category)#gives the category
print(page.fullurl)#gives the link to the page

time.sleep(8)#waits 5 seconds for you to prepare yourself and read the rules
print('START!')
countdown(time_)

