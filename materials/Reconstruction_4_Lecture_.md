## Lecture #12
# Architecture Reconstruction (Part IV): Dynamic Analysis

M. Lungu 

mlun@itu.dk

April 20th, 2020


**NOTE**: If you want to follow along during the interactive part, clone/download **Dynamic_Analysis.ipynb** from:
    
    https://github.com/mircealungu/itu-architecture-reconstruction/
    


### Plan for the day

- An Introduction to [Dynamic Analysis](Dynamic_Analysis.ipynb)
- Trailer: Software Engineering Specialization
- Discussion: Individual Assignment

### Trailer: Software Engineering Specialization

- you can have me as advisor :)

but even more: 
- multiple lecturers
- multiple topics
- lots to choose from


### Individual Assignment / Deliverable

What: **Reporting on an Architecture Reconstruction Project** 


**Deadlines**: Submit **first draft** by the end of week 18 (May 3rd) if you want early feedback; otherwise submit together with the final report.

Goal: The report should present the architecture reconstruction process done on an open source system. You have to have a very strong argument for analyzing something that’s not open source. The report should be structured along the five steps of the Symphony process. Make sure to also provide a brief description of the (semi-)automated tools that you used. 

The system can be Zeeguu-Ecosystem (https://github.com/zeeguu-ecosystem/) a component of which (Core) we are using as a case study during the class) or can be another system that you are interested in. Your report should show that you have developed a good understanding of the system, and much more importantly, that you have a good understanding of the techniques of architecture reconstruction. 

In fact, if you decide to focus more on tool building and starting from the examples that we do in class you make them into slightly more advanced/intelligent analysis tools, then you can spend less time on the system analysis itself. And the other way around.

However, although we would be happiest to see that you take the code that we build in class and you improve on it building your own analysis toolbox, if you are not confortable with this ***(i.e. with coding)*** you can also: 

* use the analysis scripts we did in class and focus more on the manual investigation of the source code and other resources around the project

* **use a third party tool** that does equivalent analysis to what we do in class; however, in this case make sure to start early in evaluating tools because not all are easy to use;

You choose which architecturally relevant viewpoints you want to include in your report. 

* A module view is the simplest, and this is also why we focused the first two AR lectures on it. However, make sure to explain it well by investigating and eventually describing the roles of both the modules and the dependencies (remember the discussion about “verbs and nouns” in Lecture 11). 

* If you decide to extract a reflexion model that’s cool. Ask one of the developers of your system for a hypothetical diagram; or find one in the documentation and see whether the system conforms to it. 

* Other viewpoints would definitely be interesting to see. 


*** Effort should be proportional to 4 days of work (you should have a bit of time to become immersed in the problem)*** 
-- (possible time allocation: 60% analysis  -- 40% writing)


Focus on some part that's most intriguing to you. 
