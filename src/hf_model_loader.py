from ctransformers import AutoModelForCausalLM

class HuggingFaceModelLoader:
    def __init__(self, model_name: str):
        self.__model_name: str = model_name

    def load_model(self):
        return AutoModelForCausalLM.from_pretrained(
            self.__model_name
        )
