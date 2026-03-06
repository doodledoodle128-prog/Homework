print(" choose from jack, mike, sam, bob, joshua")

jack = "january 4th"
mike = "Febuary 8th"
sam = "July 27th"
bob = "December 2nd"
joshua = "November 17th"

who = input("who's birthday do you want to know?: ".lower())

if who == 'jack':
    print(jack)
if who == 'mike':
    print(mike)
if who == 'sam':
    print(sam)
if who == 'bob':
    print(bob)
if who == 'joshua':
    print(joshua)
else:
    print("birthday not recorded")