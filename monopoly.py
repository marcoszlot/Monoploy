print "\n\nMONOPOLY 1.0\n"
userOne = raw_input("\nENTER USER ONE: ")
userTwo = raw_input("\nENTER USER TWO: ")
userThree = raw_input("\nENTER USER THREE: ")
userFour = raw_input("\nENTER USER FOUR: ")
print "\n\nWELCOME %s, %s, %s, %s" % (userOne, userTwo, userThree, userFour)
while( 3 > 1):
   moneyOne = 25000
   moneyTwo = 25000
   moneyThree = 25000
   moneyFour = 25000
   print "\n\n%s TURN" % (userOne)
   userOneTurn = input("\nENTER: ")
   moneyOne = moneyOne + userOneTurn
   print moneyOne
   print "\n\n%s TURN" % (userTwo)
   userTwoTurn = input("\nENTER: ")
   moneyTwo = moneyTwo + userTwoTurn
   print moneyTwo
   print "\n\n%s TURN" % (userThree)
   userThreeTurn = input("\nENTER: ")
   moneyThree = moneyThree + userThreeTurn
   print moneyThree
   print "\n\n%s TURN" % (userFour)
   userFourTurn = input("\nENTER: ")
   moneyFour = moneyFour + userFourTurn
   print moneyFour
   getOut = raw_input("\n\nGET OUT?")
   if getOut == "yes":
      print " \n\n%s POINTS: %d\n%s POINTS: %d\n%s POINTS: %d\n%s POINTS: %d" % (userOne, moneyOne, userTwo, moneyTwo, userThree, moneyThree, userFour, moneyFour)
      break;
   else:
      print "\n"
