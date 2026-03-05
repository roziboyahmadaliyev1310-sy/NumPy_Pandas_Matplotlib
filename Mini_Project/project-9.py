# This code visalization of the cleaned dataset of universities of United State.
# I created diffrent types of charts according to dataset features.
# I alse used subplots to show multiple charts in one figure for better comparision
# and understanding of the data distribution and relationships between features.
# Different chart types [bar, histogram], but i mainly used hist, because it ia more 
# suitible foe showing distribution of numerical data.





import pandas as pd

df=pd.read_csv("/Users/akhmadalievruziboy/Desktop/GitHub/NumPy/universities_cleaned.csv")

# This dataset was already cleaned in project-6, so we can directly visualize it.

import matplotlib.pyplot as plt

fig=plt.figure(figsize=(20,10))

# institutions types
univer_types=df["institution_type"].value_counts()
plt.subplot(2,2,1)
univer_types.plot(kind='bar')
plt.title('Distribution of Institution types', fontsize=14, 
                                                fontweight='bold',
                                                pad=20,color='blue')
plt.ylabel('Count', fontsize=12, 
                    fontweight='bold',
                    color='green',
                    labelpad=7)
plt.xlabel('Institution Type', fontsize=12,
                    fontweight='bold',
                    color='green')

# states ditribution
state_counts=df['state'].value_counts().head(10)
plt.subplot(2,2,2)
state_counts.plot(kind='bar', color='orange')
plt.title('Top 10 States by Number of Universities', fontsize=14,
                                                color='blue',
                                                fontweight='bold',
                                                pad=20)
plt.xlabel('State', fontsize=12,
                    color='green',
                    fontweight='bold')
plt.ylabel('Number of Universities', fontsize=12,
                                      color='green',
                                      fontweight='bold')


# research_impact_score distribution
plt.subplot(2,2,3)
plt.hist(df['research_impact_score'], bins=20,color='purple', edgecolor='black')
plt.title('Distribution of Research Impact Scores', fontsize=14,
                                                color='blue',
                                                fontweight='bold',
                                                pad=20)
plt.xlabel('Research Impact score', fontsize=12,
                                      color='green',
                                      fontweight='bold')
plt.ylabel('Frequency', fontsize=12,
                        fontweight='bold',
                        color='green')

plt.subplot(2,2,4)
plt.hist(df['employment_rate'], bins=20, color='cyan', edgecolor='black')
plt.title('Distribution of Employment Rates', fontsize=14,
                                                color='blue',
                                                fontweight='bold',
                                                pad=20)
plt.xlabel('Employment Rate (%)', fontsize=12,
                                      color='green',
                                      fontweight='bold')
plt.ylabel('Frequency', fontsize=12,
                        fontweight='bold',
                        color='green')

plt.tight_layout()
plt.show()