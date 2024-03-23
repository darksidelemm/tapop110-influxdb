#!/usr/bin/env python
#
# Tapo P110 to InfluxDB Collection
#
import influxdb_client, os, time
from PyP100 import PyP110, MeasureInterval
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from pprint import pprint

# Collect Environment Variables
TAPO_HOST = os.environ.get("TAPO_HOST")
TAPO_USER = os.environ.get("TAPO_USER")
TAPO_PASSWORD = os.environ.get("TAPO_PASSWORD")
INFLUXDB_URL = os.environ.get("INFLUXDB_URL")
INFLUXDB_TOKEN = os.environ.get("INFLUXDB_TOKEN")
INFLUXDB_ORG = os.environ.get("INFLUXDB_ORG")
INFLUXDB_BUCKET = os.environ.get("INFLUXDB_BUCKET")
INFLUXDB_MEASNAME = os.environ.get("INFLUXDB_MEASNAME")


print(f"Tapo Hostname: \t{TAPO_HOST}")
print(f"Tapo Username: \t{TAPO_USER}")
print(f"Tapo Password: \t{len(TAPO_PASSWORD)} chars")
print(f"InfluxDB URL: \t{INFLUXDB_URL}")
print(f"InfluxDB Token: \t{INFLUXDB_TOKEN}")
print(f"InfluxDB Org: \t{INFLUXDB_ORG}")
print(f"InfluxDB Bucket: \t{INFLUXDB_BUCKET}")
print(f"InfluxDB Measurement Name: \t{INFLUXDB_MEASNAME}")

# Collect Tapo data

p110 = PyP110.P110(TAPO_HOST, TAPO_USER, TAPO_PASSWORD)
energy = p110.getEnergyUsage()

instantaneous_power_w = energy["current_power"]/1000.0 # mW -> W
today_energy_kWh = energy["today_energy"]/1000.0 # Wh -> kWh

print("Tapo Energy Data:")
pprint(energy)

# Push into InfluxDB
write_client = influxdb_client.InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)
write_api = write_client.write_api(write_options=SYNCHRONOUS)

p = influxdb_client.Point(INFLUXDB_MEASNAME).field("instantaneous_power_w", instantaneous_power_w).field("energy_today_kWh", today_energy_kWh)
write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=p)

print("Done!")