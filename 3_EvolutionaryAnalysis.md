class: center, middle

IT University of Copenhagen

#### Software Architecture Reconstruction

# III: Evolutionary Analysis

Assoc. Prof. Mircea Lungu

mlun@itu.dk


<div style="font-size:small; margin-top:150px">
<a href="https://github.com/mircealungu/reconstruction">github.com/mircealungu/reconstruction</a>
</div>


---

# Outline

- What is Evolutionary Analysis
- How can it help in architecture recovery?
- Challenges of Evolutionary Analysis 

---

## What is Software Evolution?

![400](images/heraclitus.png)

> Everything changes, and nothing stands still,
> and you can not step twice ... in the same system.

> -- Heraclitus on Software Evolution


---

## People used to talk about software maintenance as a separate phase.

Nowadays, academics talk about software evolution. 
A term introduced by M. Lehman. 
Who also proposed the laws of software evolution. 

From this POV, the architecture metaphor is not the best. A garden evolves. Would have been a better metaphor.

Although, architecture is also not that bad.
How buildings learn. 
Even buildings evolve.

---


##  Where can we find information about the evolution?

Version control repository.


---

# In which way can this information be useful for architecture recovery?

It can tell us about which parts of the system are most changed. 
And thus, very likely, most important. 


---

## Architectural Viewpoint: Evolutionary Hotspots

  
### Evolutionary Hotspots =(*def*) **code entities where most effort was invested ** [1]


Assumption: effort is proportional to architectural relevance  

Why?

Philosophycally

> *"The value of anything is proportional to time invested in it."* (M. Lungu)


Practically:
- high *churn* (change density) predicts bugs better than size [...]
- studies observe correlation between churn and complexity metrics [...]
- it's likely that they'll require more effort in the future (e.g. yesterday's weather [Girba et al.])

Pragmatically:
- can be detected with **language independent analysis** (which is good for polyglot systems)

---

## What are the challenges when analyzing software evolution? 





