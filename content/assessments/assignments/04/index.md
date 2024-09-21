<h1 align="center">
A04
</h1>

<p style="text-align: center;">
    <object hspace="50">
        <strong>Due</strong></a>: Sep 26, 2024 by 11:59 p.m.
    </object>
    <object hspace="50">
        <strong>Points</strong></a>: 60
    </object>
</p>

## Q01

Compare and contrast genomics and transcriptomics in terms of:

-   The type of information they provide;
-   The frequency of sampling required;
-   Their ability to capture cellular responses.

## Q02

Compare RNA-seq to microarray technology.
What are the key advantages of RNA-seq?

## Q03

What is the RNA Integrity Number (RIN)?
How is it measured and why is it important in RNA-seq experiments?
Describe what a low RIN indicates about a sample.

## Q04

Describe the process of mRNA enrichment in RNA-seq experiments.
Why is this step important, and how does it affect the resulting data?

## Q05

Explain why adding the `$` symbol at the end of the string is important when constructing suffix arrays and Burrows-Wheeler Transform.

## Q06

Create a suffix array for the string "mississippi$" and show your work.
Present the suffix array as a list of starting indices.

## Q07

Why is the BWT useful for compression?
Explain with an example.

## Q08

Perform the Burrows-Wheeler Transform (BWT) for the following DNA sequence: `ATTGCATTTGGCA`.
Show your work (including the matrix) and specify what is the output.

**a)** Without performing the full LF-mapping, explain how you would start searching for the pattern `ATT` in this BWT.
What would be your initial range in the F column, and what character would you look for first in the L column?

**b)** The sequence contains both `TTT` and `TGC`.
Without doing the full LF-mapping, explain which of these patterns would likely be easier to search for using the BWT, and why.

**c)** How does the presence of unique substrings (like `GCA`) in the original sequence affect the structure of the BWT?
Explain why we see certain patterns in the BWT string.

## Q09

Reverse the Burrows-Wheeler Transform output `BBAAB$AABA` to get the original string.
What is the original string?
Show all of your steps.

## Programming+

These problems are not required and will not impact your BIOSC 1540 grade.
The instructor will assess these separately to validate correctness without an assigned grade.
Thus, you may work on these problems individually or in a team-based setting and "due" by the end of the semester.
Happy coding!

**Acceptable languages**: Python v3.10+

!!! success "Rewards"
    Engaging with these optional programming problems offers several valuable academic and professional growth opportunities.

    -   Consistent engagement with these **Programming+** problems will allow me to write more detailed, compelling recommendation letters highlighting your computational skills.
    These personalized letters can significantly boost your applications for future academic programs, internships, or job opportunities.
    -   If there is enough interest, optional Friday recitations will be provided.
    This will give you individualized attention to accelerate learning and actionable feedback on your code and problem-solving approaches.
    -   Exceptional solutions may be featured on our course website with the students' permission. This is a way for us to recognize and appreciate your hard work and dedication to these problems.

!!! note
    These problems would be similar to ones given in a major-only version of the class.
    Although, there would be more relevant instructions during class and would be given more than a week to complete.

### P01

Implement a function that creates a suffix array for a given string.

**Function Signature:**

```python
def create_suffix_array(s: str) -> List[str]:
```

**Requirements:**

1.  The input string `s` will not always end with a `$` character.
2.  Use Python's built-in sorting function.
3.  Return a list of all suffixes of the input string, sorted lexicographically.
4.  Include the empty suffix (represented by `$`) in the output.
5.  Return the actual suffixes as strings, not their starting positions.

**Example:**

```python
Input: "banana$"
Output: [`$`, 'a$', 'ana$', 'anana$', 'banana$', 'na$', 'nana$']
```

### P02

Implement two functions: one to perform the Burrows-Wheeler Transform (BWT) and another to inverse the transform.

**Function Signature:**

```python
def bwt(s: str) -> str:
def inverse_bwt(bwt: str) -> str:
```

**Requirements:**

1.  For `bwt(s)`:
    -   The input string `s` will not always end with a `$` character.
    -   Use a simple approach, such as sorting all rotations of the string.
    -   Return the last column of the sorted rotation matrix as the BWT.
2.  For `inverse_bwt(bwt)`:
    -   The input `bwt` is a BWT-transformed string.
    -   Reconstruct and return the original string that produced the given BWT.
3.  Ensure that `inverse_bwt(bwt(s)) == s` for any valid input `s`.

**Example:**

```python
bwt("banana$") → "annb$aa"
inverse_bwt("annb$aa") → "banana$"
```

### P03

Implement a function that performs pattern searching using a Burrows-Wheeler transformed string.

**Function Signature:**

```python
def bwt_search(bwt: str, pattern: str) -> List[int]:
```

**Requirements:**

1.  The `bwt` input is a Burrows-Wheeler transformed string.
2.  Implement the backward search algorithm using the BWT.
3.  Return a list of integers representing the starting positions (0-indexed) of all occurrences of the pattern in the original text.
4.  Return an empty list if the pattern is not found.
5.  Correctly handle overlapping occurrences of the pattern.
6.  Implement necessary helper functions (e.g., for counting occurrences).

**Example:**

```python
bwt_search("annb$aa", "ana") → [1, 3]
```

**Hints:**

-   You may find it helpful to implement additional helper functions, such as:
    -   A function to compute the First column (F) from the Last column (L) of the BWT matrix.
    -   A function to perform the Last-to-First (LF) mapping.
    -   A function to count occurrences of characters in a prefix of the BWT string.
-   Remember that the BWT string represents the last column of the sorted rotation matrix of the original string.
-   The backward search algorithm involves iteratively narrowing down the range of rows in the BWT matrix that match the pattern, starting from the last character of the pattern.
