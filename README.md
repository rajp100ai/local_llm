**Input (Prompt) -> Tokenizer ( converts human-readable text (like "AI world!") into a sequence of numbers (called tokens) -> LLMs**      
#### Download LLM localy
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
