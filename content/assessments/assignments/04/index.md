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

??? success "Solution"

    In the field of molecular biology, **genomics** and **transcriptomics** are two pivotal disciplines that offer distinct yet complementary insights into the functioning of living organisms.
    While both are integral to understanding biological systems at the molecular level, they differ fundamentally in the type of information they provide, the frequency of sampling they necessitate, and their capacity to capture cellular responses.

    | **Aspect**                           | **Genomics**                                                                 | **Transcriptomics**                                                                 |
    |--------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
    | **Information Provided**            | Complete DNA sequence, gene locations, structural variations                  | Gene expression levels, splice variants, non-coding RNA expression                   |
    | **Stability**                        | Largely static across an organism's lifespan                                  | Highly dynamic, varies with time, conditions, and cell states                        |
    | **Sampling Frequency**               | Infrequent; typically one-time per individual or species                      | Frequent and time-resolved; multiple samples under different conditions               |
    | **Cellular Response Capture**        | Limited; provides potential response capabilities based on genetic makeup     | Comprehensive; captures real-time and dynamic changes in gene expression               |
    | **Applications**                     | Identifying genetic predispositions, evolutionary studies, personalized medicine | Understanding gene regulation, cellular responses, disease mechanisms, developmental processes |
    | **Technological Methods**            | Whole-genome sequencing, SNP genotyping, comparative genomics                  | RNA sequencing (RNA-Seq), microarrays, single-cell transcriptomics                     |

## Q02

Compare RNA-seq to microarray technology.
What are the key advantages of RNA-seq?

