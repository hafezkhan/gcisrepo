def choose_operation():
    print('Which operation would you like to perform?')
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiplication')
    print('4 - Division')
    return input('enter your choice: ')
choice = choose_operation()
if choice == '4':
   print('Which type of division you would like to do?')
   print('1 - Regular Division')
   print('2 - Integer Division')
   division_type = input('Enter your choice: ')

first_operand = int(input('enter your first operand: '))
second_operand = int(input('enter your second operand: '))

if choice == '1':
    result = first_operand + second_operand
    print('The result is:', result)
elif choice == '2':
    result = first_operand - second_operand
    print('The result is:', result)
elif choice == '3':
    result = first_operand * second_operand
    print('The result is:', result)
elif choice == '4':
 if division_type == '1':
       result = first_operand / second_operand
       print ('The result is:', result)
 elif division_type == '2':
       result1 = first_operand // second_operand
       print ('The result is:', result1)
else:
    print('invalid choice')
