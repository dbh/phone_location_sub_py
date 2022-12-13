# Phone Loc Sub Writer

# Input from config / environment

|Variable|Example|Description|
|-|-|-|
|MQTT_SERVER|mqtt.example.com| Server FQDN|
|MQTT_USER|dbh|User Name|
|MQTT_PASSWORD|NOT_REALLY|PW |
|MQTT_TOPIC|MY_TOPIC|Topic|
|DB_CONN|mysql://\<user\>:\<password\>@\<host\>[:\<port\>]/\<dbname\>|Connection URL for DB|



Database schema
```sql
DROP TABLE phone_geo;
CREATE TABLE phone_geo (
    id INT NOT NULL AUTO_INCREMENT
    , name varchar(255)
    , device_id varchar(255)
    , timestamp BIGINT
    , event_ts TIMESTAMP
    , latitude DECIMAL(10,8)
    , longitude DECIMAL(11,8) 
    , speed DECIMAL(5,2)
    , CONSTRAINT PRIMARY KEY (ID)
);
```

Run it
```bash
python -m pip install -r requirements.txt
nohup python phone_location_sub_py/sub_and_write.py & 

```
