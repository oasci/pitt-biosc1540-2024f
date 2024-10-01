<h1 align="center">
A04
</h1>

<p style="text-align: center;">
    <object hspace="50">
        <strong>Due</strong></a>: Sep 27, 2024 by 11:59 p.m.
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

??? success "Solution"

    Adding the `$` symbol (or any distinct end-of-string marker) at the end of a string is a crucial step when constructing **suffix arrays** and the **Burrows-Wheeler Transform (BWT)**.
    Without the `$` symbol, constructing accurate and efficient suffix arrays and performing the BWT would be problematic, leading to ambiguities and potential errors in applications that depend on these techniques.
    This special character plays several important roles that ensure the correct and efficient functioning of these data structures and algorithms.

    **Unique Termination of the String**

    - **Avoiding Ambiguity:** In the context of suffix arrays and BWT, suffixes of a string are sorted lexicographically. Without a unique termination symbol like `$`, one suffix could be a prefix of another, leading to ambiguities in ordering. For example, consider the string `"banana"`:
        - Suffixes: `"banana"`, `"anana"`, `"nana"`, `"ana"`, `"na"`, `"a"`
        - Without `$`, the suffix `"a"` is a prefix of `"ana"`, `"anana"`, and `"banana"`, making it unclear how to order them uniquely.
    - **Defining End Boundaries:** The `$` symbol clearly marks the end of the string, ensuring that every suffix is distinct. For example:
        - With `$`: `"banana$"`, `"anana$"`, `"nana$"`, `"ana$"`, `"na$"`, `"a$"`, `"$"`
        - Now, each suffix has a distinct end, eliminating any ambiguity in their ordering.

    **Ensuring Lexicographical Order**

    - **Consistent Ordering:** The `$` symbol is typically defined to be lexicographically smaller than any other character in the string. This ensures that the suffix starting with `$` (i.e., the `$` itself) will always appear first in the sorted order of suffixes. This consistent ordering is essential for algorithms that rely on the first and last elements, such as BWT.
    - **Boundary Conditions:** In BWT, the first and last columns of the transformed matrix have special significance. The presence of `$` ensures that these boundary conditions are well-defined and that the transformation can be reversed correctly.

    **Facilitating Reversal and Decoding**

    - **Uniqueness for Reversal:** The BWT is a reversible transformation, meaning you can reconstruct the original string from its BWT.
        The `$` symbol plays a vital role in this reversal process by providing a unique starting point. Without a unique end marker, it would be challenging to determine where the original string starts and ends.
    - **Unambiguous Parsing:** During the decoding process, the algorithm looks for the `$` symbol to identify the end of the string.
        This unambiguous marker ensures that the reconstruction process can correctly determine the sequence of characters.

    **Optimizing Data Structures**

    - **Efficient Sorting and Searching:** In suffix arrays, having a unique termination symbol simplifies the sorting process of suffixes. It ensures that all suffixes are of different lengths and can be compared without running into issues where one suffix is a prefix of another.
    - **Simplifying Data Structures:** The presence of `$` allows certain optimizations in data structures like the suffix tree or the suffix array. It can reduce the complexity of algorithms by providing a clear stopping point.

    **Practical Applications and Standards**

    - **Standard Practice:** In many implementations and theoretical treatments of suffix arrays and BWT, appending a unique end-of-string symbol like `$` is standard practice. This consistency aids in interoperability and understanding across different systems and implementations.
    - **Error Prevention:** Forgetting to append the `$` symbol can lead to subtle bugs and incorrect behavior in applications that rely on suffix arrays or BWT, such as data compression algorithms (e.g., bzip2) and bioinformatics tools (e.g., genome sequence analysis).

    **Illustrative Example**

    Let's consider the string `"banana"` and see the difference with and without the `$` symbol when constructing a suffix array and BWT.

    !!! example "Without `$`"

        **Suffixes:**

        1. `banana`
        2. `anana`
        3. `nana`
        4. `ana`
        5. `na`
        6. `a`

        **Sorted Suffixes:**

        1. `a`
        2. `ana`
        3. `anana`
        4. `banana`
        5. `na`
        6. `nana`

        **Issues:** Ambiguity in ordering as `"a"` is a prefix of `"ana"`, `"anana"`, and `"banana"`.

    !!! example "With `$`"

        - **String:** `banana$`

        **Suffixes:**

        1. `banana$`
        2. `anana$`
        3. `nana$`
        4. `ana$`
        5. `na$`
        6. `a$`
        7. `$`

        **Sorted Suffixes:**

        1. `$`
        2. `a$`
        3. `ana$`
        4. `anana$`
        5. `banana$`
        6. `na$`
        7. `nana$`

        **Advantages:**

        - Each suffix is uniquely identifiable.
        - Clear lexicographical order without ambiguity.

        **BWT Construction:** The last characters of the sorted suffixes form the BWT: `annb$aa`

## Q06

Create a suffix array for the string "mississippi$" and show your work.
Present the suffix array as a list of starting indices.

??? success "Solution"

    First, let's list out the string with its corresponding **0-based** indices:

    Index | Character
    ------|----------
    0   | m
    1   | i
    2   | s
    3   | s
    4   | i
    5   | s
    6   | s
    7   | i
    8   | p
    9   | p
    10   | i
    11   | $

    A **suffix** is a substring that starts at a particular index and extends to the end of the string.
    Let's list all possible suffixes of `mississippi$` along with their starting indices:

    | Starting Index | Suffix         |
    |----------------|----------------|
    | 0              | mississippi$   |
    | 1              | ississippi$    |
    | 2              | ssissippi$     |
    | 3              | sissippi$      |
    | 4              | issippi$       |
    | 5              | ssippi$        |
    | 6              | sippi$         |
    | 7              | ippi$          |
    | 8              | ppi$           |
    | 9              | pi$            |
    | 10             | i$             |
    | 11             | $              |

    Next, we sort the suffixes in **lexicographical order**.
    Here's how the sorting proceeds:

    1. **$**: The dollar sign is typically considered lexicographically smaller than any other character.
    2. **i$**: Starts with 'i'.
    3. **ippi$**: Starts with 'i', followed by 'p'.
    4. **issippi$**: Starts with 'i', followed by 's'.
    5. **ississippi$**: Starts with 'i', followed by 's', then another 's'.
    6. **mississippi$**: Starts with 'm'.
    7. **pi$**: Starts with 'p'.
    8. **ppi$**: Starts with 'p', followed by another 'p'.
    9. **sippi$**: Starts with 's', followed by 'i'.
    10. **sissippi$**: Starts with 's', followed by 'i'.
    11. **ssippi$**: Starts with 's', followed by 's'.
    12. **ssissippi$**: Starts with 's', followed by 's', followed by 'i'.

    Here's the sorted list:

    | Sorted Order | Starting Index | Suffix         |
    |--------------|-----------------|----------------|
    | 1            | 11              | $              |
    | 2            | 10              | i$             |
    | 3            | 7               | ippi$          |
    | 4            | 4               | issippi$       |
    | 5            | 1               | ississippi$    |
    | 6            | 0               | mississippi$   |
    | 7            | 9               | pi$            |
    | 8            | 8               | ppi$           |
    | 9            | 6               | sippi$         |
    | 10           | 3               | sissippi$      |
    | 11           | 5               | ssippi$        |
    | 12           | 2               | ssissippi$     |

    The **suffix array** is a list of the starting indices of the sorted suffixes.
    Based on the sorted order above, the suffix array for `"mississippi$"` is:

    ```text
    [11, 10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]
    ```

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
