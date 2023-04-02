# Software Evolution Analysis

![](heraclitus.png)

> Everything changes, and nothing stands still, 
> 
> and you can not step twice in the same... system.
> 
> -- Heraclitus


# Metaphor Limitations: Software Architecture

- Makes it sound like it's something fixed...
- Even real world architecture, in time changes [Brand]
- [Brand] - *How Buildings Learn*. Steward Brand
  - The Long Now Foundation - Podcast








## Further Metaphors

My Favorite Metaphors of Software Development Emphasize Change...


### 1. Performance Art
- art: because it's creative
- performance: you can't put it in a frame 
- => *advice:* if you ever create a cool innovative software then **make a screencast** about it


### 2. A Garden 
- It needs somebody to always tend to it

> I still remember the jolt I felt in 1958 when I first heard a friend talk about building a program, as opposed to writing one. In a flash he broadened my whole view of the software process.

Brooks however thinks the building metaphor is not well equipped to handle the current projects we’re developing. Instead of building, which requires adequate plans and foresight, we should focus on growing a program organically. (Once even a very simple program is up and running, developers are much more enthusiastic about the progress.)



### 3. Software Aging 

David Parnas's **Software Aging** [1]

> Programs, like people, get old. 

- We can’t prevent aging, but 
  - we can understand its causes, 
  - take steps to limits its effects, 
  - temporarily reverse some of the damage it has caused, 
  - and prepare for the day when the software is no longer viable

[1] Software Aging. David Lorge Parnas, https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=296790


# Laws of Software Evolution

Lehman[1] proposed the laws about **e-type systems**:
  - an e-type system is *embedded* in the real world
  - and since the real world always changes... 
      - even if it weren't, the software ecosystem eventually changes [2] 
      - e.g. javascript packages, etc.

[1] Lehman, Belady. Program Evolution: Processes of Software Change, London Academic Press, London, 1985

[2] We'll talk more about ecosystems in the ASE course

## 1st Law of Software Evolution: E-Type Systems Must Change


