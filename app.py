import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from typing import List

# loading env variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

#structured output model using Pydantic
class Activity(BaseModel):
    city: str
    todo: str

class ActivitiesResponse(BaseModel):
    activities: List[Activity]

app = Flask(__name__)

@app.route("/recommendations", methods=["POST"])
def get_recommendations():
    data = request.get_json()
    if not data or "city" not in data:
        return jsonify({"error": "Missing 'city' parameter"}), 400 #handle missing city parameter
    city = data["city"]

    prompt = f"""
List exactly 10 unique things to do in summer in {city}.
Respond in JSON format as an object with a single field "activities",
which is a list of objects each containing "city" and "todo".
If city is not valid, return an empty list.
"""

    try: 
        response = client.responses.parse(
            model="gpt-4o-2024-08-06",
            input=[
                {"role": "system", "content": "You are a helpful travel assistant."},
                {"role": "user", "content": prompt}
            ],
            text_format=ActivitiesResponse 
        )

        # Convert output to list of dicts
        activities = [a.model_dump() for a in response.output_parsed.activities]

        return jsonify(activities), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500 #invalid api key

if __name__ == "__main__":
    app.run(debug=True)
