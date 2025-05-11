import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig


class HuggingFaceModelLoader:
    def __init__(self, model_name: str):
        self.__model_name: str = model_name

    def load_model(self):
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_storage="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16,
        )
        return AutoModelForCausalLM.from_pretrained(
            self.__model_name, quantization_config=bnb_config
        )
