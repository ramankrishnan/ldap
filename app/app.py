from flask import Flask, request, render_template
import ldap

app = Flask(__name__)
LDAP_SERVER = "ldap://ldap:389"
BASE_DN = "dc=example,dc=com"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            conn = ldap.initialize(LDAP_SERVER)
            conn.simple_bind_s(f"uid={username},{BASE_DN}", password)
            return "Login Successful!"
        except ldap.INVALID_CREDENTIALS:
            return "Login Failed!"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