??? success "Solution"

    While microarray technology laid the groundwork for large-scale gene expression studies, RNA-Seq has emerged as a more powerful and versatile tool, offering comprehensive, sensitive, and precise insights into the transcriptome.
    Its ability to detect novel transcripts, provide higher dynamic range and specificity, and facilitate a deeper understanding of gene regulation positions RNA-Seq as the technology of choice for modern genomics research.
    As sequencing technologies continue to advance, the advantages of RNA-Seq are likely to further solidify its role in unraveling the complexities of gene expression and regulation.

    ---

    **Overview of Microarray Technology and RNA-Seq**

    **Microarray Technology:**
    Microarrays, introduced in the mid-1990s, revolutionized gene expression studies by allowing simultaneous measurement of thousands of genes. A microarray consists of a solid surface, typically a glass slide, onto which probes (short DNA sequences) corresponding to specific genes are fixed in an orderly grid. During an experiment, fluorescently labeled cDNA or cRNA derived from the sample's RNA is hybridized to the probes on the array. The intensity of fluorescence at each probe spot correlates with the expression level of the corresponding gene.

    **RNA Sequencing (RNA-Seq):**
    RNA-Seq, emerging in the late 2000s, leverages next-generation sequencing (NGS) technologies to provide a comprehensive and high-resolution view of the transcriptome. Unlike microarrays, RNA-Seq does not rely on predefined probes. Instead, it sequences the entire pool of RNA molecules (after conversion to cDNA) present in a sample, generating millions of short reads that are then aligned to a reference genome or assembled de novo. This approach enables both the quantification of gene expression and the discovery of novel transcripts, alternative splicing events, and other transcriptomic complexities.

    ---

    **Comparative Analysis: RNA-Seq vs. Microarrays**

    | **Feature**                 | **Microarrays**                                                   | **RNA-Seq**                                                      |
    |-----------------------------|-------------------------------------------------------------------|------------------------------------------------------------------|
    | **Detection Method**       | Hybridization of labeled RNA to fixed probes                      | Sequencing of cDNA fragments                                     |
    | **Dynamic Range**          | Limited (typically 2-3 orders of magnitude)                       | Broad (up to 6-7 orders of magnitude)                            |
    | **Sensitivity**            | Moderate; may miss low-abundance transcripts                      | High; can detect lowly expressed genes and rare transcripts      |
    | **Specificity**            | Dependent on probe design; potential cross-hybridization issues   | High; sequence-based, reducing cross-reactivity                   |
    | **Coverage**               | Limited to known genes and transcripts defined by probe set       | Comprehensive; includes known and novel transcripts               |
    | **Resolution**             | Gene-level; limited ability to detect isoforms                    | Nucleotide-level; can identify alternative splicing and variants |
    | **Quantification**         | Relative expression levels based on fluorescence intensity        | Absolute expression levels based on read counts                   |
    | **Cost**                   | Generally lower per sample for large-scale studies                | Initially higher, but costs have been decreasing                  |
    | **Data Analysis Complexity**| Relatively simpler bioinformatics requirements                   | More complex, requiring advanced bioinformatics tools             |
    | **Reproducibility**        | High within the same platform                                      | High, with consistency across different sequencing runs           |
    | **Scalability**            | Limited by the need for specific probes                           | Highly scalable with advancements in sequencing technologies      |

    ---

    **Key Advantages of RNA-Seq Over Microarrays**

    While both technologies have their merits, RNA-Seq offers several distinct advantages that make it the preferred choice for many contemporary gene expression studies:

    <u>Comprehensive Transcriptome Coverage</u>

    -   RNA-Seq does not rely on predefined probes, allowing the detection of previously unknown genes, non-coding RNAs, and novel splice variants. This capability is crucial for expanding our understanding of the transcriptomic landscape beyond what is currently annotated.
    -   RNA-Seq can identify and quantify different splice variants of genes, providing insights into the complexity of gene regulation and the functional diversity of proteins. Microarrays, limited by their probe design, often cannot distinguish between isoforms.

    <u>Enhanced Sensitivity and Dynamic Range</u>

    -   RNA-Seq's high sensitivity enables the detection of transcripts expressed at very low levels, which microarrays may fail to identify due to background noise and limited dynamic range.
    -   RNA-Seq can accurately quantify gene expression over a broad range of abundances, from very low to extremely high, without saturation issues inherent in microarray fluorescence measurements.

    <u>Higher Specificity and Accuracy</u>

    -   RNA-Seq relies on direct sequencing of RNA-derived cDNA, minimizing cross-hybridization issues that can occur with microarrays.
        This leads to more accurate and specific identification of transcripts.
    -   RNA-Seq provides nucleotide-level resolution, allowing for the detection of single nucleotide polymorphisms (SNPs), insertions, deletions, and other genetic variations within transcripts. Microarrays generally lack this level of detail.

    <u>Flexibility and Adaptability</u>

    -   RNA-Seq does not require the design and optimization of probes for each gene, making it more adaptable to studies involving non-model organisms or organisms with poorly annotated genomes.
    -   RNA-Seq can identify gene fusions, structural rearrangements, and other complex genomic alterations that are challenging to detect with microarrays.

    <u>Improved Quantification and Data Quality</u>

    -   RNA-Seq provides counts of reads mapping to each gene, offering a more direct and quantitative measure of gene expression compared to the relative fluorescence intensities of microarrays.
    -   The sequencing-based approach of RNA-Seq reduces background noise, enhancing the signal-to-noise ratio and improving the reliability of gene expression measurements.

    <u>Scalability and Technological Advancements</u>

    -   Advancements in sequencing technologies have continually increased the throughput and reduced the cost of RNA-Seq, making it increasingly accessible for large-scale studies.
    -   RNA-Seq data can be seamlessly integrated with other next-generation sequencing data types (e.g., DNA sequencing, ChIP-Seq), facilitating comprehensive multi-omics analyses.

    <u>Better Handling of GC Bias and Other Technical Variations</u>

    -   RNA-Seq protocols and bioinformatics tools have improved methods to account for GC content bias and other technical variations, leading to more uniform coverage across transcripts compared to microarrays.

    ---

    **Practical Implications of Choosing RNA-Seq Over Microarrays**

    The superior advantages of RNA-Seq translate into several practical benefits for researchers:

    - **Enhanced Discovery Potential:** The ability to uncover novel transcripts and splice variants opens new avenues for understanding gene function and regulation.
    - **Precision Medicine Applications:** Accurate detection of gene expression changes and genetic variants supports the development of personalized therapeutic strategies.
    - **Dynamic Range for Diverse Applications:** From studying highly expressed housekeeping genes to rare transcripts involved in specific biological processes, RNA-Seq accommodates a wide spectrum of expression levels.
    - **Future-Proofing Research:** As genomic annotations evolve, RNA-Seq data remains relevant and can be reanalyzed with updated references, whereas microarray data is constrained by the fixed probe sets used during the experiment.

    ---

    **Considerations and Challenges**

    Despite its numerous advantages, RNA-Seq also presents certain challenges:

    - **Data Analysis Complexity:** The vast amount of data generated by RNA-Seq requires robust computational infrastructure and expertise in bioinformatics for processing and analysis.

    - **Higher Initial Costs:** Although sequencing costs have decreased, RNA-Seq can still be more expensive than microarrays, especially for very large studies.

    - **Standardization Issues:** Variability in library preparation methods and sequencing platforms can introduce inconsistencies, necessitating standardized protocols for comparative studies.

