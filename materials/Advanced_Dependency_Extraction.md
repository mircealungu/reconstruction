# Advanced Dependency Extraction

### Tool Demo: Softwarenaut


<a href="https://vimeo.com/62767181">
    <img src="images/softwarenaut.png" width=600/>
</a>

## Limitations of Regular Expressions

In our *import parser* case: 
- remember that we only parse the imports at the top of a file
- we could change the regex to not start with `^` but then we might match comments...

In general
- regexes are not good at parsing recursive grammars (e.g. nested methods)

Challenge:
- How to extract low-level dependencies between classes / methods?

## Chomsky Hierarchy of Languages  

![](lectures/images/languages.png)

- Regexes are the weakest of the formal grammars
- You can prove that they can't parse real programming languages

Your regex would have a hard time knowing that this import is not actually executed

    """
    import py-cool
    """

## Semantic Analysis (Parsing)

- basic component in compiler technology
- the most precise way to **extract** information from source code


Approaches
- manual: e.g. PEGs (Parsing Expression Grammars)
- parser generators (Bison, Antlr, etc.)
- language specific parsing libraries (e.g. `ast` package in Python)


In general, a complicated business (See: A Few Billion LOC Later)

## Parse Tree

The parse tree is a 
- concrete representation of the input
- retains all of the information of the input
- the empty boxes represent whitespace (i.e. EOL)

![](lectures/images/parse__tree.png)



## AST = Abstract Syntax Tree

The minimal representation of the meaning of the program

Contains nodes that correspond to constructs in the language

Enables inspection and modification of the program (or program transformation)

![](lectures/images/ast.png)

## In Python

- `ast` package is part of the default language distribution
  - similar packages in other languages
- tree of nodes representing syntactic constructs
- nodes are instances of ast.AST

### AST nodes 

Have two types of attributes:
  - attributes (properties)
    - lineno, col_offset
  - fields (subnodes)
    - One of 5 types: identifier, int, string, object, bool

### Loading an AST from a file


```python
import ast
f = open("/Users/mircea/Zeeguu-Core/zeeguu_core/model/user.py")
user_ast = ast.parse(f.read())
print(user_ast.body[0])  
```

    <_ast.Import object at 0x10c64f048>


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


```python
class GenericVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print (type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)
```


```python
visitor = GenericVisitor()
visitor.visit(user_ast)
```


```python
class ImportVisitor(ast.NodeVisitor):

    def visit_Import(self, import_node):
        # retrieve the name from the returned object
        # normally, there is just a single alias
        for alias in import_node.names:
            print (f'importing {alias.name}')
        
        # allow_parser to continue 
        super(ImportVisitor, self).generic_visit(import_node)


```


```python
ImportVisitor().visit(user_ast)
```

    importing datetime
    importing json
    importing random
    importing re
    importing sqlalchemy.orm
    importing zeeguu_core
    importing dateutil.relativedelta


### More on the `ast` package

https://docs.python.org/3/library/ast.html



## Beyond Source Code

What other sources of information do we have for dependencies?
- runtime dependencies 
- indirect dependencies
- and we'll see more ...


## Programming Challenge

- replace the naïve import in the Basic_Abstraction notebook with imports based on the AST package
- if this is too boring, try to extract info about classes and method calls between them


```python

```
