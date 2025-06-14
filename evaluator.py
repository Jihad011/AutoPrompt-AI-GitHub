import random

class Evaluator:
    def evaluate(self, prompt):
        # Simple heuristic scoring + randomness
        keyword_score = sum([1 for kw in ['AI', 'data', 'learn', 'ethics', 'blockchain'] if kw in prompt])
        length_score = len(prompt)
        return keyword_score * 10 + length_score + random.uniform(-3, 3)