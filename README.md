# CISC101-Henry-Sean-Project
## Chosen Problem (1-2 sentences)
for this project I chose the scholarship shortlist problem
## Chosen Algorithm (name + why it fits)
For the Scholarship Shortlist problem, I deliberately chose Merge Sort. To start merge sort has consistent performance unlike quick sort which can degrade to O(n^2) time complexity in worst case scenarios. Merge sort guarantees a time complexity of O(nlogn) across all cases. On top of that merge sort is a stable sorting algorithm meaning that original relative order is preserved if two students tie maintaining the initial order.
## Demo (video/gif/screenshot of at least one run)
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
## Author & Acknowledgment (sources + AI use, if any)
