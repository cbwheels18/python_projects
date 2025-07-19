def add(text):
    user_input = input(text)
    running_list.append(user_input)
    return user_input

def remove(text):
    user_input = input(text)
    running_list.remove(user_input)
    return user_input

running_list = []
user_input = ''
add_item = ''
rem_item = ''
print('Welcome to your To Do List app, what would you like to do?')
while user_input.lower() != 'exit':
    print('Would you like to Add an item, Remove an item, View your list, or Exit? ')
    user_input = input('Add, Remove, View, or Exit? ')
    if user_input.lower() == 'add':
        add_item = add('Add an item to the list of items: ')
        print(f'you added {add_item}')
    elif user_input.lower() == 'remove':
        rem_item = remove('Remove an item from the list of items: ')
        print(f'you removed {rem_item}')
    elif user_input.lower() == 'view':
        print(running_list)
    elif user_input.lower() == 'exit':
        print('Thanks for visiting!')
    else:
        print('Not an accepted value, please try again. Accepted values are: add, remove, view or exit.')