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
