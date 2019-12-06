import matplotlib.pyplot as plt;
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

Country = ('Germany', 'USA')
y_pos = np.arange(len(Country))
Number_Of_Medals = [360,653]

plt.bar(y_pos, Number_Of_Medals, align='center', alpha=0.5)
plt.xticks(y_pos, Country)
plt.ylabel('Number_Of_Medals')
plt.xlabel('Country')
plt.title('Number Of Medals won by Germany and USA')

plt.legend(
            title="Germany VS USA",
            loc="upper right",
            bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()