from autoprompt_agent import AutoPromptAgent

if __name__ == "__main__":
    generations = 10
    population_size = 6

    agent = AutoPromptAgent(population_size=population_size)
    agent.run(generations=generations)