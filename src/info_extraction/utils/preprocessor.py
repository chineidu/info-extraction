from transformers import AutoTokenizer

model_checkpoint: str = "bert-base-cased"
tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

# Check that the tokenizer object is backed by 🤗 Tokenizers:
assert tokenizer.is_fast is True
