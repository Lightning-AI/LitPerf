# LitPerf
Lightweight performance tracker for Python code - zero overhead when disabled.

# install
```bash
pip install litperf
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