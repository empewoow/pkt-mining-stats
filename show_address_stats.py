import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

from app import app
from settings import *

# https://stackoverflow.com/questions/60172150/dash-python-how-to-fill-dcc-dropdown-with-csv-content
# https://stackoverflow.com/questions/48614158/read-json-file-as-pandas-dataframe
# 

address_stats_csv_file = 'address_stats/address_stats.csv'

datetime_range_from = 0
datetime_range_to = 0

def get_current_datetime_range():
	global datetime_range_from, datetime_range_to
	# Generate graph from last 48 hours:
	date_to = datetime.now()
	date_from = date_to - timedelta(days = timeScale)
	datetime_range_from = date_from.strftime("%Y-%m-%d %H:%M")
	datetime_range_to = date_to.strftime("%Y-%m-%d %H:%M")

addresses_json_file_path = 'addresses.json'
df = pd.read_json(addresses_json_file_path)
addresses = df['addresses'].unique()
my_options = [{'label': address, 'value': address} for address in addresses]

get_current_datetime_range()

layout = html.Div([
	html.H2('PKT address statistics'),
	dcc.Link('View PKT pool statistics', href = '/pool_stats'),
	#html.Button("Test", id = 'btn', n_clicks = 0),
	html.Div([
		html.H4('Choose PKT address:'),
		dcc.Dropdown(
			id = 'my_dropdown',
			options = my_options,
			optionHeight = 35,					#height/space between dropdown options
			value = '',	#dropdown value selected automatically when page loads
			disabled = False,					 #disable dropdown value selection
			multi = False,						#allow multiple dropdown values to be selected
			searchable = True,					#allow user-searching of dropdown values
			search_value = '',					#remembers the value searched in dropdown
			placeholder = 'Please select...',	 #gray, default text shown when no option is selected
			clearable = True,					 #allow user to removes the selected value
			persistence = True,				 #remembers dropdown value. Used with persistence_type
			persistence_type = 'session'		 #remembers dropdown value selected until...
		)
		],
		style={"width": "500px"},
	),
	dcc.Graph(id="graph1"),
	dcc.Graph(id="graph2"),
	dcc.Graph(id="graph3"),
	dcc.Graph(id="graph4"),
	dcc.Interval(
		id = 'graph-update',
		interval = 4 * 60 * 1000, # Refresh every 4 minutes
		n_intervals = 0
	)
])

@app.callback(
	Output("graph1", "figure"),
	[Input('graph-update', 'n_intervals')],
	[Input(component_id = 'my_dropdown', component_property = 'value')]
)
def display_graph1(n_intervals, pktAddressToUse):
	if not pktAddressToUse: return {}
	dataframe = pd.read_csv(address_stats_csv_file)
	dataframe = dataframe[dataframe['pktAddress'] == pktAddressToUse]
	x, y = 'date', 'currentEncryptionsPerSecond'
	get_current_datetime_range()
	fig = px.line(dataframe, x = x, y = y, color = 'pool', title = "Encryptions per second (Ke/s)", range_x = [datetime_range_from, datetime_range_to])	
	return fig

@app.callback(
	Output("graph2", "figure"),
	[Input('graph-update', 'n_intervals')],
	[Input(component_id = 'my_dropdown', component_property = 'value')]
)
def display_graph2(n_intervals, pktAddressToUse):
	if not pktAddressToUse: return {}
	dataframe = pd.read_csv(address_stats_csv_file)
	dataframe = dataframe[dataframe['pktAddress'] == pktAddressToUse]
	x, y = 'date', 'kbps'
	get_current_datetime_range()
	fig = px.line(dataframe, x = x, y = y, color = 'pool', title="Bandwidth (MB/s)", range_x = [datetime_range_from, datetime_range_to])	
	return fig

@app.callback(
	Output("graph3", "figure"),
	[Input('graph-update', 'n_intervals')],
	[Input(component_id = 'my_dropdown', component_property = 'value')]
)
def display_graph3(n_intervals, pktAddressToUse):
	if not pktAddressToUse: return {}
	dataframe = pd.read_csv(address_stats_csv_file)
	dataframe = dataframe[dataframe['pktAddress'] == pktAddressToUse]
	x, y = 'date', 'warmupPercent'
	get_current_datetime_range()
	fig = px.line(dataframe, x = x, y = y, color = 'pool', title="Warmup (%)", range_x = [datetime_range_from, datetime_range_to])	
	return fig

@app.callback(
	Output("graph4", "figure"),
	[Input('graph-update', 'n_intervals')],
	[Input(component_id = 'my_dropdown', component_property = 'value')]
)
def display_graph4(n_intervals, pktAddressToUse):
	if not pktAddressToUse: return {}
	dataframe = pd.read_csv(address_stats_csv_file)
	dataframe = dataframe[dataframe['pktAddress'] == pktAddressToUse]
	x, y = 'date', 'credits'
	get_current_datetime_range()
	fig = px.line(dataframe, x = x, y = y, color = 'pool', title="Credits", range_x = [datetime_range_from, datetime_range_to])	
	return fig

