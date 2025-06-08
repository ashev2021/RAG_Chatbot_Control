import gradio as gr

# simple ui using gradio
def launch_gradio_interface(qa_chain):
    def answer_question(query):
        result = qa_chain({"query": query})
        return result["result"]

    iface = gr.Interface(
        fn=answer_question,
        inputs=gr.Textbox(lines=2, placeholder="Ask something about the document..."),
        outputs="text",
        title="📄 RAG Chatbot for Control Theory",
        description="Ask questions about the loaded document (control.pdf)",
    )

    iface.launch(server_name="0.0.0.0", server_port=7860)

