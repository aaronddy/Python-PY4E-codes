x = 5
print("hello world")

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fn':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('es')
greet('fn')

def greeting(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fn':
        return 'Bonjour'
    else:
        return 'Hello'

print(greeting('es'), 'Fatima')
print(greeting('fn'), 'Eden')
print(greeting('kr'), 'Daye')