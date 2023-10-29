import time
from collections import Counter
import matplotlib.pyplot as plt
import requests
import numpy as np
from scipy.stats import norm

# Decorator to log execution time
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# Function to count words using a dictionary
def word_count_with_dict(text):
    word_count = {}
    lines = text.split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip('.,?!()[]{}":;')
            word = word.lower()
            if word:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count

# Function to count words using the Counter function
def word_count_with_counter(text):
    word_count = Counter()
    lines = text.split('\n')
    for line in lines:
        words = line.split()
        for word in words:
            word = word.strip('.,?!()[]{}":;')
            word = word.lower()
            if word:
                word_count[word] += 1
    return word_count

# Download Shakespeare's text and store it in a variable
shakespeare_url = "https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt"
response = requests.get(shakespeare_url)
shakespeare_text = response.text

# Measure execution time of word counting functions
@time_it
def run_word_count(text, count_func):
    return count_func(text)

# Store execution times for 100 runs
execution_times_dict = []
execution_times_counter = []

for _ in range(100):
    start_time = time.time()
    word_count_dict = run_word_count(shakespeare_text, word_count_with_dict)
    end_time = time.time()
    execution_times_dict.append(end_time - start_time)
    
    start_time = time.time()
    word_count_counter = run_word_count(shakespeare_text, word_count_with_counter)
    end_time = time.time()
    execution_times_counter.append(end_time - start_time)

# Calculate mean and variance
mean_dict = np.mean(execution_times_dict)
variance_dict = np.var(execution_times_dict)
mean_counter = np.mean(execution_times_counter)
variance_counter = np.var(execution_times_counter)

# Plot the distributions of execution times
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(execution_times_dict, bins=20, color='b', alpha=0.7, density=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean_dict, np.sqrt(variance_dict))
plt.plot(x, p, 'k', linewidth=2)
plt.title('Execution Times with Dictionary')

plt.subplot(1, 2, 2)
plt.hist(execution_times_counter, bins=20, color='g', alpha=0.7, density=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean_counter, np.sqrt(variance_counter))
plt.plot(x, p, 'k', linewidth=2)
plt.title('Execution Times with Counter')

plt.show()

# Calculate mean and variance
mean_dict = np.mean(execution_times_dict)
variance_dict = np.var(execution_times_dict)
mean_counter = np.mean(execution_times_counter)
variance_counter = np.var(execution_times_counter)

print(f"Mean Execution Time (Dictionary): {mean_dict:.4f} seconds")
print(f"Variance (Dictionary): {variance_dict:.4f}")
print(f"Mean Execution Time (Counter): {mean_counter:.4f} seconds")
print(f"Variance (Counter): {variance_counter:.4f}")