## Q03

What is the RNA Integrity Number (RIN)?
How is it measured and why is it important in RNA-seq experiments?
Describe what a low RIN indicates about a sample.

??? success "Solution"

    The RNA Integrity Number (RIN) is a standardized numerical value ranging from 1 to 10 that quantifies the integrity of RNA within a biological sample. Developed by Agilent Technologies, the RIN provides an objective measure of RNA quality, with higher values indicating intact RNA and lower values signifying degraded RNA. The RIN facilitates the comparison of RNA quality across different samples and experiments, enabling researchers to make informed decisions about the suitability of RNA for downstream applications like RNA-seq.

    ---

    **How is RIN Measured?**

    RIN is determined using specialized instrumentation, such as the Agilent Bioanalyzer or similar systems that perform capillary electrophoresis.
    The measurement process involves several key steps:

    1. **Sample Preparation:**
        - **RNA Extraction:** RNA is first extracted from the biological sample using appropriate extraction methods to ensure purity and integrity.
        - **Quantification:** The concentration of RNA is quantified, often using spectrophotometric methods, to ensure that sufficient material is available for analysis.
    2. **Capillary Electrophoresis:**
        - **Loading the Sample:** A small volume of the RNA sample is loaded onto a microfluidic chip designed for RNA analysis.
        - **Separation of RNA Species:** The RNA molecules are separated based on size through capillary electrophoresis. This process distinguishes between intact ribosomal RNA (rRNA) subunits and degraded RNA fragments.
    3. **Automated Analysis:**
        - **Electropherogram Generation:** The instrument generates an electropherogram, a graphical representation of RNA fragments separated by size.
        - **Algorithmic Assessment:** An integrated algorithm analyzes the electropherogram, evaluating various parameters such as the ratio of rRNA subunits (e.g., 28S to 18S in eukaryotic cells), the presence of degradation products, and the overall RNA distribution.
        - **RIN Calculation:** Based on these assessments, the algorithm assigns a RIN value between 1 and 10, with 10 representing highly intact RNA.

    ---

    **Why is RIN Important in RNA-Seq Experiments?**

    RNA-seq is a powerful technique for profiling gene expression, identifying novel transcripts, and studying the transcriptomic landscape of cells and tissues. The accuracy and reliability of RNA-seq data are heavily dependent on the quality of the input RNA. Here's why RIN plays a pivotal role:

    4. **Ensuring Data Reliability:** High-quality RNA ensures that the sequencing data accurately reflects the true transcriptomic state of the sample. Degraded RNA can lead to incomplete or biased representation of transcripts.
    5. **Reducing Technical Variability:** By assessing RIN, researchers can standardize RNA quality across different samples, minimizing technical variability that could confound biological interpretations.
    6. **Optimizing Library Preparation:** RNA integrity affects the efficiency of library preparation steps such as fragmentation, reverse transcription, and adapter ligation. High-quality RNA facilitates more uniform and efficient library construction, leading to better sequencing outcomes.
    7. **Enhancing Downstream Analyses:** High RIN values contribute to more straightforward and accurate bioinformatics analyses, including alignment, quantification, and differential expression studies. Degraded RNA can introduce artifacts and complicate data interpretation.
    8. **Resource Optimization:** Ensuring high RNA quality before proceeding to expensive sequencing steps prevents the wastage of resources on suboptimal samples that may yield unusable data.

    ---

    **What Does a Low RIN Indicate About a Sample?**

    A low RIN value signifies that the RNA sample is degraded, meaning that the RNA molecules have been fragmented or broken down. Several factors can contribute to RNA degradation, including improper sample handling, delayed extraction, enzymatic activity (e.g., RNases), and suboptimal storage conditions. The implications of a low RIN in RNA-seq experiments are significant:

    9. **Incomplete Transcript Representation:** Degraded RNA often results in a bias towards the 3' ends of transcripts, as the 5' regions are more susceptible to degradation. This can distort gene expression profiles and affect the detection of full-length transcripts.
    10. **Reduced Sequencing Efficiency:** Fragmented RNA may lead to libraries with lower complexity, increasing the likelihood of redundant reads and reducing the ability to detect rare transcripts.
    11. **Inaccurate Quantification:** Degradation can cause uneven coverage across transcripts, leading to inaccurate quantification of gene expression levels and potentially misleading biological conclusions.
    12. **Challenges in Bioinformatics Analysis:** Fragmented reads may align ambiguously or incorrectly to the reference genome, complicating downstream analyses such as splice variant identification and differential expression.
    13. **Increased Technical Noise:** Degraded samples introduce technical noise that can obscure true biological signals, making it harder to discern meaningful patterns in the data.
    14. **Potential Exclusion from Analysis:** Samples with RIN values below a certain threshold may be excluded from RNA-seq analyses to maintain data integrity, potentially reducing sample size and statistical power.

    ---

    **Best Practices for Managing RIN in RNA-Seq Experiments**

    To mitigate the adverse effects of low RNA integrity, researchers should adhere to best practices during sample collection, handling, and processing:

    15. **Rapid Sample Preservation:** Promptly freezing samples or using RNA stabilization reagents immediately after collection can prevent RNA degradation.
    16. **Minimizing RNase Exposure:** Employing RNase-free consumables and maintaining a clean workspace reduces the risk of enzymatic degradation.
    17. **Optimized RNA Extraction Protocols:**  Utilizing protocols that swiftly and effectively extract RNA while minimizing exposure to degradative conditions is essential.
    18. **Proper Storage Conditions:** Storing RNA samples at -80°C or lower preserves integrity over extended periods.
    19. **Routine Quality Assessment:** Routinely assessing RNA quality using RIN measurements allows for early detection of degradation and timely intervention.
    20. **Sample Selection:** Implementing quality thresholds based on RIN values ensures that only high-integrity RNA samples proceed to sequencing.

