# Iterating through Pandas Dataframe.

import pandas as pd

student_scores = {
    "student": ["Lizzy", "Sheena", "Ezra"],
    "score": [60, 80, 10]
}

student_df = pd.DataFrame(student_scores)

for (index, row) in student_df.iterrows():
    if row.student == 'Ezra':
        print('Ogomunanasi, how has been the day my dear friend')