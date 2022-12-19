from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP
from base import Base


class PhoneGeo(Base):
    __tablename__ = "phone_geo"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    device_id = Column(String)
    timestamp = Column(String)
    latitude = Column(DECIMAL(10,8))
    longitude = Column(DECIMAL(11,8))
    speed = Column(DECIMAL(5,2))

    def __init__(self, name, device_id, timestamp, latitude, longitude, speed):
        self.name = name
        self.device_id = device_id
        self.timestamp = timestamp
        self.latitude = latitude
        self.longitude = longitude, 
        self.speed = speed

    def __repr__(self):
        return "<phone_geo(name='%s', device_id='%s', timestamp='%s', latitude='%s', longitude='%s' speed='%s')>" % (
            self.name,
            self.device_id,
            self.timestamp,
            self.latitude,
            self.longitude,
            self.speed
        )
