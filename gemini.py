import sys
import google.generativeai as genai
import PIL.Image

GOOGLE_API_KEY="" # Replace with google api key
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
image_model = genai.GenerativeModel('gemini-pro-vision')

def main():
    arguments = sys.argv[1:]
    prompt = "".join(arguments)
    prompt_list = prompt.split(" ")

    if len(prompt_list) >= 1 and len(prompt_list) == 2 and prompt_list[0] == '--image':
        img = PIL.Image.open(prompt_list[1])
        response = image_model.generate_content(img)
    elif len(prompt_list) >= 1 and len(prompt_list) > 2 and prompt_list[0] == '--image':
        img = PIL.Image.open(prompt_list[1])
        response = image_model.generate_content([''.join(prompt_list[2:]), img])
    else:
        prompt = "".join(arguments)
        response = model.generate_content(prompt)

    print(":)")
    print()
    print(response.text)
    print()

main()