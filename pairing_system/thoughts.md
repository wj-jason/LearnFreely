# Pairing Algorithm

GOAL: Create a function, that given a student, returns "compatability" scores over all tutors.

We first need a way to encode each course as a unique variable.
- we can use the first letter followed first number to denote level.
- To account for AP/IB, add an extra letter denoting the class type (A, I, or N for none)
- Chemistry 3200 -> CN3
- IB English 4238 -> EI4
