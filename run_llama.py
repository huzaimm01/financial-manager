from huggingface_hub import hf_hub_download
from transformers import AutoModelForCausalLM, AutoTokenizer

# Download the model and tokenizer
model_id = "meta-llama/Llama-3-8B-Instruct"
hf_hub_download(repo_id=model_id, cache_dir="./models")

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
