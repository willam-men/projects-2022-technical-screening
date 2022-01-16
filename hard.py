"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
import json

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    total_uoc = len(courses_list) * 6
    # print(total_uoc)

    target_conditions = CONDITIONS[target_course]

    # no courses required
    if target_conditions == "":
        return True

    if "and" in target_conditions.lower():
        target_conditions = target_conditions.split('AND')
        print(target_conditions)
        for targets in target_conditions:
            print(targets)
            for courses in courses_list:
                print(courses)
                if courses not in targets: 
                    return False
            
    target_conditions = target_conditions.split(" ")

    if "or" in target_conditions:
        for courses in courses_list:
            if courses in target_conditions:
                return True

    # certain number of credits required
    if "credit" in target_conditions: 
        # extract the number of credits required
        for word in target_conditions:
            if word.isdigit():
                credit = int(word)
        # print(credit)
        # if there is not enough credits return False
        if total_uoc >= credit:
            return True
        else: 
            return False
        
    for courses in courses_list:
        if courses in target_conditions:
            return True

    # TODO: COMPLETE THIS FUNCTION!!!
    # print(CONDITIONS[target_course])
    # print(courses_list)
    # print(target_course)

    
    return False

if __name__ == "__main__":
    print(is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521"], "COMP4161"))
    # is_unlocked(["ELEC2141"], "COMP3211")
    # is_unlocked(["COMP1511", "COMP1521", "COMP1531"], "COMP3153")



    