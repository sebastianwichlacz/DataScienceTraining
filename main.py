import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

low_random = [random.randint(0, 7) for _ in range(65)]
medium_random = [random.randint(8, 16) for _ in range(25)]
high_random = [random.randint(17, 36) for _ in range(10)]
timepoint = list(range(1, 101))


data = low_random + medium_random + high_random
data = random.sample(data, len(data))

data1 = {'ResistanceSumD:': data, 'timepoint': timepoint }

df = pd.DataFrame(data1)

sns.relplot(data=df, kind="line", x="timepoint", y=data, err_style="bars", ci="sd")

# Adding labels and title
plt.xlabel('Time')
plt.ylabel('ResistanceSumD')
plt.title('ResistanceSumD over time')

# Show plot
plt.show()