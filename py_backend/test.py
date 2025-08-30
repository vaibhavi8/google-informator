from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
# my_variable = os.getenv("MY_VARIABLE")
api_key = os.getenv("OPENAI_API_KEY")

# print(f"My Variable: {my_variable}")
print(f"API Key: {api_key}")