import chainlit as cl
from src.hf_model_loader import HuggingFaceModelLoader

model_name: str = "TheBloke/Mistral-7B-Instruct-v0.1-GGUF"


# Runs when the chat starts
@cl.on_chat_start
def main():
    # Load the llm
    llm = HuggingFaceModelLoader(model_name).load_model()
    # Store the llm in the user session
    cl.user_session.set("llm", llm)


@cl.on_message
async def main(message: cl.Message):
    # Retrieve the chain from the user session
    llm = cl.user_session.get("llm")

    msg = cl.Message(
        content="",
    )

    prompt = f"[INST]{message.content}[/INST]"
    for text in llm(prompt=prompt):
        await msg.stream_token(text)

    await msg.send()
