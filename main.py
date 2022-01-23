# Ask the player if they would like to start the game
def startGame():
  answer = input("Do you want to play 'The Adventure of Pax the Cat'? Type either YES or NO.\n")

  if answer.lower() == "yes":
    print("And the story begins...")
    missingRope()
  elif answer.lower() == "no":
    print("Hopefully, you will play it next time!\n Goodbye!")
  else:
    print("Please re-read and type in one of the options.")
    startGame()

# Pax missing rope
def missingRope():
  answer = input(""" 
    Once upon a time there was a fluffy cat named Pax. Pax had a favourite piece of yellow rope that he liked to play with. 

    One day he went to play with his rope but it was gone. Where could it be?

    Could it be in the bowl or the washing machine? 

    Type either BOWL or MACHINE.
  """)

  if answer.lower() == "bowl":
    bowl()
  elif answer.lower() == "machine":
    machine()
  else:
    print("Please re-read and type in one of the options.")
    missingRope()

# Looks for rope in the bowl
def bowl():
  answer = input("""
    Pax hopped into the bowl. No rope here. He curled up and had a little rest. 

    After his rest he wondered what to do next. Maybe having a drink or something to eat would help.

    Type either DRINK or EAT

  """)

  if answer.lower() == "drink":
    drink()
  elif answer.lower() == "eat":
    eat()
  else:
    print("Please re-read and type in one of the options.")
    bowl()

# Looks for rope in machine
def machine():
  answer = input("""
    Pax looked in the washing machine. There was an odd sock but no rope. Maybe he should have a sleep but where would be best, on the computer on a shoe?

    Type either COMPUTER or SHOE
  """)

  if answer.lower() == "computer":
    computer()
  elif answer.lower() == "shoe":
    shoe()
  else: 
    print("Please re-read and type in one of the options.")
    machine()

# Pax takes a drink
def drink():
  answer = input("""
    Pax had a drink from his water fountain. Then he carried on looking. 

    Where should he look next? In the dishwasher or in a plastic bottle?

    Type either DISHWASHER or BOTTLE

  """)

  if answer.lower() == "dishwasher":
    dishwasher()
  elif answer.lower() == "bottle":
    bottle()
  else:
    print("Please re-read and type in one of the options.")
    drink()

# Pax is going to eat something
def eat():
  answer = input("""
  Pax ate his dinner then he carried on looking. 

  Where should he look next? In a bag or in a box?

  Type either BAG or BOX.

  """)

  if answer.lower() == "bag":
    bag()
  elif answer.lower() == "box":
    box()
  else:
     print("Please re-read and type in one of the options.")
     eat()

# Pax is going to sleep on the shoe
def shoe():
  answer = input("""
    Pax had a little sleep on the shoe then carried on looking. 

    Where should he look next? In the dishwasher or in a plastic bottle?

    Type either DISHWASHER or BOTTLE

  """)

  if answer.lower() == "dishwasher":
    dishwasher()
  elif answer.lower() == "bottle":
    bottle()
  else:
    print("Please re-read and type in one of the options.")
    shoe()

# Pax is going to sleep on the computer
def computer():
  answer = input("""
    Pax had a little sleep on the computer then carried on looking. 

    Where should he look next? In a bag or in a box?

    Type either BAG or BOX.

  """)

  if answer.lower() == "bag":
    bag()
  elif answer.lower() == "box":
    box()
  else:
     print("Please re-read and type in one of the options.")
     computer()

# Pax goes to look in the dishwasher
def dishwasher():
  answer = input("""
    It wasn’t in the dishwasher so he carried on looking.

    Where should he look next? In a suitcase or on the couch.

    Type either SUITCASE or COUCH.

  """)

  if answer.lower() == "suitcase":
    suitcase()
  elif answer.lower() == "couch":
    couch()
  else:
     print("Please re-read and type in one of the options.")
     dishwasher()

# Pax goes to look in the plastic bottle
def bottle():
  answer = input("""
    It wasn’t in the bottle so he carried on looking.

    Where should he look next? In a suitcase or on the couch.

    Type either SUITCASE or COUCH.

  """)

  if answer.lower() == "suitcase":
    suitcase()
  elif answer.lower() == "couch":
    couch()
  else:
     print("Please re-read and type in one of the options.")
     bottle()

# Pax goes to check the purse
def bag():
  answer = input("""
    It wasn’t in the bag so he carried on looking.

    Where should he look next? In the suitcase or in a couch.

    Type either SUITCASE or COUCH.

  """)

  if answer.lower() == "suitcase":
    suitcase()
  elif answer.lower() == "couch":
    couch()
  else:
     print("Please re-read and type in one of the options.")
     dishwasher()

# Pax goes to check the box
def box():
  answer = input("""
    It wasn’t in the box so he carried on looking.

   Where should he look next? In the suitcase or in a couch.

    Type either SUITCASE or COUCH.

  """)

  if answer.lower() == "suitcase":
    suitcase()
  elif answer.lower() == "couch":
    couch()
  else:
     print("Please re-read and type in one of the options.")
     box()

# Pax goes to check the couch
def couch():
  answer = input("""
    No it wasn't there. 

    Maybe he should try the suitcase.

    Type SUITCASE.

  """)
  if answer.lower() == "suitcase":
    suitcase()
  else:
     print("Please re-read and type in one of the options.")
     couch()

# Pax goes to check the suitcase
def suitcase():
  answer = input("""
   Yes, it was in the suitcase. Pax was very happy.

   Would you like to play again or end the game?

   Type either PLAY or END

  """)
  if answer.lower() == "play":
    missingRope()
  elif answer.lower() == "end":
    print("Thanks for playing! Credits to Jan-Marie Kellow - http://jmksportfolio.weebly.com/")
  else:
     print("Please re-read and type in one of the options.")
     suitcase()

startGame()


