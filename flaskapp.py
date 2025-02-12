from flask import *
from flask_mysqldb import MySQL

app = Flask("Flask App Jenkins")
app.config["MYSQL_USER"] = "admin"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "triggerdb"
app.config["MYSQL_HOST"] = "192.168.0.26"
app.config["MYSQL_PORT"] = 3306 # I made this a string and it was causing errors

mysql = MySQL(app)
# insert delete and update query

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/insert", methods=["GET", "POST"])
def insert():
    if request.method == "POST":
        name = request.form.get("name")
        salary = float(request.form.get("salary"))
		
        if name and salary:
            try:
                cur = mysql.connection.cursor()
                query = "INSERT INTO EMPLOYEES (ename, esalary) VALUES (%s, %s)"
                cur.execute(query, (name, salary))  
                mysql.connection.commit()
                cur.close()
                return render_template("insert.html", status="Good")
            except Exception as e:
                return render_template("insert.html", status="Bad")
    else:
        # helloooooooooo
        return render_template("insert.html")



@app.route("/view-all")
def view():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM employees"
    cur.execute(query)
    employees = cur.fetchall()
    cur.close()

    return render_template("see-all.html", employees=employees)
	


app.run(host="0.0.0.0", port=5000, debug=True)
