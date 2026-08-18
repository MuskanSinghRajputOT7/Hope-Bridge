# HopeBridge - Team Setup Guide 
# HopeBridge - Team Setup Guide

## 📋 Prerequisites
- Python 3.11+
- Git
- VS Code (recommended)

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/MuskanSinghRajputOT7/Hope-Bridge.git
cd Hope-Bridge
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Server
```bash
python manage.py runserver
```

## 👥 Team Assignments

| Member | Folder | Task |
|--------|--------|------|
| Member 1 (Muskan) | `apps/users/` | ✅ Complete - DO NOT TOUCH |
| Member 2 | `apps/donations/` | Children, Sponsorships, Donations |
| Member 3 | `apps/adoptions/` | Adoption Applications, Visits |
| Member 4 | `apps/analytics/` | AI Chatbot, Analytics Dashboard |

## 📁 Folder Structure
```
apps/
├── users/          ← MEMBER 1 (DO NOT TOUCH) ✅ Complete
├── donations/      ← MEMBER 2 Build here
├── adoptions/      ← MEMBER 3 Build here
└── analytics/      ← MEMBER 4 Build here
```

## 🔧 Git Workflow

### Daily Routine:
```bash
# 1. Pull latest changes
git pull origin main

# 2. Create a branch for your feature
git checkout -b feature/your-feature-name

# 3. Work on your code (in your folder only!)

# 4. Commit your changes
git add .
git commit -m "Description of what you did"

# 5. Push your branch
git push origin feature/your-feature-name

# 6. Create a Pull Request on GitHub
```

## 📡 APIs Available (Already Built)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register/` | POST | Register a new user |
| `/api/auth/login/` | POST | Login and get JWT token |
| `/api/auth/user/{id}/` | GET | Get user profile |
| `/api/auth/user/{id}/update/` | PUT | Update profile |
| `/api/auth/ngo/create/` | POST | Create NGO (NGO Staff only) |
| `/api/auth/ngo/list/` | GET | List all NGOs |

## 📝 Rules

1. **DO NOT touch `apps/users/`** - That's Member 1's work
2. **Work ONLY in your assigned folder**
3. **Always pull before starting work**
4. **Commit frequently** with meaningful messages
5. **Never push directly to main** - use branches and PRs

## 🆘 Getting Help
- Check `API_DOCS.md` for all API details
- Contact Muskan (Team Lead) for any issues

---

**Happy Coding! 🚀**