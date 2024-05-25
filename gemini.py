import sys
import google.generativeai as genai
import PIL.Image
import xml.etree.ElementTree as ET

from xml_parser import XMLParser

GOOGLE_API_KEY=""
genai.configure(api_key=GOOGLE_API_KEY)

def read_file(file_path):
    with open(file_path, 'r') as file:
    # Read the contents of the file
        content = file.read()
        # Print the content
        return content

parser = XMLParser()

selected_model = parser.get_selected_model()
selected_image_model = parser.get_image_model()

model = genai.GenerativeModel(selected_model)
image_model = genai.GenerativeModel(selected_image_model)

def update_model(parser, prompt_list):
    if len(prompt_list) == 2 and prompt_list[0] == '--updatemodel':
        parser.update_selected_model(prompt_list[1])
        return True
    return False

def list_models(parser, prompt_list):
    if len(prompt_list) == 1 and prompt_list[0] == '--models':
        models = parser.get_all_models()
        print(models)
        return True
    return False

def process_file(parser, model, prompt_list):
    if len(prompt_list) == 3 and prompt_list[0] == '--file':
        prompt = parser.get_prompt_by_tag(prompt_list[1])
        if prompt:
            file_content = read_file(prompt_list[2])
            return model.generate_content(prompt + " " + file_content).text
        else:
            return 'Could not find prompt'
    return None

def process_image(image_model, prompt_list):
    if len(prompt_list) >= 2 and prompt_list[0] == '--image':
        img = PIL.Image.open(prompt_list[1])
        if len(prompt_list) == 2:
            return image_model.generate_content(img).text
        else:
            return image_model.generate_content([''.join(prompt_list[2:]), img]).text
    return None

def generate_response(model, arguments, parser, image_model):
    prompt = "".join(arguments)
    prompt_list = prompt.split(" ")

    if update_model(parser, prompt_list) or list_models(parser, prompt_list):
        return

    response = process_file(parser, model, prompt_list)
    if response is None:
        response = process_image(image_model, prompt_list)
    if response is None:
        response = model.generate_content(prompt).text

    print(":)")
    print()
    print(response)
    print()

def main():
    arguments = sys.argv[1:]
    generate_response(model, arguments, parser, image_model)


if __name__ == "__main__":
    main()
