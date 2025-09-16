import os, sys
from dotenv import load_dotenv

def main():
    print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    from google import genai

    client = genai.Client(api_key=f'{api_key}')

    try:
        response = client.models.generate_content(model="gemini-2.0-flash-001", contents=f"{sys.argv[1]}")
    except Exception as e:
        print("No prompt provided!")
        exit(1)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
