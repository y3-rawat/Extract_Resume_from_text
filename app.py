from flask import Flask, request, jsonify
import apis
from flask_cors import CORS
from concurrent.futures import ThreadPoolExecutor
import calculations
import time

app = Flask(__name__)
cors = CORS(app, resources={r"/submit": {"origins": "*"}})

executor = ThreadPoolExecutor(max_workers=4)

def get_resume(additional_information, extracted_text):
    final_resume = calculations.final_run_resume(extracted_text, additional_information)
    return final_resume

def async_api_call(api_key):
    apis.API_func(api_key)

@app.route('/submit', methods=['POST'])
def submit():
    job_description = request.args.get('job_description', '')
    additional_information = request.args.get('additional_information', '')
    extracted_text = request.args.get('ext-text', '')
    api_key = request.args.get('api', '')

    start_time = time.time()

    # Start the API call asynchronously
    future = executor.submit(async_api_call, api_key)

    # Process the resume
    output = get_resume(additional_information, extracted_text)

    # Ensure the API call completes
    future.result()

    end_time = time.time()
    time_taken = end_time - start_time

    print("Processing Completed")
    print(f"Time taken: {time_taken:.2f} seconds")

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
