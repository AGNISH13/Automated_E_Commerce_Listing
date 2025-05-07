class Pipeline:
    def __init__(self):
        self.step = 0

    def run(self):
        self.step += 1
        return self.step

    def reset(self):
        self.step = 0
        return self.step
    
    def end(self):
        self.step = -1
        return self.step