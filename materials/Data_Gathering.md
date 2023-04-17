# Data Gathering

Going deeper in this aspect: 
- Kinds of Data
  - Expert Knowledge (most important!)
  - Source Code Analysis
    - Textual (Regular Expressions)
    - Parsing (extracting ASTs) 
  - Version Control Information
  - Deployment Files
  - Database 
  - Dynamic Analysis 



# Abstraction 

- Kinds of Abstraction
  - Based on Existing Folder Structure
  - Based on Explicit Module Declarations
  - Automated based on Clustering Algorithms
  - "Key Components"


## Static Analysis

analysis of computer software without actually executing programs

- what we did with extracting `import` statements
   - ... it's SA at the most basic level
   - it's easy and fast
   - similar approaches would work for other languages


## Limitation of RegEx-es

Not powerful enough for PLs

Most basic in the Chomsky hierarchy of languages 
<img style="float:right; margin-right: 200px;" src="images/languages.png" width="400px"/>



## Limitations of RegEx based SA

- not be able to know whether it's commented out 
- would not be able to know that it's actuall real (could not be used)



## Limitations of  `import` based analysis

- too high level (e.g. how **strong** is a dependency) (fr: google automatically assessing the strength of dependencies)
- is the dependency really used? 


## Solution: Syntactic Analysis

- based on the grammar of the language
- grammar can be complicated to define !!!
  - Ref: grammar complexity for various languages
- many languages have embedded support (e.g. `ast` package in Python)



## Abstract Syntax Trees

extracted by parsing using the grammar of the language

intermediate representation that is used by the compilers
  - which use it to generate executables
  
can be used to extract dependencies (intresting for us)

can also be used for program transformations (not the topic of today)






## Dynamic Analysis

performed on executing software


## Strategies for Abstraction



## Key Components

use metrics
- FAN-IN / FAN-OUT
- PageRank
- ... 



## Discussion: Static vs. Dynamic Dependency Extraction

In terms of precision and recall: 
- high precision low recall: ... ?
- low precision high recall: ... ?

In terms of ease of execution:
- code 
- unit tests

In terms of data volume:
- huge
- large





```python

```
