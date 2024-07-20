from sqlalchemy import Column, Integer, String, Boolean, Text, Date, DateTime, create_engine, engine, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date
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
    date = Column(Date, default=date.today)  # Set the default value to the system date
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

class Cluster(Base):
    __tablename__ = "clusters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.utcnow)

class ServerUsage(Base):
    __tablename__ = "server_usages"

    id = Column(Integer, primary_key=True, index=True)
    cluster_id = Column(Integer, ForeignKey('clusters.id'))
    cpu_usage = Column(String, index=True)
    memory_usage = Column(String, index=True)
    storage_usage = Column(String, index=True)
    created_date = Column(DateTime, default=datetime.utcnow)

    cluster = relationship("Cluster", back_populates="server_usages")

class OnlineUser(Base):
    __tablename__ = "online_users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    cluster_id = Column(Integer, ForeignKey('clusters.id'))
    online_time = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="online_users")
    cluster = relationship("Cluster", back_populates="online_users")

class LiveApplication(Base):
    __tablename__ = "live_applications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    cluster_id = Column(Integer, ForeignKey('clusters.id'))
    created_date = Column(DateTime, default=datetime.utcnow)

    cluster = relationship("Cluster", back_populates="live_applications")

Cluster.server_usages = relationship("ServerUsage", order_by=ServerUsage.id, back_populates="cluster")
Cluster.online_users = relationship("OnlineUser", order_by=OnlineUser.id, back_populates="cluster")
Cluster.live_applications = relationship("LiveApplication", order_by=LiveApplication.id, back_populates="cluster")
User.online_users = relationship("OnlineUser", order_by=OnlineUser.id, back_populates="user")

# Create the tables in the database
# Base.metadata.create_all(bind=engine)