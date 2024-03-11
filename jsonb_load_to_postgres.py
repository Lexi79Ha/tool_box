import psycopg2
import json

# Your JSON data
json_data = '''
{
    "WeeklyTasks": {
        "Monday": {
            "Indexer Project": {
                "Task 1": "Reviewed and downloaded different transaction types to start planning the next steps of the project.",
                "Task 2": "Attempted to reformat some of the Json files to prepare for Postgres."
            }
        },
        "Tuesday": {
            "Online Bookstore": {
                "Task 1": "Created data files for the bookstore and built schema based on the ERD diagram."
            }
        },
        "Wednesday": {
            "Indexer Project": {
                "Task 1": "Started to pull transaction data by individual objects and send those to an ibc_transactions Postgres table."
            },
            "Online Bookstore": {
                "Task 1": "Added some sample customer orders to order tables and made a query script to pull book information based on ISBN numbers."
            }
        },
        "Thursday": {
            "Indexer Project": {
                "Task 1": "Created a Python script to send decrypted transaction data to a new Json file and a new directory.",
                "Task 2": "Cleaned up the Json file data with pandas and converted it to a tabular format for Postgres."
            },
            "Documentation": {
                "Task 1": "Created documentation for the project."
            }
        }
    }
}
'''

# Parse the JSON data
data = json.loads(json_data)

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="Week",
    user="postgres",
    password="auth2020"
)

# Create a cursor
cur = conn.cursor()

# Create a table with columns for Monday, Tuesday, Wednesday, Thursday, and Friday
cur.execute("""
    CREATE TABLE IF NOT EXISTS weekly_tasks (
        id SERIAL PRIMARY KEY,
        monday JSONB,
        tuesday JSONB,
        wednesday JSONB,
        thursday JSONB,
        friday JSON
    );
""")

# Insert data into the table
cur.execute("""
    INSERT INTO weekly_tasks (monday, tuesday, wednesday, thursday)
    VALUES (%s, %s, %s, %s);
""", (
    json.dumps(data["WeeklyTasks"]["Monday"]),
    json.dumps(data["WeeklyTasks"]["Tuesday"]),
    json.dumps(data["WeeklyTasks"]["Wednesday"]),
    json.dumps(data["WeeklyTasks"]["Thursday"])
))

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()

print("Data inserted successfully!")

