wincard = {
    'r': 'p',
    'p': 's',
    's': 'r'
} 

# ['r', 'p', 's']
# list comprehension

print([item for item in wincard])

map(lambda item: item, wincard) 