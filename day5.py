# Advent of code Day 5: Supply Stacks

# move is a keyword to find line of instruction
# first number = number_of_crates_to_move
# second number = row_to_move_from
# third number = row_to_move_to

# Finding Crates
# Read line and find index of first bracket?
# index - 1 / 3

moving_instructions = []
stack_height_index = 0
crate_stacks = [x[:] for x in [[""] * 3] * 3] # TEST INPUT
# crate_stacks = [x[:] for x in [[""] * 9] * 8] # REAL INPUT

print(crate_stacks)

def makeCrateRow(line):
  row_of_crates = []

  total_length = len(line)
  index = 0
  while(index < total_length):
    end_index = index + 3
    crate = line[index:end_index]
    row_of_crates.append(crate)
    index += 4

  crate_stacks[stack_height_index] = row_of_crates

def moveCrates(line):
  number_of_crates_to_move = line[5]
  stack_to_move_from = line[12]
  stack_to_move_to = line[17]

  print(number_of_crates_to_move, stack_to_move_from, stack_to_move_to)

with open("day5_test.txt", "r") as supply_stacks_data:
  for line in supply_stacks_data:
    if "move" in line:
      moving_instructions.append(line)
    elif "[" not in line:
      continue
    else:
      makeCrateRow(line)
      stack_height_index += 1

print(crate_stacks)
print(moving_instructions)