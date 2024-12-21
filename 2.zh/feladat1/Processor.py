class Processor:
    def __init__(self, spec: str):
        freq, cores = spec.split()
        self.freq = freq
        self.cores = cores

    def get_performance_score(self):
        return self.freq * self.cores

    def is_high_performance(self):
        if self.cores >= 6:
            if self.freq >= 3.5:
                return True

        return False

    def compare(self, cpu: "Processor") -> int:
        if self.get_performance_score() > cpu.get_performance_score():
            return 1
        elif self.get_performance_score() < cpu.get_performance_score():
            return -1

    def __str__(self):
        return "Processor(" + self.freq + ", " + self.cores + " cores)"
