import apis
from prompts import *
import concurrent.futures
def resume(full_resume,Prompt,Keys):
    full_prompt = f"""
        {Prompt}
        {full_resume}
        """
    output = apis.final(full_prompt)
    return Keys,output
def final_run_resume(resume,additional_information):
    resume_final = f"""
        {resume}
        New Things which candidate has done recently
        {additional_information}
        """
    resume_dictionary = {}
    inputs = [(resume_experience,"Experience"),(resume_skills,"Skills"),(resume_certifications,"Certifications"),(resume_summary,"summary"),(resume_projects,"projects")]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(resume, resume_final, b, c): c for b, c in inputs}
        for future in concurrent.futures.as_completed(futures):
            key, result = future.result()
            resume_dictionary[key] = result
    return resume_dictionary