import os
import json

from influxdb import InfluxDBClient

def testInflux():
    # Load 'ENSAAS_SERVICES' from enviroment variable and parse the URI
    ensaas_services = os.getenv('ENSAAS_SERVICES')
    ensaas_services = json.loads(ensaas_services)
    try:
        influx_database = ensaas_services['influxdb'][0]['credentials']['database']
        influx_host = ensaas_services['influxdb'][0]['credentials']['externalHosts'][:-5]
        influx_port = ensaas_services['influxdb'][0]['credentials']['port']
        influx_user = ensaas_services['influxdb'][0]['credentials']['username']
        influx_password = ensaas_services['influxdb'][0]['credentials']['password']
    except:
        return "Cannot get InfluxDB credentials from $ENSAAS_SERVICES environment variable!"

    try:
        client = InfluxDBClient(host=influx_host, port=influx_port, username=influx_user, password=influx_password)
    except:
        return "Unable to connect to InfluxDB instance!"
    # Print the list of databases to verify connection
    dbList = client.get_list_database()
    print(dbList)
    client.close()
    return json.dumps(dbList)
