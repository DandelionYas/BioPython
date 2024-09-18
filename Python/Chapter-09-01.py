# Funcions in Python
def salam():
    print('Hello world!')
salam()    

# Funcion with one parameter
def salam_user(username):
    print(f'Hello {username}')
salam_user('Yaser')    

# Funcion with two parameters
def formatted_name(first_name, last_name):
    full_name=f'{first_name} {last_name}'
    return full_name.upper()
f_name='navid'    
l_name='arian'
print(formatted_name(f_name, l_name))

# Recieve value and pass to function
def dandelion_academia(username):
    print(f'Welcome! {username.title()}')
user=input('Enter your name:')    
dandelion_academia(user)

# Pass argument by choosing the name. otherwise order will be considered
def describe_car(car_brand, car_year):
    print(f'Your car is {car_brand.title()}.')
    print(f'Your {car_brand} was made in {car_year}.')
describe_car(car_year='ford', car_brand='Ford')

# Define Funcion for Molecular Weight calculation
def protein_mw(prot_seq):
    aa_mass = {'A':89, 'V':117, 'L':131, 'I':131, 'P':115, 'F':165, 'W':204, 'M':149, 'G':75, 'S':105, 
           'C':121, 'T':119, 'Y':181, 'N':132, 'Q':146, 'D':133, 'E':147, 'K':146, 'R':174, 'H':155}
    prot_mw=0
    for aa in prot_seq:
        prot_mw = prot_mw + aa_mass.get(aa.upper(),0)
    return prot_mw - (18*(len(prot_seq)-1))
prot_seq = input('Enter your protein sequence: ')
print(protein_mw(prot_seq))

# Call function in while loop
while True:
    print('\nPlease tell me your name:')
    print("(Enter 'q' at any time to quit)")
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    formatted_name=formatted_name(first_name=f_name, last_name=l_name)
    print(f'\nHello, {formatted_name}')

# An Arbitrary number of arguments
def mean(*numbers):
    if len(numbers) == 0:
        return None
    else:
        total = sum(numbers)
    return total / len(numbers)

print('mean: ', mean(2,5,3,65,4,6))

def taghsim(my_number, *numbers):
    if len(numbers) == 0:
        return None
    else:
        total = sum(numbers)
    return total / my_number

print('division ', taghsim(3, 5,4,6,3))
