#!/bin/bash
#
# Tapo P110 -> InfluxDB Collection Script
#
# Run with cron on whatever update rate you want
#

# Enter the hostname of your Tapo P110 device here
export TAPO_HOST=""
# Tapo account login details - use a unique password as this is all in plaintext!
export TAPO_USER=""
export TAPO_PASSWORD=""


# InfluxDB Settings
export INFLUXDB_URL="http://localhost:8086"
export INFLUXDB_TOKEN=""
export INFLUXDB_ORG=""
export INFLUXDB_BUCKET=""
export INFLUXDB_MEASNAME=""

# Use a local venv if it exists
VENV_DIR=venv
if [ -d "$VENV_DIR" ]; then
    echo "Entering venv."
    source $VENV_DIR/bin/activate
fi

python3 tapo_collect.py
