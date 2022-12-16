import os 
import json
import paho.mqtt.client as mqtt
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from dotenv import load_dotenv

from model import PhoneGeo

load_dotenv()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(mqtt_topic)

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    obj = str(msg.payload)[2:-1]
    
    print(obj)
    print('converting to json')
    obj = json.loads(obj)
    print('got json')

    pg = PhoneGeo()
    pg.latitude=obj['latitude']
    pg.longitude=obj['longitude']
    pg.name=obj['device_name']
    pg.device_id=obj['device_id']
    pg.timestamp=obj['timestamp']
    pg.speed=obj['speed']
    pg.event_ts = obj['event_ts']
    res = session.add(pg)
    print(f'add pg {pg}: res {res}')
    session.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

mqtt_server = os.getenv('MQTT_SERVER')
mqtt_user = os.getenv('MQTT_USER')
mqtt_password = os.getenv('MQTT_PASSWORD')
mqtt_topic = os.getenv('MQTT_TOPIC')
db_conn = os.getenv('DB_CONN')

client.username_pw_set(os.getenv('MQTT_USER'),os.getenv('MQTT_PASSWORD'))
client.connect(os.getenv('MQTT_SERVER'), 1883, 60)

print('Create database connection')
engine = create_engine(db_conn, pool_recycle=3600)
session = Session(engine)
client.loop_forever()