# timer
A small import for timing files (saves you about 10 seconds of hard work). In under 50 lines of code. No further packages needed.

It wraps your file in: 
```python
import time
start = time.time()
...
end = time.time()
print(end - start)
```

## Usage

Get the file via: 
```bash
wget https://raw.githubusercontent.com/avocardio/timer/main/timer.py
```

Then import it in your file:
```python
from timer import timer
timer()
...
```

And run the file with: 
```bash
python your_file.py -t
```

Inspired by Geohot's debugging optimization scripts and the search for the ever faster implementation.
