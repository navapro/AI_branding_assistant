import argparse
import os
import openai
import argparse
import re

MAX_PROMPT_LEN = 32

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type = str, required= True)
    args = parser.parse_args()
    user_input = args.input
    if validate_input(user_input):
        branding = generate_branding(user_input)
        keywords = generate_keywords(user_input)
        print(f"{branding} \n  {keywords}")
    else:
        raise ValueError(f"Input length is too long, Must be under {MAX_PROMPT_LEN}")

def validate_input(prompt):
    return len(prompt) <= MAX_PROMPT_LEN

def generate_keywords(subject):
    prompt = f"Generate related branding keywords for {subject}"
    keywords_str = call_api(prompt)
    keywords = re.split(",|\n|-", keywords_str)
    keywords = [k.strip().lower() for k in keywords]
    keywords = [k for k in keywords if len(k) > 1]
    return keywords

def generate_branding(subject):
    prompt = f"Generate upbeat branding snippet for {subject}"
    branding = call_api(prompt)
        # If text is truncated then add ...
    if branding[-1] not in {".", "!", "?"}:
        branding += "..."

    return branding


def call_api(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model = "text-davinci-002", prompt = prompt, max_tokens = 32
    )
    text = response["choices"][0]["text"].strip()
    return text

if __name__ == "__main__":
    main()