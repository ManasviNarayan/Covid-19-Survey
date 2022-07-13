print('importing libraries...')

from jinja2 import Environment, FileSystemLoader
import pandas as pd

print('processing...')
env = Environment(loader=FileSystemLoader('templates'))

template = env.get_template('template.html')

df = pd.read_csv('Responses (1).csv')

print('creating dashboard ...')
board = template.render(title='Covid-19 Survey',
                        df = df)


with open('templates/index.html', 'w') as f:
    f.write(board)
print('done!')