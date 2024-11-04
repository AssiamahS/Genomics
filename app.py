import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('cancer_genomics.csv')

# Create a scatter plot
fig = px.scatter(df, x='Gene', y='Expression', color='Sample', title='Cancer Genomics Expression Levels')
fig.show()
