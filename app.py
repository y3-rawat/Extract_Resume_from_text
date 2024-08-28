import time 
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor
import calculations
import concurrent.futures
import json
app = Flask(__name__)
cors = CORS(app, resources={r"/submit": {"origins": "*"}})
api = None
executor = ThreadPoolExecutor(max_workers=5)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

def get_resume(additional_information, extracted_text):
    final_resume = calculations.resume_final(extracted_text, additional_information)
    return final_resume

@app.route('/submit', methods=['POST'])
def submit():

    job_description = request.args.get('job_description', '')
    additional_information = request.args.get('additional_information', '')
    extracted_text = request.args.get('ext-text', '')
    api_key = request.args.get('api', '')
    apis.API_func(api_key)
    start_time = time.time()

    output = get_resume(additional_information, extracted_text)
    end_time = time.time()
    time_taken = end_time - start_time
    # Print the time taken
    print("processing Completed")
    print(f"Time taken by get_data: {time_taken:.2f} seconds")

    return jsonify(output)
 
if __name__ == '__main__':
    app.run(debug=True)