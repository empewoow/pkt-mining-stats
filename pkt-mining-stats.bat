@echo off
@echo Starting address_stats
start cmd /k "python get_address_stats.py"
@echo Starting pool_stats
start cmd /k "python get_pool_stats.py"
@echo Starting webserver
start cmd /k "python pkt-mining-stats.py"
@echo Services started - this window will be closed
Pause
