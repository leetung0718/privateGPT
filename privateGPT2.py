import llama_cpp
model = llama_cpp.Llama(
    model_path="Mistral-7B-Instruct-v01-GGUF/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
    chat_format="llama-2",
)
print(model.create_chat_completion(
    messages=[{
        "role": "user",
        "content": "what is the meaning of life?"
    }]
))