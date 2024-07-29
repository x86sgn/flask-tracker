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
    return redirect("https://www.personality-database.com/en-US/join_group?cid=livestream%3Agroup-1816015-da215a46-373a-4b4a-a472-b84e2f32dde9&id=30907&inviteFrom=1816015")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
