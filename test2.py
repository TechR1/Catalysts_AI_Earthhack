import requests
import time


API_TOKEN = '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'
headers = {"Authorization": f"Bearer {API_TOKEN}"}

model_name = 'aisquared/dlite-v1-1_5b'
#model_name = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0'
api_url = "https://api-inference.huggingface.co/models/"+model_name

def get_prediction(text):
    data = {"inputs": text}
    response = requests.post(api_url, headers=headers, json=data)
    result = response.json()
    return result

# Example usage
text_to_predict = "What are your capabilities"
start_time = time.time()
prediction = get_prediction(text_to_predict)
print(prediction)
print("--- %s seconds ---" % (time.time() - start_time))