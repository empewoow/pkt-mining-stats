# PKT mining statistics

View statisctics of your miner(s) such as encryptions/s, MB/s, warmup percentage and credits percentage on your PKT address(es).

I started this project because I was tired of visiting the whotopay JSON files of the pools and searching for my PKT address manually... I hope you like it just as much as I do!

## Screenshot

![Screenshot of PKT mining statisctics](/docs/pkt-mining-stats-screenshot.png?raw=true)

## Configuration

Configure these files first (they work by default):

* `addresses.json` (To add the PKT addresses you want to monitor)
* `pools.json` (To add/modify the pool URLs)
* `settings.py` (To change ip/port settings of your web application.)

## Prerequisites

Tested on Linux and Windows

Prerequisites:

* [Python3]https://www.python.org/downloads/
* dash
* pandas
* requests

## Installing

Get Python and get the required packages:

```
pip install requests

pip install dash

pip install pandas
```

(Possibly you need to use `pip3` instead of `pip`.)

## Running

### Linux
Once configured, on Linux you can run `./pkt-mining-stats.sh` to run all the scripts. It basically runs these three scripts in the background:

* `get_address_stats.py` (To get the statistics for your PKT addresses every 10 minutes.)
* `get_pool_stats.py` (To get additional statistics of all pools every 1 hour.)
* `pkt-mining-stats.py` (To run the web application.)

So what you can also do manually:

```
python get_address_stats.py
python get_pool_stats.py
python pkt-mining-stats.py
```
(Run them in 3 different terminals.)

### Windows

Run `pkt-mining-stats.bat`

Or, start the services manually via command prompt:

```
start cmd /k "python get_address_stats.py"
start cmd /k "python get_pool_stats.py"
start cmd /k "python pkt-mining-stats.py"
```

### Opening the webinterface
Once it runs, visit <http://localhost:8050> (or whatever you configured in `setings.py`).
Ignore the errors the first time you visit the page. Select your PKT address and start monitoring!

If prompted with an SSL error. Try accessing in incognito mode.
Make sure to access the page with http:// and not https://

By default the graphs display the last 2 days.

## Built with

* [Dash](https://plotly.com/dash/) - To make nice graphs :)

## Contributing

Please contribute! You can also contact me.

## Versions

Not yet applicable.

## Authors

* **Matthijs** - *Initial work*

## License

This project is licensed under the MIT License.

## Acknowledgments

* None yet.
