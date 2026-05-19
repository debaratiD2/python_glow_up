'''
Union (| or union()): Combines the elements from both sets, excluding duplicates
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

'''
Intersection (& or intersection()): Returns a set containing only the elements that are common to both sets
'''
intersection_set = set1 & set2
print(intersection_set)

'''
Difference (- or difference()): Returns a set containing the elements that are in the first set but not in the second set
'''
difference_set = set1 - set2
print(difference_set)

'''
Symmetric Difference (^ or symmetric_difference()): Returns a set containing the elements that are in either of the sets, but not in both
'''
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)

def set_operations(set1, set2):
    
    union_result = set1 | set2

    
    intersection_result = set1 & set2

    
    difference_result =set1 - set2

    symmetric_difference_result = set1 ^ set2

    return {
        "union": union_result,
        "intersection": intersection_result,
        "difference": difference_result,
        "symmetric_difference": symmetric_difference_result
    }

#intersection of multiple sets: intersection()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set3 = {5, 6, 7}

intersection_result = set1 & set2 & set3
# Or
intersection_result = set1.intersection(set2, set3)
print(intersection_result)

#difference of multiple sets: difference()
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set3 = {5, 6, 7}

difference_result = set1 - set2 - set3
# Or
difference_result = set1.difference(set2, set3)
print(difference_result)

#subset: <= or issubset() 
set1 = {1, 2}
set2 = {1, 2, 3}
is_subset = set1 <= set2
print(is_subset)

#proper subset: <
set1 = {1, 2}
set2 = {1, 2, 3}
is_proper_subset = set1 < set2
print(is_proper_subset)

set1 = {1, 2, 3}
set2 = {1, 2}
is_superset = set1 >= set2
print(is_superset)

#proper superset: >
set1 = {1, 2, 3}
set2 = {1, 2}
is_proper_superset = set1 > set2
print(is_proper_superset)

#example
def check_sets(set1, set2):
    # Check if set1 is a subset of set2
    is_subset = set1.issubset(set2)

    # Check if set2 is a superset of set1
    is_superset = set2 >= set1

    # Check if set1 is a proper subset of set2
    is_proper_subset = set1 < set2

    # Check if set2 is a proper superset of set1
    is_proper_superset = set2 > set1

    # Return a dictionary containing the results
    return {
        "is_subset": is_subset,
        "is_superset": is_superset,
        "is_proper_subset": is_proper_subset,
        "is_proper_superset": is_proper_superset
    }