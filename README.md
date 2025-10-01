# Disco Llama CLI

A command-line interface (CLI) utility for interacting with a Ollama instance. This tool allows users to list available models and run prompts against specified models directly from the terminal.

## Installation

To use the Disco Llama CLI, you need to have Python 3.13 or higher installed. You can then install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

The CLI provides the following commands:

- `list`: List all available models.
- `run`: Run a prompt against a specified model.

### Listing Models

To list all available models, use the following command:

```bash
python main.py list
```

### Running a Model

To run a prompt against a specific model, use the following command:

```bash
python main.py run --model <model_name> <prompt>
```

Replace `<prompt>` with the prompt you want to send to the model, and `<model_name>` with the name of the model you want to use.

## License

This project is licensed under the MIT License.