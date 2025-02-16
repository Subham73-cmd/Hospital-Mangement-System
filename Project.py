print("""
================================
Welcome to Krishna Hospital
================================
""")

import mysql.connector as sql

pd = str(input("Enter Database Password:"))
conn = sql.connect(host='localhost', user='root', passwd=pd, database="hospital")
c1 = conn.cursor()

print("1.LOGIN")
print("2.EXIT")
choice = int(input("ENTER YOUR CHOICE:"))

if choice == 1:
    u1 = input("Enter User Name:")
    pwd1 = input("Enter The Password:")

    if u1 == 'admin' and pwd1 == 'subham@2000':
        print("WELCOME TO THE HOSPITAL MANAGEMENT SYSTEM")

        while True:
            print('1.Registering Patient details')
            print('2.Registering Doctor details')
            print('3.Registering Worker details')
            print("4.Patient Details")
            print("5.Doctor Details")
            print("6.Worker Details")
            print('7.Exit')
            choice = int(input('ENTER YOUR CHOICE:'))

            if choice == 1:
                p_name = input('Enter Patient Name:')
                p_age = int(input('Enter Age:'))
                p_problems = input('Enter the Problem/Disease:')
                p_phono = int(input('Enter Phone number:'))

                sql_insert = f"INSERT INTO patients (name, age, problems, phone) VALUES ('{p_name}', {p_age}, '{p_problems}', {p_phono})"
                c1.execute(sql_insert)
                print('SUCCESSFULLY REGISTERED')
                conn.commit()

            elif choice == 2:
                d_name = input('Enter Doctor Name:')
                d_age = int(input('Enter Age:'))
                d_department = input('Enter the Department:')
                d_phono = int(input('Enter Phone number:'))

                sql_insert = f"INSERT INTO doctors (name, age, department, phone) VALUES ('{d_name}', {d_age}, '{d_department}', {d_phono})"
                c1.execute(sql_insert)
                print('SUCCESSFULLY REGISTERED')
                conn.commit()

            elif choice == 3:
                w_name = input('Enter Worker Name:')
                w_age = int(input('Enter Age:'))
                w_workname = input('Enter type of work:')
                w_phono = int(input('Enter Phone number:'))

                sql_insert = f"INSERT INTO workers (name, age, workname, phone) VALUES ('{w_name}', {w_age}, '{w_workname}', {w_phono})"
                c1.execute(sql_insert)
                print('SUCCESSFULLY REGISTERED')
                conn.commit()

            elif choice == 4:
                sql_w = 'SELECT * FROM patients'
                c1.execute(sql_w)
                r = c1.fetchall()
                for i in r:
                    print(i)

            elif choice == 5:
                sql_x = "SELECT * FROM doctors"
                c1.execute(sql_x)
                s = c1.fetchall()
                for i in s:
                    print(i)

            elif choice == 6:
                sql_y = "SELECT * FROM workers"
                c1.execute(sql_y)
                t = c1.fetchall()
                for i in t:
                    print(i)

            elif choice == 7:
                print("Exiting the system.")
                break

            else:
                print('Invalid choice. Please try again.')
    else:
        print('Wrong username & password')

elif choice == 2:
    print("Exiting the system.")
else:
    print("Invalid choice. Please try again.")

conn.close()