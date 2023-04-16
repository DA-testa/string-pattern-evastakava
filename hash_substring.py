# python3

def read_input():

    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        with open(input().rstrip()) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

   # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function


def print_occurrences(output):

    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    p = 10**9 + 7
    x = 263
    occurrences = []
    m = len(pattern)
    n = len(text)
    if n < m:
        return occurrences
    p_hash = hash_string(pattern, p, x)
    H = precompute_hashes(text, m, p, x)
    for i in range(n - m + 1):
        if p_hash != H[i]:
            continue
        if pattern == text[i:i+m]:
            occurrences.append(i)

    return occurrences


def hash_string(s, p, x):
    h = 0
    for c in reversed(s):
        h = (h * x + ord(c)) % p
    return h

def precompute_hashes(text, m, p, x):
    n = len(text)
    H = [0] * (n - m + 1)
    s = text[n-m:]
    H[n-m] = hash_string(s, p, x)
    y = 1
    for i in range(m):
        y = (y * x) % p
    for i in range(n - m - 1, -1, -1):
        prehash = x * H[i+1] + ord(text[i]) - y * ord(text[i+m])
        H[i] = prehash % p
    return H


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

