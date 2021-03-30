import os # and path
from os import path
from time import time, sleep
from datetime import datetime
import requests
import json
import csv

# https://community.plotly.com/t/interval-with-pandas-dataframe/11860/3
# https://www.tutorialspoint.com/downloading-files-from-web-using-python
# https://www.kite.com/python/answers/how-to-check-if-a-string-is-valid-json-in-python
# 

print('Get PKT pool statistics')

json_file_path = 'pool_stats'
csv_filepath = 'pool_stats/pool_stats.csv'

pool_json_file_path = 'pools.json'

if not os.path.exists(json_file_path):
    os.makedirs(json_file_path)

while True:
	now = datetime.now()
	datetime_file = now.strftime("%Y-%m-%d-%H-%M-%S")
	datetime_string = now.strftime("%Y-%m-%d %H:%M:%S") # YYYY-MM-DD hh:mm:ss
	
	print("Loop started at: " + datetime_string)
	
	with open(pool_json_file_path) as pools_json_file:
		
		try:
			pools_data = json.load(pools_json_file)
			
			for pool in range(len(pools_data['pools'])):
			
				currentPool = pools_data['pools'][pool]
				
				pool_name = currentPool['name']
				pool_filepath = json_file_path + "/" + currentPool['filename'] + '-' + datetime_file + '.json'
				pool_config_url = currentPool['config']
		
				#status = wget.download(pool_config_url, pool_filepath)
				#print(status);
				
				try:
					r = requests.get(pool_config_url, allow_redirects = True)
					status = open(pool_filepath, 'wb').write(r.content)
					
					sleep(1);
					
					#print("\n")
					#print("Is it File?" + str(path.isfile(pool_filepath)))
					
					downloadComplete = path.isfile(pool_filepath)
					fileIsNotEmpty = os.path.getsize(pool_filepath) > 0
					
					if downloadComplete and fileIsNotEmpty:
					
						with open(pool_filepath) as json_file:
							
							print('\n')
							print(pool_name);
							
							try:
								data = json.load(json_file)
								
								annTarget = data['annTarget']
								
								print("Ann target: " + str(annTarget))
								
								data_file = open(csv_filepath, 'a', newline = '')
								
								csv_writer = csv.writer(data_file)
								
								csv_writer.writerow(
									[pool_name,
									datetime_string,
									annTarget]
								)
								
								data_file.close()
							except Exception as e:
								print(e)
								print("File contains no proper JSON.")
				except Exception as e:
					print(e)
					print("Download of JSON failed.")
		
		except Exception as e:
			print(e)
			print("Reading pool JSON file failed.")
	
	sleep(60 * 60) # 1 hour