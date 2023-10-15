from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from config import db_params  # Import the db_params from the external config module

app = Flask(__name__)

# Remove the local definition of db_params in this file

@app.route('/')
def index():
    # Connect to the database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Query the data from the table
    cursor.execute("SELECT payment_date, name, amount FROM public_test.payments;")
    rows = cursor.fetchall()

    rounded_rows = [(row[0], row[1], round(row[2], 2)) for row in rows]

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return render_template('form.html', data=rounded_rows)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        payment_date = request.form['payment_date']
        name = request.form['name']
        amount = request.form['amount']

        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO public_test.payments (payment_date, name, amount) VALUES (%s, %s, %s)", (payment_date, name, amount))
        conn.commit()  # Commit the changes to the database

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
