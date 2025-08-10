from flask import Flask, render_template, request
import mysql.connector as m

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('playerform.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        city = request.form['city']
        position = request.form['position']
        speed = int(request.form['speed'])
        stamina = int(request.form['stamina'])
        accuracy = int(request.form['accuracy'])
        agility = int(request.form['agility'])
        strength = int(request.form['strength'])
        uniqueness = request.form['unique']
        status = request.form['status']

        con = m.connect(
            host="localhost",
            username="root",
            password="karthik",
            database="scoutai"
        )
        cur = con.cursor()

        query = """
        INSERT INTO player (name, age, gender, city, position, speed, stamina, accuracy, agility, strength, uniqueness, scouting_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query,(
            name, age, gender, city, position,
            speed, stamina, accuracy, agility, strength,
            uniqueness, status
        ))
        con.commit()
        return "Data Collected Successfully!"
    
    except Exception as e:
        return f"Error: {str(e)}"
    
    finally:
        try:
            cur.close()
            con.close()
        except:
            pass

if __name__ == '__main__':
    app.run(debug=True)

