import json
import plotly.graph_objs as go
import plotly.offline as pyo
#import dash
#import dash_core_components as dcc
from dash import Dash, html, dcc
import pandas as pd
import urllib.request

#source = pd.read_csv(https://github.com/codeforamerica/click_that_hood/blob/master/public/data/brazil-states.geojson)
# Downloading the JSON file from the remote server
url = 'https://raw.githubusercontent.com/codeforgermany/click_that_hood/main/public/data/brazil-states.geojson'
urllib.request.urlretrieve(url, 'brazil-states.geojson')

# Carregando o arquivo JSON com os dados do mapa do Brasil
with open('brazil-states.geojson') as f:
    brazil_states = json.load(f)

# Criando o objeto de layout para o mapa
layout = go.Layout(
    title='Mapa do Brasil',
    geo=dict(
        scope='south america',
        showlakes=True,
        lakecolor='rgb(255, 255, 255)'
    ),
)

# Criando o objeto de figura usando o objeto de layout e o arquivo JSON do mapa
fig = go.Figure(layout=layout)
fig.add_trace(
    go.Choroplethmapbox(
        geojson=brazil_states,
        locations=['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'],
        z=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
        colorscale='Viridis',
        zmin=1,
        zmax=26,
        marker=dict(opacity=0.5),
        colorbar=dict(title='Estados')
    )
)

# Renderizando a figura usando a biblioteca Dash
#app = dash.Dash(__name__)
app = Dash(__name__)
app.layout = dcc.Graph(figure=fig)
if __name__ == '__main__': 
    app.run_server(debug=True)  
#    app.config['FLASK_DEBUG'] = True
    


