import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from settings import *
from app import app
import show_pool_stats, show_address_stats

app.layout = html.Div([
	dcc.Location(id = 'url', refresh = False),
	html.Div(id = 'page-content')
])

@app.callback(Output('page-content', 'children'),
	Input('url', 'pathname'))
def display_page(pathname):
	if pathname == '/pool_stats':
		return show_pool_stats.layout
	elif pathname == '/address_stats':
		return show_address_stats.layout
	else:
		return show_address_stats.layout # '404'

if __name__ == '__main__':
	app.run_server(debug = True, host = myHost, port = myPort)