import os

import mysql.connector
from flask import Flask, render_template


app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="tourism_user",
        password=os.environ["TOURISM_DB_PASSWORD"],
        database="tourism",
    )


@app.route("/")
def index():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT
            tours.tour_id,
            countries.country_name,
            hotels.hotel_name,
            hotels.stars,
            tours.price,
            tours.start_date,
            tours.end_date
        FROM tours
        JOIN hotels
            ON tours.hotel_id = hotels.hotel_id
        JOIN countries
            ON hotels.country_id = countries.country_id
        ORDER BY tours.tour_id
        """
    )

    tours = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template("index.html", tours=tours)


if __name__ == "__main__":
    app.run(debug=True)