## **Day 65: The Labyrinth Navigator – Find Your Way Out with BFS** 🗺️🚪

### **📜 Kahani / Story**  
Deep in the enchanted realm lies a mysterious labyrinth—its twisting corridors and hidden passages have confused many. To escape, you must find the shortest path from the entrance to the exit. This challenge isn’t just magic; it mirrors real-world navigation systems and robotics that use Breadth-First Search (BFS) to find the optimal route.

Echo explains,  
*"Imagine you’re in a maze where every turn could be the way out. In real-world applications, like GPS systems and robotics, BFS helps to quickly determine the shortest path. Tumhara challenge hai ek simple maze ko solve karna using BFS, so you can guide the hero safely to the exit."*

Nariyal Bhai adds,  
*"Yeh bilkul waise hai jaise hum building evacuation plans banate hain – har room aur corridor ko check karke exit tak pahunchna. Bas, algorithm ko sahi tarah implement karo aur maze se bahar nikal jao!"*

Mayur concludes,  
*"Let your code be the guiding light that navigates through every twist and turn. Use BFS to ensure you find the quickest escape route from this enchanted labyrinth."*

Iss tarah, tumhari coding journey ne advanced DSA (BFS) ko real-world navigation and magic se connect kar diya hai.

---

### **🎯 Challenge: Maze Solver using Breadth-First Search (BFS)**  
Write a program that:  
1. **Represents a maze as a grid** (2D array) where:  
   - `'S'` denotes the start position.  
   - `'E'` denotes the exit.  
   - `'.'` denotes an open path.  
   - `'#'` denotes a wall (blocked path).  
2. **Uses BFS to find the shortest path** from the start to the exit.  
3. **Prints the shortest path length** or the path itself (optional).

*Note:*  
- You may assume that the maze is bounded and there is only one start and one exit.  
- Movements are allowed in four directions: up, down, left, and right.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Maze Grid:
S . . #
. # . .
. # E .
```
*(This can be represented as a 2D array or a list of strings.)*

**Output:**  
```
Shortest path length: 5
```
*(One possible path: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2))*

#### **Example 2**  
**Input:**  
```
Maze Grid:
S # .
. . .
. # E
```

**Output:**  
```
Shortest path length: 4
```
*(One possible path: (0,0) -> (1,0) -> (1,1) -> (1,2) -> (2,2))*

#### **Example 3**  
**Input:**  
```
Maze Grid:
S . #
# . #
# . E
```

**Output:**  
```
Shortest path length: 6
```
*(One possible path: (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2))*
  
---

### **💡 Hints**  
- **BFS Fundamentals:**  
  - Use a queue to store the coordinates of cells to visit.  
  - Track visited cells to avoid loops.
- **Movement:**  
  - Define the four possible moves: up, down, left, and right.  
- **Path Calculation:**  
  - Maintain a distance counter for each cell reached.
- **Real-World Connection:**  
  - Think of it like navigating through a city grid using a GPS, where BFS finds the shortest driving route.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day65_labyrinth_navigator.[ext]` (e.g., `day65_labyrinth_navigator.py`).

---

### **🌟 Motivational Quote**  
*"In every maze, there’s a way out. With every step guided by logic, you can transform confusion into clarity. Let your code be the beacon that lights the path to freedom!"* 🚀

---

Your Labyrinth Navigator challenge ties the magic of an enchanted maze to the practical efficiency of BFS, demonstrating how DSA concepts can lead to real-world solutions in navigation and robotics.  
Ready for **Day 66**? Let's keep exploring the wonders of the multiverse!