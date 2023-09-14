from flask import Flask, Response, stream_with_context
import time

app = Flask(__name__)

record_value = '{} - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n'

@app.route('/stream_records', methods=['GET'])
def stream_records():

    # Use yield to stream results
    def generate():

        list_x = []

        for x in range(10000):
            # Assuming the table has two columns: col1 and col2
            # list_x.append(record_value.format(x))

            # if x % 10 == 0:
            string_x = record_value.format(x)
            yield string_x
            # list_x.clear()
            time.sleep(.01)
        
    return Response(stream_with_context(generate()), content_type='text/plain')


@app.route('/get_records', methods=['GET'])
def get_records():

    list_x = []
    for x in range(10000):
        # Assuming the table has two columns: col1 and col2
        list_x.append(record_value.format(x))
        time.sleep(.01)
        
    string_x = "".join(list_x)

    return Response(string_x, content_type='text/plain')


if __name__ == "__main__":
    app.run(debug=True)