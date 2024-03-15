# Programming languages

Here we cover the different types of programming languages and when you would use them.
Due to its popularity and small learning curve, Python was chosen for this course.

## Compiled languages

A compiled language is a programming language whose code is translated from the high-level programming language to machine code by a compiler before it is executed.
This compiled code is then executed directly by the computer's hardware.

Examples of compiled languages include Rust, C++, Fortran, and Go.

### Advantages

-   **Performance**: Compiled languages often result in faster and more efficient code execution compared to interpreted languages.
    The compilation process allows for extensive optimizations, producing machine code that can take full advantage of the underlying hardware.
-   **Optimization Opportunities**: Compilers can analyze the entire program during the compilation process, enabling them to make optimizations for speed, memory usage, and other performance-related factors.
    This can lead to highly optimized and efficient executable code.
-   **Security**: Since the source code is translated into machine code, it is less accessible and harder to reverse engineer compared to interpreted code.
    This can provide a level of security by protecting intellectual property and sensitive algorithms.
-   **Static Typing**: Many compiled languages are statically typed, meaning that variable types are determined at compile-time.
    This can catch type-related errors early in the development process, reducing the likelihood of runtime errors.
-   **Early Error Detection**: Compilation often includes rigorous checks for syntax errors and certain types of logical errors.
    This can help catch issues early in the development process before the program is executed.
-   **Efficient Use of System Resources**: Compiled languages can be more efficient in terms of memory usage and CPU utilization.
    This is particularly important for applications where resource efficiency is a critical factor, such as embedded systems or high-performance computing.
-   **Native Code Execution**: Compiled languages produce native machine code that can be executed directly by the computer's hardware, eliminating the need for an interpreter.
    This can result in better performance and lower overhead during execution.
-   **Predictable Performance**: The performance of a compiled program is often more predictable because optimizations are applied during compilation.
    In contrast, interpreted languages may introduce variability in performance due to interpretation overhead.
-   **Support for Low-Level Operations**: Compiled languages often provide more direct control over low-level operations, memory management, and hardware interactions.
    This can be advantageous for systems programming and tasks that require fine-grained control.
-   **Wide Range of Applications**: Compiled languages are used in a variety of domains, including systems programming, embedded systems, game development, high-performance computing, and more.
    Their versatility makes them suitable for a broad range of applications.

### Disadvantages

-   **Portability**: Compiled languages often generate machine-specific code, making it less portable across different platforms or architectures. Programs compiled on one system may not run on another without recompilation or adaptation.
-   **Development Speed**: The compilation process itself can be time-consuming, especially for large projects. This can slow down the development process as developers may need to wait for the code to be compiled before testing or debugging.
-   **Debugging**: Debugging compiled code can be more challenging than debugging interpreted or dynamically typed languages. The translation from high-level code to machine code can obscure some of the source code's details, making it harder to trace and fix errors.
-   **Flexibility**: Compiled languages may be less flexible during runtime compared to interpreted languages. Changes to the code often require recompilation, making it less dynamic and adaptable to certain situations.
-   **Learning Curve**: Working with compiled languages may have a steeper learning curve for beginners. Developers often need to manage memory explicitly, deal with complex data types, and understand low-level details, which can be more challenging for newcomers to programming.
-   **Platform Dependencies**: Compiled languages may have dependencies on specific libraries or tools that are platform-dependent. This can complicate the deployment process and make it harder to ensure consistent behavior across different systems.

## Interpreted languages

Interpreted languages are programming languages where the source code is executed line by line, typically by an interpreter, without the need for a separate compilation step.
Instead of translating the entire source code into machine code or an intermediate code before execution, an interpreter reads and executes the code directly.

Examples of interpreted languages include Python and R.

### Advantages

-   **Platform Independence**: Interpreted languages are often designed to be platform-independent.
    As long as the required interpreter is available for a specific platform, the same source code can run on different operating systems without modification.
-   **Ease of Learning and Development**: Interpreted languages are often easier to learn and use, making them accessible for beginners and promoting rapid development.
    They typically have simpler syntax and provide higher-level abstractions, allowing developers to focus on solving problems rather than managing low-level details.
