import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

Gender = ('Men', 'Women')
y_pos = np.arange(len(Gender))
Number_Of_Medals = [203,157]

plt.bar(y_pos, Number_Of_Medals, align='center', alpha=0.5)
plt.xticks(y_pos, Gender)
plt.ylabel('Number_Of_Medals')
plt.xlabel('Gender')
plt.title('Number Of Medals won by Men and Women')

plt.legend(
            title="Gender",
            loc="upper right",
            bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()