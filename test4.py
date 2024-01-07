"""
__SUMMARY__

"""

from gpt4all import GPT4All 
import time
import pandas as pd

dataset_path = 'test_startup.csv'

df = pd.read_csv(dataset_path, encoding='latin-1')

print(df) 
for index, row in df.iterrows():
    print(row["Name"], row["Age"])

start_time = time.time()

#model = GPT4All('D:\IIT\Business\Ai Hack Earth\earthhack_code\offline_models\gpt4all-falcon-q4_0.gguf', allow_download=False)


response=[]
'''
with model.chat_session():
    
    
    response.append(model.generate(prompt='hello', temp=0))
    #response.append(model.generate(prompt='Harish has a best friend, his name is Ragav. Harish is good at singing and Ragav is good at drawing', temp=0))
    #response.append(model.generate(prompt="Who is Harish's best friend?", temp=0))
    #response.append(model.generate(prompt='What is Harish good at?', temp=0))
    print(response)
    print("--- %s seconds ---" % (time.time() - start_time))
    # above lines can be replaced with the retrieved data part

    while True:
        user_input = input('> ')
        if user_input.lower() == '':
            pass
        elif user_input.lower() in ['q', 'quit']:
            break
        else:
            print(model.generate(user_input, max_tokens=300))
    print(model.current_chat_session)

    '''