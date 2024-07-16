# src/schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    standard_id: str
    email: str
    team: str
    purpose: str
    mrm_declaration: bool = False
    unixuser: bool = False
    jupyter_access: bool = False
    hdfs_access: bool = False
    jupyter_config: str
    vault_config: str
    databases: str
    custom_profile: bool = False
    s3_buckets: str
    s3_buckets_access_list: str
    quartz_access: bool = False
    comments: str
    isUserSetupCompleted: bool = False  # New field

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
