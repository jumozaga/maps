import plotly.graph_objs as go

# Dados dos estados e capitais
estados = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 
'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RO', 'RS', 'RR', 'SC', 
'SP', 'SE', 'TO']

capitais = [
 'Rio Branco', 'Maceió', 'Manaus', 'Macapá', 'Salvador',
 'Fortaleza', 'Brasília', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 
 'Campo Grande', 'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 
 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Velho', 
 'Porto Alegre', 'Boa Vista', 'Florianópolis', 'São Paulo', 
 'Aracaju', 'Palmas'
]

latitudes = [
-8.77, -9.62, -3.47, 0.038, -12.97, -3.71, -15.83, -20.32, -16.64,
 -2.55, -15.61, -20.51, -19.81, -1.46, -7.06, -25.42, -8.05, -5.09, -22.91,
 -5.78, -8.76, -30.01, 2.82, -27.33, -23.55, -10.90, -10.25
]

longitudes = [-70.55, -35.73, -65.10, -51.05, -38.51, -38.54, -47.86, -40.34,
 -49.31, -44.30, -56.10, -54.54, -43.94, -48.48, -34.87, -49.25, -34.88,-42.81,
  -43.17, -36.56, -63.90, -51.22, -60.67, -48.55, -46.63, -37.07, -37.77
]

# Informações do clima para cada capital
temperaturas = [29, 26, 33, 29, 28, 31, 25, 27, 30, 32, 31, 32, 26, 30, 28, 24,
 28, 33, 27, 31, 28, 24, 32, 23, 25, 31, 27]

# Criação do mapa
fig = go.Figure()

# Adiciona a geografia do Brasil
fig.add_trace(go.Scattergeo(
    locationmode = 'ISO-3',
    lon = [-51.9253, -47.9292, -44.3060, -41.6862, -39.3200, -38.4803, 
    -38.5283,-37.0475, -43.2775, -54.7041, -57.6531, -46.6333, -44.0059,
    -48.0777, -51.9253],
    lat = [-14.2350, -15.7801, -5.7940, -3.0742, -12.9777, -3.7167, -15.7797,
     -19.9208, -16.6869, -2.5307, -13.5319, -20.4428, -18.5122, -1.4558,
     -7.1195, -25.4284,-8.0557, -5.0892, -22.9035, -5.7947, -10.9472, 
     -30.0277, 1.8394, -27.5935,-30.0277, -23.5505, -10.3333],
    hoverinfo = 'text',
    text = estados,
    mode = 'lines',
    line = dict(width = 2, color = 'black'),))
    
#Adiciona os marcadores de cada capital
for i in range(len(capitais)):
	fig.add_trace(go.Scattergeo(
		locationmode = 'ISO-3',
		lon = [longitudes[i]],
		lat = [latitudes[i]],
		hoverinfo = 'text',
		text = capitais[i] + '<br>' + str(temperaturas[i]) + '°C',
		mode = 'markers',
		marker = dict(
		size = 8,
		color = 'red',
		line = dict(width = 1, color = 'black'))))

#Configurações do layout
fig.update_layout(
	title = dict(text = 'Mapa do Brasil 3D com Capitais e Clima', x = 0.5),
	geo = dict(
	scope = 'south america',
	showland = True,
	landcolor = 'rgb(217, 217, 217)',
	showcountries = True,
	countrycolor = 'rgb(255, 255, 255)',
	showocean = True,
	oceancolor = 'rgb(204, 204, 204)',
	projection = dict(type = 'orthographic', rotation = dict(lon = -60, 
		lat = -10, roll = 0)),
	lonaxis = dict(showgrid = True, gridcolor = 'rgb(102, 102, 102)'),
	lataxis = dict(showgrid = True, gridcolor = 'rgb(102, 102, 102)'),
)
)


#Exibe o mapa
fig.show()

