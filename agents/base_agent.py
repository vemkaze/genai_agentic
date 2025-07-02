from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, model):
        self.model = model

    @abstractmethod
    def run(self, prompt: str):
        pass
