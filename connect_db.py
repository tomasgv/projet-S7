import pandas as pd
import sqlite3

# check pandas version
print(pd.__version__)

# This block adds the data to the database
# conn = sqlite3.connect("./db/resourcesDB")
# df = pd.read_csv("./db/edu_resource.csv", sep='\t')
# df.to_sql("eduresources", conn, if_exists='append', index=False)

# Connect to the database
conn = sqlite3.connect("./db_test/resourcesDB")
# Create a cursor
c = conn.cursor()
# Execute a query
c.execute("SELECT * FROM eduresources")
# Fetch all the results
print(c.fetchall())
