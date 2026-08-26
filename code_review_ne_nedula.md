# Annex C: 
# Code Quality Assessment Worksheet

**Score:** ___
**Section:** Neon  
**C/M Name:** Aya Daniella Jabagat, Iyanna Rigelle Nedula  
**Date:** 8-26-2026  


### Instructions:
**The problem:** Search for a Number in a Sorted List

For example: Both algorithms could search:  
`numbers = [5, 12, 18, 23, 31, 47, 56, 68, 74, 90]`
`target = 47`

#### Implementation 1
```python
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1
```

#### Implementation 2
```python
def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    
    while low <= high:
        middle = (low + high) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
```

---

## Questions with Checklists

### 1. Efficiency
**Which algorithm is faster when the list of numbers is very large? Why?**

The first thing we notice about algorithm 2 was the fact that as it searches, it reduces the search area in a way it separates the search area into intervals. On the other hand, algorithm 1 checks every single item in the list before its breakdown, making it inefficient when handling large datasets.

| Implementation 1 | Implementation 2 |
| :--- | :--- |
| - [x] How many elements might the algorithm need to check? | - [x] How many elements might the algorithm need to check? |
| - [x] Does the algorithm reduce the search area as it runs? | - [x] Does the algorithm reduce the search area as it runs? |
| - [x] Does the algorithm still work efficiently with a very large list? | - [x] Does the algorithm still work efficiently with a very large list? |

---

### 2. Readability
**Which algorithm is easier to understand at first glance? What makes it clearer?**

The first algorithm is easier to understand as the code is simple and the intent is clear. For an individual with a certain level of background knowledge regarding loops in coding, it's understandable what the program is trying to do. However, for the second algorithm, the variable names and the goal of the program is unclear if it's not exactly the step child at first glance. Although algorithm 2 uses if loops—which are easier to intuitively understand—the variable names and conditions are confusing.

| Implementation 1  | Implementation 2  |
| :--- | :--- |
| - [x] How meaningful are the variable names? | - [x] How meaningful are the variable names? |
| - [x] How simple is the logic? | - [x] How simple is the logic? |
| - [x] How concise is the code? | - [x] How concise is the code? |
| - [x] How easy is it to follow the search process? | - [x] How easy is it to follow the search process? |

---

### 3. Maintainability
**If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?**

Due to algorithm 1's simplicity, it's much more straightforward than algorithm 2. Ergo, it's easier to manipulate without causing minimal error. Meanwhile, the second algorithm uses a more complex structure, which may leave it vulnerable to more errors.

| Implementation 1  | Implementation 2  |
| :--- | :--- |
| - [x] Is the logic straightforward? | - [x] Is the logic straightforward? |
| - [x] Would adding new steps break the code easily? | - [x] Would adding new steps break the code easily? |
| - [x] Is there less chance of errors when updating? | - [x] Is there less chance of errors when updating? |

---

### 4. Testability
**Which algorithm is easier to test with different inputs? Why?**

The first algorithm is much easier to test with different inputs. It can easily search through small lists and it has less things to check compared to the structure in algorithm 2. Since the structure is straightforward and easy to manipulate compared to that of algorithm 2, the output is easier to predict.

| Implementation 1  | Implementation 2  |
| :--- | :--- |
| - [x] Can you test with small lists easily? | - [x] Can you test with small lists easily? |
| - [x] Does the algorithm have fewer conditions to check? | - [x] Does the algorithm have fewer conditions to check? |
| - [x] Is the output predictable and clear? | - [x] Is the output predictable and clear? |

---

### 5. Reliability and Input Validation
**What should the algorithm do to avoid errors when receiving input from a user?**

Algorithm 2, although highly effective for datasets with numerical values, is less resilient to user errors than the first implementation. Between algorithms 1 and 2, the latter relies on arithmetic operations to search for its target. In the event there is an error in the "numbers" list, such as the inclusion of a non-numerical value, it won't be able to run properly. The first algorithm, meanwhile, simply checks whether or not a value in the list is equal to the target or not. In fact, the first algorithm does not need the values to be numbers in the first place.

| Implementation 1  | Implementation 2  |
| :--- | :--- |
| - [x] Does the algorithm check if the list is empty? | - [x] Does the algorithm check if the list is empty? |
| - [x] Does it handle non-numeral inputs (like letters instead of numbers)? | - [x] Does it handle non-numeral inputs (like letters instead of numbers)? |
| - [x] Does it avoid crashing when inputs are unusual? | - [x] Does it avoid crashing when inputs are unusual? |
| - [x] Does it check that the list is sorted before running binary search? | - [x] Does it check that the list is sorted before running binary search? |

---

### 6. Final Answer
**Based on your answers from 1 to 5, which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.**

Although the first algorithm is easier to modify, the second algorithm is more efficient in searching for a number in a sorted list, especially long arrays. However, the first algorithm is better for programs where modifying the algorithm structure is needed since it has less conditions to check and is less likely to cause errors.
