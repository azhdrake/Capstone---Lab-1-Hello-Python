user_class = input('Please enter your first class: ')
class_list.append(user_class)
while user_class != 'x' and user_class != 'X':
	user_class = input('Please typein yout next class, or type x to exit.')
	class_list.append(user_class)
print('Thank you. Heres a list of all your classes. ' + clast_list)