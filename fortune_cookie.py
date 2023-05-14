# We want to print out a fortune for the user who is wondering what will happen to them

import random

print("\nYour fortune: \n")

lucky_number = random.randint(1,100)

fortune_number = random.randint(1,12)

fortune_text = ''

if fortune_number == 1:
  fortune_text = 'You should be able to undertake and complete anything.'
if fortune_number == 2:
  fortune_text = 'An exciting opportunity lies ahead of you.'
if fortune_number == 3:
  fortune_text = 'You are wise beyond your years.'
if fortune_number == 4:
  fortune_text = 'A routine task will turn into an enchanting adventure.'
if fortune_number == 5:
  fortune_text = 'You will receive money from an unexpected source.'
if fortune_number == 6:
  fortune_text = 'People are naturally attracted to you.'
if fortune_number == 7:
  fortune_text = 'A chance meeting opens new doors to success and friendship.'
if fortune_number == 8:
  fortune_text = 'A dream you have will come true.'
if fortune_number == 9:
  fortune_text = 'Now is the time to try something new.'
if fortune_number == 10:
  fortune_text = 'Wealth awaits you very soon.'
if fortune_number == 11:
  fortune_text = 'You will travel to many exotic places in your lifetime.'
if fortune_number == 12:
  fortune_text = 'Your ability for accomplishment will follow with success.'


print(f'\n{fortune_text}')
print(f'Your lucky number is: {lucky_number}\n')
