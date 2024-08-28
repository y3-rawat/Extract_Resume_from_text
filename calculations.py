import apis
from prompts import *
import concurrent.futures

# Renamed function to avoid conflict with parameter name
def process_resume(full_resume, prompt, key):
    full_prompt = f"""
    {prompt}
    {full_resume}
    """
    output = apis.final(full_prompt)
    return key, output

def final_run_resume(resume, additional_information):
    resume_final = f"""
    {resume}
    New Things which candidate has done recently:
    {additional_information}
    """
    # Ensure that these variables (resume_experience, etc.) are defined or passed correctly
    inputs_prompt = [(resume_experience,"Experience"),(resume_skills,"Skills"),(resume_certifications,"Certifications"),(resume_summary,"summary"),(resume_projects,"projects")]

    resume_dictionary = {}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            executor.submit(process_resume, resume_final, b, c): c for b, c in inputs_prompt
        }

        for future in concurrent.futures.as_completed(futures):
            key, result = future.result()
            resume_dictionary[key] = result

    return resume_dictionary








