from sqlalchemy import Column, Integer, String, Boolean, Text
from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    standard_id = Column(String, index=True)
    email = Column(String, index=True)
    team = Column(String, index=True)
    purpose = Column(String)
    mrm_declaration = Column(Boolean, default=False)
    unixuser = Column(Boolean, default=False)
    jupyter_access = Column(Boolean, default=False)
    hdfs_access = Column(Boolean, default=False)
    jupyter_config = Column(Text)
    vault_config = Column(Text)
    databases = Column(Text)
    custom_profile = Column(Boolean, default=False)
    s3_buckets = Column(Text)
    s3_buckets_access_list = Column(Text)
    quartz_access = Column(Boolean, default=False)
    comments = Column(Text)
    isUserSetupCompleted = Column(Boolean, default=False)
