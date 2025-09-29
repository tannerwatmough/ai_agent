import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    print("Hello from ai-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=f'{api_key}')

    verbose_fl = False

    try:
        if sys.argv[1] == "--verbose":
            raise Exception
        user_prompt = sys.argv[1]
        if len(sys.argv) >= 3:
            if sys.argv[2] == "--verbose":
                verbose_fl = True
    except Exception as e:
        print("No prompt provided!")
        exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt))

    print(response.text)
    if verbose_fl:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
