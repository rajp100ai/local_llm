## End to end flow (1):  
![image](https://github.com/user-attachments/assets/e5be7bb4-8793-4de5-a6af-f173aa2b9c4f)    

### How Tokenizater works?  
![image](https://github.com/user-attachments/assets/12c6eea7-2f6d-4203-88d6-dc892241a0b4)    

```
For example: 'hello' will be converted into token ID 31373 by Tokenizer as LLM only understand numbers     
31373: 'hello'    
 6894: 'world'

Special tokens:
50256: '<|endoftext|>'
```

### How Model works?    
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

## Also include RAG steps in the end to end flow (2):   
![image](https://github.com/user-attachments/assets/5ede2a2e-beee-441b-9092-e0466a3ed9fc)   
**RAG (Retrieval-Augmented Generation) is a leading pattern for augmenting LLMs with external knowledge.**

We need to pass 2 things to LLM:  
 1. Prompts
 2. Context (for that we can fetch embeddings from vector DB to build context (RAG) )      

![image](https://github.com/user-attachments/assets/48ab2702-0fcb-4acf-9eaa-3b585bccfca9)      

**All other methosds:**    
![image](https://github.com/user-attachments/assets/3be68016-bd6c-43fd-9f0f-1f7af14319bd)    

---

### Can Function Calling Replace RAG?   
![image](https://github.com/user-attachments/assets/2d33a0e9-dacf-4700-b92a-b5e423ade8f4)


  
