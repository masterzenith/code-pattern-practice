"""
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely
reconstructed from the array of sequences.
Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the
array are subsequences of it.
Example 1:
I/P: original_seq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
O/P: true
Explanation: The sequences [1, 2], [2, 3] and [3, 4] can uniquely reconstruct [1, 2, 3, 4], in other words, all the
given sequences uniquely define the order of numbers in the 'original_seq'.

Example 2:
I/P: original_seq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
O/P: false
Explanation: The sequences [1, 2], [2, 3] and [2, 4] cannot uniquely reconstruct [1, 2, 3, 4].
            There are two possible sequences we can construct from the given sequences:
            1) [1, 2, 3, 4]
            2) [1, 2, 4, 3]

Example 3:
I/P: original_seq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
O/P: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct [3, 1, 4, 2, 5].

Time: In step 'd', each number can become a source only once and each edge (a rule) will be accessed and removed once.
    Therefore, the time complexity of the above algorithm will be O(V+E), where 'V' is the count of distinct numbers
    and 'E' is the total number of the rules. Since, at most, each pair of numbers can give us one rule, we can conclude
    that the upper bound for the rules is O(N) where 'N' is the count of numbers in all sequences. So, we can say that
    the time complexity of our algorithm is O(V+N)

Space: The space complexity will be O(V+N), since we are storing all of the rules for each number in an adjacency list.

"""
from collections import deque


def can_construct(original_seq, seqs):
    sorted_order = []
    if len(original_seq) <= 0:
        return False

    # a. Initialize the graph
    in_degree = {}  # count of incoming edges
    graph = {}  # adjacency list graph
    for seq in seqs:
        for num in seq:
            in_degree[num] = 0
            graph[num] = []

    # b. Build the graph
    for seq in seqs:
        for i in range(1, len(seq)):
            parent, child = seq[i-1], seq[i]
            graph[parent].append(child)
            in_degree[child] += 1

    # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
    if len(in_degree) != len(original_seq):
        return False

    # c. Find all sources i.e., all vertices with 0 in_degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # d. For each source, add it to the sorted_order and subtract one from all of its children's in_degrees
    # if a child's in_degree becomes zero, add it to the sources queue
    while sources:
        if len(sources) > 1:
            return False    # more than one sources mean, there is more than one way to reconstruct the sequence
        if original_seq[len(sorted_order)] != sources[0]:
            # the next source(or number) is different from the original sequence
            return False

        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:     # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # if sorted_order's size is not equal to original sequence's size, there is no unique way to construct
    return len(sorted_order) == len(original_seq)


def main():
    print("Can Construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can Construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can Construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


if __name__ == "__main__":
    main()

