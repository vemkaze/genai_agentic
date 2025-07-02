from agents.base_agent import BaseAgent

class SummarizerAgent(BaseAgent):
    def run(self, prompt: str):
        full_prompt = f"Summarize the following text:\n\n{prompt}"
        response = self.model.generate_content(full_prompt)
        return response.text
