## **Day 62: The Magic Mirror – Binary Search for the Ancient Spell** ✨🔍

### **📜 Kahani / Story**  
Deep within the enchanted library of the multiverse lies a magic mirror that reveals secrets of ancient spells. The mirror displays a **sorted list** of spells known only to the wisest wizards.  
   
Echo explains,  
*"Dekho, is magic mirror mein sab spells already sorted hain. Agar tumhe koi particular spell dhoondhna ho, toh tumhe binary search ka istemal karna hoga – just like how efficient systems search through sorted data in real-world applications. Yeh technique is as crucial in algorithm design as it is in maintaining quick access to important information."*  

Nariyal Bhai softly advises,  
*"Bilkul, binary search se tum quickly decide kar sakte ho ki koi spell list mein hai ya nahi. Socho, yeh bilkul waise hi hai jaise digital systems databases se data retrieve karte hain – fast and efficient!"*  

Mayur adds,  
*"Let your code be as sharp as a wizard’s wand! Use binary search to find the spell, and prove that your magical and algorithmic skills are equally enchanting."*

Iss tarah, tumhari coding journey real-world data search techniques (binary search) ko magical storytelling ke saath connect karti hai, jo practical applications mein bhi bahut kaam aata hai.

---

### **🎯 Challenge: Binary Search for an Ancient Spell**  
Write a program that:  
1. **Takes a sorted list of spells (strings) as input.**  
2. **Prompts the user for a target spell to search for.**  
3. **Implements binary search** to efficiently determine if the target spell exists in the list.  
4. **Prints a message** indicating whether the spell was found and, if found, its index.

*Note:*  
- The list of spells is already sorted in alphabetical order.  
- The search should be case-insensitive if possible.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Sorted Spells: "alohomora", "expelliarmus", "leviosa", "obliviate", "sectumsempra"
Enter target spell: leviosa
```  
**Output:**  
```
Spell found at index 2.
```

#### **Example 2**  
**Input:**  
```
Sorted Spells: "alohomora", "expelliarmus", "leviosa", "obliviate", "sectumsempra"
Enter target spell: wingardium
```  
**Output:**  
```
Spell not found.
```

#### **Example 3**  
**Input:**  
```
Sorted Spells: "accio", "expecto patronum", "lumos", "nox", "protego"
Enter target spell: nox
```  
**Output:**  
```
Spell found at index 3.
```

---

### **💡 Hints**  
- **Binary Search Logic:**  
  - Start with two pointers, `low` and `high`, set to the beginning and end of the list, respectively.  
  - Find the middle index and compare the target spell with the spell at the middle.  
  - Narrow down the search interval based on the comparison until the target is found or the interval is empty.
- **Real-World Connection:**  
  - This method is analogous to searching through sorted databases or directories in real-world applications, ensuring fast and efficient retrieval.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day62_magic_mirror.[ext]` (e.g., `day62_magic_mirror.py`).

---

### **🌟 Motivational Quote**  
*"When you combine the magic of code with the precision of binary search, every secret is just a search away. Keep exploring and let your curiosity guide you!"* 🚀

---

Your Magic Mirror challenge uses binary search to locate ancient spells, seamlessly blending algorithmic efficiency with a touch of enchantment. Tumhara solution will prove that even in the realm of magic, precision and efficiency are key.  
Ready for **Day 63**? Let's continue our journey through the multiverse!