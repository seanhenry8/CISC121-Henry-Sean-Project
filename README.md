# CISC121-Henry-Sean-Project
## Chosen Problem (1-2 sentences)
for this project I chose the scholarship shortlist problem
## Chosen Algorithm (name + why it fits)
For the Scholarship Shortlist problem, I deliberately chose Merge Sort. To start merge sort has consistent performance unlike quick sort which can degrade to O(n^2) time complexity in worst case scenarios. Merge sort guarantees a time complexity of O(nlogn) across all cases. On top of that merge sort is a stable sorting algorithm meaning that original relative order is preserved if two students tie maintaining the initial order.
## Demo (video/gif/screenshot of at least one run)

https://github.com/user-attachments/assets/d8730447-4b17-4a0f-b4a0-0eac13349444

## Problem Breakdown & Computational Thinking (include a flowchart + the 4 pillars as brief bullets)

**Decomposition**

1. Sort through the input list to calculate a final score for each applicant based on their gpa, volunteer hours and essay scores
2. Take the list of applicants and repeatedly divides it in half until it results in multiple lists contains only one applicant each 
3. Take the sub lists and compares the final scores and combines them into a sorted list
4. Every time an element is moved take a snapshot for the arrays current state and save it for the GUI to read an animate

**Pattern recognition**

Splitting values: find the midpoint with (length/2) and split

Two pointer comparison: when merging two lists the algorithm places a pointer at the first index of the left list and the first index on the right lists. It will repeatedly move the higher score to the new combined array and the the pointer shifts until both sub lists are empty

**Abstraction**

Details to show
- Grouped blocks
- Visual indicators to show what’s being done

Details not to show
- Does not need to see the recursive depth
- Index numbers

**Algorithm design**

- Input: user uploads applicant data
- Process: calculates scores and begins merge sort. Every time an element is moved or two sub arrays are merged take a snapshot of the current array state and saves it to a queue
- GUI: the goes through the queue displaying each snapshot creating a animation
- Output: outputs a animation of the list getting sorted

**Flowchart**

<img width="855" height="1958" alt="IMG_0219" src="https://github.com/user-attachments/assets/06cc5ccb-df82-43f3-bb80-6deccf700d0d" />

## Steps to Run (local) + requirements.txt

**Prerequisites**

- python 3.8+
- a terminal or command prompt

1. clone repository

  git clone https://github.com/your-username/merge-sort-visualizer.git
cd merge-sort-visualizer

2. Setup Virtual Environment

   windows:

   python -m venv venv
   
   venv\Scripts\activate

   mac/linux:

   python3 -m venv venv
   
   source venv/bin/activate

4. install dependencies

   pip install -r requirements.txt

6. launch the app

   python app.py

8. view the app

   After running the command, the terminal will display a local URL:

   Open this link in your web browser to start the interactive sorting animation.

## Hugging Face Link
## Testing (what you tried + edge cases)

**test case 1: standard input**

 input:
 
Alice, 3.8, 50, 90

Bob, 3.2, 100, 75

Charlie, 3.9, 10, 95

Result: all aplicants sorted correctly. Final board turned green

screenshot:

<img width="1267" height="658" alt="TESTCASE1" src="https://github.com/user-attachments/assets/f0fc47e8-f04b-4889-9ad9-bc0397360a62" />

**test case 2: invalid input**

 input:

 User, GPA, 10, Score

 result: Error: Please use format 'Name, GPA, Vol, Essay' per line. forces you to input using the proper format

 screenshot:

 <img width="1276" height="597" alt="TESTCASE2" src="https://github.com/user-attachments/assets/c30e436b-467a-4627-9e50-96e49305fcd2" />

## Author & Acknowledgment (sources + AI use, if any)

AI Disclosure: Level 4

the original algorithm was all written by me but I used AI to help draft and understand implimenting the GUI and how to create the visual animation of the sorting process

AI was also used to review code for checking for bugs in the code
