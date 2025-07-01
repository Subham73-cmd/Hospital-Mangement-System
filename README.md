# Hospital Management System

A simple Python-based command-line application for managing patient, doctor, and worker records in a hospital. This project uses MySQL as the backend database and is designed for educational or small-scale use.

## Features

- **Admin Login:** Secure access for hospital management.
- **Register Patients, Doctors, and Workers:** Add new records with essential details.
- **View Records:** Display all registered patients, doctors, or workers.
- **User-Friendly CLI:** Simple menu-driven interface.
- **MySQL Database Integration:** All data is stored and managed in a MySQL database.

## Requirements

- Python 3.x
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- MySQL server running locally
- Pre-created MySQL database named `hospital` with tables:
    - `patients (name VARCHAR(50), age INT, problems VARCHAR(100), phone BIGINT)`
    - `doctors (name VARCHAR(50), age INT, department VARCHAR(50), phone BIGINT)`
    - `workers (name VARCHAR(50), age INT, workname VARCHAR(50), phone BIGINT)`

## Setup Instructions

1. **Clone this repository or download the script.**
2. **Install required Python package:**
    ```bash
    pip install mysql-connector-python
    ```
3. **Create the MySQL database and tables:**
    ```sql
    CREATE DATABASE hospital;
    USE hospital;

    CREATE TABLE patients (
        name VARCHAR(50),
        age INT,
        problems VARCHAR(100),
        phone BIGINT
    );

    CREATE TABLE doctors (
        name VARCHAR(50),
        age INT,
        department VARCHAR(50),
        phone BIGINT
    );

    CREATE TABLE workers (
        name VARCHAR(50),
        age INT,
        workname VARCHAR(50),
        phone BIGINT
    );
    ```
4. **Run the script:**
    ```bash
    python hospital_management.py
    ```
5. **Login as admin:**
    - Username: `admin`
    - Password: `subham@2000`

## Usage

- **Register New Records:** Choose options to add patients, doctors, or workers.
- **View Records:** Display all entries for each category.
- **Exit:** Safely close the application.


## Author

- [Subham Nayak](https://github.com/Subham73-cmd)


**Feel free to fork and extend this project for your own hospital or educational needs!**
