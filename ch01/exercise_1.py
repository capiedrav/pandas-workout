"""
Pandas Workout

Chapter 1 - Series

Exercise 1 - Test Scores

Create a series of 10 elements, random integers from 70 to 100, representing scores
on a monthly exam. Set the index to be the month names, starting in September and
ending in June. (If these months don’t match the school year in your location, feel
free to make them more realistic.)

With this series, write code to answer the following questions:

1. What is the student’s average test score for the entire year?
2. What is the student’s average test score during the first half of the year (i.e., the
first five months)?
3. What is the student’s average test score during the second half of the year?
4. Did the student improve their performance in the second half? If so, by how
much?
"""

from pandas import Series
import numpy as np


g = np.random.default_rng(seed=0) # random number generator
s = Series(g.integers(70, 101, 10)) # a series of 10 random integers between 70 and 100
s.index = "Sep Oct Nov Dec Jan Feb Mar Apr May Jun".split() # update index of the series to the months from Sep to Jun

# answer the questions
print(f"Student scores:\n{s}\n")
print(f"1. What is the student’s average test score for the entire year?\nAnswer: {s.mean()}\n")
avg_score_first_half = s.loc['Sep':'Jan'].mean()
print(f"2. What is the student’s average test score during the first half of the year?"
      f"\nAnswer: {avg_score_first_half}\n")
avg_score_second_half = s.loc['Feb':'Jun'].mean()
print(f"3. What is the student’s average test score during the second half of the year?"
      f"\nAnswer: {avg_score_second_half}\n")
print(f"4. Did the student improve their performance in the second half? If so, by how much?"
      f"\nAnswer: {'Yes' if avg_score_second_half > avg_score_first_half else 'No'}"
      f"\n% of improvement: {((avg_score_second_half - avg_score_first_half) / avg_score_first_half) * 100:.2f}\n")

# beyond the exercise
month_highest_score = s.idxmax()
print("5. In which month did this student get their highest score?"      
      f"\nAnswer: {month_highest_score} with a score of {s.loc[month_highest_score]}\n")
print("6. What were this student's five highest scores"
      f"\nAnswer:\n{s.sort_values(ascending=False).iloc[:5]}")
rounded_scores = s.round(decimals=-1) # round to nearest 10
print("7. Round the student’s scores to the nearest 10. (A score of 82 would be rounded down to 80, "
      f"but a score of 87 would be rounded up to 90.)\nAnswer:\n{rounded_scores}")
