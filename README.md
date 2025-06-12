# 🚗 Driver-for-Hire Aggregator App

A comprehensive ride-sharing platform built with FastAPI backend and HTML frontend, enabling passengers to request rides and drivers to accept them.
[It is a App's API testing interface which helps to easily understand how actually such apps works at backend when we provide a input in the interface (frontend)]

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Frontend Usage](#frontend-usage)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## ✨ Features

### Backend (FastAPI)
- **User Authentication**: JWT-based login system
- **Role-based Access**: Separate functionalities for passengers and drivers
- **Ride Management**: Create, view, and manage ride requests
- **Real-time Updates**: Accept/reject ride requests
- **Database Integration**: SQLAlchemy ORM with support for multiple databases

### Frontend (HTML/CSS/JavaScript)
- **Modern UI**: Responsive design with smooth animations
- **Complete API Testing**: Interface to test all backend endpoints
- **Real-time Status**: Live authentication and user status updates
- **Role-based Interface**: Different views for passengers and drivers

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (Download from [python.org](https://www.python.org/downloads/))
- **pip** (Python package manager - usually comes with Python)
- **Git** (Optional, for cloning the repository)

## 📦 Installation

### Step 1: Clone/Download the Project

**Option A: Using Git**
```bash
git clone <your-repository-url>
cd driver-for-hire-app
```

**Option B: Download ZIP**
- Download the project files
- Extract to a folder named `driver-for-hire-app`
- Navigate to the folder in terminal/command prompt

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv ride_app_env

# Activate virtual environment
# On Windows:
ride_app_env\Scripts\activate

# On macOS/Linux:
source ride_app_env/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install all required packages
pip install fastapi[all] sqlalchemy python-multipart python-jose[cryptography] passlib[bcrypt] uvicorn

# Or install from requirements.txt (if available)
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
# Check if FastAPI is installed correctly
python -c "import fastapi; print('FastAPI installed successfully')"
```

## 📁 Project Structure

Ensure your project structure matches this layout:

```
driver-for-hire-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # Main FastAPI application
│   ├── models.py            # Database models
│   ├── schemas.py           # Pydantic schemas
│   ├── crud.py              # Database operations
│   ├── auth.py              # Authentication logic
│   ├── database.py          # Database configuration
│   └── routes/
│       ├── __init__.py
│       ├── user.py          # User-related endpoints
│       └── ride.py          # Ride-related endpoints
├── index.html            # Frontend interface
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## ⚙️ Configuration

### Database Configuration

The app uses Postgresql. To configure the database:

1. **SQLite (Default)**: No additional setup required
2. **PostgreSQL**: Update `database.py` with your PostgreSQL credentials (database used by me)
3. **MySQL**: Update `database.py` with your MySQL credentials

### Environment Variables (Optional)

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=sqlite:///./ride_app.db
```

## 🚀 Running the Application

### Step 1: Start the Backend Server

```bash
# Navigate to the project root directory
cd driver-for-hire-app

# Start the FastAPI server
uvicorn app.main:app --reload
```

**Alternative commands:**
```bash
# If main.py is in root directory
uvicorn main:app --reload

# Specify custom port
uvicorn app.main:app --reload --port 8001

# Run on all interfaces (for network access)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Step 2: Verify Backend is Running

Open your browser and visit:
- **API Root**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

You should see the API documentation and be able to test endpoints.

### Step 3: Open the Frontend

1. **Locate the HTML file**: Find `index.html` in your project directory
2. **Open in browser**: 
   - Double-click the file, or
   - Right-click → "Open with" → Choose your browser, or
   - Drag the file into your browser window

### Step 4: Update API URL (if needed)

If your backend runs on a different port:
1. Open `index.html` in a text editor
2. Find the line: `const API_BASE_URL = 'http://localhost:8000';`
3. Update the port number to match your backend server

## 📚 API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/users/register` | Register new user |
| POST | `/users/login` | User login |
| GET | `/users/me` | Get current user info |

### Ride Endpoints

| Method | Endpoint | Description | Role |
|--------|----------|-------------|------|
| POST | `/rides/` | Create ride request | Passenger |
| GET | `/rides/my` | Get user's rides | Passenger |
| GET | `/rides/my/current` | Get current ride | Passenger |
| GET | `/rides/my/pastrides` | Get past rides | Passenger |
| GET | `/rides/pending` | Get pending rides | Driver |
| PUT | `/rides/{ride_id}/accept` | Accept ride | Driver |
| GET | `/rides/my/accepted` | Get accepted rides | Driver |

## 🖥️ Frontend Usage

### Getting Started

1. **Open the frontend** in your browser
2. **Register users**: Create both passenger and driver accounts
3. **Test the workflow**:
   - Login as passenger → Create ride requests
   - Login as driver → View and accept rides
   - Switch between roles to test full functionality

### Interface Overview

- **Authentication Tab**: User registration, login, and profile management
- **Passenger Tab**: Create and manage ride requests
- **Driver Tab**: View pending rides and manage accepted rides

### Testing Features

- **Real-time Status**: Shows current login status and user role
- **API Response Display**: View JSON responses from all API calls
- **Error Handling**: Clear error messages for debugging
- **Form Validation**: Input validation for all forms

## 🧪 Testing

### Manual Testing Steps

1. **User Registration**:
   ```
   - Register a passenger account
   - Register a driver account
   - Verify both registrations are successful
   ```

2. **Authentication Flow**:
   ```
   - Login with passenger credentials
   - Access passenger-only endpoints
   - Login with driver credentials
   - Access driver-only endpoints
   ```

3. **Ride Workflow**:
   ```
   - Passenger: Create ride request
   - Driver: View pending rides
   - Driver: Accept ride request
   - Passenger: View accepted ride
   ```

### API Testing with curl

```bash
# Register user
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "user_role": "passenger",
    "password_hash": "password123"
  }'

# Login
curl -X POST "http://localhost:8000/users/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john@example.com&password=password123"
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. **Port Already in Use**
```bash
# Error: Port 8000 is already in use
# Solution: Use a different port
uvicorn app.main:app --reload --port 8001
```

#### 2. **CORS Errors**
```bash
# Error: Access to fetch at 'http://localhost:8000' from origin 'null' has been blocked by CORS policy
# Solution: Ensure CORS middleware is added to main.py
```

#### 3. **Module Import Errors**
```bash
# Error: ModuleNotFoundError: No module named 'app'
# Solution: Ensure you're running from the correct directory and using the right command
cd driver-for-hire-app
uvicorn app.main:app --reload
```

#### 4. **Database Errors**
```bash
# Error: Database connection failed
# Solution: Check database configuration in database.py
# For SQLite: Ensure the directory is writable
# For PostgreSQL/MySQL: Verify connection credentials
```

#### 5. **Frontend Not Loading**
```bash
# Error: Frontend shows blank page or API errors
# Solution: 
# 1. Ensure backend server is running
# 2. Check API_BASE_URL in frontend.html matches your server
# 3. Open browser developer tools to see specific errors
```

### Debug Mode

Enable debug logging:
```bash
# Run with debug logging
uvicorn app.main:app --reload --log-level debug
```

### Checking Logs

- **Backend logs**: Displayed in the terminal where you started the server
- **Frontend logs**: Open browser Developer Tools (F12) → Console tab

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit your changes: `git commit -m 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request


## 📞 Support

If you encounter any issues:

1. **Check this README**: Most common issues are covered above
2. **Review the logs**: Check both backend and frontend console logs
3. **Test with API docs**: Use http://localhost:8000/docs to test endpoints directly 
4. **Create an issue**: If you find a bug, please create an issue with:
   - Your operating system
   - Python version
   - Complete error message
   - Steps to reproduce

---

**Happy Coding! 🚗💨**