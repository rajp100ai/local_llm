![image](https://github.com/user-attachments/assets/3eef2074-fd69-47cd-8af0-36bab384a127)    
![image](https://github.com/user-attachments/assets/fc45709e-33f2-4f8a-a399-f7739043edef)     


## Flow  
**Input text(Prompts) → Tokenization → Converting to IDs → Model processing → Next token prediction → Token selection → Building the response**   
```
For example: 'hello' will be converted into token ID 31373 by Tokenizer as LLM only understand numbers     
31373: 'hello'    
 6894: 'world'

Special tokens:
50256: '<|endoftext|>'
Note: 
Tokenizer first convert input text 'chars' into 'token' then by the help of lookup table, it maps token with token ID.
tokenizer.json file contains lookup table for token->token ID, which is used at runtime
```
#### Download LLM localy (Example code)    
```
!uv pip install transformers

from transformers import AutoTokenizer, AutoModelForCausalLM
import os

# Create the directory if it doesn't exist
save_directory = "./local_model" 
os.makedirs(save_directory, exist_ok=True)

# Load model and tokenizer
print("Downloading model from Hugging Face Hub...")
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

print(f"\nSaving model to {save_directory}...")
# Save the model and tokenizer to the specified directory
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)
```
