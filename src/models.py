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
    purpose = Column(Text)
    mrm_policy_1 = Column(Boolean, default=False)
    mrm_policy_2 = Column(Boolean, default=False)
    mrm_policy_3 = Column(Boolean, default=False)
    mrm_policy_4 = Column(Boolean, default=False)
    mrm_policy_5 = Column(Boolean, default=False)
    notice_2 = Column(Boolean, default=False)
    vault_config = Column(Text, default="")
    databases = Column(Text, default="")
    custom_profile = Column(Boolean, default=False)
    s3_buckets = Column(Text, default="")
    s3_buckets_access_list = Column(Text, default="")
    quartz_access = Column(Boolean, default=False)
    comments = Column(Text, default="")
    isUserSetupCompleted = Column(Boolean, default=False)
