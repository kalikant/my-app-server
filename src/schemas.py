# src/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class UserBase(BaseModel):
    first_name: str
    last_name: str
    standard_id: str
    email: EmailStr
    team: str
    purpose: str
    mrm_policy_1: bool
    mrm_policy_2: bool
    mrm_policy_3: bool
    mrm_policy_4: bool
    mrm_policy_5: bool
    notice_2: bool
    vault_config: Optional[str] = ""
    databases: Optional[str] = ""
    custom_profile: bool
    s3_buckets: Optional[str] = ""
    s3_buckets_access_list: Optional[str] = ""
    quartz_access: bool
    comments: Optional[str] = ""
    isUserSetupCompleted: bool = False  # New field

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    date: date

    class Config:
        orm_mode = True
