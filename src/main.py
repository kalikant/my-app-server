from fastapi import FastAPI, Depends, HTTPException, WebSocket, WebSocketDisconnect, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database, onboarding
from fastapi.middleware.cors import CORSMiddleware
from io import StringIO
import csv
from pydantic import BaseModel

app = FastAPI()

# CORS settings
origins = [
    "http://localhost:3000",  # Add your frontend URL here
    # Add other origins if necessary
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Simulated LDAP user database
mock_ldap_users = {
    "admin_user": {
        "username": "admin_user",
        "password": "admin_pass",
        "role": "admin"
    },
    "regular_user": {
        "username": "regular_user",
        "password": "user_pass",
        "role": "user"
    }
}

# Pydantic model for login request
class AuthRequest(BaseModel):
    username: str
    password: str

# Pydantic model for login response
class AuthResponse(BaseModel):
    username: str
    role: str

# Mocked LDAP authentication endpoint
@app.post("/api/authenticate", response_model=AuthResponse)
def authenticate(auth: AuthRequest):
    user = mock_ldap_users.get(auth.username)
    
    if not user or user["password"] != auth.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"username": user["username"], "role": user["role"]}

# Initialize the database
@app.on_event("startup")
def on_startup():
    database.init_db()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = onboarding.create_user(db=db, user=user)
    return db_user

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = onboarding.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = onboarding.get_users(db, skip=skip, limit=limit)
    return users

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = onboarding.update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = onboarding.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/incomplete-users-setup", response_model=List[schemas.User])
def get_incomplete_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return onboarding.get_incomplete_users(db, skip=skip, limit=limit)


@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    
    content = await file.read()
    decoded_content = content.decode('utf-8')
    reader = csv.DictReader(StringIO(decoded_content))
    
    users = []
    for row in reader:
        try:
            user = models.User(**row)
            users.append(user)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error parsing CSV data: {e}")

    # Here you would typically save the data to the database
    # For example:
    # async with async_session() as session:
    #     async with session.begin():
    #         session.add_all(users)
    
    return {"message": "CSV data uploaded successfully", "users": [user.dict() for user in users]}

class ChartData(BaseModel):
    name: str
    value: int

class LineData(BaseModel):
    name: str
    uv: int

@app.get("/api/server-usage-analysis", response_model=List[ChartData])
def get_server_usage_analysis():
    dummy_data = [
        {"name": "High Usage", "value": 400},
        {"name": "Medium Usage", "value": 300},
        {"name": "Low Usage", "value": 300},
        {"name": "No Usage", "value": 200},
    ]
    return dummy_data

@app.get("/api/user-onboarding-trend", response_model=List[LineData])
def get_user_onboarding_trend():
    dummy_data = [
        {"name": "Apr", "uv": 400},
        {"name": "May", "uv": 300},
        {"name": "Jun", "uv": 200},
        {"name": "Jul", "uv": 278},
        {"name": "Aug", "uv": 189},
        {"name": "Sep", "uv": 239},
        {"name": "Oct", "uv": 349},
        {"name": "Nov", "uv": 430},
        {"name": "Dec", "uv": 400},
    ]
    return dummy_data
