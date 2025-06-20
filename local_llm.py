'''!uv pip install transformers'''

from transformers import AutoTokenizer, AutoModelForCausalLM
import os

# STEP 1
# Create the directory if it doesn't exist
save_directory = "./local_model" 
os.makedirs(save_directory, exist_ok=True)

# STEP 2 (Download)
# Load model and tokenizer - All language models are trained on "numerical data", not raw strings.  
# all language models, including newer ones like GPT-4, Gemini 1.5/2.5, Claude, LLaMA, etc., do not understand raw text directly. 
# They all require tokenization as a first step.
print("Downloading model from Hugging Face Hub...")
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# STEP 3 (Save locally)
print(f"\nSaving model to {save_directory}...")
# Save the model and tokenizer to the specified directory
model.save_pretrained(save_directory)
tokenizer.save_pretrained(save_directory)

# STEP 3 (Use locally saved model. Note Model is nothing but a "binary file" which we have downlaoded in the STEP 3.)
# -rw-rw-rw- 1 vscode vscode 327657928 Jan 19 14:01 model.safetensors
# Now we can load from local directory instead of downloading again
print("Loading model from local directory...")
local_model = AutoModelForCausalLM.from_pretrained(save_directory)
local_tokenizer = AutoTokenizer.from_pretrained(save_directory)
local_tokenizer.pad_token = local_tokenizer.eos_token

device = "cpu"
print(f"\nUsing device: {device}")


def generate_text(prompt,
                  max_length=50,
                  temperature=0.8,
                  top_p=0.9,
                  top_k=50,
                  do_sample=True):
    """Generate text from a prompt with customizable parameters
    
    Args:
        prompt (str): The input text to continue
        max_length (int): Maximum length of generated text (including prompt)
        temperature (float): Higher values (>1.0) increase randomness, lower values (<1.0) make it more deterministic
        top_p (float): Nucleus sampling parameter (0-1.0)
        top_k (int): Limits selection to k most likely tokens
        do_sample (bool): If False, uses greedy decoding instead of sampling
        
    Returns:
        str: The generated text including the prompt
    """
    # Prepare the inputs
    inputs = local_tokenizer(prompt, return_tensors="pt",
                             return_attention_mask=True).to(device)

    # Generate text
    output = local_model.generate(
        input_ids=inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_length=max_length,
        do_sample=do_sample,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        pad_token_id=local_tokenizer.pad_token_id
    )

    # Decode the output
    generated_text = local_tokenizer.decode(
        output[0], skip_special_tokens=True)
    
    # Clean up excess whitespace with regex
    import re
    cleaned_text = re.sub(r'\s+', ' ', generated_text)

    return cleaned_text

prompt = "Welcome to this world of AI"

print(f"Generated: {generate_text(prompt, temperature=0.9, max_length=75)}")

