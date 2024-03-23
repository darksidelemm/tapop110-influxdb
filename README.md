# Tapo P110 to InfluxDB Collector
Very quickly developed Tapo P110 to InfluxDB data collector.

## Setup
```
python3 -m venv venv
pip install -r requirements.txt
```

Edit tapo_collect.sh and update env vars with appropriate settings.

Setup crontab to run tapo_collect.sh every minute.

## InfluxDB Stuff
Writes the following fields into the user-defined bucket with the user-defined measurement name:
* `instantaneous_power_w` - Instantaneous Power Measurement in Watts
* `energy_today_kWh` - Today's energy usage in kWh. Resets to 0 at midnight.
