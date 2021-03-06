'''
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as
arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course
A must be taken before course B. Return the minimum number of semesters required to complete all n courses.
There is no limit on how many courses you can take in a single semester, as long the prerequisites of a course
are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester.
You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.
'''


def semesters_required(num_courses, prereqs):
    distance = {}
    graph = create_graph(num_courses, prereqs)
    for course in graph:
        if len(graph[course]) == 0:
            distance[course] = 1

    for course in graph:
        traverse_distance(graph, course, distance)

    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    max_distance = 0
    for neighbor in graph[node]:
        neighbor_distance = traverse_distance(graph, neighbor, distance)
        if neighbor_distance > max_distance:
            max_distance = neighbor_distance
    distance[node] = max_distance + 1
    return distance[node]


def create_graph(num_courses, prereqs):
    graph = {}

    for course in range(num_courses):
        graph[course] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


num_courses = 7
prereqs = [
    (4, 3),
    (3, 2),
    (2, 1),
    (1, 0),
    (5, 2),
    (5, 6),
]
semesters_required(num_courses, prereqs)  # -> 5
