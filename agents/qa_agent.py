from agents.base_agent import BaseAgent

class QAAgent(BaseAgent):
    def run(self, prompt: str):
        full_prompt = f"Answer the question:\n\n{prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text
