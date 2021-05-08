#!/bin/bash

pkill -f get_address_stats.py
pkill -f get_pool_stats.py
pkill -f pkt-mining-stats.py

#mv nohup.out logs/$(date +%F-%H-%M).log

nohup python3 get_pool_stats.py > get_pool_stats.log 2>&1 &
nohup python3 get_address_stats.py > get_address_stats.log 2>&1 &
nohup python3 pkt-mining-stats.py > pkt-mining-stats.log 2>&1 &

echo "(Re)started PKT-mining-stats."
