#!/bin/bash
python twisted/dumb_json_server.py &
node scripts/web-server.js &

