# Facebook Hackathon 2017 Backend

This project is the one half of an app that we ([Matthew 
Thomas](https://github.com/mthomas2992), [Stephanie Chua](https://github.com/stephaniesac) 
and [myself](https://github.com/mattjegan)) created for the 2017 Sydney Facebook Hackathon. 
It serves as the RESTful API used as part of our task crowdsourcing app. The other half, our 
frontend is located [here](https://github.com/mthomas2992/fbHackFrontEnd).

## Requirements
* Python 3.5+
* Virtualenv
* Google Cloud Vision API key

## Setup
```
# Clone the repository
git clone https://github.com/mattjegan/FBHT17
cd FBHT17

# Create a virtualenv
virtualenv venv -p python3

# Activate the virtualenv
source venv/bin/activate

# Install all other requirements
pip install -r requirements.txt

# Run the backend
python fbht17/manage.py runserver
```

## API Docs

## Authentication
### Register
See "Profiles -> Create Profile"

### Login
POST /login/
```
{
  "email": "myemail@example.com",
  "password": "mypassword"
}
```
Response 200
```
{
  "detail": "Success"
}
```
Response 400
```
{
  "detail": "Failed"
}
```

## Steps
### List Steps
GET /steps/
```
[
  {
    "id": 1,
    "name": "Take Pic",
    "type": "camera",
    "desc": "Take a picture of Bondi beach",
    "cost": 0.30,
    "mission": 1 // Mission ID
  }
]
```
### Create Step
POST /steps/
```
{
  "name": "Take Pic",
  "type": "camera",
  "desc": "Take a picture of Bondi beach",
  "cost": 0.30,
  "mission": 1
}
```
Response
```
{
  "id": 1,
  "name": "Take Pic",
  "type": "camera",
  "desc": "Take a picture of Bondi beach",
  "cost": 0.30,
  "mission": 1
}
```
### Get Step
GET /steps/:step_id/
```
{
  "id": 1,
  "name": "Take Pic",
  "type": "camera",
  "desc": "Take a picture of Bondi beach",
  "cost": 0.30,
  "mission": 1
}
```

## Missions
### List Missions
GET /missions/
```
[
  {
    "id": 1,
    "name": "My Sunday Mission",
    "lat": 0.5555,
    "long": 0.5555,
    "author": 1, // Profile ID
    "desc": "I need my mission completed",
    "cost": 1.20, // Total cost of steps - Calculated
    "num_users": 5,
    "expire": "2008-09-15T15:53:00", // Default: 1hr after creation, no timezone info
    "active": true,
    "steps": [1, 2, 3] // Step IDs - Calculated
  }
]
```
### Create Mission
POST /missions/
```
{
  "name": "My Sunday Mission",
  "lat": 0.5555,
  "long": 0.5555,
  "author": 1,
  "desc": "I need my mission completed",
  "cost": 1.20,
  "num_users": 5,
  "expire": "2008-09-15T15:53:00",
  "active": true,
  "steps": [1, 2, 3]
}
```
Response
```
{
  "id": 1,
  "name": "My Sunday Mission",
  "lat": 0.5555,
  "long": 0.5555,
  "author": 1,
  "desc": "I need my mission completed",
  "cost": 1.20,
  "num_users": 5,
  "expire": "2008-09-15T15:53:00",
  "active": true,
  "steps": [1, 2, 3]
}
```
### Get Mission
GET /missions/:mission_id/
```
{
  "id": 1,
  "name": "My Sunday Mission",
  "lat": 0.5555,
  "long": 0.5555,
  "author": 1,
  "desc": "I need my mission completed",
  "cost": 1.20,
  "num_users": 5,
  "expire": "2008-09-15T15:53:00",
  "active": true,
  "steps": [1, 2, 3]
}
```

## Profiles
### List Profiles
GET /profiles/
```
[
  {
    "id": 1,
    "email": "bobby@example.com",
    "first_name": "Bobby",
    "last_name": "Droptables",
    "current_mission": 1, // Mission ID
    "completed_missions": [2, 3, 4], // Mission IDs - Calculated
    "expired_missions": [5, 6, 7], // Mission IDs - Calculated
    "active_missions": [8, 9, 10], // Mission IDs - Calculated
    "amount": 31.45
  }
]
```
### Create Profile
POST /profiles/
```
{
  "email": "bobby@example.com",
  "password": "mypassword",
  "first_name": "Bobby",
  "last_name": "Droptables",
  "current_mission": 1,
  "amount": 31.45
}
```
Response
```
{
  "id": 1,
  "email": "bobby@example.com",
  "first_name": "Bobby",
  "last_name": "Droptables",
  "current_mission": 1,
  "completed_missions": [2, 3, 4],
  "expired_missions": [5, 6, 7],
  "active_missions": [8, 9, 10],
  "amount": 31.45
}
```
### Get Profile
GET /profiles/:profile_id/
```
{
  "id": 1,
  "email": "bobby@example.com",
  "first_name": "Bobby",
  "last_name": "Droptables",
  "current_mission": 1,
  "completed_missions": [2, 3, 4],
  "expired_missions": [5, 6, 7],
  "active_missions": [8, 9, 10],
  "amount": 31.45
}
```

## Results
### List Results
GET /results/
```
[
  {
    "id": 1,
    "profile": 1, // Profile ID
    "step": 1, // Step ID
    "content": "My evidence here" // Base64 Encoded images or just plain string,
    "completed": "2008-09-15T15:53:00" // Generated by the API on creation
  }
]
```
### Create Result
POST /results/
```
{
  "profile": 1,
  "step": 1,
  "content": "My evidence here"
}
```
Response
```
{
  "id": 1,
  "profile": 1,
  "step": 1,
  "content": "My evidence here",
  "completed": "2008-09-15T15:53:00"
}
```
### Get Result
GET /results/:result_id/
```
{
  "id": 1,
  "profile": 1,
  "step": 1,
  "content": "My evidence here",
  "completed": "2008-09-15T15:53:00"
}
```
## Images
### Upload Image
POST /upload/
```
{
  "image": "R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" // Base64 Encoded Image File
}
```
Response
```
{
  "id": 1,
  "image": "https://res.cloudinary.com/hua3msykn/image/upload/v1/images/451b8eb7-6f8_infvkr"
}
```
