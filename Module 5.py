import random
import time

main_key = True
key = False

# True / False input statement
while main_key is True:

    # Main question Input
    question1 = input('Do you happen to own any Cats? \n' 
                      '>>> ')
    if question1.lower() == 'y':
        key = True
        main_key = False
    elif question1.lower() == 'n':
        key = False
        main_key = False
    else:
        print('Not an Answer!')
    # Main question Input

# Response to Question1 in Boolean True / False while statement
while key is True:
    print('I would like to own a cat \n')
    time.sleep(1.5),
    print('Especially if it is a Maine Coon!')
    break
while key is False:
    print('Well maybe you should look into getting one! \n')
    time.sleep(1.5)
    print('They are adorable and have there own personalities. \n')
    time.sleep(1.5)
    print('Either way, you should learn about the type of cat your going to get first to see which one best matches you!')
    break
# Response to Question1 in Boolean True / False while statement
