# WCGS Cricket Program
#
# over() - an over is cricket is 6 balls bowled by the batting team

# validateball()
# Routine to capture the value for a run
# Better version of enterball(). Uses try and except to make the code robust
# Still needs better validatiion of the range of values for a run
#

def validateball(ball) :
  valid = False
  while (not valid) :
    try: 
      msg = "Enter runs scored on ball number " + str(ball) + ": "
      runs = int (input (msg))
      # Validate the runs input
      if (runs >= 0 and runs <= 6):
        valid = True
      else :
        print ("Invalid run - please re-enter")
    except: 
      print ("Invalid entry - please re-enter")

  return runs

def over (over_number) :
  total = 0

  if (over_number < 1) :
    print ("over(): invalid over number: ", over_number)
    return -1

  print ("Over number: ", over_number)
  for ball in range (1, 7) :
    runs = validateball (ball)
    total += runs
  print ("Runs for over: ", total)
  return total

#over (1)
#input ("Enter <return> to continue")

# Task Two
#
# Write a test plan with at least three tests that can be performed on your over() routine
# Include your test plan below:
# 
# For, example:
# Test 1: Call over with a negative over number
# If your test crashes your program, comment it out after running it

#over (-1)
#input ("Enter <return> to continue")

# Task Three
# Innings. An innings in cricket a number of overs bowled to a team. In limited overs, the bowling team
# bowls a limited/set number of overs, e.g. 20 overs or 50 overs.
#

def innings (team_name, novers) :
  total = 0

  if (novers <1 or novers > 20) :
    print ("innings(): invalid number of overs: ", novers)
    return -1

  print ("Batting Team: ", team_name)
  for o in range (1, novers + 1) :
    total += over (o)
  print ("Innings total for ", team_name, "is: ", total)
  print ()
  return total

#innings ("WCGS", 2)
#input ("Enter <return> to continue")

# Task Four
#
# Write a test plan with at least three tests that can be performed on your innings() routine
# For, example:
# Test 1: Call innings()  with a negative over number
# If your test crashes your program, comment it out after running it

#innings ("Wilsons", -1)
#input ("Enter <return> to continue")

# Task Five
# Match. A cricket match consists of two teams having the same number of innings and 
# deciding which team has scored the most runs.
#

import random

def match () :

  print ("WCGS Cricket Match")
  oppo = input ("Enter the opposition team name: ")
  overs = int (input ("Enters the number of overs: "))
  toss = random.randint (0, 1)
  # Heads = 0, tails = 1
  
  #
  # Prompt for heads or tails
  #

  # Assume heads for WCGS and tails for opp
  if (toss == 0) :
    print ("WCGS win the toss and bat first")
    wcgs_score = innings ("WCGS", overs)
    oppo_score = innings (oppo, overs)
  else :
    print ("WCGS lose the toss and bowl first")
    oppo_score = innings (oppo, overs)
    wcgs_score = innings ("WCGS", overs)
    
  if (wcgs_score == oppo_score) :
    print ("Match drawn")
  elif (wcgs_score > oppo_score) :
    print ("WCGS Win!")
  else: 
    print (oppo, " Win!")
    
  print ("Thank you for coming")


# Run the match
match()