## Q04

Describe the process of mRNA enrichment in RNA-seq experiments.
Why is this step important, and how does it affect the resulting data?

??? success "Solution"

    **Messenger RNA (mRNA) enrichment** is a critical preparatory step in RNA sequencing (RNA-seq) experiments aimed at selectively isolating and concentrating mRNA molecules from a complex mixture of RNA species present within a biological sample.
    This process ensures that the subsequent sequencing effort is focused primarily on the transcripts that carry genetic information from DNA to the protein synthesis machinery, thereby enhancing the quality and relevance of the resulting data.

    **The Process of mRNA Enrichment**

    1. **Isolation of Total RNA:**
        The first step in RNA-seq involves extracting total RNA from the biological sample, which includes a diverse array of RNA molecules such as ribosomal RNA (rRNA), transfer RNA (tRNA), small nuclear RNA (snRNA), and various non-coding RNAs, in addition to mRNA.
        However, mRNA typically constitutes only about 1-5% of the total RNA in eukaryotic cells, making its isolation essential for efficient sequencing.
    2. **Removal of rRNA:**
        Given that rRNA represents the majority of total RNA, its removal is paramount.
        This can be achieved through methods such as poly-A selection or rRNA depletion.
        - **Poly-A Selection:**
            Most eukaryotic mRNAs possess a polyadenylated (poly-A) tail at their 3' end. Poly-A selection leverages this feature by using oligo-dT (thymidine) primers attached to magnetic beads or other solid supports to hybridize and capture poly-A-tailed mRNAs.
            The non-polyadenylated RNAs, including rRNA and tRNA, remain unbound and are subsequently washed away, enriching the sample for mRNA.
        - **rRNA Depletion:**
            Alternatively, specific probes can be designed to bind rRNA molecules, allowing their removal from the total RNA pool.
            This method is particularly useful for organisms or cell types where mRNA does not have a poly-A tail or for studies aiming to capture non-polyadenylated transcripts.
    3. **Purification and Quality Control:**
        After enrichment, the mRNA is purified to remove any remaining impurities and is then assessed for quality and quantity.
        Techniques such as agarose gel electrophoresis, Bioanalyzer profiles, or qPCR may be employed to ensure that the enrichment process has been successful and that the RNA is intact and free from degradation.
    4. **Library Preparation:**
        The purified mRNA is then converted into a sequencing library through processes like fragmentation, reverse transcription into complementary DNA (cDNA), adapter ligation, and amplification.
        This library is subsequently sequenced using high-throughput sequencing platforms to generate the data for analysis.

    ---

    **Importance of mRNA Enrichment**

    -   **Enhancing Data Quality and Efficiency:**
        mRNA enrichment is crucial because it significantly increases the proportion of informative sequences in the RNA-seq data. Without enrichment, the sequencing reads would be overwhelmingly dominated by rRNA and other non-coding RNAs, leading to wasted sequencing resources and reduced coverage of mRNA transcripts of interest.
    -   **Focusing on Coding Regions:**
        By isolating mRNA, researchers can focus their analysis on the coding regions of the genome, which are directly involved in protein synthesis. This focus is essential for studies aimed at understanding gene expression patterns, identifying differentially expressed genes, and uncovering functional elements within the transcriptome.
    -   **Reducing Sequencing Costs:**
        Enriching for mRNA reduces the amount of sequencing required to achieve sufficient coverage of the transcripts of interest. This cost-effectiveness is particularly important for large-scale studies or when working with limited sequencing budgets.
    -   **Improving Downstream Analysis:**
        High-quality, mRNA-enriched samples facilitate more accurate and reliable downstream analyses, including gene expression quantification, variant detection, and transcript assembly. The reduced complexity of the library minimizes noise and enhances the signal-to-noise ratio, leading to more robust and interpretable results.

    **Impact on Resulting Data**

    -   **Increased Depth of Coverage:**
        mRNA enrichment ensures that a larger proportion of sequencing reads correspond to mRNA molecules, thereby increasing the depth of coverage for each transcript. This enhanced coverage improves the ability to detect low-abundance transcripts and subtle changes in gene expression.
    -   **Enhanced Detection of Differential Expression:**
        With more reads mapping to mRNA, statistical analyses for differential gene expression become more powerful and sensitive. This increased sensitivity allows for the identification of genes that may play critical roles in biological processes or disease states but are expressed at lower levels.
    -   **Facilitation of Transcriptome Complexity:**
        mRNA enrichment aids in capturing the full complexity of the transcriptome, including alternative splicing variants and isoforms. This comprehensive representation is vital for understanding the diverse functional roles of genes and their regulatory mechanisms.
    -   **Reduction of Bias and Artifacts:**
        By minimizing the presence of highly abundant non-coding RNAs like rRNA, mRNA enrichment reduces potential biases and artifacts in the sequencing data. This leads to a more accurate reflection of the true mRNA landscape within the sample.
    -   **Compatibility with Downstream Technologies:**
        Enriched mRNA samples are better suited for integration with various downstream technologies and analyses, such as single-cell RNA-seq, where the limited amount of RNA requires efficient capture and representation of the transcriptome.

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

