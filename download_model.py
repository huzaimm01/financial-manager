from huggingface_hub import hf_hub_download

model_id = "TheBloke/Llama-2-8B-Chat-GGUF"
model_basename = "llama-2-8b-chat.Q4_K_M.gguf"

model_path = hf_hub_download(
    repo_id=model_id,
    filename=model_basename,
    cache_dir="./models"
)

print("Model downloaded to:", model_path)
