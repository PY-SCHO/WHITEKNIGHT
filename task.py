names =  [
    ['alice', 'bob', 'charlie'],
    ['david', 'eve', 'frank'],
    ['grace', 'heidi', 'ivan'],
    ['judy', 'ken', 'laura']
]
names[0].remove('alice')

for list in names:
        for name in list:
            print(name)
        
USER = input("enter new name:")
names[0].append(USER)
print(names)