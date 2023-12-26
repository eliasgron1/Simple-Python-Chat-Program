# host     = mariadb.vamk.fi
# user     = e2203097


from flask import *
#from flaskext.mysql import MySQL
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
  host="mariadb.vamk.fi",
  user="e2203097",
  password="********",
  database="e2203097_comments"

)
mycursor = mydb.cursor()

def getFromDatabase():
    mycursor.execute ("DELETE FROM comments WHERE comment IS NULL OR comment = '';")
    mycursor.execute("SELECT * FROM comments")
    data = mycursor.fetchall()
    for string in data:
        if string != " ":
            print(string)
        
    return data


def sendToDatabase(name, text):
    cmd = "INSERT INTO comments (comment, name) VALUES (%s, %s)"
    val = (f"{text}",f"{name}",)
    mycursor.execute(cmd, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")







@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = (request.form["name"])
        text = (request.form["text"])
        sendToDatabase(name, text)

    return render_template("index.html", dbhtml = getFromDatabase())



if __name__ == "__main__":
    app.run(debug=True)

