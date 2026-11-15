
"""
Mini-LLM-Explorer
A beginner-friendly text generation project
using Hugging Face Transformers.
"""

from transformers import pipeline, set_seed

MODEL_NAME = "distilbert/distilgpt2"


def load_model():
    print("Loading language model...")
    set_seed(42)

    generator = pipeline(
        "text-generation",
        model=MODEL_NAME
    )

    print("Model loaded successfully!")
    return generator


def generate_text(generator, prompt):
    results = generator(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.8,
        top_p=0.9,
        pad_token_id=generator.tokenizer.eos_token_id,
        return_full_text=False
    )

    return results[0]["generated_text"]


def main():
    generator = load_model()

    print("\n===== Mini LLM Explorer =====")
    print("Enter 'exit' to quit.")

    while True:
        prompt = input("\nEnter your prompt: ").strip()

        if prompt.lower() == "exit":
            print("Thank you for exploring LLMs!")
            break

        if not prompt:
            print("Please enter a prompt.")
            continue

        print("\nGenerating response...")
        response = generate_text(generator, prompt)

        print("\nLLM Output:")
        print(response)


if __name__ == "__main__":
    main()
  
