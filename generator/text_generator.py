from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


MODEL_NAME = "google/flan-t5-small"


print("========================================")
print("Loading local Hugging Face text model...")
print("Please wait...")
print("========================================")


# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


# Load FLAN-T5 model
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


print("Text generation model loaded successfully! ✅")


def generate_answer(question, context):
    """
    Generate an answer using ONLY the context
    retrieved from ChromaDB.
    """

    prompt = f"""
Answer the question using only the information in the context.

Context:
{context}

Question:
{question}

Answer:
"""

    # Convert prompt into tokens
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # Generate answer
    outputs = model.generate(
        **inputs,
        max_new_tokens=100,
        do_sample=False
    )

    # Convert tokens back into text
    answer = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return answer.strip()


# Test the generator directly
if __name__ == "__main__":

    test_question = (
        "What is the difference between Docker "
        "and a virtual machine?"
    )

    test_context = """
    Containers share the host kernel, making them lightweight and fast.
    Virtual machines include a complete guest operating system,
    making them heavier and slower to start.
    """

    print("\n========================================")
    print("TEST QUESTION")
    print("========================================")
    print(test_question)

    answer = generate_answer(
        test_question,
        test_context
    )

    print("\n========================================")
    print("TEST ANSWER")
    print("========================================")
    print(answer)
