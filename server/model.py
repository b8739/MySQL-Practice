from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'NewDatabase'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}

    user_id = Column(String(30), primary_key=True, unique=True)
    user_name = Column(String(30))
    profile_url = Column(String(100))

    def __init__(self, user_id, user_name, profile_url):
        self.user_id = user_id
        self.user_name = user_name
        self.profile_url = profile_url

    def __repr__(self):
        return 'user_id : %s, user_name : %s, profile_url : %s' % (self.user_id, self.user_name, self.profile_url)

    def as_dict(self):
        return {x.name: getattr(self, x.name) for x in self.__table__.columns}

