## **Union-Find (Disjoint Set Union) – Simple Explanation**  

**Concept:**  
- **Union-Find** is a data structure used to keep track of elements that are split into one or more disjoint (non-overlapping) sets.  
- It supports two primary operations:  
  - **Find:** Determines which set a particular element belongs to. This is often used to check if two elements are in the same set.  
  - **Union:** Merges two sets into one.

**Simple Example:**  
Imagine you have 5 devices labeled 1, 2, 3, 4, and 5. Initially, each device is isolated (i.e., in its own set):  
- Set 1: {1}  
- Set 2: {2}  
- Set 3: {3}  
- Set 4: {4}  
- Set 5: {5}

Now, suppose you connect device 1 with device 2. You perform a **union(1, 2)**, and now they become one set:  
- Set A: {1, 2}  
- Set 3: {3}  
- Set 4: {4}  
- Set 5: {5}

Next, you connect device 2 with device 3 by doing **union(2, 3)**. Because device 2 is already in set A, now devices 1, 2, and 3 are all in one set:  
- Set A: {1, 2, 3}  
- Set 4: {4}  
- Set 5: {5}

To check if device 1 and device 3 are connected, you use **find(1)** and **find(3)**. If they return the same representative (or root), then they are in the same set. In this case, they are connected.  

**Real-World Analogy:**  
Think of it as grouping friends together. Initially, everyone is alone. As you make connections (friendships), groups form. If you want to check if two people are in the same friend circle, you check if they belong to the same group. And if two friend circles merge, all friends are now part of one larger circle.

---

Now, let's apply this concept in our challenge.

---

## **Day 66: The Circuit Connector – Union-Find for Network Connectivity** ⚙️🔗

### **📜 Kahani / Story**  
In the multiverse’s power network, circuits and components have been disrupted by The Glitch, causing parts of the system to become isolated. The Debuggers need to restore full connectivity so that every component communicates properly.

Echo explains,  
*"Imagine each component as a device in a network. We need to check which devices are connected, and if not, we must connect them. Tumhara challenge hai to implement the Union-Find algorithm to efficiently manage these connections."*

Nariyal Bhai adds,  
*"Yeh bilkul waise hai jaise hum power grids mein check karte hain ki sab devices connected hain ya nahi. Agar alag network hai, unhe join karo."*

Mayur concludes,  
*"Let your code be the tool that bridges the gaps. Use union-find to detect connectivity and merge networks—ensuring the entire system works as one seamless unit."*

Iss tarah, tumhari coding journey DSA ke Union-Find concept ko real-world network connectivity se connect karti hai.

---

### **🎯 Challenge: Circuit Connector using Union-Find**  
Write a program that:  
1. **Takes as input the number of components (nodes)** and a list of connections (edges) between them.  
2. **Uses the Union-Find data structure** to:  
   - **Check if two components are connected.**  
   - **Merge networks by connecting components.**  
3. **Processes queries** where each query either asks:  
   - "Are components X and Y connected?"  
   - Or "Connect component X with component Y."  
4. **Prints the result** of each query (for connectivity queries, output "Connected" or "Not Connected").

*Note:*  
- Initialize each component as its own set.  
- Use path compression in the find operation and union by rank if possible for efficiency.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Number of components: 5  
Initial Connections:  
1 2  
3 4  

Queries:  
Q1: Are 1 and 2 connected?  
Q2: Are 2 and 3 connected?  
Q3: Connect 2 and 3  
Q4: Are 2 and 3 connected?
```  

**Output:**  
```
Connected  
Not Connected  
(After connection)  
Connected  
```

#### **Example 2**  
**Input:**  
```
Number of components: 4  
Initial Connections:  
1 2  

Queries:  
Q1: Are 1 and 3 connected?  
Q2: Connect 3 and 4  
Q3: Are 3 and 4 connected?
```  

**Output:**  
```
Not Connected  
Connected  
```

#### **Example 3**  
**Input:**  
```
Number of components: 6  
Initial Connections:  
2 3  
4 5  

Queries:  
Q1: Are 1 and 2 connected?  
Q2: Connect 1 and 2  
Q3: Are 1 and 3 connected?
```  

**Output:**  
```
Not Connected  
Connected  
```

---

### **💡 Hints**  
- **Implementation Steps:**  
  - Create an array `parent[]` where each element is initially its own parent.  
  - For **find**, recursively find the root of an element and apply path compression.  
  - For **union**, link the roots of the two sets (use union by rank to keep the tree shallow if possible).
- **Query Processing:**  
  - For connectivity queries, use the find operation on both components and compare their roots.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day66_circuit_connector.[ext]` (e.g., `day66_circuit_connector.py`).

---

### **🌟 Motivational Quote**  
*"Every connection counts. Build bridges, merge worlds, and let your code unite the fragmented pieces into a harmonious whole!"* 🚀

---

Your Circuit Connector challenge ties the Union-Find data structure to real-world network connectivity issues, demonstrating how efficient merging of components can restore a broken system. Tumhara solution will ensure that every part of the multiverse is connected and working together seamlessly.

Ready for **Day 67**? Let's continue our journey into advanced systems!