#Patrick Duong
#ptd4npb



gradebook = {}
# assignment_counts = {}
denominator = {}
# total_count = 0

def assignment(kind,grade, weight = 1):
    """
    add running total grade for given kind, with different running total for each kind stored in a dict
    :param kind: str, indicate which group of assignments this one belongs to 
    :param grade: number from 0 to 100 
    :param weight: optional, indicates how much weight this assignment has compared to others of same kind
    :return: running total for each kind 
    """
    if kind not in gradebook:
        denominator[kind] = weight
        gradebook[kind] = grade

    elif kind in gradebook:
        denominator[kind] += weight
        temp_average = (gradebook[kind] * (denominator[kind]-weight) + weight * grade)/denominator[kind]
        gradebook[kind] = temp_average
        # print(denominator)

    # print(gradebook)


# MAYBE MAKE A LIST HOLDING ON THE WEIGHTS, REFERENCE THE LIST TO KNOW HOW TO GET THE AVERAGES


def total(proportions):
    """
    return cumulative grade so far based on given set of proportions (weights of each type of assignment)
    :param proportions: weights of each class, all should add to 1
    :return: cumulative grade
    """
    cumulative_grade = 0
    # print(proportions)
    for each in proportions:
        print(each)
        if each not in gradebook:
            gradebook[each] = 0
            denominator[each] = 0

        else:
            cumulative_grade += proportions[each] * gradebook[each]

    return cumulative_grade

# assignment("test", 100, 2)
# assignment("test", 80, 3)
# assignment("test", 90)
#
# assignment("project", 20, 2)
# assignment("project", 40, 1.5)
# assignment("project", 80, 3)
#
