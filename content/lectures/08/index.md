<h1 align="center">
<b>Lecture 08</b><br>
Read mapping
</h1>
<p align="center">
<b>Date:</b> Sep 19, 2024
</p>

!!! danger "DRAFT"

    This page is a work in progress and is subject to change at any moment.

We'll explore the challenges of aligning millions of short reads to a reference genome and discuss various algorithms and data structures that make this process efficient.
The session will focus on the Burrows-Wheeler Transform (BWT) and the FM-index, two key concepts that revolutionized read alignment by enabling fast, memory-efficient sequence searching.
We'll examine how these techniques are implemented in popular alignment tools and compare their performance characteristics.

## Learning objectives

What you should be able to do after today's lecture:

1.  Describe the challenges of aligning short reads to a large reference genome.
2.  Compare read alignment algorithms, including hash-based and suffix tree-based approaches.
3.  Explain the basic principles of the Burrows-Wheeler Transform (BWT) for sequence alignment.
4.  Discuss the FM-index and how it enhances the efficiency of BWT-based alignments.

## Readings

Relevant content for today's lecture.

-   Burrows-Wheeler transform
    -   [Omics website](https://omics.crumblearn.org/appendices/algorithms/compression/bwt/)
    -   [JHU](https://www.cs.jhu.edu/~langmea/resources/lecture_notes/10_bwt_and_fm_index_v2.pdf)
-   FM-index
    -   [Omics website](https://omics.crumblearn.org/appendices/algorithms/search/fm-index)
-   Suffix trees
    -   [JHU](https://www.cs.jhu.edu/~langmea/resources/lecture_notes/08_suffix_trees_v2.pdf)
-   Suffix arrays
    -   [JHU](https://www.cs.jhu.edu/~langmea/resources/lecture_notes/09_suffix_arrays_v2.pdf)

## Presentation

<!-- -   **View:** [slides.com/aalexmmaldonado/biosc1540-l08](https://slides.com/aalexmmaldonado/biosc1540-l08) -->
-   **Live link:** [slides.com/d/v69HoBk/live](https://slides.com/d/v69HoBk/live)
<!-- -   **Download:** [biosc1540-l08.pdf](/lectures/08/biosc1540-l08.pdf) -->

<iframe src="https://slides.com/aalexmmaldonado/biosc1540-l08/embed?byline=hidden&share=hidden" width="100%" height="600" title="BIOSC 1540: Lecture 08" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
