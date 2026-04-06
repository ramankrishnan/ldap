from flask import Flask, request, render_template, redirect
import ldap

app = Flask(__name__)

LDAP_SERVER = "ldap://ldap:389"  # keep as-is for docker network
BASE_DN = "dc=example,dc=com"

@app.route("/")
def home():
    return render_template("login_choice.html")  # new page

@app.route("/ldap_login", methods=["GET", "POST"])
def ldap_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            conn = ldap.initialize(LDAP_SERVER)
            conn.simple_bind_s(f"uid={username},{BASE_DN}", password)
            return f"LDAP Login Successful! Welcome {username}"
        except ldap.INVALID_CREDENTIALS:
            return "LDAP Login Failed!"
    return render_template("login.html")

@app.route("/sso_login")
def sso_login():
    # Redirect to Keycloak (SAML/OpenID Connect)
    return redirect("http://keycloak:8080/realms/master/protocol/openid-connect/auth?client_id=flask-demo&response_type=code&redirect_uri=http://localhost:5000/sso_callback")

@app.route("/sso_callback")
def sso_callback():
    return "SSO Login Successful! Token received."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
