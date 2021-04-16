import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Participants/output.csv")

df = pd.DataFrame(data, columns = data.columns)

p1 = df[df['Filename'] == 'participant1']
p2 = df[df['Filename'] == 'participant2']
p3 = df[df['Filename'] == 'participant3']
p4 = df[df['Filename'] == 'participant4']

participants = [p1, p2, p3, p4]

for p in participants:
    labels = p['Label'].unique()
    name_p = p['Filename'].unique()
    name_p = name_p[0]
    sents = []
    for l in labels:
        temp = p[df['Label'] == l]
        # replacing undefined values with np.nan
        temp['f0'] = temp['f0'].replace('--undefined--', np.nan)
        # # forward fill na
        # temp = temp.fillna(method='ffill')
        # # back fill na
        # temp = temp.fillna(method='bfill')
        # make sure the type is float
        temp['f0'] = temp['f0'].astype(float)
        temp.plot(x="time", y="f0")

        # saving plot
        f_name = "Participants/plots/" + name_p + "/" + l
        plt.savefig(f_name)

