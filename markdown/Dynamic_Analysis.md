# Dynamic Analysis

### the analysis of computer software that is performed by executing programs on a real or virtual processor

1. Comparison with Static Analysis
2. Uses of Dyanmic Analysis
3. Technical Approach
4. Limitations



# 1. Comparison with Static Analysis

### Static analysis

- analyzes the system’s artifacts to obtain information that is valid for all possible executions (e.g, program structure or potential calls between different modules). (*View-Driven Software Architecture Reconstruction*...)


- static view of the system is valid for all executions


Cons: 
- Some structural relationships are not known before execution
- There is no information about runtime properties (memory consumption, timing)





### Some structural relationships are not known at compile time

- Example: *can't see beyond polymorphism*

```python

class Person(object):
   def have_fun():
      pass
   
class Student(Person):
   def have_fun():
      print("student kind of fun")
   
class SoftwareArchitect(Person):
   def have_fun():
      print("architect kind of fun")
      
# later in code...
def process(p:Person):
   p.have_fun()

# statical analysis tool can't know which `have_fun` implementation is called 

```



### There is no information about runtime properties

Architecturally Relevant
- Actual resource consumption
- Timing, performance

Open Source Research Tool: [Flask Monitoring Dashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard)
And [Related Student Projects](https://github.com/mircealungu/student-projects/labels/flask-monitoring-dashboard)  



# 2. Uses of Dynamic Analysis in Architecture Recovery


In general:
- compensate for limitations of static analysis (e.g. Can't reliably detect `dead code` https://news.ycombinator.com/item?id=27036626)


In Architecture Recovery -> Extraction phase: 
  - dependencies between components (e.g. `Model` -> `UI`)
  - properties of components (e.g. `Model` is never used, `Connection` is slow, etc.)



# 3. Technical Approach

1. Instrument System <- focus
2. Run System and Collect Data
3. Analyze data
4. Iterate


## Step 1: Instrument System

- Add Logging Statements
- Modify Code at Runtime
- Analyze Network Traffic

### Instrumentation (1): Add Logging Statements

- allows surgical precision - adding log statements only where relevant
- might already be there; although it's usually higher-level
- log-levels: (DEBUG, TRACE)

con:
- invasive - implies changing the program
- usually we want to log extensively



### Instrumentation (2): Modify Code at Runtime

What to Modify? 

- source code
  - using reflection (or code generation)

- bytecode
  - using specialized tools


### Modifying Program with Reflection

#### Reflection = the ability of a program to manipulate as data something representing the state of the program during its own execution

> - **Introspection** is the ability for a program to observe and therefore reason about its own state. 
> - **Intercession** is the ability for a program to modify its own execution state or alter its own interpretation or meaning.

In some languages it's easier to do (e.g. Ruby, Python)  than in others (Java)



### Example: Introspection in Python

Goal: 
- a program to observe it's own state (e.g. a class observing it's own methods)


Python Specific: 
- use the `cls_name.__dict__.items( )` to get all the attributes of a class 
- filter those which represent a method because they have the `__call__` annotation


```python
""" 
    introspects a class
    returns a _dictionary_ with 
    (method name, method body) tuples
    
"""
def methods_in_class(cls_name):

    result = {}
    
    for item_name, value in cls_name.__dict__.items( ):
            if hasattr( value, '__call__' ):
                result [item_name] = value

    return result.items()

```


```python
# an object-oriented foobar example
class Foo(object):

    def __init__(self):
        self.x= 'foo'

    def do(self):
        print(self.x)


class Bar(object):

    def __init__(self, foo):
        self.foo = foo

    def do(self):
        self.foo.do()
```


```python
methods_in_class(Foo)
```




    dict_items([('__init__', <function Foo.__init__ at 0x10d8060d0>), ('do', <function Foo.do at 0x10d868b80>)])



### Example: Intercession in Python

Goal: 
- let's have our program replace it's methods on the fly 

Python specific: 
- We rely on `setattr( cls_name, key, replacement )` to replace the method found under the name `key` with `replacement`
  - each with another method that prints a note when the function is called
  - we will thus trace the execution of the program!





```python
""" 
    Implementing decorator pattern by defining a new function 
    that does a print and then calls the original function
"""
def print_decorator( original_function ):

    def decorated( *args, **kwargs ):
        print (f'Calling: {original_function}')
        return original_function( *args, **kwargs )
    
    return decorated

```


```python
""" 
    Replace every method in class cls_name 
    with the replacement method 
"""
def replace_methods( cls_name, replacement ):

    methods = methods_in_class(cls_name)
    
    for method_name, implementation in methods:
            setattr( cls_name, 
                     method_name, 
                     replacement ( implementation ) )
```


```python
# same classes as before
class Foo(object):

    def __init__(self):
        self.x= 'foo'

    def do(self):
        print(self.x)

```


```python
replace_methods(Foo, print_decorator)
Foo().do()
```

    Calling: <function Foo.__init__ at 0x10d8ff8b0>
    Calling: <function Foo.do at 0x10d8ff820>
    foo



```python
class Bar(object):

    def __init__(self, foo):
        self.foo = foo

    def do(self):
        self.foo.do()
```


```python
replace_methods(Bar, print_decorator)
bar = Bar(Foo())
bar.do()
```

    Calling: <function Foo.__init__ at 0x10d8ff8b0>
    Calling: <function Bar.__init__ at 0x10d8ff430>
    Calling: <function Bar.do at 0x10d8ff4c0>
    Calling: <function Foo.do at 0x10d8ff820>
    foo


### Function Wrappers 

- we have used **function wrappers**, a pattern inspired from the Decorator design pattern:
  - a function *wraps* another function in order to
    - perform some *prologue* and/or *epilogue* tasks
    - optimize (e.g. cache results )
  - while the *wrapper* is *fully* compatible with the wrapped function so it can be used instead

More on Function Wrappers: 
- https://wiki.python.org/moin/FunctionWrappers
- Wrappers to the Rescue: http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.18.6550&rep=rep1&type=pdf


### Advantages of Wrappers

- allows surgical precision 
- allow **even more surgical deployment and removal** of wrappers at runtime
  - e.g. FlaskMonitoringDashboard 
  - as opposed to off-the-shelf tools that trace the entire execution of the program
      
### Disadvantages of Wrappers
- they introduce an overhead (but then, so do all code related tracing)
- they require you to obtain the **live** objects (must be in the same process as the instrumented code)
      

### Challenges for You

#### Extract dynamic dependencies from your case study system?
- can you create a wrapper that traces method calls (both the caller and the callee?)
- fully qualified names of the caller method
- can you run it on your Python case study? (ping me if you need help!)


#### Implement a **Code Coverage Viewpoint**?
  - for every class compute the ratio of methods called in the unit tests from the total number of methods
  - aggregate to module level


### Modyfing Bytecode at Runtime: Java Example


- Java programs are compiled into bytecode
- Bytecode is executed on the JVM
- You can provide a Java Agent (via command line argument -javaagent) that modifieds the bytecode before it being executed


<img src="./images/java_instrumentation.png" style="width:70%" />


Advantage: JVM bytecode instrumentation works for multiple languages; And Source code is harder

Image source: https://blog.sqreen.com/building-a-dynamic-instrumentation-agent-for-java/


## Instrumentation (3): Network Traffic Analysis

Not exactly `traditional` dynamic analysis:
- useful for service oriented architectures
- monitors the messages on the wire
- powerful approach for reverse engineering services


Read: https://danlebrero.com/2017/04/06/documenting-your-architecture-wireshark-plantuml-and-a-repl/


Note: **Something like this would be a great starting point for a thesis**



## Step 2: Run Code and Collect Data

Not that trivial as you might think

Running the Code At all: 

- Challenges
  - configuration
  - dependencies
  - unwritten rules
  - some systems don't have a clear entry point (e.g. libraries)


- Helpful practices
  - continuous integration
  - containerization
  - infrastructure as code
  

## Which Scenarios to Run from the System?

- Run the unit tests if they exist 
- Exercise "features" 

> A feature is a realized functional requirement of a system. [...] an observable unit of behavior of a system triggered by the user [Eisenbarth et al., 2003].


# Limitations of Dynamic Analysis

- limited by execution coverage 
  - a program does not reach an execution point... => no data (e.g. Word but user never prints)
- can slow down the application considerably 
- can result in a large amount of of data

  


## Further Reading

[Optional] Papers: 
- **Visualizing the Execution of Java Programs**. Wim De Pauw, Erik Jensen, Nick Mitchell, Gary Sevitsky, John Vlissides, Jeaha Yang

- **Correlating Features and Code Using a Compact Two-Sideed Trace Analysis Approach**. Orla Greevy, Stephane Ducasse. 


### References

[Eisenbarth et al., 2003]. Thomas Eisenbarth, Rainer Koschke, and Daniel Simon. Locating features in source code. IEEE Computer, 29(3):210–224, March 2003.

## Uses Beyond Architecture Recovery

- Performance monitoring (e.g. the FMD)
- Intercepting and tracing specific calls
  - e.g. calls to the DB, calls across the network
  
- Quality control (e.g. test coverage tool)
- Dynamic optimizations 
- Logging Energy Usage (https://help.apple.com/instruments/mac/current/#/dev03a7149d)
