#!/usr/bin/env python3

round = 0
answer = " "
while round < 3 and answer != "Brian":
    round += 1
    answer = input('Finish the movie title, "Monthly python\'s The life of ------"')
    if answer == 'Brian':
        print("Correct")
    elif round == 3:
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry. Try again!')
