# Architecture Reconstruction (AR)

> The process of obtaining a (partially) documented architecture for an existing system

> A reverse engineering approach that aims at reconstructing viable architectural views of
a software application (Ducasse & Pollet)
__ 


Synomym: Architecture Recovery


Ducasse & Pollet. *Software Architecture Reconstruction:
a Process-Oriented Taxonomy* (https://rmod.inria.fr/archives/papers/Duca09c-TSE-SOAArchitectureExtraction.pdf)

## Motivation - #1: Many tasks in SE need architectural documentation
 - Adoption
 - Refactoring 
 - Reengineering
 - Understanding
 - Coding
 - Risk assessment for security
 - Architectural Evaluation

 


 


## Motivation - #2 Often Architectural Documentation is Missing or Obsolete

- Have you seen architectural documentation for every system?

Discussions:
- Why is it missing? 
- Why is it obsolete? 
  

## Why is Architectural Documentation Often Obsolete?

 - it's hard to maintain
 - link (traceability ) between architecture and code is often not obvious
 - no perceived value for the customer
 - because people make changes that are not aligned (**architectural drift**)
   - possible solution: enforcing architectural constraints 
     - special DSL for architecture constraints definition
     - implemented as Unit Tests  


# What Happens When Developers Are Not Aware of Architecture?

e.g. possible scenario of dev not being aware of architecture => architectural anti-pattern.

 ![](lectures/images/adjacent_connector_.png)

## What to Do? 

- reading the code? ArgoUML vs. War and Peace


- **Reverse Reengineering** -- a general process for making sense of code bases
- **Reengineering** -- reverse engineering + restructuring
- **Architecture recovery** -- Specific method: **Symphony** 


# Reverse Engineering & Reengineering


> “Reverse Engineering is the process of analyzing a subject system to identify the system’s components and their interrela- tionships and create representations of the system in another form or at a higher level of abstraction.”

> “Reengineering ... is the examination and alteration of a subject system to reconstitute it in a new form and the subsequent im- plementation of the new form.”

(Demeyer et al., Object Oriented Reengineering Patterns,http://scg.unibe.ch/download/oorp/OORP.pdf)




# Symphony: A Process for Reconstruction

- By van Deursen et al.
- Recovers views and viewpoints as in IEE 1471 / 3+1
- Distinguishes between three kinds of views:
    1. Source 
     - view extracted from artifacts of a sytem
     - not necessarily architectural (e.g. AST)
    1. Target  
     - describes architecture-as-implemented
     - any of the 3+1 views
    1. Hypothetical 
     - architecture-as-designed
     - existing documentation
     - presentations


## Symphony Stages: Design (blue) & Execution (yellow)

![sympony](lectures/images/symphony.png)

## Symphony: Design

Problem elicitation
- “Business case” for reconstruction
- What is the problem? 

Concept determination
- What architectural information is needed to solve the problem?
- Which viewpoints are relevant?


## Symphony: Execution

Data gathering
 - collecting and extracting low-level source views
 - can involve a multitude of sources
 
 
Knowledge inference
 - going from source to target views
 - abstracting low-level information
 
 
Information interpretation 
 - analysis, creating new documentation


# Meta-Architecture of Architecture Recovery Tools

### Extract-Abstract-Present

    Extract = data gathering

    Abstract = knowledge inference

    Present = information interpretation

![](lectures/images/eap2.png)

# Your Own Architectural Expertise

- the tools and analyses we present in this course are just tools
- you *know the master by their tools*
- however, what matters very often is **the master** themselves
- the more knowledge you have, the more sense you will make of a given system during AR

e.g. you are reconstructing the architecture of a web framework
- which of the following classes is critical for it's understanding
  - Request
  - Markup
- the answer depends on your expertise

And although, to a certain extent some of the tools we talk about in this course can complement your own expertise, there is no AR without it. 

There are things that you just have to know
e.g. 
- usually, in python, all the code in a package 

# Data Gathering

Sources of information
- Source Code [(Interactive)](./code/Data_Gathering_Intro.ipynb)
- Running System (next lecture)
- Version Control System (after the next lecture)

## Bibliography


**Symphony: View-Driven Software Architecture Reconstruction**. 
- Authors: van Deursen, A., Hofmeister, C., Koschke, R., Moonen, L., Riva, C. In Proceedings of the Fourth Working IEEE/IFIP Conference on Software Architecture (WICSA’04), pp. 122-132


**What architects should know about reverse engineering and reengineering**. 
- Authors: Koschke, R. (2005). In Proceedings of the Third Working IEEE/IFIP Conference on Software Architecture (WICSA’05), pp 4-10

**[Object Oriented Reengineering Patterns](http://scg.unibe.ch/download/oorp/OORP.pdf)**
- Authors: Demeyer, Ducasse, Nierstrasz

