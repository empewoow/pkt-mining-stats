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

Linux, tested on Ubuntu. Also works on Windows, but there is no batch file yet to start all scripts.

What you need:

* Python3
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

Once configured, on Linux you can run `./pkt-mining-stats.sh` to run all the scripts. It basically runs these three scripts in the background:

* `get_address_stats.py` (To get the statistics for your PKT addresses every 10 minutes.)
* `get_pool_stats.py` (To get additional statistics of all pools every 1 hour.)
* `pkt-mining-stats.py` (To run the web appplication.)

So what you can also do manually:

```
python get_address_stats.py
python get_pool_stats.py
python pkt-mining-stats.py
```
(Run them in 3 different terminals.)

Once it runs, visit <http://localhost:8050> (or whatever you configured in `setings.py`) Ignore the errors the first time you visit the page. Select your PKT address and start monitoring!

By default the graphs display the last 48 hours, it is hardcoded in `show_address_stats.py` on line 22.

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