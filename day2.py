# Total Score is the sum of your scores for each round
# A = Rock, B = Paper, C = Scissors (YOUR GUESS)
# X = Rock, Y = Paper, Z = Scissors (OPPONENTS GUESS)
# Scoring
#   Rock beats Scissors, Scissors beats Paper, Paper beats Rock
#   1 for Rock, 2 for Paper, and 3 for Scissors
#   0 if you lost, 3 if you draw, 6 if you win

games_data = open('day2.txt', 'r')
totalLines = games_data.readlines()

totalScore = 0

#### QUESTION 1

for line in totalLines:
  opponent_choice = line[0]
  your_choice = line[2]

  if opponent_choice == "A": ## ROCK
    if your_choice == "X":
      totalScore += (1 + 3)
    elif your_choice == "Y":
      totalScore += (2 + 6)
    else:
      totalScore += (3 + 0)
  elif opponent_choice == "B": ## PAPER
    if your_choice == "X":
      totalScore += (1 + 0)
    elif your_choice == "Y":
      totalScore += (2 + 3)
    else:
      totalScore += (3 + 6)
  else:   ## SCISSORS
    if your_choice == "X":
      totalScore += (1 + 6)
    elif your_choice == "Y":
      totalScore += (2 + 0)
    else:
      totalScore += (3 + 3)

print(totalScore)


### QUESTION 2
for line in totalLines:
  opponent_choice = line[0]
  expected_outcome = line[2]

  if opponent_choice == "A":       ## ROCK
    if expected_outcome == "X":    ## LOSE
      totalScore += (3 + 0)
    elif expected_outcome == "Y":  ## DRAW
      totalScore += (1 + 3)
    else:                          ## WIN
      totalScore += (2 + 6)


  elif opponent_choice == "B":     ## PAPER
    if expected_outcome == "X":    ## LOSE
      totalScore += (1 + 0)
    elif expected_outcome == "Y":  ## DRAW
      totalScore += (2 + 3)
    else:                          ## WIN
      totalScore += (3 + 6)


  else:                            ## SCISSORS
    if expected_outcome == "X":    ## LOSE
      totalScore += (2 + 0)
    elif expected_outcome == "Y":  ## DRAW
      totalScore += (3 + 3)
    else:                          ## WIN
      totalScore += (1 + 6)

print(totalScore)
