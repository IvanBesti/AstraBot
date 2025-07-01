from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import json
from datetime import datetime
import os

app = FastAPI(title="AstraBot Mock User API", version="1.0.0")

# In-memory storage for users (in real app, this would be a database)
users_db = []

class UserCreateRequest(BaseModel):
    full_name: str
    email: Optional[str] = None
    department: Optional[str] = "IT"

class UserResponse(BaseModel):
    success: bool
    username: str
    password: str
    email: str
    message: str
    user_id: str

@app.get("/")
async def root():
    return {"message": "AstraBot Mock User API", "status": "running"}

@app.post("/create_user", response_model=UserResponse)
async def create_user(user_data: UserCreateRequest):
    """Mock endpoint to create user account"""
    
    # Generate username from full name
    username = user_data.full_name.lower().replace(' ', '.')
    
    # Generate email if not provided
    if not user_data.email:
        email = f"{username}@astra.com"
    else:
        email = user_data.email
    
    # Generate user ID
    user_id = f"USR{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    # Generate password (in real app, this would be more secure)
    password = "Astra2024!"
    
    # Create user object
    user = {
        "user_id": user_id,
        "username": username,
        "full_name": user_data.full_name,
        "email": email,
        "department": user_data.department,
        "password": password,
        "created_at": datetime.now().isoformat(),
        "status": "active"
    }
    
    # Add to in-memory database
    users_db.append(user)
    
    # Save to file for persistence
    save_users_to_file()
    
    return UserResponse(
        success=True,
        username=username,
        password=password,
        email=email,
        message="Akun berhasil dibuat",
        user_id=user_id
    )

@app.get("/users")
async def get_users():
    """Get all users"""
    return {"users": users_db, "count": len(users_db)}

@app.get("/users/{username}")
async def get_user(username: str):
    """Get user by username"""
    for user in users_db:
        if user["username"] == username:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{username}")
async def delete_user(username: str):
    """Delete user by username"""
    global users_db
    original_count = len(users_db)
    users_db = [user for user in users_db if user["username"] != username]
    
    if len(users_db) < original_count:
        save_users_to_file()
        return {"message": f"User {username} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

def save_users_to_file():
    """Save users to JSON file for persistence"""
    os.makedirs("mock_api/data", exist_ok=True)
    with open("mock_api/data/users.json", "w") as f:
        json.dump(users_db, f, indent=2)

def load_users_from_file():
    """Load users from JSON file"""
    global users_db
    try:
        with open("mock_api/data/users.json", "r") as f:
            users_db = json.load(f)
    except FileNotFoundError:
        users_db = []

# Load existing users on startup
load_users_from_file()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 