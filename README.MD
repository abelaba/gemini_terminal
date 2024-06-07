# Google Gemini API Terminal

This project provides a simple command-line interface (CLI) to access the Google Gemini API. It allows users to interact with the API directly from their terminal, making it easy to integrate Google Gemini's capabilities into your workflow.


## Features

- **Query the Google Gemini API:** Send requests and receive responses directly in your terminal.
- **Update Selected Model:** Change the model used for generating responses.
- **List All Models:** Get a list of all available models.
- **Generate Content from Images:** Use image inputs to generate content.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.7+** installed on your machine.
- **pip** (Python package installer).
- A **Google Gemini API key**. You can obtain this from the [Google AI Studio](https://ai.google.dev/aistudio).

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/abelaba/gemini_terminal.git
    cd google_terminal
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your API key and configuration:**

    Go to `gemini.py` file in the project root directory and add your Google Gemini API key:

    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

4. **Ensure you have the `gemini.xml` configuration file** in the project root directory with the necessary model details.

5. **Inorder to give proper permissions for the script file** in the project root directory open a terminal and execute the following command
        
    ```bash
    chmod +x gemini.zsh 
    ```

## Usage

To start using the CLI, run the provided shell script with appropriate commands:

### Example Commands

**Query the API:**

```bash;:
./gemini.zsh "your query here"
```

### Query the API using a file:

```bash
./gemini.zsh --file filename.txt
```

### Update the selected model:

```bash
./gemini.zsh --updatemodel model_name
```

### List all available models:

```bash
./gemini.zsh --models
```

### Generate content from an image:

```bash
./gemini.zsh --image path/to/image.jpg
```

## Available Options
`<text>`: Send a text query to the Google Gemini API.

`--file <filename>`: Send a text query from a file.

`--updatemodel <model_name>`: Update the selected model.

`--models`: List all available models.

`--image <image_path>`: Generate content from an image.

