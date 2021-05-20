#!/usr/bin/env python

"""
blocks until a specific time, 
useful for planning to run a script at a specific time
usage: 
til.py tomorrow 9:00 && script.py
"""
import dateparser
from datetime import datetime, timedelta
import time
import argparse

def wait_til_time(run_time):
    tgt = dateparser.parse(run_time)
    print('will run at:', tgt)
    while True:
        now = dateparser.parse('now')
        print('wait for:', tgt - now)
        if tgt < now: break
        time.sleep(10)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Block until run time')
    parser.add_argument('time', type=str, nargs='+')
    args = parser.parse_args()
    run_time = ' '.join(args.time)
    wait_til_time(run_time)
