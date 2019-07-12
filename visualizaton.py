import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from knn import *

data= pd.read_json("dataset.json")
final= merge_data(data.to_numpy(), 5)
df= pd.DataFrame(final, columns= ['Openness', 'Conscientiousness', 'Extraversion', 'Agreeableness',
       'Emotional range', 'Challenge', 'Closeness', 'Curiosity', 'Excitement',
       'Harmony', 'Ideal', 'Liberty', 'Love', 'Practicality',
       'Self-expression', 'Stability', 'Structure'])
df["Decision"]= 1
df.iat[-5, -1]= 0
df.iat[-4, -1]= 0
df.iat[-3, -1]= 0
df.iat[-2, -1]= 0
df.iat[-1, -1]= 0
df.iat[0, -1]= 3
df.loc[df.Decision == 0, 'Decision'] = 'Reject'
df.loc[df.Decision == 1, 'Decision'] = 'Accept'
df.loc[df.Decision == 3, "Decision"] = 'Test Data'

b, c = df.iloc[0], df.iloc[7]
temp = df.iloc[0].copy()
df.iloc[0] = c
df.iloc[7] = temp

axes= pd.plotting.parallel_coordinates(
        df, 'Decision',
        color=('green', 'yellow', "red"), lw= 3)
plt.xticks(rotation=90)
plt.rcParams['text.color'] = 'white'
title_obj = plt.title('Parallel Coordinate Graph of Team Trait Breakdown')
plt.setp(title_obj, color='black')
leg= plt.legend(bbox_to_anchor=(1, 1.05))
plt.ylabel("Raw Score")
plt.xlabel("Personality Traits and Needs")
ax = plt.gca()
ax.set_facecolor= "black"
plt.show()