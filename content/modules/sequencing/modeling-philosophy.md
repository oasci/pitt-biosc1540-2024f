# The Philosophy of Modeling

## Explaining or predicting

The philosophy of science grapples with the fundamental distinction between explanation and prediction.
The definition of scientific explanation crystallizes around the emphasis on accurate causal accounts or models, serving as the backbone of understanding complex phenomena.
Determining the explanatory scope or “level of explanation” provides a nuanced lens through which scientists can analyze and interpret their findings.
Yet, the necessity of predictive models intertwines with the very fabric of explanation, prompting a deeper exploration of their fundamental role.

The role of the level of explanation emerges as a pivotal factor in model construction, necessitating a careful incorporation of data from diverse domains.
Testing predictive capabilities against this backdrop further refines the scientific process, underscoring the significance of achieving a delicate balance between explanation and prediction.
The realm of computational biology&mdash;where the intricacies of living systems meet the precision of computational models&mdash;requires a harmonious integration of theoretical frameworks and empirical data.

## Laws versus principles

In the exploration of scientific methodology, the dichotomy between laws and principles takes center stage, as highlighted by [Giere in “Science Without Laws” (1999)](https://www.google.com/books/edition/Science_Without_Laws/XZZORWOo8fIC).
Giere contends that the confinement of science to the pursuit of universal ‘True’ Laws of Nature is limiting.
Instead of adhering to a conventional objectivist perspective of producing statements categorized as true or false, he advocates for viewing science as a dynamic practice generating models of the world.
These models, much like maps, may approximate the world to varying degrees.

Giere proposes a paradigm shift, urging the interpretation of key scientific discoveries as principles rather than laws.
In this context, principles are conceptualized as human-devised rules utilized in constructing models to represent specific facets of the natural world.

???+ example

    Taking Newton’s principles of mechanics as an example, these are viewed not as immutable laws dictating the relationship between mass, force, and acceleration, but as rules guiding the construction of models to represent mechanical systems, encompassing phenomena from comets to pendulums.
    The essence lies in providing a perspective for comprehending mechanical motions, demonstrating that insights into the world emerge not as universal truths, but through successful representations of a diverse array of real-world systems based on these principles.

## What is a computational model?

A computational model is a computer program that is used to simulate and study complex systems using an algorithmic or mechanistic approach.
In the context of this discussion, it is utilized to generate data for comparison with real-world behavior.
This definition emphasizes the crucial aspect of quantitative comparison, where the implications of a total rule set within the computer program can be unambiguously derived and then compared to the actual experimental results.

The central question then becomes: What constitutes a good computational model in the realm of computational biology?

This question is intricately linked to how scientists are expected to utilize computational models in this field.
While certain general statements can be made about the expectations for a useful computational model, such as

-   the likelihood of extensive use of iteration,
-   or the necessity for sensing inputs and generating outputs,

these statements apply broadly to computer programs in general and do not provide specific criteria for assessing the effectiveness of a computational model.
The scientific community has identified several attributes that distinguish a valuable computational model within the scientific context.

## Good models

The task of computational modeling in the realm of biology involves identifying sets of ‘good’ models that effectively ‘fit’ specific real-world behaviors.
The criteria for determining what qualifies as a ‘good’ model and how well it ‘fits’ the observed data are pivotal considerations.
As [Simon and Wallach (1999)](https://doi.org/10.1007/BF03354931) assert, the question of what constitutes a good approximation is pragmatically answered.
Therefore, understanding the pragmatic measures for assessing computational models becomes crucial.

!!! tip

    In simple terms, when we use a computer to make predictions or simulations, we need to make sure that the results are accurate enough for our needs.
    But what does “accurate enough” mean?
    That’s where the idea of a “good approximation” comes in.
    A good approximation is a result that is close enough to the true answer to be useful, but not so close that it takes too much time or resources to calculate.

    So, when we’re evaluating a computational model, we need to ask ourselves: is this model giving us good approximations?
    To answer that question, we need to use some practical measures that help us assess the accuracy of the model.
    These measures are important because they help us make sure that the model is reliable and that we can trust its predictions.

In computational biology, the connection between mathematical models and observed data is established by comparing numerical predictions with real experimental results.
Acknowledging that exact matches are rare, the concept of being ‘close enough’ is introduced.
However, two essential sources of variability&mdash;measurement error and internal variation&mdash;impact the comparison between model and real-world data.

Measurement error arises due to imperfections in observational techniques, resulting in slightly imprecise data.
In computational biology, statistical techniques often incorporate confidence intervals, accounting for the inherent variability in measurements.
Internal variation, on the other hand, stems from the fact that behaviors of interest in computational biology are seldom precisely repeated.
This variability is not dissimilar to the slight variations observed in physical sciences, but the computational biology realm is more prone to chaos, where small initial changes lead to significant differences in outcomes.

Replicability within computational biology becomes challenging due to the inherent variability in individual behavior.
However, the solution lies in recognizing that models should mirror the same degree of variability present in the real-world situation.
The goal is not to model average performance but to capture individual performance.
This approach acknowledges the difficulty of characterizing the distribution of real-world performance and emphasizes the importance of measuring variability.

## Identify the relevant phenomena

Computational modeling is a cornerstone of scientific research, with applications ranging from simulating complex biological processes to predicting climate patterns.
However, the vastness of scientific domains coupled with the constraints of limited computational resources necessitates a strategic approach to focus on the most critical components that drive the research objectives.
Defining the scope of a modeling project is paramount to its success.
This entails a meticulous examination of the project’s overarching goals and the specific outcomes researchers aim to achieve.
With objectives clearly delineated, the next crucial step involves identifying the key components or phenomena that wield the most influence over the desired outcomes.
This process demands a comprehensive understanding of the scientific goals and the contextual relevance of each component within the broader research framework.

!!! example

    In the realm of computational biology, the discernment of crucial components takes center stage.
    A nuanced analysis of each element’s impact on the overall research goals guides the decision-making process.
    For instance, when modeling protein-ligand binding, a targeted approach may involve omitting large length scales that do not significantly contribute to the phenomena of interest.
    This deliberate exclusion not only streamlines the computational process but also optimizes the use of limited resources.
    Through this focused lens, researchers can navigate the intricate balance between computational efficiency and modeling accuracy, ensuring that the selected components align with the project’s objectives.

## Make reasonable assumptions

Navigating the intricate landscape of computational modeling within the constraints of limited resources necessitates the judicious application of reasonable assumptions.
In acknowledging these constraints, researchers must grapple with the challenge of making approximations to render their models tractable.

For instance, in the realm of modeling atomistic interactions, is it necessary to factor in gravity?
Given the minuscule scale of atomic interactions, the gravitational force is often overshadowed by other molecular forces.
Hence, a reasonable assumption may involve neglecting gravity in favor of focusing computational resources on more pertinent molecular forces that significantly impact the system under study.

The exploration of genomics and transcriptomics options further underscores the need for thoughtful assumptions.
In the vast genomic landscape, researchers are confronted with myriad possibilities.
Making informed decisions involves weighing the computational cost against the scientific value of each option.

Moving beyond assumptions, the next pivotal stage in computational modeling involves choosing the most suitable model.
Within the realm of computational biology and bioinformatics, various models cater to different facets of research.
Bioinformatics tools serve as indispensable aids in data analysis, offering insights into complex biological datasets.
Molecular dynamics and quantum mechanics step into the realm of physics-based models, capturing the intricacies of molecular interactions.
Additionally, machine learning models provide a powerful tool for predictive analysis, leveraging patterns within vast datasets.
The careful selection of a model aligns with the objectives of the research and the available computational resources.

## Interpretability and transparency

Model interpretability and transparency are crucial aspects in various scientific domains.

In physics, the use of interpretable models becomes imperative.
Physicists often rely on intricate models to simulate and predict behaviors in various systems.
The challenge lies in making these models transparent and interpretable.
To address this, there is a growing trend towards adopting explainable AI approaches in physics modeling.
By incorporating interpretable elements into the models, physicists can not only enhance their understanding of the underlying principles but also communicate these insights effectively to a broader audience.

Communication is a central theme in the intersection of bioinformatics, physics, and model interpretability.
Bridging the gap between scientists from different disciplines requires effective communication of results.
When bioinformatics findings are communicated to biologists or physicists, it is crucial to convey the relevance of identified patterns in a language understandable to the receiving audience.
This interdisciplinary communication is equally essential in physics, where the translation of complex model outcomes into insights accessible to biologists and bioinformaticians ensures the collaborative advancement of knowledge.

## Acknowledgements

Some of this content is adapted from the following resources.

-   Stewart, T. C. (2005) Notes for the development of a Philosophy of Computational Modeling. *Carleton University Cognitive Science Technical Report*. uri: [https://carleton.ca/cognitivescience/research/technical-reports/view-reports/](https://carleton.ca/cognitivescience/research/technical-reports/view-reports/)
