"""
Topological Sort
You're given a list of arbitrary jobs that need to be completed; these jobs are represented by distinct integers. You're
also given a list of dependencies. A dependency is represented as a pair of jobs where the first job is a prerequisite
of the second one. In other words, the second job depends on the first one; it can only be completed once the first job
is completed.
Write a function that takes in a list of jobs and a list of dependencies and returns a list containing a valid order in
which the given jobs can be completed. If no such order exists, the function should return an empty array.
Sample Input:
jobs = [1, 2, 3, 4]
deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
Sample Output:
[1, 4, 3, 2] or [4, 1, 3, 2]

Hints:
1. Try representing the jobs and dependencies as a graph, where each vertex is a job and each edge is a dependency. How
can you traverse this graph to topologically sort the list of jobs?
2. One approach to solving this problem is to traverse the graph mentioned in Hint #1 using Depth-first Search. Starting
at a random job, traverse its prerequisite jobs in Depth-first Search fashion until you reach a job with no prerequisites;
such a job can safely be appended to the final order. Once you've traversed and added all prerequisites of a job to the
final order, you can append the job in question to the order. This approach will have to track whether nodes have been
traversed already, whether they're in the process of being traversed (which would indicate a cycle in the graph and
therefore no valid topological order), or whether they're ready to be traversed.
3. Another approach to solving this problem is to traverse the graph mentioned in Hint #1 starting specifically with jobs
that have no prerequisites. Keep track of all the jobs that have no prerequisites, traverse them one by one, and append
them to the final order. For all of these jobs, remove their dependencies from the graph and update the number of prerequisites
for each of these dependencies accordingly (these dependencies should now have one prerequisite less since one of their
prerequisite job has just been added to the final order). As you update the number of prerequisites for these other jobs,
keep track of the ones that no longer have prerequisites and that are ready to be traversed. You'll eventually go through
all the jobs if there are no cycles in the graph. If there is a cycle in the graph, there will still be jobs with
prerequisites and you'll know that there is no valid topological order. This approach will involve keeping track of the
number of prerequisites per job as well as all the actual dependencies of each job.

Optimal Space & Time Complexity
O(j + d) time | O(j + d) space - where j is the number of jobs and d is the number of dependencies

https://github.com/das-jishu/algoexpert-data-structures-algorithms/blob/master/Hard/topological-sort.py
"""


class JobNode:
    def __init__(self, job):
        self.job = job
        self.prereqs = []
        self.visited = False
        self.visiting = False


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.add_node(job)

    def add_prereq(self, job, prereq):
        job_node = self.get_node(job)
        prereq_node = self.get_node(prereq)
        job_node.prereqs.append(prereq_node)

    def add_node(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def get_node(self, job):
        if job not in self.graph:
            self.add_node(job)
        return self.graph[job]


def topological_sort(jobs, deps):
    job_graph = create_job_graph(jobs, deps)
    return get_ordered_jobs(job_graph)


def create_job_graph(jobs, deps):
    graph = JobGraph(jobs)
    for prereq, job in deps:
        graph.add_prereq(job, prereq)
    return graph


def get_ordered_jobs(graph):
    ordered_jobs = []
    nodes = graph.nodes
    while len(nodes):
        node = nodes.pop()
        contains_cycle = depth_first_traverse(node, ordered_jobs)
        if contains_cycle:
            return []
    return ordered_jobs


def depth_first_traverse(node, ordered_jobs):
    if node.visited:
        return False
    if node.visiting:
        return True

    node.visiting = True
    for prereq_node in node.prereqs:
        contains_cycle = depth_first_traverse(prereq_node, ordered_jobs)
        if contains_cycle:
            return True
        node.visited = True
        node.visiting = False
        ordered_jobs.append(node.job)
    return False


def main():
    jobs = [1, 2, 3, 4]
    deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    # job_graph = JobGraph

    print(topological_sort(jobs, deps))


if __name__ == "__main__":
    main()
