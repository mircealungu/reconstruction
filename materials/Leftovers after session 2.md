

---

# Backmatter

## What are the limitations of our relationship extraction?

--

- Missing Details
- Imprecisely Extracted

*Why?* 

---

### Missing Details

Other relationships that are more precise exist between the elements of the system
- Inheritance between classes
- Implementation of interfaces
- Method call
- The *cardinality of the relationship is not clear*
	- one import might be used 100 times in the file
	- another one might not be used at all

A special kind of dependency: logical coupling.

---

### Imprecisely Extracted
- Even imports are too imprecisely extracted
- What if an import is in a comment
- What if it is inside of a method
- What if it is inside of a commented out method?

*Why?*  

Because of the limitations of regular expressions.

*Solution?*

Parsing. 

---

## Parsing Source Code

  
- basic component in compiler technology: a.k.a. semantic analysis
- a precise way of **extracting** information from source code (vs. RE)


Approaches
- manual: e.g. PEGs (Parsing Expression Grammars)
- parser generators (Bison, Antlr, etc.)
  

In general, a complicated business 
- See: A Few Billion LOC Later
- use a language specific parsing library (e.g. `ast` package in Python)


---

## Parse Tree

- Full representation of the structure of a program
- Includes whitespace (e.g., EOL): empty boxes in  the figure
  

![540](lectures/images/parse__tree.png)

---

## AST = Abstract Syntax Tree

- Minimal representation of the meaning of the program
- Nodes correspond to constructs in the language
- Enables: inspection, modification and program transformation

  

![400](lectures/images/ast.png)


---

## In Python: the `ast` package

- `ast` package ([docs](https://docs.python.org/3/library/ast.html)) is part of the standard language distribution
- similar packages in other languages
- tree of nodes representing syntactic constructs
- nodes are instances of ast.AST
 

---

### AST nodes

Have two types of attributes:

- attributes (properties)

- lineno, col_offset

- fields (subnodes)

- One of 5 types: identifier, int, string, object, bool


---

### Visiting an AST

  

The Visitor design pattern strikes back :)

- Your class should subclass `ast.NodeVisitor`

- `NodeVisitor` subclasses traverse an AST

- Traversal is depth-first, preorder

- i.e. first node, then children

- You become involved by defining visit_<nodetype> methods

	- Visit your chidren, or define `generic_visit`
	
	- generic_visit calls visit() on all children of the node.

- Note: child nodes of nodes that have a custom visitor method won’t be visited unless the visitor calls generic_visit() or visits them itself.

  
- visit lets you *skip* subtrees
	- if you don't call generic_visit the visitor will not recurse in the current node
	- can be convenient for expediency

---

For Next Time
- Choose a system for yor case study
  - start familiarizing yourself with the system
    - [read all the code in one hour](https://eng.libretexts.org/Bookshelves/Computer_Science/Book%3A_Object-Oriented_Reengineering_Patterns_(Demeyer_Ducasse_and_Nierstrasz)/03%3A_First_Contact/3.03%3A_Read_all_the_Code_in_One_Hour)
    - download the code; can you make it run locally?
  - you should at least know what the system does before trying to recover it's architecture
  

- If your system is a Python system start applying the scripts of today on it
  - Consider applying them on [Zeeguu-API](https://github.com/zeeguu-ecosystem/Zeeguu-API) 
    - you'll have to make a few changes to the code though
    - Should be doable even if you don't have much programming skills (or?)
    - Submit [anonymous questions](https://docs.google.com/forms/d/e/1FAIpQLSeAyKO1WUYn9W9-ZN3UrPU2ScEkI0a6fKZsNMHmtuLUb6RHAg/viewform) or post on Teams if you encounter any problems 


- If you're a programmer: try implementing some of the programming challenges [for abstraction](Basic_Abstraction.ipynb#Programming-Challenges) and [extraction](Advanced_Dependency_Extraction.ipynb#Programming-Challenge)
- If you're not a programmer: start looking for tools that you'd like to use and start evaluating them


