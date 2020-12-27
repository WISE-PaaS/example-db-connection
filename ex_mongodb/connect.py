import os
import json

from pymongo import MongoClient

def testMongo():
    # Load 'ENSAAS_SERVICES' from enviroment variable and parse the URI
    ensaas_services = os.getenv('ENSAAS_SERVICES')
    ensaas_services = json.loads(ensaas_services)
    try:
        mongo_database = ensaas_services['mongodb'][0]['credentials']['database']
        mongo_host1 = ensaas_services['mongodb'][0]['credentials']['host1']
        mongo_port1 = ensaas_services['mongodb'][0]['credentials']['port1']
        mongo_user = ensaas_services['mongodb'][0]['credentials']['username']
        mongo_password = ensaas_services['mongodb'][0]['credentials']['password']
        mongo_uri = 'mongodb://' + mongo_user + ':' + mongo_password + '@' + ensaas_services['mongodb'][0]['credentials']['externalHosts'] + '/' + mongo_database
    except:
        return "Cannot get MongoDB credentials from $ENSAAS_SERVICES environment variable!"

    try:
        client = MongoClient(mongo_uri)
    except:
        return "Unable to connect to MongoDB instance!"
    db = client.get_default_database()
    # Issue the dbStats command and print the results
    dbStatsResult = db.command("dbStats")
    print(dbStatsResult)
    client.close()
    return dbStatsResult
