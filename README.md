<div align="center">
  
# TesiT
  
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-cloud-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)]()
[![Status](https://img.shields.io/badge/license-MIT-red?style=for-the-badge)]()

</div>



Open source A/B testing platform. Self hostable. Free.

Assign users to variants, log conversion events and compare results through a dashboard or directly via the API. No SDK required, no pricing page, no lock-in.

---

## How it works

1. Create an experiment with a name and a list of variants
2. Call the assign endpoint with any user ID to get a variant back
3. Log a conversion event when something meaningful happens
4. Check the results endpoint or open the dashboard to see which variant is winning

---

## API

**Create an experiment**
POST /experiments

**Assign a user to a variant**
GET /experiments/:id/assign?user_id=xyz

**Log a conversion**
POST /experiments/:id/event

**Get results**
GET /experiments/:id/results

---

## Stack

- Backend: Flask, MongoDB Atlas
- Frontend: HTML, CSS, JavaScript
- Fonts: IBM Plex Sans, IBM Plex Mono

---

## Running locally

**Backend**

```bash
cd backend
pip install -r requirements.txt
```

Create a `.env` file in the backend folder:
MONGO_URI=mongodb_atlas_connection_string
SECRET_KEY=enter-a-random-string

Then run:

```bash
python app.py
```

**Frontend**

Open `frontend/index.html` in your browser. No build step required.


