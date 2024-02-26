# Text Analysis Assignment

## Objective
The goal of this assignment is to implement a series of Python functions to perform basic text analysis. You will work with a provided text corpus and stop words, preprocess the data, remove stop words, and then conduct analysis to identify the most frequent words and the maximum word length within the corpus.

## Instructions

### Setup
- Ensure Python 3.11 is installed on your system.
- Only standard library required
- Two files are provided: `corpus.txt` containing the text data and `stop_words.txt` listing common stop words separated by comma.

### Tasks

1. **Read Corpus**
   - Implement a function `read_corpus(filename: str) -> list[str]` that reads text from `corpus.txt` split it into list of words (tokens separated by space) returns it as a list of strings.

2. **Read Stop Words**
   - Implement a function `read_stop_words(filename: str) -> list[str]` that reads stop words (comma separated) from `stop_words.txt` and returns them as a list of strings.

3. **Preprocess**
   - Implement a function `preprocess(corpus: list[str]) -> list[str]` that takes the corpus as a list and converts each word to lowercase.

4. **Remove Stop Words**
   - Implement a function `remove_stop_words(corpus: list[str], stop_words: list[str]) -> list[str]` that removes stop words from the corpus.

5. **Identify K Most Frequent Words**
   - Implement a function `find_most_frequent_words(corpus: list[str], k: int) -> list[(str, int)]` that identifies the K most frequent words in the corpus and their counts.

6. **Identify Mean Length of Word in Corpus**
   - Implement a function `find_mean_word_length(corpus: list[str]) -> int` that returns the mean length of the word in the corpus.

### Example Usage

```python
corpus = read_corpus('corpus.txt')
stop_words = read_stop_words('stop_words.txt')
words = preprocess(corpus)
words = remove_stop_words(words, stop_words)
top_words = find_most_frequent_words(words, 5)
print(f'Top 5 words: {top_words}')
mean_length = find_mean_word_length(words)
print(f'Mean word length: {max_length}')
```

## Evaluation Criteria
1. **Correctness**: The implemented functions should correctly perform the tasks as described.
2. **Code Quality**: Your code should be clear, concise, and well-documented.
3. **Efficiency**: Your implementation should efficiently handle the text processing and analysis tasks.
4. **Pythonic Practices**: Use of Pythonic coding style.
