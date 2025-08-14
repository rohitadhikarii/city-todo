Objective

Develop a Python Flask server that accepts a city name from a user, queries a Large Language Model (LLM), and returns a structured list of the top 10 things to do in summer for that city.

Setup Instructions

Clone the repository

git clone <repository-url>
cd <repository-folder>


Create a virtual environment

python -m venv .venv


Activate the virtual environment

Windows

.venv\Scripts\activate


macOS / Linux

source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


Start the Flask server

python app.py

API Usage
Endpoint
POST /recommendations
Content-Type: application/json

Request Body
{
  "city": "Hyderabad"
}


city (string) – The name of the city to get summer activity recommendations for. This field is mandatory.

Example Successful Response
[
  { "city": "Hyderabad", "todo": "Visit Ramoji Film City" },
  { "city": "Hyderabad", "todo": "Explore Charminar" },
  { "city": "Hyderabad", "todo": "Walk around Hussain Sagar Lake" },
  { "city": "Hyderabad", "todo": "Try street food at Laad Bazaar" },
  { "city": "Hyderabad", "todo": "Visit Salar Jung Museum" },
  { "city": "Hyderabad", "todo": "Take a heritage walk in Old City" },
  { "city": "Hyderabad", "todo": "Enjoy boating at Osman Sagar" },
  { "city": "Hyderabad", "todo": "Explore Golconda Fort" },
  { "city": "Hyderabad", "todo": "Relax at Shilparamam cultural village" },
  { "city": "Hyderabad", "todo": "Attend summer workshops at Birla Science Museum" }
]

Example Error Responses

Missing city field

{
  "error": "Missing 'city' parameter"
}


HTTP Status: 400 Bad Request

Invalid or missing OpenAI API key

{
  "error": "Error code: 401 - {'error': {'message': 'Missing bearer or basic authentication in header', 'type': 'invalid_request_error'}}"


HTTP Status: 500 Internal Server Error

Technical Details

Backend Framework: Flask

LLM Integration: OpenAI GPT-4o Responses API

Structured Output: Pydantic models for JSON validation

Error Handling:

Missing "city" field → 400

Invalid API key → 500

Unexpected LLM output → 500

Dependencies

All required packages are listed in requirements.txt, including:

Flask

openai

python-dotenv

pydantic
