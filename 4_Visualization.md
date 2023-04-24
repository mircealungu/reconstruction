
class: center, middle

IT University of Copenhagen

#### Software Architecture

###  Session #11

# Reconstruction (IV): Visualization

Assoc. Prof. Mircea Lungu

mlun@itu.dk

<div style="font-size:small; margin-top:150px">
<a href="https://github.com/mircealungu/reconstruction">github.com/mircealungu/reconstruction</a>
</div>


---

## Outline 

- The importance of presenting information
- Polymetric Views - Metrics-Enhanced Architectural Views
- Student Submission Examples

---
# The Importance of Presenting Information

Well presented information visualization: 
- Can tell stories
- Can save lives
- Can help understand complexity

---


## Napoleon's Invasion of Russia in One Infographic

![](images/tufte_napoleon.png)

---

## Dr. John Snows Cholera Map of London

![520](images/london-cholera-map.png)

???

In a now legendary experiment in 1854, Dr. John Snow, a London physician, conducted a simple yet brilliant test that helped to settle the debate about the transmission of cholera. Snow drew a map [see Figure 2 below] of a virulent cholera outbreak in one of the poorest neighborhoods of London – served by central wells and no sewage collection. He plotted the homes and numbers of people affected, and in a flash of insight, mapped the location of the wells that provided water for the hardest hit neighborhoods. The maps he generated and the interviews he conducted with the families of victims convinced him that the source of contamination was the water from the Broad Street well. **He received permission from local authorities to remove the pump, which forced residents to go to other, uncontaminated wells for water. Within days, the outbreak subsided**.”

From: https://www.circleofblue.org/2013/world/peter-gleick-200-years-of-dr-john-snow-a-significant-figure-in-the-world-of-water/


---

## Book Recommendation

![200](images/tufte-book.png)

Contains the previous examples and many more

Encourages you to think about presenting information 

---

# Visualizing Software 

- UML
- Polymetric Views


---

## UML As an Information Presentation Mechanism

![600](images/uml_diagram_of_poker_game.png)

##### The UML Diagram of a Pocker Game: 25 Classes

---

## A More Realistic UML Diagram

![](images/java_link_api.png)

##### Java Link API - A persistence API

---

### Limitations of UML Class Diagrams

- do not scale well
- it is not an information visualization tool
- it was designed as a specification language
- not even ArgoUML has class diagrams about itself

*Solution? Learn from Infovis!*


---

## An Infovis Approach: Polymetric Views

System Complexity of ArgoUML
	- Class Hierarchies
	- Height: LOC
	- Width: NOM
	- Color: number of commits

![600](images/argouml_system_complexity.png)



???

- TODO: add reference to the Polymetric Views paper

---

### Polymetric Views

Infovis approach

Make use of the preattentive processing features
- size
- color
- shape
- position


![300](images/argouml_system_complexity.png)



---

### An Architectural Polymetric View

- Dependency width: number of low-level method calls
- Node size: LOC

![400](images/snaut_as_polymetric_view.png)



