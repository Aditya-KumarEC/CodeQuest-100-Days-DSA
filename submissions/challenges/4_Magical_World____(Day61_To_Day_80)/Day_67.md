## **Day 67: The Labyrinth Explorer – Navigate with Depth-First Search (DFS)** 🗺️🔦

### **Topic Explanation: Depth-First Search (DFS)**  
- **DFS** is an algorithm used to traverse or search through graphs and trees.
- It works by exploring as far as possible along a branch before backtracking.
- **How It Works:**  
  - Start from a given node.
  - Explore one branch completely before moving to the next branch.
  - This can be implemented recursively or using a stack.
  
**Simple Example:**  
Imagine exploring a cave system:  
- You enter a cave (node 1) and follow a tunnel (node 2).  
- At the end of tunnel 2, you find another passage (node 4).  
- When you reach a dead-end, you backtrack and explore another tunnel (node 3) from the entrance.  
- DFS ensures you explore every possible path deeply before moving on.

---

## **📜 Kahani / Story**  
In the heart of the multiverse, you find yourself trapped in an ancient labyrinth filled with winding passages and secret chambers. The Debuggers have told you that the exit lies hidden somewhere deep within this maze.  
   
Echo instructs,  
*"To navigate this labyrinth, you must explore every twist and turn thoroughly. Use Depth-First Search (DFS) to traverse the maze, exploring one path deeply before backtracking and trying another. This is just like systematically exploring every corridor in a mysterious building."*  

Nariyal Bhai adds,  
*"Yeh bilkul waise hai jaise hum purane haveli ke har kamre mein ghuste hain, taaki koi raasta na chhut jaye. Tumhara DFS algorithm har door ko khol ke dekh lega!"*  

Mayur concludes,  
*"Let your code be your torch in this dark maze. Traverse every path with DFS until you find the exit – and prove that no labyrinth is too complex for your logic!"*

Iss tarah, tumhari coding journey DFS ke practical use ko real-world maze exploration se jodti hai.

---

### **🎯 Challenge: Maze Traversal using DFS**  
Write a program that:  
1. **Represents a maze or graph as an adjacency list.**  
2. **Performs a DFS traversal** starting from a given start node.  
3. **Prints the order in which nodes are visited.**

*Note:*  
- You can implement DFS recursively or iteratively using a stack.
- Assume the graph is connected and there are no cycles (or handle cycles by marking visited nodes).

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Graph (Adjacency List):
1: [2, 3]
2: [4]
3: [5]
4: []
5: []
Start Node: 1
```  
**Output:**  
```
DFS Order: 1 2 4 3 5
```

#### **Example 2**  
**Input:**  
```
Graph:
A: [B, C]
B: [D, E]
C: [F]
D: []
E: []
F: []
Start Node: A
```  
**Output:**  
```
DFS Order: A B D E C F
```

#### **Example 3**  
**Input:**  
```
Graph:
X: [Y, Z]
Y: [W]
Z: []
W: []
Start Node: X
```  
**Output:**  
```
DFS Order: X Y W Z
```

---

### **💡 Hints**  
- **Recursive Implementation:**  
  - Define a DFS function that marks the current node as visited and recursively calls itself on unvisited adjacent nodes.
- **Iterative Implementation:**  
  - Use a stack to manage nodes, push the starting node, then pop and process nodes while pushing their unvisited neighbors.
- **Cycle Handling:**  
  - Maintain a set or list of visited nodes to avoid infinite loops if cycles exist.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day67_labyrinth_explorer.[ext]` (e.g., `day67_labyrinth_explorer.py`).

---

### **🌟 Motivational Quote**  
*"In every labyrinth, persistence leads to discovery. Explore deeply, and let your code light up the darkest corners!"* 🚀

---

Your Labyrinth Explorer challenge uses DFS to navigate an ancient maze, illustrating how methodical exploration can uncover hidden paths—just as real-world systems and algorithms work to find solutions in complex environments.  
Ready for **Day 68**? Let's continue our journey!