from typing import List, Optional
import xml.etree.ElementTree as ET


class XMLParser:
    """Utility for reading and updating an XML configuration file."""

    def __init__(self, xml_file_path: str) -> None:
        self.XML_FILE_PATH = xml_file_path
        self.tree = ET.parse(self.XML_FILE_PATH)
        self.root = self.tree.getroot()

    def _get_element(self, parent: ET.Element, tag: str) -> ET.Element:
        """Get the child element of a single tag under a parent element."""

        element = parent.find(tag)
        if element is None:
            raise ValueError(f"element with name={tag} is None")
        return element

    def _get_text(self, parent: ET.Element, tag: str) -> str:
        """Get the text value of a single tag under a parent element."""

        element = self._get_element(parent, tag)
        if element.text is None:
            raise AttributeError(
                f"text attribute doesn't exist for xml element with name={tag}"
            )
        return element.text

    def _get_value(self, tag: str) -> str:
        """Get the text value of a single tag under root."""

        return self._get_text(self.root, tag)

    def get_selected_model(self) -> str:
        """Get the name for the selected model"""

        selected = self._get_value("selected")
        return selected

    def get_image_model(self) -> str:
        """Get the name for the selected image model"""

        image_model = self._get_value("image_model")
        return image_model

    def get_all_models(self) -> List[str]:
        """List all supported models"""

        models = [self._get_text(model, "name") for model in self.root.findall("model")]
        return models

    def update_selected_model(self, new_model_name: str) -> str:
        """Change selected model to a model specified in the list of models in the xml file"""

        models = self.get_all_models()

        if new_model_name not in models:
            raise ValueError(
                f"Model '{new_model_name}' is not in the models list. Available models: {models}"
            )

        selected_element = self.root.find("selected")
        if selected_element is None:
            raise ValueError("There is no element with selected tag in XML root.")

        selected_element.text = new_model_name
        self.tree.write(self.XML_FILE_PATH, encoding="UTF-8", xml_declaration=True)

        return f"Selected model updated to {new_model_name}"

    def get_prompt_by_tag(self, tag: str) -> Optional[str]:
        """Get the prompt that is going to be passed to the llm model for coding tasks"""

        code_element = self._get_element(self.root, "prompt")

        for code in code_element.findall(".//code"):
            if self._get_text(code, "tag") == tag:
                return self._get_text(code, "prompt")

        return None
