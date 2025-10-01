import argparse
import ollama
import sys


def list_models(args):
    try:
        models = ollama.list().models
        print("Available models:")

        for model in models:
            print(f"- {model}")

        return 0
    except Exception as e:
        print(f"Error listing models: {e}")
        return 1


def run_model(args):
    prompt = args.prompt

    print(f"Running model '{args.model}' with prompt: {prompt}")

    try:
        response = ollama.generate(model=args.model, prompt=prompt)
        print(response)
        return 0
    except Exception as e:
        print(f"Error running model: {e}")
        if getattr(e, "status_code", None) == 404:
            print(f"Model '{args.model}' not found. Pulling the model...")
            try:
                ollama.pull(args.model)
                try:
                    print(
                        f"Model '{args.model}' pulled successfully. Running the model..."
                    )
                    response = ollama.generate(model=args.model, prompt=args.prompt)
                    print(response)
                except Exception as e:
                    print(f"Error running model after pulling: {e}")
                    return 0
            except Exception as e:
                print(f"Error pulling model: {e}")
                return 1
        return 1


def main():
    # Create the arguments needed for this CLI utility
    parser = argparse.ArgumentParser(description="Interact with an Ollama model(s)")

    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Positional argument for listing models using the 'list' command
    subparsers.add_parser("list", help="List available models.")

    # Positional argument for running a model using the 'run' command
    run_parser = subparsers.add_parser("run", help="Prompt to send to the model.")

    # Positional argument for the prompt when using the 'run' command
    run_parser.add_argument("prompt", type=str, help="Prompt to send")

    # Flag for specifying the model to use, when running the 'run' command
    run_parser.add_argument("--model", type=str, default="llama2", help="Model to use")

    # Parse the arguments
    if len(sys.argv) == 1:
        args = parser.parse_args(["--help"])
    else:
        args = parser.parse_args()

    # Execute the appropriate function based on the command
    if args.command == "list":
        exit_code = list_models(args)
    elif args.command == "run":
        exit_code = run_model(args)
    else:
        parser.print_help()
        exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
