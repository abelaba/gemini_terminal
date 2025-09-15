import os
import sys
from typing import Any, List
import google.generativeai as genai
import PIL.Image
from dotenv import load_dotenv
from utils import read_file
from xml_parser import XMLParser

load_dotenv()

DESCRIPTION_FILE = "./description.txt"


class GeminiCLIInterface:
    def __init__(self, xml_parser: XMLParser, llm_api: Any) -> None:
        self.parser = xml_parser

        selected_model = self.parser.get_selected_model()
        selected_image_model = self.parser.get_image_model()

        self.model = llm_api.GenerativeModel(selected_model)
        self.image_model = llm_api.GenerativeModel(selected_image_model)
        self._prompts = {}

    def initalize_prompts(self) -> None:
        self._prompts["--help"] = self._get_description
        self._prompts["--updatemodel"] = self._update_model
        self._prompts["--models"] = self._list_models
        self._prompts["--file"] = self._process_file
        self._prompts["--image"] = self._process_image
        self._prompts["--generate"] = self._generate_content

    def invoke_prompt(self, arguments: List[str]) -> str:
        prompt_list = arguments

        if len(prompt_list) == 0:
            raise ValueError("You haven't passed a prompt")

        prompt = prompt_list[0]
        if prompt not in self._prompts:
            raise ValueError(f"Invalid prompt={prompt}")

        response = self._prompts[prompt](prompt_list)
        return response

    def _validate_prompts_list(self, prompt_list: List[str], length: int) -> None:
        if len(prompt_list) != length:
            raise ValueError("Invalid prompt")

    def _get_description(self, prompt_list: List[str]) -> str:
        self._validate_prompts_list(prompt_list, 1)

        description = read_file(DESCRIPTION_FILE)
        return description

    def _update_model(self, prompt_list: List[str]) -> str:
        self._validate_prompts_list(prompt_list, 2)

        return self.parser.update_selected_model(prompt_list[1])

    def _list_models(self, prompt_list: List[str]) -> str:
        self._validate_prompts_list(prompt_list, 1)

        models = self.parser.get_all_models()
        return "\n".join(models)

    def _process_file(self, prompt_list: List[str]) -> str:
        self._validate_prompts_list(prompt_list, 3)

        prompt = self.parser.get_prompt_by_tag(prompt_list[1])
        if prompt:
            file_content = read_file(prompt_list[2])
            return self.model.generate_content(prompt + " " + file_content).text
        else:
            return "Could not find prompt"

    def _process_image(self, prompt_list: List[str]) -> str:
        if len(prompt_list) < 2:
            raise ValueError("Invalid prompt")

        img = PIL.Image.open(prompt_list[1])
        if len(prompt_list) == 2:
            return self.image_model.generate_content(img).text
        else:
            return self.image_model.generate_content(
                ["".join(prompt_list[2:]), img]
            ).text

    def _generate_content(self, prompt_list: List[str]) -> str:
        message = "".join(prompt_list[1:])
        return self.model.generate_content(message).text


def main():
    try:
        GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)

        xml_parser = XMLParser(xml_file_path="./gemini.xml")

        cli = GeminiCLIInterface(xml_parser=xml_parser, llm_api=genai)
        cli.initalize_prompts()

        arguments = sys.argv[1:]
        result = cli.invoke_prompt(arguments)
        print(f"\n{result}\n")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