-   **Rapid Prototyping**: The interactive nature of interpreted languages facilitates rapid prototyping and experimentation.
    Developers can test code snippets or make changes on the fly, leading to faster development cycles.
-   **Dynamic Typing**: Interpreted languages often use dynamic typing, allowing for flexible and dynamic variable types.
    This flexibility can make the development process more agile, enabling developers to write code without specifying variable types explicitly.
-   **Ease of Debugging**: Debugging in interpreted languages is often more straightforward.
    Developers can identify and fix errors during runtime, and some interpreted languages provide interactive debugging tools that simplify the process.
-   **Scripting and Automation**: Many interpreted languages, such as Python and Bash, are commonly used for scripting and automation tasks.
    Their ease of use and platform independence make them suitable for writing scripts to automate repetitive tasks.
-   **Community Support and Libraries**: Interpreted languages often have vibrant and active communities, leading to extensive libraries and frameworks.
    This wealth of resources can accelerate development by providing pre-built solutions for common tasks.
-   **Interactivity**: Interpreted languages often support interactive development environments, allowing developers to execute code line by line or in small chunks.
    This interactivity can aid in learning and exploration.

### Disadvantages

-   **Slower Execution Speed**: Interpreted languages are generally slower in terms of execution speed compared to compiled languages. The interpreter needs to analyze and execute the source code line by line, introducing overhead that can impact performance, especially for computationally intensive tasks.
-   **Dependency on Interpreters**: Interpreted languages rely on interpreters to execute code. Ensuring that the required interpreter is available on the target system may introduce dependencies and complicate deployment.
-   **Less Efficient Memory Usage**: Interpreted languages may not be as efficient in managing memory compared to compiled languages. This can result in higher memory usage and reduced performance for certain applications.
-   **Limited Optimization Opportunities**: Since the code is interpreted at runtime, the interpreter has limited opportunities for global optimization. Compiled languages, on the other hand, can perform extensive optimizations during the compilation process, potentially leading to more efficient code.
-   **Harder to Hide Source Code**: Interpreted languages are often associated with more accessible source code. While this can foster transparency and collaboration, it may be a disadvantage in situations where code protection or intellectual property concerns are paramount.
-   **Security Concerns**: Interpreted languages may have security vulnerabilities, especially when executing untrusted code. Ensuring the security of an interpreter and managing potential risks is crucial when working with interpreted languages in certain contexts.
-   **Lack of Compilation Checks**: Interpreted languages often lack the compile-time checks that are present in statically typed compiled languages. This can lead to errors only being discovered during runtime, potentially affecting program reliability.
-   **Limited Performance for Intensive Computing Tasks**: For applications requiring heavy computational processing, such as scientific simulations or graphics rendering, the slower execution speed of interpreted languages may be a significant drawback.
    Solutions involve using packages like NumPy and SciPy which call compiled languages from Python.
-   **Dependency on Language Runtimes**: Some interpreted languages require a runtime environment, which may need to be installed separately. This can complicate the deployment process and introduce compatibility issues.
-   **Less Control Over Hardware**: Interpreted languages may provide less direct control over hardware interactions compared to low-level languages like C or assembly. This limitation can be a concern for systems programming or tasks requiring fine-grained control.

## Special cases

Some languages defy strict categorization as purely compiled or interpreted languages due to their hybrid or mixed execution models.

In the case of JavaScript, it is commonly considered an interpreted language as browsers execute its code on the fly.
However, modern JavaScript engines, like Google Chrome's V8, leverage Just-in-Time (JIT) compilation to translate parts of the code into machine code just before execution, introducing a compiled aspect to its execution.

Java, on the other hand, follows a two-step process where the source code is initially compiled into bytecode by the Java Compiler.
This bytecode, being platform-independent, can run on any system equipped with the Java Virtual Machine (JVM).
The JVM then utilizes JIT compilation to convert the bytecode into native machine code during runtime, blurring the line between compilation and interpretation.
This approach combines the portability of interpretation with the performance benefits of compilation.

