DROP DATABASE IF EXISTS tourism;

CREATE DATABASE tourism
CHARACTER SET utf8mb4;

USE tourism;


CREATE TABLE countries (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    climate VARCHAR(200)
);


CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(100) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    address VARCHAR(200),
    phone VARCHAR(20)
);


CREATE TABLE hotels (
    hotel_id INT AUTO_INCREMENT PRIMARY KEY,
    country_id INT NOT NULL,
    hotel_name VARCHAR(100) NOT NULL,
    stars INT,
    room_capacity INT,

    FOREIGN KEY (country_id)
        REFERENCES countries(country_id)
);


CREATE TABLE tours (
    tour_id INT AUTO_INCREMENT PRIMARY KEY,
    hotel_id INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,

    FOREIGN KEY (hotel_id)
        REFERENCES hotels(hotel_id)
);


CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    tour_id INT NOT NULL,
    booking_date DATE NOT NULL,
    people_count INT NOT NULL,

    FOREIGN KEY (client_id)
        REFERENCES clients(client_id),

    FOREIGN KEY (tour_id)
        REFERENCES tours(tour_id)
);


INSERT INTO countries (
    country_name,
    climate
)
VALUES
    ('Турция', 'Средиземноморский климат'),
    ('Египет', 'Жаркий пустынный климат'),
    ('Россия', 'Умеренный климат');


INSERT INTO clients (
    last_name,
    first_name,
    middle_name,
    address,
    phone
)
VALUES
    (
        'Иванов',
        'Иван',
        'Сергеевич',
        'Москва',
        '+79990000001'
    ),
    (
        'Петрова',
        'Анна',
        'Алексеевна',
        'Нижний Новгород',
        '+79990000002'
    );


INSERT INTO hotels (
    country_id,
    hotel_name,
    stars,
    room_capacity
)
VALUES
    (1, 'Sun Hotel', 5, 3),
    (2, 'Nile Hotel', 4, 2),
    (3, 'Сочи Отель', 4, 4);


INSERT INTO tours (
    hotel_id,
    price,
    start_date,
    end_date
)
VALUES
    (1, 85000.00, '2026-08-10', '2026-08-17'),
    (2, 92000.00, '2026-09-05', '2026-09-12'),
    (3, 65000.00, '2026-07-20', '2026-07-27');


INSERT INTO bookings (
    client_id,
    tour_id,
    booking_date,
    people_count
)
VALUES
    (1, 1, '2026-07-15', 2),
    (2, 3, '2026-07-16', 1);


SELECT
    bookings.booking_id,
    clients.last_name,
    clients.first_name,
    countries.country_name,
    hotels.hotel_name,
    tours.price,
    tours.start_date,
    tours.end_date,
    bookings.people_count
FROM bookings
JOIN clients
    ON bookings.client_id = clients.client_id
JOIN tours
    ON bookings.tour_id = tours.tour_id
JOIN hotels
    ON tours.hotel_id = hotels.hotel_id
JOIN countries
    ON hotels.country_id = countries.country_id;