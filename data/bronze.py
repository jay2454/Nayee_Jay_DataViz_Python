import csv
import matplotlib.pyplot as plt

australian= []
german = []
usa = []

catagories = []

with open('data/AUS_GER_USA_BRONZE - Sheet1.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row in the spredsheet")
			catagories.append(row)
			line_count += 1

		else:
			if row [4] == "AUS":
				print("Australian medal")
				australian.append(row[4])
			elif row[4] == "GER":
				print("German medal")
				german.append(row[4])
			elif row[4] == "USA":
				print("USA medal")
				usa.append(row[4])

			print(line_count)
			line_count += 1

print(len(australian))
print(len(german))	
print(len(usa))

labels = ["Australian", "German", "USA"]
sizes = [len(australian), len(german), len(usa)]
color = ['green', 'salmon', 'red']


plt.pie(sizes, colors=color, shadow= True, startangle=190)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Total Bronze Medal wins")
plt.xlabel("Medal counts since 1942")
plt.show()
						