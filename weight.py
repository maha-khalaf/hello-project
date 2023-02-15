weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.toLowercase == 'l':
    weight_in_kilo = float(weight) * 0.45
    print('You are ' + str(weight_in_kilo) + 'kilograms')
elif unit.toLowercase == 'k':
    weight_in_pounds = float(weight) * 2.2
    print('You are ' + str(weight_in_pounds) + 'pounds')
