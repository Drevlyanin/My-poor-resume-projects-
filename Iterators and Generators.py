""" 
I will continue to add my solutions to interesting task.

https://stepik.org/lesson/24464/step/4?unit=6769

In this problem, we ask you to implement a multifilter class that will perform the same function as the standard filter class, but will use several functions instead of one.
The decision to allow an element will be made based on how many functions allow the element and how many do not. Let's denote these quantities as pos and neg.
Let's introduce the concept of a decision function - this is a function that takes two arguments - the numbers pos and neg, and returns True if the element is allowed, and False otherwise.
Let's consider the admission process in more detail in the following example.
a = [1, 2, 3]
f2(x) = x % 2 == 0
f3(x) = x % 3 == 0
judge_any(pos, neg) = pos >= 1
'''

def first(x):
    return x % 2 == 0

def second(x):
    return x % 3 == 0

def third(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

class multifilter:

    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        for element in self.iterable:
            pos = 0
            neg = 0
            for func in self.funcs:
                if func(element):
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg):
                yield element