??? success "Solution"

    The Burrows-Wheeler Transform is instrumental in data compression due to its ability to:

    - **Enhance Data Redundancy:** By rearranging the input to cluster similar characters.
    - **Improve Compression Efficiency:** Making it easier for compression algorithms to reduce data size.
    - **Maintain Reversibility:** Ensuring that the original data can be accurately retrieved.

    BWT is a core component of compression tools like **bzip2**, which leverages BWT in conjunction with other compression techniques to achieve high compression ratios.

    ---

    **Purpose of the Burrows-Wheeler Transform (BWT)**

    - **Rearrangement for Efficiency:** BWT restructures the input data to enhance the performance of subsequent compression algorithms by increasing data locality and repeating patterns.
    - **Facilitation of Compression Algorithms:** Transformed data exhibits more redundancy, which can be exploited by compression techniques like Run-Length Encoding (RLE) and Move-to-Front (MTF) encoding.

    ---

    **Analysis of Transformed String `banana` to `annb$aa`:**

    - **Clustering of Identical Characters:** Noticeable grouping of `a`s and `n`s.
    - **Enhanced Redundancy:** Increased repetition aids compression algorithms.

    **Compression Techniques Leveraging BWT:**

    - **Run-Length Encoding (RLE):**
        - **Process:** Encode consecutive repeated characters by their count.
        - **Example:** `annb$aa` becomes `a1n2b1$1a2`.
    - **Move-to-Front (MTF) Encoding:**
        - **Process:** Reorder characters based on their usage, placing recently used characters at the front.
        - **Benefit:** Enhances the effectiveness of subsequent entropy encoding methods like Huffman coding.

    ---

    **Reversibility of BWT**

    - **Key Property:** BWT is reversible, allowing the original string to be perfectly reconstructed from the transformed data.
    - **Importance:** Ensures data integrity during the compression and decompression processes.


