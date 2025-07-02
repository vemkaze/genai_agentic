from agents.base_agent import BaseAgent

class CodeExplainerAgent(BaseAgent):
    def run(self, prompt: str):
        full_prompt = f"Explain the following code in simple terms:\n\n{prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text
