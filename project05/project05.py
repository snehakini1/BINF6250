import numpy as np


def cal_score(matrix, seq1, seq2, i, j, match, mismatch, gap):
    '''
    Calculate score for position (i,j) in scoring matrix, also record move to trace back.
    '''
    # Calculate diagonal score
    if seq1[i - 1] == seq2[j - 1]:
        diag_score = matrix[i - 1, j - 1] + match
    else:
        diag_score = matrix[i - 1, j - 1] + mismatch

    # Calculate vertical and horizontal gap scores
    up_score = matrix[i - 1, j] + gap
    left_score = matrix[i, j - 1] + gap

    # Apply the Smith Waterman
    score = max(0, diag_score, up_score, left_score)

    # Record the move for the traceback matrix
    if score == 0:
        move = 0
    elif score == diag_score:
        move = 1  # Diagonal move
    elif score == up_score:
        move = 2  # Up move
    else:
        move = 3  # Left move

    return score, move


def traceback(seq1, seq2, traceback_matrix, scoring_matrix, maximum_position):
    '''
    Find the optimal path through the scoring matrix starting from the highest score.
    '''
    aligned_seq1 = []
    aligned_seq2 = []
    curr_i, curr_j = maximum_position

    # Perform traceback until we hit a score of 0
    while curr_i > 0 and curr_j > 0 and scoring_matrix[curr_i, curr_j] > 0:
        move = traceback_matrix[curr_i, curr_j]

        if move == 1:  # match or mismatch
            aligned_seq1.append(seq1[curr_i - 1])
            aligned_seq2.append(seq2[curr_j - 1])
            curr_i -= 1
            curr_j -= 1
        elif move == 2:  # gap in sequence 2
            aligned_seq1.append(seq1[curr_i - 1])
            aligned_seq2.append("-")
            curr_i -= 1
        elif move == 3:  # gap in sequence 1
            aligned_seq1.append("-")
            aligned_seq2.append(seq2[curr_j - 1])
            curr_j -= 1
        else:
            break

    # Reverse sequences
    return "".join(reversed(aligned_seq1)), "".join(reversed(aligned_seq2))


def smith_waterman(seq1, seq2, match=1, mismatch=-1, gap=-1):
    '''
    Main function for Smith-Waterman local sequence alignment.
    '''
    m, n = len(seq1), len(seq2)

    # Initialize scoring matrix with zeros
    score_matrix = np.zeros((m + 1, n + 1), dtype=int)
    traceback_matrix = np.zeros((m + 1, n + 1), dtype=int)

    max_score = 0
    max_pos = (0, 0)

    # Fill scoring matrix using the Smith Waterman algorithm
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            score, move = cal_score(score_matrix, seq1, seq2, i, j, match, mismatch, gap)
            score_matrix[i, j] = score
            traceback_matrix[i, j] = move

            # Record the highest score and its position for traceback
            if score >= max_score:
                max_score = score
                max_pos = (i, j)

    # Reconstruct the optimal local alignment
    aligned1, aligned2 = traceback(seq1, seq2, traceback_matrix, score_matrix, max_pos)

    return aligned1, aligned2, score_matrix


if __name__ == "__main__":
    # Test case
    seq1 = 'TACTTAG'
    seq2 = 'CACATTAA'

    # Execute the algorithm
    aligned1, aligned2, matrix = smith_waterman(seq1, seq2)

    print(f"Aligned Sequence 1: {aligned1}")
    print(f"Aligned Sequence 2: {aligned2}")
    print(f"Alignment Score:    {np.max(matrix)}")
    print("\nScoring Matrix:")
    print(matrix)