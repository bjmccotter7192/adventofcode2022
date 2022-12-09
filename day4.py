

with open("day4_test.txt", "r") as assignment_data:
  # totalLines = assignment_data.readlines()
  print("Let's get it for day 4")
  for line in assignment_data:
    print(line)
    seating_assignments = line.split(',')
    elf1_assignment = range(seating_assignments[0].split('-')[0], seating_assignments[0].split('-')[1])
    elf2_assignment = range(seating_assignments[1].split('-')[0], seating_assignments[0].split('-')[1])

    print(elf1_assignment)
    print(elf2_assignment)
