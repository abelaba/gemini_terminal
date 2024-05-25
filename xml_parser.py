import xml.etree.ElementTree as ET

class XMLParser:
    XML_FILE_PATH = './gemini.xml'

    def __init__(self):
        self.tree = ET.parse(self.XML_FILE_PATH)
        self.root = self.tree.getroot()

    def get_selected_model(self):
        selected = self.root.find('selected').text 
        return selected
    
    def get_image_model(self):
        image_model = self.root.find('image_model').text
        return image_model

    def get_all_models(self):
        models = [model.find('name').text for model in self.root.findall('model')]
        return models

    def update_selected_model(self, new_model_name):
        models = self.get_all_models()

        if new_model_name not in models:
            print(f"Model '{new_model_name}' is not in the models list. Available models: {models}")
            return 

        selected_element = self.root.find('selected')
        selected_element.text = new_model_name
        self.tree.write(self.XML_FILE_PATH, encoding='UTF-8', xml_declaration=True)
        print(f"Selected model updated to {new_model_name}")


    def get_prompt_by_tag(self, tag):
        
        for code in self.root.findall(".//code"):
            if code.find('tag').text == tag:
                return code.find('prompt').text
        return None

