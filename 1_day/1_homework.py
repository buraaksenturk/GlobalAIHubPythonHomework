# Getting data from the user
nameandsurname = str(input('What is your name and surname :'))
age = int(input('How old are you :'))
height = float(input('What is your height :'))
study = bool(input('Are you study (True/False) :'))
letter = list(input('What are your favorite letters :'))

# Printing data types
print(f'''
Name and Surname Type : {type(nameandsurname)}
Age Type : {type(age)}
Height Type : {type(height)}
Study Type : {type(study)}
Letters Type : {type(letter)}
''')

# Printing values ​​entered on inputs
print(f'''
Name  and Surname : {nameandsurname}
Age : {age}
Height : {height}
Study : {study}
Letters : {letter}
''')
