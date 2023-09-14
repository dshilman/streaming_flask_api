from flask import Flask, Response, stream_with_context
import snowflake.connector

app = Flask(__name__)

# Snowflake connection details
SNOWFLAKE_ACCOUNT = 'YOUR_SNOWFLAKE_ACCOUNT'
SNOWFLAKE_USER = 'YOUR_SNOWFLAKE_USERNAME'
SNOWFLAKE_PASSWORD = 'YOUR_SNOWFLAKE_PASSWORD'
SNOWFLAKE_DATABASE = 'YOUR_DATABASE'
SNOWFLAKE_WAREHOUSE = 'YOUR_WAREHOUSE'
SNOWFLAKE_SCHEMA = 'YOUR_SCHEMA'
SNOWFLAKE_ROLE = 'YOUR_ROLE'

def get_snowflake_connection():
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        role=SNOWFLAKE_ROLE
    )
    return conn

@app.route('/stream_records', methods=['GET'])
def stream_records():
    query = "SELECT * FROM YOUR_TABLE_NAME"
    
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    # Use yield to stream results
    def generate():
        cursor.execute(query)
        for row in cursor:
            # Assuming the table has two columns: col1 and col2
            yield f"col1: {row[0]}, col2: {row[1]}\n"
        
        yield "end"
        cursor.close()
        conn.close()

    return Response(stream_with_context(generate()), content_type='text/plain')

if __name__ == "__main__":
    app.run(debug=True)



