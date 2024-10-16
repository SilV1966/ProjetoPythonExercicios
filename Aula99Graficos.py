# Este programa cria um gráfico com uma barra de calor mostrando as taxas de desemprego no País
# É necessário importar as bibliotecas Folium e Pandas no Python com o pip install
# Caso contrário não funcionará
# os arquivos br_stares.jasom e o arquivo taxa_desemprego_br.csv precisam estar no diretório do projeto


import folium
#print(folium.__version__)
    width=600,height=400,
    location=[-15.77972, -47.92972], 
    zoom_start=3
)
folium.GeoJson(
    geo_json_data,
    style_function=lambda feature: {
        'fillColor': 'green',
        'color': 'darkred',
        'weight': 0.5,
    }
).add_to(mapa)
mapa
import pandas as pd

desemprego_br = pd.read_csv('taxa_desemprego_br.csv', sep=';', decimal=',', usecols=['Sigla', '4º trimestre 2018'])

desemprego_br.rename(columns={
     'Sigla': 'estado', 
     '4º trimestre 2018': '2018'}, inplace=True)
desemprego_br.head(3)
desemprego_br.describe()
from branca.colormap import linear

colormap = linear.YlOrRd_09.scale(6,20)
colormap
desemprego_br_2018 = desemprego_br.set_index('estado')['2018']
mapa = folium.Map(
    width=600, height=400,
    location=[-15.77972, -47.92972], 
    zoom_start=4
)
folium.GeoJson(
    geo_json_data,
    name='2018',
    style_function=lambda feature: {
        'fillColor': colormap(desemprego_br_2018[feature['id']]),
        'color': 'black',
        'weight': 0.3,
    }
    
).add_to(mapa)
colormap.caption = 'Taxa de desemprego no Brasil 2018'
colormap.add_to(mapa)
folium.LayerControl(collapsed=False).add_to(mapa)
mapa.save('taxa_br_2018.html')
mapa
