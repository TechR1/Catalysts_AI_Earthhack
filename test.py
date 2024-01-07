import requests

model_name = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0'
api_url = "https://api-inference.huggingface.co/models/"+model_name

def get_prediction(text):
    data = {"inputs": text}
    response = requests.post(api_url, json=data)
    result = response.json()
    return result

# Example usage
text_to_predict = "Your input text here."
prediction = get_prediction(text_to_predict)
print(prediction)
