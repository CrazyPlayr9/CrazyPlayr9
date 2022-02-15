#import modules for later
import time
#taking variable
cpa = 0
a = 0
#sensors of door(imaginative)
doorstate = 'open','closed'
#code used for salting
salt = 'f%d'
#the actual lock
lock = 'Hello_2OO7'
#salting the lock with one algorythm
salted = lock[:3]+salt+lock[3:6]+salt+lock[6:]
#Hashing the lock so it stays protected
hashed = hash(salted)
#taking a var to true
t = 0
#usint the var for making the main loop
while t == 0:
    #Braking code of program
    if cpa == 4:
        print('Data is gone and gone for good :)')
        t += 1
    #input that is what we enter
    inp = input('Pls Enter Lock : ')
    #Salting Lock with same algorythm
    saltedinp = inp[:3]+salt+inp[3:6]+salt+inp[6:]
    #hashing the input so it matchs to lock
    hashedinp = hash(saltedinp)
    #condition
    if hashedinp == hashed:
        print('Greetings, Mr.Vishnu.')
        door = doorstate[0]
        print(door)
        time.sleep(7)
        door = doorstate[1]
        print(door)
        a = 0
        continue
        
    else:
        print('Sorry! Wrong password')
        a += 1
    if a == 1:
         continue
    if a == 2:
         continue
    if a == 3:
         continue
    if a == 4:
         continue
    if a == 5:
         continue
    if a >= 5:
         print('Wait for 10 minutes to recollect the data')
         time.sleep(1)
    if a == 6:
         print('Clue: Helloyear')
         continue
    if a == 7:
         continue
    if a == 8:
         print('Hello_bornyear-1')
         continue
    if a == 9:
         print('Clue: Hello_2jamesbond')
         continue
    if a == 10:
         cp = input('Pls enter given challange phrase --> "A1B2C3" : ')
         if cp == 'A1B2C3':
             cpa += 1
             a = a-3
             print('You are not a bot')
             continue
         else:
             print('You are a bot')
             break
    else:
         break
