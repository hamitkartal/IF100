# -*- coding: utf-8 -*-
"""hamit_the3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Li60ickC6ObtqmtGbXLHX4X849mLZdgh
"""

# Hamit Kartal 28404
x = False
while x == False:
  info1 = input('Products in shopping cart: ')
  t = info1.count(',')
  y = info1.count('_')
  if y == (t + 1) * 4 and y >= 4:
    x = True
  else:
    print('Invalid input for products, please enter in correct format.')
z = False
while z == False:
  info2 = input("Family members' informations: ")
  h = info2.count(',')
  k = info2.count('_')
  if k == (h + 1) * 3 and k >= 3:
    z = True
  else:
    print('Invalid input for family information, please enter in correct format.')
total_f = 0
total_c = 0
total_p = 0
a = info1.split(',')
for y in a:
  x = y.split('_')
  total_f += int(x[1]) * int(x[2])
  total_c += int(x[1]) * int(x[3])
  total_p += int(x[1]) * int(x[4])
b = info2.split(',')
total_needed_cal = 0
for c in b:
  d = c.split('_')
  if d[0] == 'M':
    total_needed_cal += 66.5 + 13.8* int(d[1]) + 5*int(d[2]) - 6.8*int(d[3])
  elif d[0] == 'F':
    total_needed_cal += 655.1 + 9.6*int(d[1]) + 1.9*int(d[2]) - 4.7*int(d[3])
if total_f*9 >= total_needed_cal*0.3:
  t = int((total_f*9) // (total_needed_cal*0.3))
  print('These products will be enough for your family in terms of fat for', t, 'days.')
else:
  print('You need to add products with more fat to your shopping cart.')
if total_c*4 >= total_needed_cal*0.5:
  l = int((total_c*4) // (total_needed_cal*0.5))
  print('These products will be enough for your family in terms of carbohydrate for', l, 'days.')
else:
  print('You need to add products with more carb to your shopping cart.')
if total_p*4 >= total_needed_cal*0.2:
  m = int((total_p*4) // (total_needed_cal*0.2))
  print('These products will be enough for your family in terms of protein for', m, 'days.')
else:
  print('You need to add products with more protein to your shopping cart.')
# Hamit Kartal 28404