## Q08

Perform the Burrows-Wheeler Transform (BWT) for the following DNA sequence: `ATTGCATTTGGCA`.
Show your work (including the matrix) and specify what is the output.

??? success "Solution"

    To ensure that the BWT is reversible and to handle rotations correctly, we append a unique end-of-string marker, typically the `$` symbol, which is lexicographically smaller than any other character.

    - **Original String:** `ATTGCATTTGGCA`
    - **Modified String:** `ATTGCATTTGGCA$`

    A **rotation** of a string is obtained by moving characters from the beginning to the end one by one.
    For the string `"ATTGCATTTGGCA$"`, which has **14** characters (indices `0` to `13`), we'll generate all **14** rotations.

    | Rotation | Rotated String  |
    |----------|------------------|
    | 0        | `ATTGCATTTGGCA$` |
    | 1        | `TTGCATTTGGCA$A` |
    | 2        | `TGCATTTGGCA$AT` |
    | 3        | `GCATTTGGCA$ATT` |
    | 4        | `CATTTGGCA$ATTG` |
    | 5        | `ATTTGGCA$ATTGC` |
    | 6        | `TTTGGCA$ATTGCA` |
    | 7        | `TTGGCA$ATTGCAT` |
    | 8        | `TGGCA$ATTGCATT` |
    | 9        | `GGCA$ATTGCATTT` |
    | 10       | `GCA$ATTGCATTTG` |
    | 11       | `CA$ATTGCATTTGG` |
    | 12       | `A$ATTGCATTTGGC` |
    | 13       | `$ATTGCATTTGGCA` |

    Next, we sort all the rotated strings in **lexicographical (dictionary) order**.
    Here's the sorted list:

    | Sorted Order | Rotation Index  | Rotated String   |
    |--------------|-----------------|------------------|
    | 1            | 13              | `$ATTGCATTTGGCA` |
    | 2            | 12              | `A$ATTGCATTTGGC` |
    | 3            | 0               | `ATTGCATTTGGCA$` |
    | 4            | 5               | `ATTTGGCA$ATTGC` |
    | 5            | 11              | `CA$ATTGCATTTGG` |
    | 6            | 4               | `CATTTGGCA$ATTG` |
    | 7            | 10              | `GCA$ATTGCATTTG` |
    | 8            | 3               | `GCATTTGGCA$ATT` |
    | 9            | 9               | `GGCA$ATTGCATTT` |
    | 10           | 2               | `TGCATTTGGCA$AT` |
    | 11           | 8               | `TGGCA$ATTGCATT` |
    | 12           | 1               | `TTGCATTTGGCA$A` |
    | 13           | 7               | `TTGGCA$ATTGCAT` |
    | 14           | 6               | `TTTGGCA$ATTGCA` |


    The **Burrows-Wheeler Transform** is obtained by taking the **last character** of each sorted rotation.
    Let's extract the last characters:

    ```
    A C $ C G G G T T T T A T A
    ```

    **Final BWT Output:** `AC$CGGGTTTTATA`

**a)** Without performing the full LF-mapping, explain how you would start searching for the pattern `ATT` in this BWT.
What would be your initial range in the F column, and what character would you look for first in the L column?

??? success "Solution"

    1.  **Understanding F and L Columns:**
        - F Column: The first column of the BWT matrix, obtained by sorting the BWT string.
        - L Column: The last column, which is the BWT string itself.
    2.  **Constructing the F Column:** Sort the BWT string `AC$CGGGTTTTATA` lexicographically.
        - F Column: `$ A A A C C G G G T T T T T`
        - L Column: `A C $ C G G G T T T T A T A`

    3.  **Initial Step for Pattern Matching ("ATT"):** The pattern `"ATT"` is processed from right to left, starting with the last character `'T'`.

    4. **Determining the Initial Range in F Column:**
        - F Column: `$ A A A C C G G G T T T T T`
        - Character to Find: `'T'`
        - Positions of `'T'` in F Column: Indices `9` to `13` (0-based indexing).
        - Initial Range: `[9, 13]`

    5. **Character to Look for in L Column:**
        - First Character of the Pattern (Rightmost): `'T'`
        - Looking for `'T'` in the L Column within the initial range `[9, 13]`.
        - L Column: `AC$CGGGTTTTATA`
            - Positions `9` to `13` correspond to characters:
               - `L[9] = T`
               - `L[10] = T`
               - `L[11] = A`
               - `L[12] = T`
               - `L[13] = A`
        - First Character to Look for in L Column: `'T'` (the current character of the pattern being matched).