> A program that is used in a real-world environment must change, or become progressively less useful in that environment. (Lehman's Law of Continuing Change)



        



## 2nd Law of Software Evolution: Ent*0py Happens!

Manny Lehmann's **Law of Increasing Entropy**: 

> As a program evolves, it becomes more complex, and extra resources are needed to preserve and simplify its structure.



# What if We Use System Evolution for Good? 
## e.g. for understanding

 
 By data mining the version repository we can find: 

  - places in the code which are high-risk (because they were risky in the past)
    - + linking with issue tracker info

  - parts of the system that need refactoring (study of Hitesh Sajnani)
  
  - navigation suggestions (e.g. Mylar for Eclipse)
  
  - infer programmer knowledge


Today: 
  1. entities in the codebase where most effort was invested
  1. invisible dependencies between files (e.g. logical coupling)
  
  
  
 






## VCS Capture The Software Evolution

VCS = version control system 


Over the last two decades **we have seen increases in**...
  - **popularity of version control systems**
https://trends.google.com/trends/explore?date=all&q=git,svn,software%20architecture,mercurial
    - it's even funny for us to think that people used to email files around to collaborate
    - one of the many practices that we, software engineers, have been teaching the rest of the world



- **knowledge of how to manage versions**
  - branching strategies
  - integration with CI
  - semantic versioning 



*How to integrate this information in AR?...*


## Architectural Viewpoint: Evolutionary Hotspots 

### Evolutionary Hotspots =(*def*) **code entities where most effort was invested ** [1]


Assumption: effort is proportional to architectural relevance


Why? 
- Philosophycally
 > *"The value of anything is proportional to time invested in it."* (M. Lungu)
 
 
- Practically:
  - high *churn* (change density) predicts bugs better than size [...]
  - studies observe correlation between churn and complexity metrics [...]
  - it's likely that they'll require more effort in the future (e.g. yesterday's weather [Girba et al.])
    
    
- Pragmatically:
  - can be detected with **language independent analysis** (which is good for polyglot systems)



### Evolutionary Hotspots In Practice

Challenges / Implementation Details: 
- how to measure effort invested? 
- what are the entities (files, aggregates?)
- on what period is the study performed 
  - results will likely differ for periods






### Example Analysis

VCS: Git

Period of study: whole history

Entities: files (+aggregation to modules)

Invested effort: number of commits

Case Study: Zeeguu-Core

Toolbox: Python + PyDriller + gitpython

Online: https://colab.research.google.com/drive/19f2-lmL07rSBoyKpx5ZQo0LY17_Un4YD?usp=sharing



```python
import sys

!{sys.executable} -m pip install pydriller
!{sys.executable} -m pip install gitpython
```


```python
from pydriller import RepositoryMining
REPO_DIR = '/Users/mircea/Zeeguu-Core/'

```

#### Every commit is modelled as "multiple modifications" each one involving a filename


```python
for commit in RepositoryMining(REPO_DIR).traverse_commits():
    print("commit" + str(commit))
    print ("- Author {}".format(commit.author.name))
    
    for m in commit.modifications:
        print(
            " modified {}".format(m.filename),
            " with a change type of {}".format(m.change_type.name),
            " and the complexity is {}".format(m.complexity)
        )

```

#### Let's Count the Modifications for Each File


```python
from collections import defaultdict

commit_counts = defaultdict(int)

for commit in RepositoryMining(REPO_DIR).traverse_commits():
    for modification in commit.modifications:
        try:
            commit_counts [modification.new_path] += 1
        except: 
            pass

sorted(commit_counts.items(), key=lambda x: x[1], reverse=True)[:42]

```

#### Problem: many `__init__.py` files in our system but only one in the counts!

- what's the full file name? 

- looking at the documentation of PyDriller [1] we see that there's two:
  - old_path
  - new_path

- why? 
- which one should we be using? 

[1] https://pydriller.readthedocs.io/en/latest/commit.html


#### Lesson: to track full paths  we need to also track *individual file evolution*


```python
from pydriller import ModificationType

commit_counts = {}

for commit in RepositoryMining(REPO_DIR).traverse_commits():
    for modification in commit.modifications:
        
        new_path = modification.new_path
        old_path = modification.old_path
        
        try:

            if modification.change_type == ModificationType.RENAME:
                commit_counts[new_path]=commit_counts.get(old_path,0)+1
                commit_counts.pop(old_path)

            elif modification.change_type == ModificationType.DELETE:
                commit_counts.pop(old_path, '')

            elif modification.change_type == ModificationType.ADD:
                commit_counts[new_path] = 1

            else: # modification to existing file
                    commit_counts [old_path] += 1
        except Exception as e: 
            print("something went wrong with: " + str(modification))
            pass
        
sorted(commit_counts.items(), key=lambda x:x[1], reverse=True)

```

#### Aggregating to module level




```python
from code.basic_abstraction import (
    module_from_path, 
    top_level_module
)

module_activity = defaultdict(int)

for path, count in commit_counts.items():
    if ".py" in str(path):
        l2_module = top_level_module(module_from_path(path), 2)
        module_activity[l2_module] += count

sorted(module_activity.items(), key=lambda x: x[1], reverse=True)


```


```python
most_active_modules = sorted(module_activity.items(), key=lambda x: x[1], reverse=True)

top_most_active_modules= [each[0] for each in most_active_modules][:5]
top_most_active_modules

```

#### Architectural View: Relationships Between Evolutionary Hotspots



```python
# packages required for drawing
import sys
!{sys.executable} -m pip install networkx --upgrade
!{sys.executable} -m pip install matplotlib
```


```python
def system_module(m):
    return m in top_most_active_modules

def module_size(m):
    return 30*module_activity[m]
```


```python
from code.basic_abstraction import (
    dependencies_graph, 
    draw_graph_with_weights,
    top_level_module,
    abstracted_to_top_level)

directed = dependencies_graph(REPO_DIR)
directedAbstracted = abstracted_to_top_level(directed, system_module)

draw_graph_with_weights(directedAbstracted, module_size, (18,8))
```

### Stepping Back

We used Git but similar for any VCS 

Alternative tools for VCS Analysis: 

- git log + Unix Command Line tools (See tutorials by Spinellis, Helge in ASE, or Tornhill)
  
- your IDE (e.g. integrated git blame, visual diff, etc.)

- Any others...?

Definition of most active can be tuned based on needs
- could be log-weighted towards recency (discard past changes more)
- could be used to replay the history of the system by looking at non-overlapping time windows


### Limitations

- ignores developer styles
  - the guy with micro-commits vs. the girl who like to commit infrequently but large chunks of code
  
- might detect files that `README.md`, or `LICENSE.md` changes the most
  - can be combined with static complexity metrics [1]






## 2. Dependency Extraction: Logical Coupling

** Logical coupling** detects when **two sub-systems** change together **frequently**
- The more they change together, the more likely they are dependent
- Can capture dependencies that are not detectable by static/dynamic analysis
  - e.g. ? 


Introduced in the context of an industrial case study [1]

[1] Detection of Logical Coupling Based on Product Release History, Gall et al., ’98

### Logical Coupling: The Details...


- What are sub-systems (files? folders? packages?)
- What does it mean change together (same commit? sliding time window?)
- The threshold for "frequently" (e.g. *75% of the commits min 10*, etc.)



### Advantages of Logical Coupling

Language Independent

Complements some Static Analysis disadvantages: 
- can not capture all the situations (i.e. writing to a file, reading from a file)
- does not work with documents that are not source code (e.g. XML files)


## Evolution Analysis Beyond Architecture Recovery

- Improved developer tools
  - e.g. recording and replaying software evolution (e.g. "Replay" for Eclipse)
    - fine-grained (method-level) evolution monitoring (Robbes et al.)


- *Program comprehension* when first encountering a new system



# References

- Detection Logical Coupling Based on Product Release History ([pdf](papers/Gall-LogicalCoupling.pdf)). Gall et al.
- Software Aging ([pdf](papers/SoftwareAging.pdf)). David Lorge Parnas 

# Further Reading
- *Source Code as a Crime Scene*. A. Tornhill
- Laws of Software Evolution Revisited. M. Lehman.





