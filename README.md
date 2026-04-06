# LDAP + Flask Hands-On Demo

## Step 1: Start OpenLDAP
cd docker/openldap
docker-compose up -d

LDAP will be available on ldap://localhost:389
Users: alice/alice123, bob/bob123

## Step 2: Start Flask App
cd app
python3 -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate         # Windows
pip install -r requirements.txt
python app.py

Open browser at http://localhost:5000
Login using LDAP credentials.

## Optional Step 3: Add Keycloak for SSO
cd docker/keycloak
docker-compose up -d

Access Keycloak at http://localhost:8080
Configure realm, client, and SSO login.
