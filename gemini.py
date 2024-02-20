import sys
import google.generativeai as genai

GOOGLE_API_KEY="" # Replace with google api key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def main():
    arguments = sys.argv[1:]

    prompt = "".join(arguments)

    response = model.generate_content(prompt)

    print(":)")
    print()
    print(response.text)
    print()

main()