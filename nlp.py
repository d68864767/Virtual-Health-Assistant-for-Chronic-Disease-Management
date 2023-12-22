# Importing necessary libraries
from transformers import GPT2LMHeadModel, GPT2Tokenizer

class NLP:
    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

    def generate_response(self, prediction):
        """
        Function to generate a human-like response based on the prediction from the machine learning model.
        This involves using the GPT-2 model to generate a text that is relevant to the prediction.
        """
        # Convert the prediction into a text
        prediction_text = str(prediction)

        # Encode the prediction text
        inputs = self.tokenizer.encode(prediction_text, return_tensors='pt')

        # Generate a response
        outputs = self.model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2, early_stopping=True)

        # Decode the response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return response

nlp = NLP()

def generate_response(prediction):
    return nlp.generate_response(prediction)
