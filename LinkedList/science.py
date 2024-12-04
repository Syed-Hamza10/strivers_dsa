from itertools import permutations

def solve_librarian_problem(test_cases):

    arrangements = sorted(permutations(['S', 'F', 'H']))
    
    results = []
    
    for books in test_cases:

        S1, F1, H1, S2, F2, H2, S3, F3, H3 = books
        total_books = S1 + F1 + H1 + S2 + F2 + H2 + S3 + F3 + H3
        
        min_moves = float('inf')
        best_arrangement = None
        
        for arrangement in arrangements:

            stack1, stack2, stack3 = arrangement
            
            books_in_position = 0
            if stack1 == 'S':
                books_in_position += S1
            elif stack1 == 'F':
                books_in_position += F1
            elif stack1 == 'H':
                books_in_position += H1

            if stack2 == 'S':
                books_in_position += S2
            elif stack2 == 'F':
                books_in_position += F2
            elif stack2 == 'H':
                books_in_position += H2

            if stack3 == 'S':
                books_in_position += S3
            elif stack3 == 'F':
                books_in_position += F3
            elif stack3 == 'H':
                books_in_position += H3
            
            moves = total_books - books_in_position
            
            if moves < min_moves or (moves == min_moves and arrangement < best_arrangement):
                min_moves = moves
                best_arrangement = arrangement
        
        results.append((''.join(best_arrangement), min_moves))
    
    return results

t = int(input())
test_cases = [list(map(int, input().split())) for _ in range(t)]

results = solve_librarian_problem(test_cases)

for arrangement, moves in results:
    print(arrangement, moves)
