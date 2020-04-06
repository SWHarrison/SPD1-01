"""
https://leetcode.com/problems/course-schedule-ii/
Problem is to take list of classes and prerequisites and create
any schedule that fulfills all requirements.

No questions.

Assumptions:
Courses can exists with no prerequisites or postrequisites
meaning they can be done at any time.

Possible solutions:
Loop through list until all classes are are added, and only add
classes if all prerequisites have been fulfilled. Would take
quadratic worst time if courses came in reverse order.

Since this problem can be represented as a graph, we can use tools
such as DFS to find courses instead, which would take close to linear time, but
use more memory.

One improvement that can be made to the code below is to add any course with no
prerequisites or postrequisites immediately after the dictionary creation.
"""

def course_schedule(numCourses, prerequisites):

    courses = {}

    # set up dictionary of courses with prereqs and classes it is a prereq for
    for course in prerequisites:

        # if class needing pre req in courses
        if course[0] in courses:
            courses[course[0]][0].append(course[1])
        else:
            courses[course[0]] = [[],[]]
            courses[course[0]][0].append(course[1])
        if course[1] in courses:
            courses[course[1]][1].append(course[0])
        else:
            courses[course[1]] = [[],[]]
            courses[course[1]][1].append(course[0])


    for i in range(numCourses):
        if not i in courses:
            courses[i] = [[],[]]

    print(courses)

    course_schedule = []
    courses_taken = set()

    for course in courses:

        #print("current course schedule:", course_schedule)
        if not course in courses_taken:

            courses_to_add = helper(courses_taken, courses, course)
            #print("adding",courses_to_add, "to", course_schedule)
            course_schedule += courses_to_add

    if len(course_schedule) < numCourses:
        return []
    return course_schedule

def helper(courses_taken, courses, course):

    #print("current course:", course)
    #print("all courses taken:", list(courses_taken))
    to_return = []
    curr_course_pre_reqs = courses[course][0]
    curr_course_is_pre_req_for = courses[course][1]

    if curr_course_pre_reqs == 0:
        #print("adding",course)
        to_return.append(course)
        courses_taken.add(course)
    else:
        all_taken = True
        for pre_req in curr_course_pre_reqs:
            if not pre_req in courses_taken:
                all_taken = False
                break
        if all_taken:
            #print("adding",course)
            to_return.append(course)
            courses_taken.add(course)

    if course in courses_taken:

        for future_course in curr_course_is_pre_req_for:

            # if future course not in classes taken, start DFS
            if not future_course in courses_taken:

                to_return += helper(courses_taken, courses, future_course)
    #print("returning",to_return)
    return to_return


classes = [[1,0],[2,1],[3,1],[4,2],[4,3],[2,5]]
#classes = [[1,0],[1,2],[0,1]]
num = 6

print(course_schedule(num,classes))
