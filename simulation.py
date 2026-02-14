

class Simulation:
    def __init__(self, expected_value: tuple[float, float], std_dev: float):
        self.expected_value = expected_value
        self.std_dev = std_dev
    
    def throw(self):
        # Tutaj można zaimplementować logikę symulacji rzutu, np. generowanie losowych punktów na tarczy
        pass

    def run(self, num_throws: int):
        results = []
        for _ in range(num_throws):
            result = self.throw()
            results.append(result)
        return results