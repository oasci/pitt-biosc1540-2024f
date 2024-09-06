<h1 align="center">
<b>Lecture 04</b><br>
De novo genome assembly
</h1>
<p align="center">
<b>Date:</b> Sep 5, 2024
</p>

This lecture aims to provide a thorough understanding of de novo assembly techniques, their applications, and their crucial role in advancing genomic research.

## Learning objectives

What you should be able to do after today's lecture:

1.  Explain the fundamental challenge of reconstructing a complete genome.
2.  Describe and apply the principles of the greedy algorithm.
3.  Understand and construct de Bruijn graphs.

## Readings

Relevant content for today's lecture.

-   [Greedy algorithm](https://omics.crumblearn.org/genomics/assembly/de-novo/greedy/)
    -   [JHU](https://www.cs.jhu.edu/~langmea/resources/lecture_notes/16_assembly_scs_v2.pdf)
-   de Bruijn
    -   [JHU](https://www.cs.jhu.edu/~langmea/resources/lecture_notes/17_assembly_dbg_v2.pdf)
    -   [JHU2](https://www.cs.jhu.edu/~langmea/resources/lecture_notes/19_assembly_dbg2_v2.pdf)
    -   [Why are de Bruijn graphs useful for genome assembly?](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5531759/)
    -   [Read mapping on de Bruijn graphs](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-1103-9)
    -   [Galaxy](https://training.galaxyproject.org/training-material/topics/assembly/tutorials/debruijn-graph-assembly/slides-plain.html)
    -   [Data science for HTS](https://data-science-sequencing.github.io/Win2018/lectures/lecture7/)

## Presentation

-   **Live link:** [slides.com/d/KOit8yE/live](https://slides.com/d/KOit8yE/live)
-   **Download:** [biosc1540-l04.pdf](/lectures/04/biosc1540-l04.pdf)

<iframe src="https://slides.com/aalexmmaldonado/biosc1540-l04/embed?byline=hidden&share=hidden" width="100%" height="600" title="BIOSC 1540: Lecture 04" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

<!--

- Students were not really engaged with hands-on practice. I guess this is fine since they can practice it later.
- I ended early, so if I take out the activities, I certainly have time to add in a galaxy activity or the OLC.
- I had a good question about why we take k-mers, then make k-1 mers for nodes. Why not just straightly make k-1 mer nodes.
- I'm not sure it was useful to include the error correction.
- I think I need to add in a little more information about how actual assemblers build contigs from de bruijn graphs. For example, graph traversal using depth-first earch or Eulerian path algorithm. Handling branches, handling repeats. Maybe we should talk about how spades does it.
- I'm also confused on if graphs need to have Eulerian walks.
- I'm not sold on the notation of k mers for length of nodes or edges.

 -->
