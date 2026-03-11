# Introduction
For this project, we used pairwise sequence alignment to implement a Smith-Waterman algorithm. 

Pairwise sequence alignment is a technique used to compare two biological sequences, such as DNA, RNA, or proteins to identify regions of similarity that can then be used to observe functional relationships. 

This implmentation of the Smith-Waterman algorithm uses a dynamic programming approach for llocal sequence alignment, and breaks the problem into smaller subproblems and stores their solutions to avoid redundant computation, reducing time complexity significantly.

The implementation is organized into three core functions:

cal_score: calculates the score for each cell in the scoring matrix
traceback: reconstructs the optimal local alignment by tracing back through the matrix from the highest score
smith_waterman: the main function, accepts two sequences and customizable scoring parameters for matches, mismatches, and gaps

The algorithm was tested using the DNA sequences TACTTAG and CACATTAA to verify that the scoring matrix is correctly populated and that the traceback accurately reconstructs the optimal local alignment.

# Pseudocode
Put pseudocode in this box:

```
Import numpy

Initialize a scoring matrix and traceback matrix with zeros
Set max_score = 0
Set max_position = (0,0)

For i from 1 to length of sequence 1:
    For j from 1 to length of sequence 2:

        If seq1[i-1] equals seq2[j-1]:
            Compute diagonal score using match score
        Else:
            Compute diagonal score using mismatch penalty

        Compute up score using gap penalty
        Compute left score using gap penalty

        Set current cell equal to the maximum of:
            0
            diagonal score
            up score
            left score

        Record which move gave the best score in the traceback matrix
            0 = stop
            1 = diagonal
            2 = up
            3 = left

        If the current score is greater than or equal to max_score:
            Update max_score
            Update max_position

Starting from max_position, perform traceback:

    While the current score is greater than 0:

        If traceback move is diagonal:
            Add the character from sequence 1 to alignment
            Add the character from sequence 2 to alignment
            Move diagonally (i-1, j-1)

        Else if traceback move is up:
            Add the character from sequence 1
            Add a gap "-" to sequence 2
            Move up (i-1)

        Else if traceback move is left:
            Add a gap "-" to sequence 1
            Add the character from sequence 2
            Move left (j-1)

Reverse the collected characters in both aligned sequences

Output:
    aligned sequence 1
    aligned sequence 2
    scoring matrix
    alignment score
```

# Successes
We learned how to implement a Smith-Waterman algorithm. We were able to get all three functions to work together to produce the expected local alignment and scoring matrix. We also learned how to handle matches, mismatches and gap penalties in the context of this algorithm.

# Struggles
Our group struggled with meeting together due to midterm exams and travel during spring break. However, we were all able to work on the code and share our versions with each other. While a divide and conquer strategy is not favorable, we were still able to learn from each other's code. 

# Personal Reflections
## Group Leader
Group leader's reflection on the project
Sneha: I was having a bit of a hard time grasping how exactly this algorithm worked, specifically with the concept of diagonal, up, and left scores. After working through the psuedocode, I got a much better understanding on what these meant and how to go about computing each of the scores/penalities. The most difficult part of this project for me was the traceback logic, because it was hard to think about the problem in reverse. I am overall proud of the result of this project as I feel like I learned a lot about how the Smith-Waterman algorithm works and how to implement it. 

## Other member
Fardina Tabassum - This project was interesting to me. I came in with some familiarity from Genomics in basic sequence features like start and stop codons from identifying ORFs, but transitioning to a dynamic programming approach proved challenging. I initially struggled to grasp how the scoring matrix uses a zero floor to prevent negative values, which is a critical local alignment rule that distinguishes it from global alignment. The traceback process was another area where I struggled. In Genomics, we looked at sequences as static objects, but here I had to learn how to move backward through a matrix of directions to reconstruct an alignment from the peak similarity score back to the origin. Ultimately, this project was a challenging shift from scanning for motifs to calculating optimal pathways, but it gave me a much deeper insight into the mathematical understanding behind tools that use these algorithms.

# Generative AI Appendix
As per the syllabus
