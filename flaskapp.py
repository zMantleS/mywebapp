from flask import *
from flask_mysqldb import MySQL

app = Flask("Flask App Jenkins")
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "triggerdb"
app.config["MYSQL_HOST"] = "192.168.0.26"
app.config["MYSQL_PORT"] = "3306"

mysql = MySQL(app)
# insert delete and update query

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        name = request.form.get("name")
        salary = request.form.get("salary")

        if name and salary:
            try:
                cur = mysql.connection.cursor()
                query = "INSERT INTO EMPLOYEES (ename, esalary) VALUES (%s, %s)"
                cur.execute(query, (name, salary))  
                mysql.connection.commit()
                cur.close()
                return render_template("insert.html", status="Good")
            except Exception as e:
                print(f"Error: {e}")
                return render_template("moviesubmit.html", status="Bad")
    else:
        return render_template("insert.html")



@app.route("/delete", methods=["GET","POST"])
def delete():
	if request.method == "POST":
		print("yay")
	else:
		return render_template("delete.html")
	

@app.route("/update", methods=["GET","POST"])
def update():
	if request.method == "POST":
		print("Yay")
	else:
		return render_template("update.html")




app.run(host="0.0.0.0", port=5000, debug=True)
