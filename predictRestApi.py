from flask import Flask, request, jsonify
import torch
from transformers import BertForSequenceClassification, BertTokenizer

app = Flask(__name__)

# Define a mapping dictionary
label_map = {
    0: "Irrelevant",
    1: "Negative",
    2: "Neutral",
    3: "Positive"
}

# Load the model
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=4)
model.load_state_dict(torch.load("model_low_lr.pth",map_location=torch.device('cpu'))) # CUDA ist spontan bei mir irgendwie kaputt gegangen, deswegen auf cpu
model.eval()

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_text = data['inputs'] 

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True, max_length=128)

    with torch.no_grad():
        outputs = model(**inputs)
    
    # Assuming you want the output logits
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=1).tolist()

    # Map predictions to labels
    mapped_predictions = [label_map[pred] for pred in predictions]
    
    return jsonify(mapped_predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
