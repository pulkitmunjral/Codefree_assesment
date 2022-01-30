
import mysql.connector

config = {
    'user': 'root',
    'password': 'any',
    'host': '35.200.192.85',
    'database':'codefree'
}

# now we establish our connection
cnxn = mysql.connector.connect(**config)

print("connected")
con = cnxn.cursor()
print("got cursore")
query1= ("select * from flower;")

con.execute(query1)
print(con.fetchall())