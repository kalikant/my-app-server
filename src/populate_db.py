from sqlalchemy.orm import Session
from datetime import datetime
from models import Base, engine, User, Cluster, ServerUsage, OnlineUser, LiveApplication

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize session
session = Session(bind=engine)

# Dummy data for Users
users = [
    User(
        first_name="John",
        last_name="Doe",
        standard_id="JD123",
        email="john.doe@example.com",
        team="Team A",
        purpose="Testing",
        mrm_policy_1=True,
        mrm_policy_2=False,
        mrm_policy_3=True,
        mrm_policy_4=False,
        mrm_policy_5=True,
        notice_2=True,
        vault_config="Config A",
        databases="DB1",
        custom_profile=False,
        s3_buckets="Bucket1",
        s3_buckets_access_list="Access1",
        quartz_access=True,
        comments="No comments"
    ),
    User(
        first_name="Jane",
        last_name="Smith",
        standard_id="JS456",
        email="jane.smith@example.com",
        team="Team B",
        purpose="Development",
        mrm_policy_1=False,
        mrm_policy_2=True,
        mrm_policy_3=False,
        mrm_policy_4=True,
        mrm_policy_5=False,
        notice_2=False,
        vault_config="Config B",
        databases="DB2",
        custom_profile=True,
        s3_buckets="Bucket2",
        s3_buckets_access_list="Access2",
        quartz_access=False,
        comments="Test comments"
    )
]

# Dummy data for Clusters
clusters = [
    Cluster(name="Cluster1", status="Active"),
    Cluster(name="Cluster2", status="Inactive")
]

# Dummy data for ServerUsage
server_usages = [
    ServerUsage(cluster_id=1, cpu_usage="70%", memory_usage="65%", storage_usage="80%"),
    ServerUsage(cluster_id=2, cpu_usage="50%", memory_usage="55%", storage_usage="60%")
]

# Dummy data for OnlineUsers
online_users = [
    OnlineUser(user_id=1, cluster_id=1, online_time=datetime.utcnow()),
    OnlineUser(user_id=2, cluster_id=2, online_time=datetime.utcnow())
]

# Dummy data for LiveApplications
live_applications = [
    LiveApplication(name="App1", status="Running", cluster_id=1),
    LiveApplication(name="App2", status="Stopped", cluster_id=2)
]

# Add all data to the session and commit
session.add_all(users + clusters + server_usages + online_users + live_applications)
session.commit()

# Close the session
session.close()
