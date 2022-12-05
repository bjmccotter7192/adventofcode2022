# Every rucksack has 2 compartments

lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

lower_alpha_priority = {}
upper_alpha_priority = {}

for i in range(26):
  lower_alpha_priority[lower_alpha[i]] = i + 1

for i in range(26):
  upper_alpha_priority[upper_alpha[i]] = i + 27

# QUESTION 1
rucksack_data = open('day3.txt', 'r')
totalLines = rucksack_data.readlines()

sum_of_priorities = 0

for line in totalLines:
  half_index = len(line) / 2

  rucksack_compartment_1 = line[0:int(half_index)]
  rucksack_compartment_2 = line[int(half_index):]

  duplicated_items = []

  for ruck in rucksack_compartment_1:
    if ruck in rucksack_compartment_2:
      duplicated_items.append(ruck)

  found_item = list(dict.fromkeys(duplicated_items))[0]

  if found_item in lower_alpha:
    sum_of_priorities += lower_alpha_priority[found_item]
  else:
    sum_of_priorities += upper_alpha_priority[found_item]

print(sum_of_priorities)

# QUESTION 2
sum_of_priorities = 0
grouped_elf_data = []

with open('day3.txt', 'r') as infile:
  lines = []
  for line in infile:
    lines.append(line)
    if len(lines) >= 3:
      grouped_elf_data.append(lines)
      lines = []

for group in grouped_elf_data:
  found_dupes = []
  elf1_rucksack = group[0]
  elf2_rucksack = group[1]
  elf3_rucksack = group[2]

  for alpha in elf1_rucksack:
    if alpha in elf2_rucksack and alpha in elf3_rucksack:
      found_dupes.append(alpha)
  
  found_item = list(dict.fromkeys(found_dupes))[0]

  if found_item in lower_alpha:
    sum_of_priorities += lower_alpha_priority[found_item]
  else:
    sum_of_priorities += upper_alpha_priority[found_item]

print(sum_of_priorities)