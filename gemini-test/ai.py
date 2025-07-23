import os
import google.generativeai as genai

# Configure your API key
# Best practice: Load from environment variable for security
# utilize dotenv library for environment files to store key
API_KEY = os.getenv("GEMINI_API_KEY")

# error case for missing API key
if not API_KEY:
    print("Error: GEMINI_API_KEY environment variable not set.")
    print("Please set it like: export GEMINI_API_KEY='your_api_key_here'")
    exit()

genai.configure(api_key=API_KEY)

# actual script
try:
    # Use the GenerativeModel class directly
    model = genai.GenerativeModel('gemini-1.5-flash') # You can choose different models like 'gemini-1.5-flash'

    # Make a content generation request
    response = model.generate_content(input("ENTER PROMPT: "))
    print(response.text)

# random errors
except Exception as e:
    print(f"An error occurred: {e}")
    # This might catch errors like invalid API key, rate limits, network issues, etc.