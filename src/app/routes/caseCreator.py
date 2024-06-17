from flask import Blueprint, jsonify, request, send_file
from app.models import AFWMailHistory, db
import pandas as pd
import io
import json
import re

blueprint = Blueprint('caseCreator', __name__)

@blueprint.route('/cases_prepared', methods=['GET'])
def get_cases_prepared():
    
    cases = db.session.query(AFWMailHistory.mahi_subject, AFWMailHistory.mahi_body).limit(1000).all()
    
    data = {
        'prompt': [case.mahi_subject for case in cases],
        'completion': [case.mahi_body for case in cases]
    }
    df = pd.DataFrame(data)
    
    jsonl_data = []
    for _, row in df.iterrows():
        prompt = row['prompt']
        completion = row['completion']
        
        if not prompt.endswith("\n\n###\n\n"):
            prompt += "\n\n###\n\n"
        if not completion.startswith(" "):
            completion = " " + completion
        
        completion = completion.replace("\n", " ")
        
        jsonl_data.append({
            "prompt": prompt,
            "completion": completion
        })
    
    jsonl_output = io.BytesIO()
    for entry in jsonl_data:
        jsonl_output.write((json.dumps(entry) + "\n").encode('utf-8'))
    jsonl_output.seek(0)
    
    return send_file(jsonl_output, mimetype='application/jsonl', download_name='cases_prepared.jsonl', as_attachment=True)


@blueprint.route('/cases', methods=['GET'])
def get_cases():
    
    cases = db.session.query(AFWMailHistory.mahi_subject, AFWMailHistory.mahi_body).limit(1000).all()
    
   
    data = {
        'prompt': [case.mahi_subject for case in cases],
        'completion': [case.mahi_body for case in cases]
    }
    df = pd.DataFrame(data)
    
   
    output = io.BytesIO()
    df.to_csv(output, index=False)
    output.seek(0)
    
    
    return send_file(output, mimetype='text/csv', download_name='cases.csv', as_attachment=True)
