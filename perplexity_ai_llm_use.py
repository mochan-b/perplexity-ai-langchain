from config import PERPLEXITY_API_KEY
from perplexity_ai_llm import PerplexityAILLM

if __name__ == '__main__':
    # Create the LLM
    llm = PerplexityAILLM(api_key=PERPLEXITY_API_KEY, model_name="mistral-7b-instruct")
    # Call the LLM
    response = llm("How many stars are there in our galaxy?")
    # Print the response
    print(response)
