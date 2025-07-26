# LitPerf
Lightweight performance tracker for Python code - zero overhead when disabled.

# install
```bash
pip install git+https://github.com/Lightning-AI/litperf.git
```

# Example use

```python
from litperf import PerfTimer

timer = PerfTimer()
    
# Step 1
numbers = [i * i for i in range(50000)]
timer.mark("step1: count")

# Step 2
total = 0
for num in numbers:
    total += num / 2

timer.mark("step2: sum_numbers")

timer.print_report()
```

The above generates the following report:    
```text
==============================
Timing Report: 

start → step1: count: 0.0031 seconds
step1: count → step2: sum_numbers: 0.0036 seconds
------------------------------
Total time: 0.0067 seconds
------------------------------
```
