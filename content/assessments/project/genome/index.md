<h1 align="center">
<b>Part 1:</b><br>
Genome assembly
</h1>

[You have been assigned](https://canvas.pitt.edu/courses/267135/files/18413175) a set of Illumina sequencing reads from a *Staphylococcus aureus* isolate.
Your task is to assemble and annotate the genome, and then identify the dihydrofolate reductase gene, which is a common target for antibiotics.
This project will give you experience with real-world bioinformatics tools and workflows used in genomics research.

## Learning Objectives

By completing this project, you will:

1.  Gain practical experience with a complete genome assembly and annotation workflow.
2.  Learn to use and interpret results from key bioinformatics tools.
3.  Understand the process of identifying potential drug targets from genomic data.
4.  Develop skills in data analysis and interpretation in a genomics context.

## Materials

You will be assigned one of 114 whole-genome sequencing runs from the BioProject [PRJNA741582](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA741582).
Each run contains Illumina HiSeq 2000 paired-end reads of 250 nucleotides in length.

## Instructions

You will use a series of bioinformatics tools to process and analyze your assigned sequencing data.
Follow these steps carefully, documenting your process and results at each stage.

### Setting Up Your Galaxy Project

Before beginning the analysis, you need to set up an account on Galaxy and create a project for this assignment.
Galaxy is a web-based platform for data-intensive biomedical research that will allow you to perform all the necessary analyses for this project.

1.  Go to <https://usegalaxy.org/>
2.  Click on the "Login or Register" button in the top middle.
3.  If you don't have an account, click on "Register here" and fill out the registration form.
    Make sure to use a valid email address as you'll need to verify it.
4.  Once you've registered and logged in, click "Create new history+" and name your new project "BIOSC 1540 Project" and provide a brief description if you wish.
    Click `Create`.

Always ensure you're working within your "BIOSC 1540 Project" for this assignment.
This will help you keep your work organized and easily accessible.

Galaxy will also save your work automatically, but it's a good practice to regularly check that your analyses are being saved correctly.

If you encounter any issues with Galaxy, check their [support](https://galaxyproject.org/support/) and [training](https://training.galaxyproject.org/).

### Getting data

In this step, you'll download the assigned sequencing data for your *S. aureus* isolate and upload it to Galaxy.
Follow these instructions carefully:

1.  Your instructor will [provide you with a unique SRA](https://canvas.pitt.edu/courses/267135/files/18413175) (Sequence Read Archive) accession number for your assigned *S. aureus* isolate.
    We will use `SRX11246059` as an example.
2.  In the Galaxy interface, click on `Tools` in the left sidebar.
3.  In the search bar at the top of the Tools panel, type `Download and Extract Reads in FASTQ format from NCBI SRA` and click on it.
4.  In the tool interface:
    -   For `select input type`, choose `SRR accession`.
    -   In the `Accession` field, enter your assigned SRA accession number.
    -   Leave all other settings as default.
5.  Click `Run Tool`.

Galaxy will now download and extract your sequencing data.
You can monitor the progress in the right sidebar, and will turn from blanched almond to green once finished.

!!! quote "Estimated time"
    7 minutes

1.  Once complete, you should see two new items in your history:
    -   `Single-end data (fastq-dump)`
    -   `Paired-end data (fastq-dump)`
2.  There will be no data in `Single-end data (fastq-dump)`, so you can delete this.
3.  To find the `forward.fastqc` file, you need to view job information for `Paired-end data (fastq-dump)`, click on your accession number (i.e., `SRX11246059`), then on `forward` to preview its contents.
    You should see sequences in FASTQ format.

!!! note "Report"

    Include the following information:

    -   Your SRA accession number that starts with `SRX`.
    -   The first five FASTQ entries in the `forward.fastq` file.

### Quality Control with FastQC

Quality control is a crucial step in any sequencing data analysis.
It helps you identify any issues with your sequencing data that might affect downstream analyses.
We'll use FastQC, a widely used tool for quality control of high throughput sequencing data.

1.  In the Galaxy interface, search for "FastQC" in the tools panel.
2.  In the tool interface:
    -   For `Raw read data from your current history`, select `Dataset Collection` and choose `Paired-end data (fastq-dump)`.
    -   Leave all other settings as default.
3.  Click `Run Tool`.

!!! quote "Estimated time"
    1 minute

Once the job is complete, you'll see new items in your history for each FastQC report (Webpage and RawData).

Click on the `FastQC on collection: Webpage`, your accession number, and then both `forward` and `reverse` eye icons.
The report contains several modules, each assessing a different aspect of your sequence data.

!!! note "Report"

    In your report, address the following questions for your `forward` reads:

    1.  What is the overall quality of your sequencing data?
        Provide evidence from the FastQC report (i.e., screenshots) to support your assessment.
    2.  Are there any concerning issues identified by FastQC?
        If so, what are they and how might they impact your downstream analyses?
    3.  Based on the "Per base sequence quality" plot, is there evidence of quality degradation towards the end of the reads?
        If so, how might this inform your approach to read trimming?
    4.  Do you see any evidence of adapter contamination or overrepresented sequences?
        If so, what steps might you take to address this?
    5. How do the results for your forward reads compare to your reverse reads?
        Are there any notable differences?

Remember, some warnings or failures in the FastQC report don't necessarily mean your data is unusable.
The context of your experiment and the specific analyses you plan to perform should guide your interpretation of these results.

### Adapter Trimming with Fastp

After assessing the quality of your raw sequencing data, the next step is to trim adapters and perform quality control.
We'll use fastp, a fast all-in-one preprocessing tool for FASTQ files.

1.  In the Galaxy interface, search for "fastp" in the tools panel.
2.  Click on "fastp: fast all-in-one preprocessing for FASTQ files".
3.  In the tool interface, set the following parameters:
    -   "Single-end or paired reads": Select "Paired Collection".
    -   "Select paired collection(s)": Choose your paired-end reads.
4.  Click "Run Tool".

!!! quote "Estimated time"
    1 minute

Click on the eye icon next to the HTML report to view it.
The report contains information about the trimming and filtering process.

!!! note "Report"

    In your report, address the following questions with either your fastp or FastQC report:

    1.  How many reads were removed during the filtering process? What percentage of reads passed the filters?
    2.  Did fastp detect and trim any adapters? If so, which ones?
    3.  How did the quality scores change after filtering? Provide specific examples from the report.
    4.  Were there any issues with base composition (e.g., GC bias) before or after filtering?
    5.  What was the duplication rate?
        Is this what you would expect for your type of sequencing data?
    6. Compare the fastp results to your earlier FastQC results.
        How do they complement each other? Are there any discrepancies?

Remember, the goal of this step is to improve the overall quality of your sequencing data by removing low-quality reads, trimming adapters, and addressing any other issues identified in the FastQC step.
The fastp results should show an improvement in data quality compared to the raw reads.

### De Novo Genome Assembly with SPAdes

After trimming and quality control, the next step is to assemble the processed reads into contigs.
We'll use SPAdes, a versatile genome assembler designed for both small genomes and single-cell projects.

1.  In the Galaxy interface, search for "SPAdes" in the tools panel.
2.  Click on "SPAdes genome assembler for genomes of regular and single-cell projects".
3.  In the tool interface, set the following parameters:
    -   "Operation mode": Select "Assembly and error correction"
    -   "Single-end or paired-end short-reads": Choose "Paired-end: list of dataset pairs"
    -   "FASTA/FASTQ file(s)": Select your paired-end output from the fastp step
4.  Click "Run Tool".

!!! quote "Estimated time"
    2 hours

Once complete, you'll see new items in your history, including the assembly graph, contigs, and scaffolds.

To get more detailed statistics about your assembly, we'll use the Bandage Info tool:

1.  In the Galaxy interface, search for `Bandage Info` in the tools panel.
2.  Click on `Bandage Info`.
3.  In the tool interface, set the following parameters:
    -   `Graphical Fragment Assembly`: Select the `SPAdes: Assembly Graph with Scaffolds`.
    -   Leave all other settings as default.
4.  Click "Run Tool".
5.  Once complete, you'll see a new item in your history with the Bandage Info output.
6.  Next, repeat the same process with `Bandage Image` and include this in your report.

!!! quote "Estimated time"
    1 minute

!!! note "Report"

    In your report, address the following questions:

    1.  How many contigs (i.e., nodes) were produced by the assembly?
    2.  What is the total length of the assembly?
        How does this compare to the expected genome size of Staphylococcus aureus (approximately 2.8 Mb)?
    3.  What is the N50 of your assembly?
    4.  Calculate the difference between the "Total length" and "Total length no overlaps".
        What does this difference represent, and why is it important to consider?
    5.  What is the N50 of your assembly?
        How does this value compare to the median node length?
        What does this tell you about the distribution of contig sizes in your assembly?
    6.  Analyze the "dead ends" in your assembly.
        How many dead ends are there?
        What percentage of the total possible ends (2 * number of nodes) do these represent?
        What might a high percentage of dead ends indicate about your assembly?
    7.  Based on all these results, how would you assess the overall quality of your genome assembly? Consider factors such as completeness, contiguity, and potential issues.
    8.  How do you think the "careful" mode in SPAdes might have influenced these assembly statistics compared to the default mode?

### Gene Annotation with Prokka

After assembling the genome, the next step is to annotate it to identify genes and their potential functions.
We'll use Prokka, a rapid prokaryotic genome annotation tool.

1.  In the Galaxy interface, search for `Prokka` in the tools panel.
2.  Click on `Prokka: Prokaryotic genome annotation`.
3.  In the tool interface, set the following parameters:
    -   "Contigs to annotate": Select the Scaffolds file from your SPAdes output
    -   "Genus name": Enter "Staphylococcus"
    -   "Species name": Enter "aureus"
4.  Click "Run Tool".

!!! quote "Estimated time"
    10 minutes

After the annotation is complete, examine the output files.
Pay particular attention to:

-   **GFF3 file (.gff)**: This contains the annotations in a standard format.
    You can use this file to visualize the annotations in a genome browser.
-   **GenBank file (.gbk)**:
    This file contains both the sequence and the annotations.
    It can be viewed in many sequence analysis tools.
-   **Statistics file (.txt)**: This provides a summary of the annotation process.
    Look at the number and types of features identified.
-   **Protein FASTA file (.faa)**: This contains the amino acid sequences of predicted proteins.
    You'll use this to find your gene of interest (dihydrofolate reductase).

!!! note "Report"

    In your report, address the following questions:

    1.  How many coding sequences (CDS) did Prokka identify in your genome?
    2.  How many rRNA and tRNA genes were annotated?
    3.  What other types of features did Prokka identify, and how many of each?
    4.  How does the number of annotated genes compare to what you would expect for a *Staphylococcus aureus* genome?
    5.  Did Prokka identify any potential plasmids?
        If so, how many genes are on the plasmid(s)?
    6.  Search the `.faa` file for the dihydrofolate reductase gene.
        Did Prokka identify this gene?
        If so, what is its protein ID and what are its start and end positions in the genome?
        What is the amino acid sequence of your protein?
    7.  Based on these results, how would you assess the quality and completeness of your genome annotation?
    8.  How might the genus and species names you provided influence the annotation process?

Remember, a typical *S. aureus* genome contains around 2,500 to 2,900 genes.
The presence or absence of certain genes can provide insights into the strain's potential characteristics or capabilities.

### Comparing to UniProt

After annotating your genome and identifying the dihydrofolate reductase gene, the next step is to compare your sequence to a known reference.
This comparison will help you verify your annotation and identify any potential variations in your sequence.

1.  Go to the UniProt website (<https://www.uniprot.org/>).
2.  Find the dihydrofolate reductase protein (folA gene) entry for *Staphylococcus aureus* (Taxon ID `1280`).

!!! note "Report"

    In your report, address the following questions:

    1.  What is the UniProt ID?
    2.  What is the length of your protein sequence?
        How does it compare to the UniProt reference (159 amino acids)?
    3.  Calculate the percentage identity between your sequence and the UniProt reference.
        Are they identical, or are there differences?
    4.  If there are differences, list their positions and the amino acid changes.
        Are these changes conservative (similar amino acids) or non-conservative?

## Submission Guidelines

-   Submit your report as a single PDF file named `LastName_FirstName_GenomeAssemblyReport.pdf` to [Gradescope](https://www.gradescope.com/).
-   Responses to questions should be numbered under a heading and be of reasonable length.
-   Ensure all figures and tables in your report are clearly labeled and referenced in the text.

## Rubric

Your answers to all the aforementioned questions will help you garner points according to this rubric.

**Data Acquisition and Initial Processing**

| Criterion | Points | Description |
|-----------|---------|-------------|
| SRA Data Retrieval | 10 | - Successfully downloads correct SRA dataset (5 pts)<br>- Properly identifies and presents first five FASTQ entries (5 pts) |

**Quality Control Analysis**

| Criterion | Points | Description |
|-----------|---------|-------------|
| FastQC Interpretation | 12 | - Accurately interprets quality metrics (4 pts)<br>- Identifies key issues in sequencing data (4 pts)<br>- Compares forward/reverse reads effectively (4 pts) |
| Fastp Analysis | 8 | - Correctly reports filtering statistics (3 pts)<br>- Analyzes quality improvement after trimming (3 pts)<br>- Interprets duplication rates appropriately (2 pts) |

**Genome Assembly**

| Criterion | Points | Description |
|-----------|---------|-------------|
| Assembly Statistics | 15 | - Accurately reports and interprets N50 (4 pts)<br>- Analyzes contig numbers and lengths (4 pts)<br>- Compares assembly size to expected genome size (4 pts)<br>- Evaluates assembly graph characteristics (3 pts) |
| Quality Assessment | 10 | - Critically evaluates assembly quality (5 pts)<br>- Identifies potential issues and limitations (5 pts) |

**Genome Annotation**

| Criterion | Points | Description |
|-----------|---------|-------------|
| Prokka Results | 15 | - Reports complete annotation statistics (5 pts)<br>- Analyzes gene content and distribution (5 pts)<br>- Compares results to expected S. aureus features (5 pts) |
| Gene Analysis | 10 | - Identifies dihydrofolate reductase gene (5 pts)<br>- Correctly reports gene characteristics and location (5 pts) |

**Protein Analysis and Comparison**

| Criterion | Points | Description |
|-----------|---------|-------------|
| UniProt Comparison | 10 | - Performs thorough sequence comparison (4 pts)<br>- Identifies and analyzes sequence variations (3 pts)<br>- Interprets biological significance of findings (3 pts) |

**Report Quality**

| Criterion | Points | Description |
|-----------|---------|-------------|
| Organization | 4 | - Clear structure and flow<br>- Proper section labeling<br>- Appropriate use of figures and tables |
| Scientific Writing | 4 | - Clear, concise scientific writing<br>- Proper terminology<br>- Appropriate citations |
| Format Compliance | 2 | - Follows submission guidelines<br>- Proper file naming<br>- Complete PDF submission |
