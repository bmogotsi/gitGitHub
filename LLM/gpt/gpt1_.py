#! Python3
#  https://medium.com/@ruslanmv/how-to-build-a-basic-llm-gpt-model-from-scratch-in-python-af83179176bc

import numpy as np
import torch
import torch.nn as nnot
import torch.nn.functional as F

import pprint

#### 3. Building the Transformer Architecture
    ## core building blocks of the GPT architecture:
        # --- Multi-Head Self-Attention
        # --- Positionwise Feedforward Layers
        # --- PositionalEmbeddings.

# Transformer Architecture 
# Step --- Multi-Head Self-Attention Mechanism
#           Self-attention allows the model to attend to different parts of the input sequence. 
#           Multi-head attention uses several attention heads, each learning different aspects of the input sequence.

try:
    myLoop =True
    while myLoop == True:
        myLoop = False 
        class MultiHeadSelfAttention(nnot.Module):
            def __init__(self, embed_size, heads):
                super(MultiHeadSelfAttention, self).__init__()
                self.embed_size = embed_size
                self.heads = heads
                self.head_dim = embed_size // heads

                assert (
                    self.head_dim * heads == embed_size
                ), "Embedding size needs to be divisible by heads"

                self.values = nnot.Linear(self.head_dim, embed_size, bias=False)
                self.keys = nnot.Linear(self.head_dim, embed_size, bias=False)
                self.queries = nnot.Linear(self.head_dim, embed_size, bias=False)
                self.fc_out = nnot.Linear(embed_size, embed_size)

            def forward(self, values, keys, query, mask):
                N = query.shape[0]
                value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

                # Split the embedding into self.heads different pieces
                values = values.reshape(N, value_len, self.heads, self.head_dim)
                keys = keys.reshape(N, key_len, self.heads, self.head_dim)
                queries = query.reshape(N, query_len, self.heads, self.head_dim)

                # Scaled dot-product attention
                energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
                if mask is not None:
                    energy = energy.masked_fill(mask == 0, float("-1e20"))
                
                attention = torch.softmax(energy / (self.embed_size ** (1 / 2)), dim=3)

                out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(
                    N, query_len, self.embed_size
                )

                out = self.fc_out(out)
                return out

        # Transformer Architecture 
        # Step --- Positional Encoding
        #           Positional encodings are added to the input embeddings to provide 
        #           the model with information about the order of tokens.

        #Step --- Positional Encoding (Updated)
        class PositionalEncoding(nnot.Module):
            def __init__(self, embed_size, max_len=5000):
                super(PositionalEncoding, self).__init__()
                self.embed_size = embed_size
                self.max_len = max_len
                self.encoding = None  # Will be created dynamically based on the sequence length

            def get_positional_encoding(self, seq_len, device):
                if self.encoding is None or seq_len > self.encoding.size(0):
                    pos = torch.arange(0, seq_len).unsqueeze(1).float()
                    two_i = torch.arange(0, self.embed_size, 2).float()
                    encoding = torch.zeros(seq_len, self.embed_size, device=device)
                    encoding[:, 0::2] = torch.sin(pos / (10000 ** (two_i / self.embed_size)))
                    encoding[:, 1::2] = torch.cos(pos / (10000 ** (two_i / self.embed_size)))
                    self.encoding = encoding
                return self.encoding[:seq_len, :]

            def forward(self, x):
                seq_len = x.size(1)
                pos_enc = self.get_positional_encoding(seq_len, x.device)
                return x + pos_enc.to(x.device)

        # Transformer Architecture 
        # Step --- Transformer Block
        #           A single Transformer block consists of multi-head attention followed by a feedforward network. 
        #           We’ll also use layer normalization and residual connections for stability.

        class TransformerBlock(nnot.Module):
            def __init__(self, embed_size, heads, dropout):
                super(TransformerBlock, self).__init__()
                self.attention = MultiHeadSelfAttention(embed_size, heads)
                self.norm1 = nnot.LayerNorm(embed_size)
                self.norm2 = nnot.LayerNorm(embed_size)
                self.feed_forward = nnot.Sequential(
                    nnot.Linear(embed_size, embed_size * 4),
                    nnot.ReLU(),
                    nnot.Linear(embed_size * 4, embed_size),
                )
                self.dropout = nnot.Dropout(dropout)

            def forward(self, value, key, query, mask):
                attention = self.attention(value, key, query, mask)
                x = self.dropout(self.norm1(attention + query))
                forward = self.feed_forward(x)
                out = self.dropout(self.norm2(forward + x))
                return out

        # Transformer Architecture 
        # Step --- GPT Model
        #           Finally, we’ll stack multiple Transformer blocks to create the overall GPT architecture.

        class GPT(nnot.Module):
            def __init__(self, vocab_size, embed_size, num_layers, heads, device, dropout, max_length):
                super(GPT, self).__init__()
                self.device = device
                self.embed_size = embed_size
                self.word_embedding = nnot.Embedding(vocab_size, embed_size)
                self.position_embedding = PositionalEncoding(embed_size, max_length)
                self.layers = nnot.ModuleList(
                    [TransformerBlock(embed_size, heads, dropout) for _ in range(num_layers)]
                )
                self.fc_out = nnot.Linear(embed_size, vocab_size)
                self.dropout = nnot.Dropout(dropout)

            def forward(self, x, mask=None):
                # x is expected to be of shape (batch_size, sequence_length)
                batch_size, seq_length = x.shape
                
                # Get the word embeddings and apply positional encodings
                word_embeddings = self.word_embedding(x)  # (batch_size, sequence_length, embed_size)
                position_encodings = self.position_embedding(word_embeddings)  # Positional encoding dynamically adjusted
                
                out = self.dropout(position_encodings)

                # Pass through each Transformer block
                for layer in self.layers:
                    out = layer(out, out, out, mask)

                logits = self.fc_out(out)
                return logits
            
        #### 4.  Preparing the Data
        #           We’ll now move to preparing a small text dataset for training. For simplicity, 
        #           we’ll use a small corpus of text (like book chapters or articles).
        # 

        # Preparing the Data
        # Step --- Tokenization
        #           We need to tokenize the text data and convert it into numerical representations that the model can understand.

        from collections import Counter
        import re

        def tokenize(text):
            tokens = re.findall(r'\w+', text.lower())
            return tokens

        def build_vocab(text):
            tokens = tokenize(text)
            vocab = Counter(tokens)
            vocab = {word: idx for idx, (word, _) in enumerate(vocab.most_common())}
            return vocab

        def encode(text, vocab):
            tokens = tokenize(text)
            return [vocab[token] for token in tokens if token in vocab]

        #### 5. Training the Model
        #

        # Training the Model
        # Step --- Training Loop
        #       We’ll use a cross-entropy loss function 
        #       and the Adam optimizer to train the model.

        def train(model, data, vocab, epochs=10, lr=1e-4):
            optimizer = torch.optim.Adam(model.parameters(), lr=lr)
            criterion = nnot.CrossEntropyLoss()

            model.train()
            for epoch in range(epochs):
                total_loss = 0
                for batch in data:
                    inputs = batch[:, :-1].to(model.device)  # Inputs: all tokens except the last
                    targets = batch[:, 1:].to(model.device)  # Targets: all tokens shifted by one position
                    mask = None

                    optimizer.zero_grad()
                    output = model(inputs, mask)  # Forward pass
                    loss = criterion(output.view(-1, output.size(-1)), targets.view(-1))  # Compute loss
                    loss.backward()  # Backpropagation
                    optimizer.step()  # Update weights

                    total_loss += loss.item()
                print(f"Epoch {epoch + 1}, Loss: {total_loss / len(data)}")

        # Training the Model
        # Step --- Dummy Data for Testing
        if myLoop == True:
            continue
            text = "This is a small test dataset for GPT training."
            vocab = build_vocab(text)
            encoded_text = encode(text, vocab)

            print("Text:  " + text)
            
            print("\n Vocab: Pretty Print ")
            pprint.pprint(vocab)

            print(" \n encoded_text:")
            pprint.pprint(encoded_text)

            #  get dictionary key using value
            print(" \n get dictionary key using value:")
            print("1 2 3"  )
            keys = [key for key, val in vocab.items() if (val == 1 or val == 2 or val == 3)]
            print(keys)

            # print("\n encoded_text: on a seperate line ")
            # print(*encoded_text, sep='\n')

            break

        #### 6. Implementing Text Generation Using Auto-Regressive Decoding

        #       Once the model is trained, we can use it to generate text. 
        #       We start with a prompt, feed it into the model, and use the model’s output to predict the next word. 
        #       This process is repeated

        # Implementing Text Generation Using Auto-Regressive Decoding
        # to generate a sequence of text.

        def generate_text(model, prompt, vocab, max_len=50):
            model.eval()
            words = tokenize(prompt)
            inputs = torch.tensor([vocab.get(word, 0) for word in words], dtype=torch.long).unsqueeze(0).to(model.device)  # Add batch dimension
            
            for _ in range(max_len):
                mask = None
                with torch.no_grad():
                    output = model(inputs, mask)
                    next_token_logits = output[0, -1, :]  # Get the logits of the last predicted token
                    predicted_token = torch.argmax(next_token_logits).unsqueeze(0).unsqueeze(0)  # Add batch and sequence dimensions
                    inputs = torch.cat([inputs, predicted_token], dim=1)  # Append predicted token to the input sequence
            
            decoded_sentence = ' '.join([list(vocab.keys())[i] for i in inputs[0].tolist()])
            return decoded_sentence


        #### 7. Example Use
        #       In this section, we will train our GPT-like model using the dummy dataset 
        #       and then use the generate_text function to generate text based on a prompt.

        # Step --- Training the Model
        #       First, we’ll define a small dataset and train the model. 
        #       This is a simplified training process, 
        #       but it demonstrates how the model works.

        # Define a small dataset

        #if myLoop == False:
            #continue
        text = """
        The quick brown fox jumps over the lazy dog. 
        This is an example of a small dataset for training a GPT model.
        We are building a transformer-based architecture.
        """
        vocab = build_vocab(text)
        encoded_text = encode(text, vocab)

        print("Text:  " + text)
        
        print("\n Vocab: Pretty Print ")
        pprint.pprint(vocab)

        print(" \n encoded_text:")
        pprint.pprint(encoded_text)

        # Prepare the training data (this is token-based data)
        # Here we split the text into batches of sequences
        sequence_length = 10
        train_data = [encoded_text[i:i + sequence_length + 1] for i in range(0, len(encoded_text) - sequence_length)]

        # We need to ensure train_data is converted to tensors with batch dimensions.
        train_data = [torch.tensor(seq, dtype=torch.long).unsqueeze(0) for seq in train_data]  # Adds batch dimension

        print(" \n trained data:")
        pprint.pprint(train_data)

        # Define model hyperparameters
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        vocab_size = len(vocab)
        embed_size = 128
        num_layers = 2
        heads = 8
        dropout = 0.1
        max_length = 50

        # Instantiate the model
        model = GPT(vocab_size, embed_size, num_layers, heads, device, dropout, max_length).to(device)


        # and finally, we can train the model with

        # Training the model on small text dataset
        train(model, train_data, vocab, epochs=100, lr=0.001)

        # Step --- Generating Text with a Prompt
        #       Once the model is trained, we can use it to generate text based on a given prompt. 
        #       The generate_text function takes in a prompt, 
        #       generates the next sequence of tokens, 
        #       and converts them back into readable text.

        # Here’s how we use it:

        # Define a prompt to generate text
        prompt = "The quick brown"

        # Generate text based on the prompt
        generated_text = generate_text(model, prompt, vocab, max_len=50)

        # Print the generated text
        print("Generated Text:")
        print(generated_text)

        # Example Output
        #       After training the model, we can expect output that resembles the data in our training set. 
        #       Since we trained on a small dataset, the output won’t be perfect, 
        #       but it will be able to predict 
        #       and generate sentences that reflect patterns in the training text.

        # Here’s an example of what the generated text might look like:

        # Generated Text:
        #   the quick brown fox jumps over the lazy dog 
        #   this is an example of a small dataset for training a small dataset 
        #   for training a small dataset 
        #   for training a small dataset 
        #   for training a small dataset for training a small dataset for training a small dataset for training a small dataset 

        # While the generated text is repetitive and simple due to the small dataset, 
        # it shows that the model is successfully learning how to generate sentences based on input prompts.

        ## Running the Code
        #       In order to reproduce the previos code follow the next steps.

        # Copy Python Code: Copy the Python code from the blog post into a file named gpt_model.py 
        # from here, within the project directory.

        # Execute the Code:
        # Direct Execution:

        # python gpt_m

        # you will get

        # Generated Text:
        #   the quick brown fox jumps over the lazy dog 
        #   this is an example of a small dataset for training a small dataset 
        #   for training a small dataset 
        #   for training a small dataset 
        #   for training a small dataset for training a small dataset for training a small dataset for training a small dataset 

except Exception as e:
    print(f"Exception.....:   {str(e)}")

exit