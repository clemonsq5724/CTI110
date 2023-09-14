import matplotlib.pyplot as plt
import turtle

# collect the data

 # empty list

"""
print("Enter Pokemon data:")
print("Day 1: ", end="")
day1 = int(input())
print("Day 2: ", end="")
day2 = int(input())
print("Day 3: ", end="")
day3 = int(input())
"""


# new version - Loop and get each day at a time
data = []
#num_days = int(input("How many days? "))
num_days = turtle.numinput("Input","How many days? ")
num_days = int(num_days)
for day in range(num_days):
  #print("Day ", day, ":", end="")

  label = "Day #" + str(day) #
  today = turtle.numinput(label, "How many Pokemon?")
  data.append(today)
     # add it to end of the list

# put the data in a list (DONE)
 #print min and max
print("Best day:", max(data))
print("Worst day:", min(data))
# TODO: total and average
total = 0
for num in data:
  total += num
  # total is now all the numbers in data, added up
average = total / num_days
print("Total:", average)
print("Average:", average)






# TODO: Graph the real data
fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("pokemon data")
plt.xlabel('day #')
plt.ylabel('pokemons collected')
plt.show()
