import os
import time
# Nacho_World
def__init__('go class', 'spicy_nachos')
  macho_spicy= 'yes'
  mild= 'maybe'
  no_spicy= 'no'
  print('macho_spicy', 'mild','no_spicy')
# direction
def _str_(direction)
  if direction == 'orange_waterfall' or direction ==  'yellow__waterfall' or direction == 'brown_waterfall' or direction ==  'right tan_waterfall':
    print(‘left_orange_waterfall’, ‘Up yellow__waterfall’, ‘down_brown_waterfall’, ’right tan_waterfall’)

  # Nacho_meat_ attack
  if you come == meat attack
    miniature_meat_attack=strings('chicken','ground_beef','veggies')
  print('meat_attack)
  #Topping Splash on you if fail 
  If_topping=="volcano splash bowl"
  Splash_Bowl_Ingredients= strings('black_olives', 'tomatoes','jalapeño', 'cucumber',' onions', 'lettuce', 'spinach', 'black_beans','sour cream', 'queso blanco')
  print('Splash_Bowl_Ingredients')


#after the end of the world
def menuScreen():
    print("WELCOME!")
    print("RPG Adventure 10")
    print("Copyright 2020")
def get_menu_options():
    option_title = input("Select an option: New Game, Load Game, Options, Exit: ")
    while option_title != 'New Game' and option_title != 'Load Game' and option_title != 'Options' and option_title != 'Exit':
        print ('Invalid Selection')
        option_title = input("Select an option: New Game, Load Game, Options, Exit: ")
    return option_title
def chooseClass():
    player_class = input('Choose your class: Potato, Karen, Unicorn: ' )
    while player_class != "Potato" and not player_class != "Karen" and not player_class !="Unicorn":
        print('Invalid choice. :(')
        player_class = input('Choose your class: Potato, Karen, Unicorn: ' )
    return player_class
def playerName(player_class):
    player_name = input(" please enter your  name ")
    print('Welcome, ' + player_name + ' the ' + player_class + '!')
    print("don't like your name?")
    time.sleep(1)
    print("too bad")
    return player_name

def eat_choice1():
     decision = input("Eat cold fries or ask for manager?")
    while decision != "Eat" and decision != "Ask":
        print("Invalid selection")
        decision = input("Eat cold fries or ask for manager?")
    if decision == "Eat":
        print('You have contracted the Coronavirus and have been doomed to Nacho Hell!!')
    if decision == "Ask":
        print('The manager walks up and says, "You dare complain about my Nacho Fries?!" and proceeds to choke you with cold Nacho Fries and banishes you to Nacho Hell!!')
    return decision
def redeem_swim():
    decision = input('Will you redeem yourself or dive further into the cold nacho cheese? Choose wisely: Redeem or Swim')
    while decision != "Redeem" and decision != "swim":
        print('Invalid')
        decision = input('Will you redeem yourself or dive further into the cold nacho cheese? Choose wisely: Redeem or Swim')
    if decision == "Swim":
        print('You jump into the river of nacho cheese and drown.')
        print("GAME OVER :(")
        exit(0)
    return decision
def dance_off():
    decision = input()
    while decision !="No" and decision!= "yes":
        print ('invalid')
        print('The Nacho reaper tells you to Dance ChampetaChallenge : Do you want to')
        decision = input()   
    if decision == "No":
          print('The Nacho Reaper bellows "Do you still want  to see the manager?!" and cast you into a nachoy darkness.')
          print('GAME OVER :(')
          exit(0)
    return decision
def learn_a_lesson():
    decision = input()
    while decision != "yes" and decision != "no":
        print("Invalid")
        print('The Nacho Reaper tell you to learn new lesson : Do you want to learn?')
        decision = input()
    if decision == "yes":
        print('The Nacho Reaper starts moving faster than you can see. He stops and looks to you: did you get all that?')

        decision = input()
        if decision == "No":
            print('well to bad im not doing it again')
    return decision
def goLeftOrRightDownTunnel():
    decision = input('Do you choose to walk to the left or right tunnel?')
    if decision == 'left':
        print('You discover a tortilla chest full of nacho helmets and armor.')
        items.append("Nacho Armor")
        items[0].append(5)
        print("After collecting the Nacho Armor, you turn around and go back the way you came.")
    return decision
def covid_19():
  decision = input('The Nacho Reaper sneezes in your direction. Do you run or fight?')
  while decision != "run" and decision != "fight":
    print("Invalid")
    print('The Nacho Reaper sneezes in your direction. Do you run or fight?')
    decision = input()
  if decision == 'fight':
    print('You might be infected now, but suddenly a burrito sword appears.')
    items.append("Burrito Sword")
    items[0].append(5)
    print("After successfully defending yourself against the Nacho Reaper, you continue on your journey.")
  else:
    print('You start to run and fall into an enormous vat of nacho cheese.')
  print("The Nacho Reaper tells you about the new virus.")
  print("As he's telling you, he starts to sweat.")
  print("You start to back away, but it becomes clear that he is infected.")
  print("Your fight or flight instinct kicks in.")

#This is an RPG Game!
#Title Screen
items = [[],[]]
skill_points = 0
player_class = ""
player_name = ""
menuScreen()
time.sleep(1)
clear = lambda: os.system('cls')
clear()
option_title = get_menu_options()


if option_title == 'New Game':
    player_class = chooseClass()
    player_name = playerName(player_class)
    print("You're at the drive-thru at Taco Bell, when out of the blue you get cold nacho fries.")
    decision = eat_choice1()
    print('You have woken up in Nacho Hell and there are skeletons floating in a river of flaming cold nacho cheese')
    print('The Nacho Reaper presents you with the option to redeem yourself')
    decision = redeem_swim()
    print('The Nacho reaper tells you to Dance ChampetaChallenge : Do you want to')
    decision = dance_off()
    print('The Nacho Reaper tell you to learn new lesson : Do you want to learn?')
    decision = learn_a_lesson()
    print('I will teach you another way.')
    print('The Nacho Reaper points to two tunnels.')
    print('The left tunnel is glowing yellowish-orange.')
    print('The right tunnel is smells like cinnamon twists.')
    decision = goLeftOrRightDownTunnel()
    decision = covid_19()
            
    


          
          

    

    

