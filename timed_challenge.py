# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
'''
2. Running Total with Reset
Track a running total of values. If a negative number is added, reset the total to 0.
Input: [5, 7, -1, 3, 2]
Output: [5, 12, 0, 3, 5]
'''

def running_total(input):
    if type(input)!=int:
        return 'List does not contain numbers'
    elif len(input)<1:
        return 'List is empty'
    final=[]
    count=0
    for item in input:
        if item>=0:
            count+=item
        else:
            count=0
        final.append(count)
    return final

print(running_total(['one','two','three'])) #testing line

'''
Reflection:
1. I chose to use a list because it's the easiest to iterate through, and this question required me to iterate 
through the entirety of the list.
2. Presuming that this question is asking how the time limit shaped my decision to answer this question in 
partiular, I just thought that this question seemed among the easiest, so I figured that, even if I couldn't 
immediately implement a solution, at least I would have plenty of time to think it through. I didn't think that 
it would be too difficult at a baseline, though, and, indeed, I did fully implement and finish testing a 
solution within 10 minutes.
3. I don't think that I made any compromises specifically under the pressure of being on a time limit. I think 
the thing that I struggled with most was deciding how the error message should be delivered if an empty list or 
a list that contained any variable type but ints was fed into the function. I thought that I should be 
consistent and write out the messages in a list, but I thought that that might be a bit too confusing, so I 
settled on just writing them out in a string.
'''
    