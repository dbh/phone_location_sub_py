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
    event_ts = Column(TIMESTAMP)
    speed = Column(DECIMAL(5,2))

    def __repr__(self):
        return "<phone_geo(name='%s', device_id='%s', timestamp='%s', event_ts='%s' latitude='%s', longitude='%s' speed='%s')>" % (
            self.name,
            self.device_id,
            self.timestamp,
            self.event_ts,
            self.latitude,
            self.longitude,
            self.speed
        )
