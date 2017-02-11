# A program that takes the name of cats and saves them
catNames = []
print('To end the input an print the list enter an empty Name:')
while True:
    name = input('Please enter the name of cat ' + str(len(catNames)) + ' to be saved: ')
    if(name == ''):
        break
    elif(name != ''):
        catNames += [name] # To enter a List element it is IMPORTANT to add Square breaks to it
    else:
        print('No one should ever get here!')
        exit()
print('The cats names are:')
for name in catNames:
    print(' - ' + name)

