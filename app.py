from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="studentdb",
    user="postgres",
    password="w1e2l3come123"
)

@app.route('/')
def home():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    cur.close()

    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO students (name, age, department) VALUES (%s, %s, %s)",
            (name, age, department)
        )
        conn.commit()
        cur.close()

        return redirect('/')

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):

    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        department = request.form['department']

        cur.execute(
            "UPDATE students SET name=%s, age=%s, department=%s WHERE id=%s",
            (name, age, department, id)
        )

        conn.commit()
        cur.close()

        return redirect('/')

    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cur.fetchone()
    cur.close()

    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):

    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()
    cur.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)