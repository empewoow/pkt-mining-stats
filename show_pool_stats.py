import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from app import app

pool_stats_csv_file = 'pool_stats/pool_stats.csv'

layout = html.Div([
	html.H2('PKT pool statistics'),
	dcc.Link('View PKT address statistics', href = '/address_stats'),
	dcc.Graph(id = "graph_ann_target"),
	dcc.Interval(
		id = 'graph-update',
		interval = 10*1000, # Refresh every 10 seconds
		n_intervals = 0
	)
])

@app.callback(
	Output('app-1-display-value', 'children'),
	Input('app-1-dropdown', 'value'))
def display_value(value):
	return 'You have selected "{}"'.format(value)

@app.callback(
	Output("graph_ann_target", "figure"),
	[Input('graph-update', 'n_intervals')]
	#[Input(component_id = 'my_dropdown', component_property = 'value')]
)
def display_graph_ann_target(n_intervals):
	dataframe = pd.read_csv(pool_stats_csv_file)
	x, y = 'date', 'annTarget'
	fig = px.line(dataframe, x = x, y = y, color = 'pool', title = "Ann target")	
	return fig