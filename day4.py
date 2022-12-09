# Advent of Code Day 4: Camp Cleanup
# 

overlapped_assignments = 0
with open("day4.txt", "r") as assignment_data:
  for line in assignment_data:
    stripped_line = line.strip()
    seating_assignments = stripped_line.split(',')

    elf1_assignment = [*range(int(seating_assignments[0].split('-')[0]), int(seating_assignments[0].split('-')[1]) + 1)]
    elf2_assignment = [*range(int(seating_assignments[1].split('-')[0]), int(seating_assignments[1].split('-')[1]) + 1)]

    if len(elf1_assignment) >= len(elf2_assignment):
      # Question 1
      result = all(assignment in elf1_assignment for assignment in elf2_assignment)
      # Question 2
      result = any(assignment in elf1_assignment for assignment in elf2_assignment)
    else:
      # Question 1
      result = all(assignment in elf2_assignment for assignment in elf1_assignment)
      # Question 2
      result = any(assignment in elf2_assignment for assignment in elf1_assignment)

    if result == True:
      overlapped_assignments += 1

print(overlapped_assignments)