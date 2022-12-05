input1 = open('day1.txt', 'r')
totalLines = input1.readlines()

totals = []
total_calories_per_elf = 0

for line in totalLines:
  if line.strip():
    total_calories_per_elf = total_calories_per_elf + int(line)
  else:
    totals.append(total_calories_per_elf)
    total_calories_per_elf = 0

totals.sort(reverse=True)

topElfAmount = totals[0]
top3ElvesAmount = totals[0] + totals[1] + totals[2]

print(topElfAmount)
print(top3ElvesAmount)