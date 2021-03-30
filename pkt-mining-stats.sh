#!/bin/bash

killall -9 python3

#mv nohup.out logs/$(date +%F-%H-%M).log

nohup python3 get_pool_stats.py > get_pool_stats.log 2>&1 &
nohup python3 get_address_stats.py > get_address_stats.log 2>&1 &
nohup python3 pkt-mining-stats.py > pkt-mining-stats.log 2>&1 &

echo "(Re)started PKT-mining-stats."
