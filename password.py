import random

def randomCase(char, index):
    '''Randomize uppercase and lowercase'''
    flag = random.randint(1,2)
    if index <= 26 and flag == 1:
        return char.upper()
    else:
        return char

def generate(lenght):
    '''Password Generator'''
    characters = 'qwertyuiopasdfghjklzxcvbnm1234567890!"£$%&/\()=^*-_'
    password = ''
    for i in range(lenght):
        index = random.randint(0,len(characters)-1)
        char = randomCase(characters[index], index)
        password += char
    return password





        
    
