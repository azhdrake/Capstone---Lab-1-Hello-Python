user_class = input('Please enter your first class: ')
class_list = []
while user_class != 'x' and user_class != 'X':
    class_list.append(user_class)
    user_class = input('Please typein yout next class, or type x to exit. ')
    
print('Thank you. Heres a list of all your classes.')
for a_class in class_list:
    print(a_class)