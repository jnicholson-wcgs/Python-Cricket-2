# Python-Cricket-2
Task two in the Python Cricket scoring prgram

Expanding on your initial routines and testing for the WCGS Cricket program, develop extra code to implement more of the rules of cricket into your program.

Background
----------

The WCGS sports department need some assistance for the cricket season and require a program 
to keep track of the scores for cricket match fixtures

In Task One you implemented three routines, all which should have validation and testing, i.e.:
  over()
  innings()
  match()


Task Two
--------

The next task is to enhance your program to cater for some more of the rules of cricket.
Use external sources to verify the rules, e.g., https://en.wikipedia.org/wiki/Laws_of_Cricket or https://www.cricket-rules.com/

Here is a video explaining the rules: https://www.youtube.com/watch?v=wHEIT32ZEVs

1) Extras

   When you enter the score for a ball, enable the user to specify if the ball as a wide, no ball, bye or leg bye
   For example, the user can enter:
   w or W for a wide: add one to the score but bowl another ball
   n or N for a no ball: add one to the score but bowl another ball
   b, B, lb, or LB for a bye/leg bye. Add one to the score

   Test and validate your code

2) Scoreboard

   Enhance your code to keep track of the number of extras in the innings (wides, no balls, bye etc.)
   At the end of the innings, print out all the extras
   Update your score entry routine to allow the user to print the current score including the breakdown of the extras:

   s or S : print out the current score, number of overs and breakdown of the extras.

   The user can ask for the scoreboard at any time when they are enter the score
   You will need to keep track of the extras in some form of data structure (variables,  lists or dictionaries).

   Produce a test plan to test your scoreboard code is correct.

3) Batsmen who are out

   Keep a track of the number of batsmen:
   - Set the number of batsmen at the start of the innings
   - Change your routine for the score entry to allow:
     o or O: batsmen out. No run scored
   - Change your code so that the innings ends when 10 batsmen have been out
   - At the end of the innings, print out the number of batsmen out, total score and overs

   Generate a test plan to check your code. Include boundary cases, e.g., batsmen out at the end of an over, 
   batsmen swapping ends, last man out etc.


4) Batting Stats

   Enhance your code so that you can keep track of the batsmen:
   - The bowling changes end at the end of each over
   - Batsman number one opens the batting
   - Batsmen run between the wickets and the batsman on strike may change
   - When a batsman is out, the batsman may have crossed, so confirm batsman on strike 
   - When a batsman is out, print out his batting stats: balls faced, runs scored and "strike rate"
   - Also track the number of Fours and Sixes scored by that batsman

   Generate a test plan test out your stats.
