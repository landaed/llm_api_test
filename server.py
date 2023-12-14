from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline('text-generation', model='distilgpt2')

@app.route('/llm', methods=['POST'])
def llm_endpoint():
    data = request.json
    prompt = data['prompt']
    # Adjusting generation settings
    response = generator(prompt, max_length=100, num_return_sequences=1, repetition_penalty=1.2)
    return jsonify(response[0]['generated_text'])

if __name__ == '__main__':
    app.run(debug=True)

