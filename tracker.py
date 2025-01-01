from flask import Flask, request, redirect
import logging

app = Flask(__name__)

# Set up logging to a file
logging.basicConfig(filename='access.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

@app.route('/track')
def track():
    ip = request.remote_addr
    query_params = request.query_string.decode('utf-8')
    logging.info(f'IP: {ip}, Query Params: {query_params}')
    return redirect("https://www.example.com")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
