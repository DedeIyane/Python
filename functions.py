def hello():
    print('Hello World!')

hello()

def calculate(a, b):
    return a + b

my_sum = calculate(50, 35)
print(my_sum)

#rpg character building
full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    

    if not isinstance(name, str):
        return 'The character name should be a string'

    if not name:
        return 'The character should have a name'
    
    if len(name) > 10:
        return 'The character name is too long'
    
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    stats = [strength, intelligence, charisma]
    
    for stat in stats:
        
        if not isinstance(stat, int):
            return 'All stats should be integers'
        
        if stat < 1:
            return 'All stats should be no less than 1'
        
        if stat > 4:
            return 'All stats should be no more than 4'
    
    if sum(stats) != 7:
        return 'The character should start with 7 points'
    else:
                STR = (full_dot * strength) +(empty_dot * (10 - strength))
                INT = (full_dot * intelligence) +(empty_dot * (10 - intelligence))
                CHA = (full_dot * charisma) +(empty_dot * (10 - charisma))

    return(f'{name}\nSTR {STR}\nINT {INT}\nCHA {CHA}')

print(create_character('ren', 4, 2, 1))

#pin extractor
def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))

#number pattern generator
def number_pattern(n):
    nums = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    elif n < 1:
        return 'Argument must be an integer greater than 0.'
    else:
        for num in range(1, n+1):
            STR_num = str(num)
            nums += STR_num + ' '
    return nums.rstrip()

print(number_pattern(4))
print(number_pattern(12))

#discount calculator
def apply_discount(price, discount):
    

    type_price = type(price)
    type_discount = type(discount)
    if type(price) not in [int, float]:
        return'The price should be a number'
    
    if type(discount) not in [int, float]:
        return 'The discount should be a number'

    if price <= 0:
        return'The price should be greater than 0'
    
    if discount < 0 or discount > 100:
        return'The discount should be between 0 and 100'
    
    new_discount = (discount/100) * price
    final_price = price - new_discount
    return final_price
    

print(apply_discount(100, 20))
apply_discount(200, 50)
apply_discount(50, 0)
apply_discount(50, 100)
apply_discount(74.5, 20.0)

#caesar cipher
def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text ='Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text= decrypt(encrypted_text, 13)
print(decrypted_text)