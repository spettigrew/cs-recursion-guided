"""
You are a new author that is working on your first book. You are working on a
series of drafts. Each draft is based on the previous draft. The latest draft
of your book has a serious typo. Since each newer draft is based on the
previous draft, all the drafts after the draft containing the typo also include
the typo.

Suppose you have `n` drafts `[1, 2, 3, ..., n]` and you need to find out the
first one containing the typo (which causes all the following drafts to have
the typo as well).

You are given access to an API tool `containsTypo(draft)` that will return
`True` if the draft contains a typo and `False` if it does not.

You need to implement a function that will find the *first draft that contains
a typo*. Also, you have to pay a fee for every call to `containsTypo()`, so
make sure that your solution minimizes the number of API calls.

Example:

Given `n = 5`, and `draft = 4` is the first draft containing a typo.

containsTypo(3) -> False
containsTypo(5) -> True
containsTypo(4) -> True
"""
def firstDraftWithTypo(n):
    # Your code here
    # [ draft1, draft2, draft3, draft4, draft n-1, draft n]
    # if we find the draft with the typo, the first draft withthe typo (target) is before the current draft
    # if current draft does not have the typo, the first draft with the typo is after the current draft. 
    
    
    # find middle index within the min and max indices
    #if the middle is the rotation point:
        # middle is rotation if the prev element > current_element
    # else:
        # rotated yet?
        # we can tell that by comparing the first element in the array.
    # if current_element >= first_element: still need to rotate.
        # search right
        # move the min index to middle + 1
    # else if current element < first element: we have rotated
        # search left:
        # move the max index to the middle index
    # Keep going until max and min cross

# start w/ min and max
    min = 0
    max = n

    while not max <= min:
        guess = (min + max) // 2
        contains_typo = containsTypo(guess)
        if contains_typo:
            # the first draft w/ the typo is before our guess
            # look left
            # we could check if it's the first draft by calling containsTypo(guess - 1)
            # if not containsTypo(guess - 1):
            #     return guess
            # move max to the guess value
            max = guess - 1
        else:
            # current draft doesn't have a typo
            # so the first draft w/ typo is after our guess
            # look right
            # move min to guess + 1
            min = guess + 1
    # repeat
    return min

