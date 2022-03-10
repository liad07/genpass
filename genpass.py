from random import choice

digits='0123456789'
chars='abcdefghijklmn' \
      'opqrstuvwxyz'
up=chars.upper()
speical='!@#$%^&*_'
all=digits+chars+up+speical
password=''.join(choice(all) for i in range(8))
print(password)