import pandas as pd
import charts


def run():
    df =pd.read_csv('data.csv')
    df = df[df['Continet']=='Africa']

    countries=df['Country'].values
    percentages = df['World Population Percentage'].values
    charts.generate