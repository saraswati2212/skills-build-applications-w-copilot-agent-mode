# OctoFit Tracker (skeleton)

Project skeleton for the OctoFit Tracker app. Follows the required structure for backend and frontend.

Backend setup (local development):

```bash
# create virtualenv
python3 -m venv octofit-tracker/backend/venv

# activate and install requirements
source octofit-tracker/backend/venv/bin/activate
pip install -r octofit-tracker/backend/requirements.txt
```

Notes:
- Use Django's ORM for data models and migrations.
- Ports to forward: 8000 (public), 3000 (public), 27017 (private).
