# HopeBridge API Documentation 


## Base URL
`http://127.0.0.1:8000/api/auth/`

## Authentication
All protected endpoints require:


## Endpoints

### 1. Register User
**POST** `/api/auth/register/`


**Request:**
```json
{
    "name": "John Doe",   
    "email": "john@email.com",
    "password": "password123",
    "phone": "9876543210",
    "role": "donor"
}

**Valid Roles:**
- `admin`
- `ngo_staff`
- `donor`
- `volunteer`
- `adoptive_parent`

**Response:**
```json
{
    "success": true,
    "message": "User registered successfully",
    "user_id": 1
}


2. Login
POST /api/auth/login/

Request:

json
{
    "email": "john@email.com",
    "password": "password123"
}
Response:

json
{
    "success": true,
    "token": "eyJhbGciOiJIUzI1NiIs...",
    "user": {
        "user_id": 1,
        "name": "John Doe",
        "email": "john@email.com",
        "phone": "9876543210",
        "role": "donor",
        "profile_photo": null,
        "is_verified": false,
        "created_at": "2026-08-18T10:00:00Z"
    }
}


3. Get User Profile
GET /api/auth/user/{user_id}/

Headers:

text
Authorization: Bearer <your_token>
Response:

json
{
    "user_id": 1,
    "name": "John Doe",
    "email": "john@email.com",
    "phone": "9876543210",
    "role": "donor",
    "profile_photo": null,
    "is_verified": false,
    "created_at": "2026-08-18T10:00:00Z"
}
4. Update User Profile
PUT /api/auth/user/{user_id}/update/

Headers:

text
Authorization: Bearer <your_token>
Request:

json
{
    "name": "John Updated",
    "phone": "9999999999"
}
Response:

json
{
    "user_id": 1,
    "name": "John Updated",
    "email": "john@email.com",
    "phone": "9999999999",
    "role": "donor"
}
5. Create NGO (NGO Staff Only)
POST /api/auth/ngo/create/

Headers:

text
Authorization: Bearer <your_token>
Request:

json
{
    "name": "Sunshine Orphanage",
    "registration_number": "NGO-2026-001",
    "address": "123 Main Road, Mumbai",
    "city": "Mumbai",
    "state": "Maharashtra",
    "pincode": "400001",
    "phone": "9876543210",
    "email": "contact@sunshine.org",
    "mission": "Caring for orphaned children",
    "capacity": 50
}
Response:

json
{
    "success": true,
    "ngo_id": 1,
    "message": "NGO registered. Awaiting admin verification."
}
6. List NGOs (Public)
GET /api/auth/ngo/list/

Response:

json
{
    "count": 2,
    "ngos": [
        {
            "ngo_id": 1,
            "name": "Sunshine Orphanage",
            "city": "Mumbai",
            "state": "Maharashtra",
            "is_verified": true,
            "total_children": 15
        }
    ]
}
🔐 Authentication Example
Login to Get Token:
bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@hopebridge.com","password":"admin123"}'
Use Token in Request:
bash
curl -X GET http://127.0.0.1:8000/api/auth/user/1/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"



  🎯 Roles & Permissions
Role	Permissions
admin	Full system access
ngo_staff	Create NGOs, manage children
donor	Sponsor children, donate
volunteer	Schedule visits
adoptive_parent	Apply for adoption
📊 Response Codes
Code	Meaning
200	Success
201	Created
400	Bad Request
401	Unauthorized
403	Forbidden
404	Not Found
500	Server Error
🚀 Next Features (Coming Soon)
Endpoint	Method	Description
/api/donations/children/	GET	List all children
/api/donations/sponsor/	POST	Sponsor a child
/api/adoptions/apply/	POST	Apply for adoption
/api/adoptions/visit/	POST	Book a visit
/api/analytics/chatbot/	POST	AI Chatbot
/api/analytics/dashboard/	GET	Analytics dashboard




---

## ✅ Step-by-Step Summary

| Step | Action |
|------|--------|
| 1 | Open `API_DOCS.md` in VS Code or Notepad |
| 2 | Scroll to the VERY BOTTOM |
| 3 | Copy ALL the content above |
| 4 | Paste it at the bottom |
| 5 | Press `Ctrl + S` to save |
| 6 | Close the file |

---

## 🚀 After You Save

### Push to GitHub:
```cmd
cd C:\Users\asus\OneDrive\Desktop\College Projects\hopebridge
git add API_DOCS.md
git commit -m "Completed API documentation"
git push origin main