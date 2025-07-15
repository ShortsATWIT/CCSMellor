from fastapi import FastAPI, Header, Cookie, Response
from fastapi.responses import JSONResponse
from typing import Optional
from datetime import datetime

app = FastAPI()

# Use (uvicorn Lab7:app --reload) to run
# Link (http://127.0.0.1:8000/docs)

# Route 1: Return user ID from custom header
@app.get("/user-id")
def read_user_id(x_user_id: Optional[str] = Header(None)):
    return {"message": f"User ID from header: {x_user_id}"}

# Route 2: Check if user is returning (via cookie)
@app.get("/visit")
def check_last_visit(last_visit: Optional[str] = Cookie(None)):
    if last_visit:
        return {"message": f"Welcome back! Your last visit was on {last_visit}"}
    else:
        return {"message": "Welcome! This is your first visit."}

# Route 3: Set a cookie with visit timestamp
@app.get("/set-visit")
def set_last_visit(response: Response):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response.set_cookie(key="last_visit", value=now)
    return {"message": f"Last visit timestamp set to {now}"}

# Route 4: Greet user using both header and cookie
@app.get("/greet")
def greet_user(x_user_id: Optional[str] = Header(None), last_visit: Optional[str] = Cookie(None)):
    user_msg = f"User ID: {x_user_id}" if x_user_id else "Unknown user"
    visit_msg = f"Last visit: {last_visit}" if last_visit else "First time here!"
    return {"user": user_msg, "visit": visit_msg}

# Route 5: Admin check using header and cookie
@app.get("/admin")
def admin_check(x_role: Optional[str] = Header(None), admin_token: Optional[str] = Cookie(None)):
    if x_role == "admin" and admin_token == "securetoken123":
        return {"status": "Access granted", "role": x_role}
    return JSONResponse(content={"status": "Access denied"}, status_code=403)
