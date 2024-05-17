import sys
import google.generativeai as genai
import PIL.Image
import xml.etree.ElementTree as ET

GOOGLE_API_KEY="" # Replace with google api key
genai.configure(api_key=GOOGLE_API_KEY)
XML_FILE_PATH = './gemini.xml'

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return tree, root

def get_selected_model():
    tree, root = parse_xml(XML_FILE_PATH)
    selected = root.find('selected').text
    
    return selected


def get_image_model():
    tree, root = parse_xml(XML_FILE_PATH)
    image_model = root.find('image_model').text
    
    return image_model



def get_all_models():
    tree, root = parse_xml(XML_FILE_PATH)
    models = [model.find('name').text for model in root.findall('model')]
    return models

def update_selected_model(new_model_name):
    tree, root = parse_xml(XML_FILE_PATH)
    models = get_all_models()
    if new_model_name not in models:
        print(f"Model '{new_model_name}' is not in the models list. Available models: {models}")
        return 

    selected_element = root.find('selected')
    selected_element.text = new_model_name
    tree.write(XML_FILE_PATH, encoding='UTF-8', xml_declaration=True)
    print(f"Selected model updated to {new_model_name}")


selected_model = get_selected_model()
selected_image_model = get_image_model()


model = genai.GenerativeModel(selected_model)
image_model = genai.GenerativeModel(selected_image_model)

def main():
    arguments = sys.argv[1:]
    prompt = "".join(arguments)
    prompt_list = prompt.split(" ")

    if len(prompt_list) == 2 and prompt_list[0] == '--updatemodel':
        update_selected_model(prompt_list[1])
        return
    elif len(prompt_list) == 1 and prompt_list[0] == '--models':
        models = get_all_models()
        print(models)
        return

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