**b)** The sequence contains both `TTT` and `TGC`.
Without doing the full LF-mapping, explain which of these patterns would likely be easier to search for using the BWT, and why.

??? success "Solution"

    1. **Frequency and Distribution in BWT:**
        - **Occurrences of `'T'`:** Appears multiple times (`T` occurs 5 times).
        - **Occurrences of `'G'` and `'C'`:** `'G'` appears 3 times; `'C'` appears 2 times.
    2. **Pattern Characteristics:**
        - **"TTT":**
            - Repeats the same character `'T'` three times.
            - High frequency in BWT.
            - Easier to locate due to consecutive `'T'`s.
        - **"TGC":**
            - Sequence of distinct characters `'T'`, `'G'`, `'C'`.
            - Less frequent as a specific sequence.
    3. **Ease of Search:**
        - **"TTT":**
            - High occurrence increases the likelihood of multiple  matches.
            - Repeated characters simplify the search as transitions involve the same character.
        - **"TGC":**
            - Requires matching a specific sequence of distinct characters.
            - Lower frequency and specific transitions make it harder to locate.

    **"TTT"** would likely be **easier to search** using the BWT because:

    - The character `'T'` is frequent and repeated.
    - The high occurrence of `'T'` simplifies the matching process.
    - Repeated characters reduce the complexity of tracking transitions during the search.

**c)** How does the presence of unique substrings (like `GCA`) in the original sequence affect the structure of the BWT?
Explain why we see certain patterns in the BWT string.

??? success "Solution"

    1. **Unique Substrings:**
        - A substring like `"GCA"` appears only once in the original string `"ATTGCATTTGGCA$"`.
    2. **Impact on Rotations and Sorting:**
        - **Rotations Containing "GCA":**
            - The substring `"GCA"` will appear in only one rotation.
            - This uniqueness affects the sorting of rotations, as the unique substring will anchor its specific rotation in a particular position within the sorted list.
    3. **Effect on BWT:**
        - **Adjacent Characters:**
            - Characters preceding unique substrings in the sorted rotations influence the BWT.
            - For example, if `"GCA"` is preceded by a unique character in its rotation, the corresponding character in the BWT will reflect that.
        - **Patterns in BWT:**
            - Unique substrings lead to unique patterns or isolated characters in the BWT.
            - Repeated substrings contribute to recurring patterns, while unique substrings introduce variability.
    4. **Illustrative Example with "GCA":**
        - **Original Rotation Containing "GCA":**
            - Suppose one rotation is `GCA$ATTGCATTTGG` (rotation index `10`).
        - **Position in Sorted Rotations:**
            - This rotation's unique structure places it in a distinct position in the sorted list.
        - **Corresponding BWT Character:**
            - The character preceding `"GCA"` in this rotation (`'G'`) becomes part of the BWT.
        - **Resulting in the BWT:**
            - This unique context ensures that the character `'G'` appears in a specific position in the BWT, contributing to the overall structure.
    5. **General Impact:**
        - **Unique Substrings:**
            - Introduce unique characters or sequences in the BWT, making certain patterns stand out.
            - Help in distinguishing specific contexts during pattern matching.
        - **Repetitive Substrings:**
            - Lead to recurring characters or patterns in the BWT, facilitating efficient compression and search operations.

    **Conclusion:**

    - **Unique Substrings** like `"GCA"` create **distinct patterns** in the BWT string.
    - These unique sequences ensure that certain characters in the BWT are **isolated or uniquely positioned**, aiding in the **differentiation** of specific parts of the original string.
    - The presence of unique substrings enhances the **structural diversity** of the BWT, which is beneficial for operations like **pattern matching** and **data compression**.

## Q09

Reverse the Burrows-Wheeler Transform output `BBAAB$AABA` to get the original string.
What is the original string?
Show all of your steps.

??? success "Solution"

    The original string is `ABBABAAAB$`.

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
