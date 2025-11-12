# open, command, close
# r => read
# w => write
# a => write append

# write into files
# -----------------------------------
# f = open('test.txt', 'w')
# f.write('hello')
# f.close()



# read files
# -----------------------------------
# f = open('test.txt', 'r')
# print(f.read())
# print(f.readline())
# print(f.readlines()[1:4])
# f.close()


# open file in advance mode
# -----------------------------------
# with open('test.txt', 'r') as f:
#     print(f.read())

    



# import json

# students = {
#     '103': {'name': 'ali', 'score': {'math': 20, 'chimi': 18}},
#     '104': {'name': 'reza', 'score': {'math': 19}},
#     '105': {'name': 'sara', 'score': {'chimi': 17}},
# }

# dump, load
# with open('students.json', 'w') as f:
#     json.dump(students, f)


# students = dict()
# with open('students.json', 'r') as f:
#     students = json.load(f)

# print(students)



# prs
import random

wincard = {
    'r': 'p',
    'p': 's',
    's': 'r'
} 

pcwin, hwin = 0

with open('test.txt', 'w') as f:
    while True:
        pc_choice = random.choice([i for i in wincard])
        h_choice = input('select from r/p/s: ')

        if h_choice == 'end':
            break
        elif h_choice not in [i for i in wincard]:
            print('invalid selection, try again')
            continue
        elif h_choice == pc_choice:
            print('same value, try again')
        elif h_choice == wincard.get(pc_choice):
            print('win')
            hwin += 1
        else:
            print('loss')
            pcwin += 1
        
        f.write(f'H: {h_choice}, PC:{pc_choice}\n')
    f.write(f'\n\n\n ----------------\n')
    f.write(f'H: {hwin}\nPC:{pcwin}\n')

