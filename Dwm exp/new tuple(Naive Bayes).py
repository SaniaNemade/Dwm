from collections import defaultdict

# Dataset provided
dataset = [['red','sports','domestic','yes'],
           ['red','sports','domestic','no'],
           ['red','sports','domestic','yes'],
           ['yellow','sports','domestic','no'],
           ['yellow','sports','imported','yes'],
           ['yellow','SUV','imported','no'],
           ['yellow','SUV','imported','yes'],
           ['yellow','SUV','domestic','no'],
           ['red','SUV','imported','no'],
           ['red','sports','imported','yes']]

# Counting occurences of target (stolen?) and attributes

attribute_count = defaultdict(lambda: defaultdict(int))
target_count = defaultdict(int)

for value in dataset:
    target = value[-1]
    target_count[target] += 1
    for i in range(len(value) - 1):
        attribute_count[target][i,value[i]] += 1


# New Tuple
color = input('Enter color: ')
car = input('Enter type: ')
origin = input('Enter origin: ')

print('\nThe new tuple to be classified is:')
print(f'X = [{color}, {car}, {origin}]')

# Calculation of probabilities
p_yes = target_count['yes'] / len(dataset)
print(f'\nProbability of yes: {p_yes}')
p_no = target_count['no'] / len(dataset)
print(f'Probability of no: {p_no}')

p_color_given_yes = attribute_count['yes'][0,color] / target_count['yes']
print(f'\nProbability of color|yes: {p_color_given_yes}')
p_type_given_yes = attribute_count['yes'][1,car] / target_count['yes']
print(f'Probability of type|yes: {p_type_given_yes}')
p_origin_given_yes = attribute_count['yes'][2,origin] / target_count['yes']
print(f'Probability of origin|yes: {p_origin_given_yes}')

p_color_given_no = attribute_count['no'][0,color] / target_count['no']
print(f'\nProbability of color|no: {p_color_given_no}')
p_type_given_no = attribute_count['no'][1,car] / target_count['no']
print(f'Probability of type|no: {p_type_given_no}')
p_origin_given_no = attribute_count['no'][2,origin] / target_count['no']
print(f'Probability of origin|no: {p_origin_given_no}')

# Using Bayes Theorem
p_stolen_given_yes = p_yes*p_color_given_yes*p_type_given_yes*p_origin_given_yes
print(f'\nProbability of stolen|X: {p_stolen_given_yes}')
p_stolen_given_no = p_no*p_color_given_no*p_type_given_no*p_origin_given_no
print(f'Probability of not stolen|X: {p_stolen_given_no}')