Similarly, Julia, with a primary focus on performance, employs JIT compilation for dynamic code generation during program execution.
This enables the language to deliver efficient machine code while maintaining interactive development features, resembling the characteristics of an interpreted language.

In essence, these languages showcase a hybrid nature, borrowing elements from both compiled and interpreted paradigms.
The incorporation of JIT compilation allows for optimizations and performance enhancements while retaining the flexibility, interactivity, and platform independence typically associated with interpreted languages.
This unique blend contributes to the versatility and broad applicability of JavaScript, Java, and Julia across various programming scenarios.

## Stack Overflow Developer Survey

Each year, Stack Overflow conducts a [developer survey](https://survey.stackoverflow.co/2023/).
Analysts, IT leaders, reporters, and other developers turn to this report to stay up to date with the evolving developer experience, and technologies that are rising or falling in favor, and to understand where tech might be going next.

!!! danger

    These statistics are mainly for [software developers](https://survey.stackoverflow.co/2023/#section-developer-roles-developer-type), so this does not necessarily translate to your field.

### Popular languages

JavaScript: 63.61% <progress value="63.61" max="100" style="--value: 63.61; --max: 63.61;"></progress>

Python: 49.28% <progress value="49.28" max="100" style="--value: 49.28; --max: 63.61;"></progress>

Java: 30.55% <progress value="30.55" max="100" style="--value: 30.55; --max: 63.61;"></progress>

C++: 22.42% <progress value="22.42" max="100" style="--value: 22.42; --max: 63.61;"></progress>

Go: 13.24% <progress value="13.24" max="100" style="--value: 13.24; --max: 63.61;"></progress>

Rust: 13.05% <progress value="13.05" max="100" style="--value: 13.05; --max: 63.61;"></progress>

R: 4.23% <progress value="4.23" max="100" style="--value: 4.23; --max: 63.61;"></progress>

Julia: 1.15% <progress value="1.15" max="100" style="--value: 1.15; --max: 63.61;"></progress>

Fortran: 0.95% <progress value="0.95" max="100" style="--value: 0.95; --max: 63.61;"></progress>

[Full table](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-programming-scripting-and-markup-languages)

### Highest paid

Zig: $103,611 <progress value="103611" max="103611" style="--value: 1; --max: 1;"></progress>

Go: $92,760 <progress value="92760" max="103611" style="--value: 0.773; --max: 1;"></progress>

Rust: $87,012 <progress value="87012" max="103611" style="--value: 0.652; --max: 1;"></progress>

Python: $78,331 <progress value="78331" max="103611" style="--value: 0.471; --max: 1;"></progress>

Julia: $74,963 <progress value="74963" max="103611" style="--value: 0.4; --max: 1;"></progress>

R: $74,963 <progress value="74963" max="103611" style="--value: 0.4; --max: 1;"></progress>

Dart: $55,862 <progress value="55862" max="103611" style="--value: 0; --max: 1"></progress>

[Full table](https://survey.stackoverflow.co/2023/#section-top-paying-technologies-top-paying-technologies)

## What language(s) should I learn?

It is important to have a diverse toolbox so you can use the right tool for the job.
Here are my&mdash;biased&mdash;opinions of what languages you should learn with decreasing importance.

### Python

One of the most popular programming languages, most private and public sectors use Python for data science, machine learning, web frameworks, and overall automation.

**When to use**: Default tool.

### JavaScript

JavaScript reigns supreme in the web development world with web applications and fancy animations.
You should also learn the basics of HTML and CSS.

!!! note

    TypeScript is a superset of JavaScript that adds static typing, allowing developers to catch potential errors early in the development process.
    It compiles down to plain JavaScript, making it compatible with existing JavaScript code and widely supported in web development.

**When to use**: Web applications and interactive plots.

### Rust

Rust is a modern compiled programming language that is growing rapidly.
C++ could be another option, but I believe Rust takes care of many things that make C++ challenging to use casually.

**When to use**: Performance and security need to be top-notch.
