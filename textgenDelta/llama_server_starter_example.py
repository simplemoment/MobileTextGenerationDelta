from llama_cpp import Llama
from llama_cpp.server import __main__
from flask import Flask, request, jsonify

app = Flask(__name__)

model_path = "./qwen2.5-1.5b-instruct-q4_k_m.gguf"

llama = Llama(
    model_path=model_path,
    chat_format="chatml",
    n_gpu_layers=-1,
    n_threads=4,
    seed=1337,
    n_ctx=4096,
)
__main__.main()

def generate_with_template(prompt: str) -> str:
    template = f"Q: {prompt}. A: "
    return template


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')

    prompt_with_template = generate_with_template(prompt)

    response = llama(prompt=prompt_with_template, max_tokens=2048)

    return jsonify({'text': response['choices'][0]['text']})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
