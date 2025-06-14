import random
import json
from evaluator import Evaluator

class AutoPromptAgent:
    def __init__(self, population_size=5):
        self.population_size = population_size
        self.population = [self.random_prompt() for _ in range(population_size)]
        self.evaluator = Evaluator()

    def random_prompt(self):
        templates = [
            "Explain {} in simple terms.",
            "What are the benefits of {}?",
            "Give an example of {}.",
            "How does {} work?",
            "List the pros and cons of {}."
        ]
        topics = ["machine learning", "quantum computing", "blockchain", "data science", "AI ethics"]
        return random.choice(templates).format(random.choice(topics))

    def mutate(self, prompt):
        return self.random_prompt()

    def evolve(self):
        scores = [(p, self.evaluator.evaluate(p)) for p in self.population]
        scores.sort(key=lambda x: x[1], reverse=True)
        survivors = [p for p, _ in scores[:self.population_size // 2]]
        offspring = [self.mutate(p) for p in survivors]
        self.population = survivors + offspring
        if len(self.population) > self.population_size:
            self.population = self.population[:self.population_size]

    def run(self, generations=5):
        history = []
        for gen in range(generations):
            print(f"\n Generation {gen+1}:")
            for prompt in self.population:
                print("   🔹", prompt)
            history.append({"generation": gen + 1, "prompts": self.population.copy()})
            self.evolve()

        # Save history
        with open("evolution_history.json", "w") as f:
            json.dump(history, f, indent=4)