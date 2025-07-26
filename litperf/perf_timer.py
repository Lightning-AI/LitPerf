import time

class PerfTimer:
    def __init__(self, disabled=False):
        self.disabled = disabled
        self.times = [("start", time.perf_counter())]

    def mark(self, label):
        if self.disabled:
            return
        self.times.append((label, time.perf_counter()))

    def print_report(self):
        if self.disabled:
            return
        print('=' * 30)
        print("Timing Report: \n")
        for i in range(1, len(self.times)):
            label, t = self.times[i]
            prev_label, t_prev = self.times[i-1]
            print(f"{prev_label} → {label}: {t - t_prev:.4f} seconds")
        total = self.times[-1][1] - self.times[0][1]
        print(f'-' * 30)
        print(f"Total time: {total:.4f} seconds")
        print(f'-' * 30)