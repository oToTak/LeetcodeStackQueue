from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq_map = defaultdict(int)
        self.freq_stack_map = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int):
        self.freq_map[val] += 1
        freq = self.freq_map[val]
        self.max_freq = max(self.max_freq, freq)
        self.freq_stack_map[freq].append(val)

    def pop(self) -> int:
        val = self.freq_stack_map[self.max_freq].pop()
        self.freq_map[val] -= 1
        if not self.freq_stack_map[self.max_freq]:
            self.max_freq -= 1
        return val
