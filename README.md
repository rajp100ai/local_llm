## End to end flow:   
**Input text(Prompts) → [Tokenization → Converting to IDs] → [Model processing → Next token prediction → Token selection → Building the response]**    
## How Tokenizater works?  
![image](https://github.com/user-attachments/assets/12c6eea7-2f6d-4203-88d6-dc892241a0b4)    

```
For example: 'hello' will be converted into token ID 31373 by Tokenizer as LLM only understand numbers     
31373: 'hello'    
 6894: 'world'

Special tokens:
50256: '<|endoftext|>'
```

## How Model works?    
![image](https://github.com/user-attachments/assets/3eef2074-fd69-47cd-8af0-36bab384a127)    
![image](https://github.com/user-attachments/assets/fc45709e-33f2-4f8a-a399-f7739043edef)    
1. We start with our prompt
2. For each new token:
   - The model processes all the text so far
   - It generates probabilities for the next token
   - We apply temperature and top-k filtering
   - We sample a token from the resulting distribution
   - The selected token is added to our text
   - We repeat until we reach our desired length

---
  
 

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
