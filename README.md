# TesiT

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
MONGO_URI=your_mongodb_atlas_connection_string
SECRET_KEY=any_random_string

Then run:

```bash
python app.py
```

**Frontend**

Open `frontend/index.html` in your browser. No build step required.


