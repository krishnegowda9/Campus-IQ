import numpy as np
from transformers import pipeline


print("Loading Hugging Face embedding model...")
print("Please wait...")


# Load the sentence embedding model
embedding_model = pipeline(
    "feature-extraction",
    model="sentence-transformers/all-MiniLM-L6-v2"
)


print("Model loaded successfully!")


def generate_embedding(text):
    """
    Convert text into a single numerical vector.
    """

    # Generate token embeddings
    result = embedding_model(text)

    # Convert to NumPy array
    embeddings = np.array(result)

    # Remove unnecessary dimensions
    embeddings = np.squeeze(embeddings)

    # Average token embeddings
    vector = embeddings.mean(axis=0)

    # Convert to normal Python list
    return vector.tolist()


if __name__ == "__main__":

    test_text = "What is Docker?"

    print("\nOriginal text:")
    print(test_text)

    embedding = generate_embedding(test_text)

    print("\nEmbedding generated successfully!")

    print("Embedding type:", type(embedding))

    print("Embedding dimensions:", len(embedding))

    print("\nFirst 10 values:")
    print(embedding[:10])
