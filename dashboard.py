print('importing libraries...')

from jinja2 import Environment, FileSystemLoader
import pandas as pd
import plotly.express as px

print('processing...')
env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('template.html')

df = pd.read_csv('Responses (1).csv')
length = len(df.columns)
def student():
    dict_ ={}
    pass

class working():
    def preprocessing():
        work=pd.read_csv('working.csv')
        return work

    def graphs(work_df):
        age_count=px.histogram(work_df, x="age", color="gender")
        state_counts=px.bar(x=work_df.state.value_counts().index,y=work_df.state.value_counts().values)
        dict_ = {age_count,state_counts}
        

print('creating dashboard ...')
board = template.render(title='Covid-19 Survey',
                        df = df,
                        length = length)


with open('templates/index.html', 'w') as f:
    f.write(board)
print('done!')