import gradio as gr
from rag_pipeline import ask_rag


def answer_question(question):
    """
    Run the complete RAG pipeline.
    """

    answer, sources = ask_rag(question)

    return answer, sources


# ========================================
# CAMPUS-IQ GRADIO INTERFACE
# ========================================

interface = gr.Interface(
    fn=answer_question,

    inputs=gr.Textbox(
        label="Ask a question",
        placeholder="Example: What is the difference between Docker and a virtual machine?",
        lines=3
    ),

    outputs=[
        gr.Textbox(
            label="AI Answer",
            lines=8
        ),

        gr.Markdown(
            label="Retrieved Sources"
        )
    ],

    title="🎓 Campus-IQ — College RAG Assistant",

    description=(
        "Ask questions about your uploaded college and training documents. "
        "Campus-IQ searches the documents using semantic search and "
        "generates an answer using a local Hugging Face model."
    ),

    examples=[
        ["What is Docker?"],
        ["What is containerization?"],
        ["What is the difference between Docker and a virtual machine?"],
        ["What is a Dockerfile?"],
        ["What is Docker Compose?"],
        ["What is a Docker Volume?"]
    ]
)


if __name__ == "__main__":

    print("========================================")
    print("       CAMPUS-IQ AI ASSISTANT")
    print("========================================")

    print("Starting Gradio server...")
    print("Open the local URL shown below.")

    interface.launch(
        server_name="0.0.0.0",
        server_port=7860
    )
