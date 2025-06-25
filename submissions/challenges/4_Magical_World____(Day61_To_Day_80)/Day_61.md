## **Day 61: The Spell Order – Arrange the Spells** ✨

### **📜 Kahani / Story**  
In the enchanted realm, magic is all about the right order. The ancient scrolls reveal that certain spells must be cast before others for their magic to work properly.  
   
Echo explains,  
*"Yaar, spells need to be arranged in a specific order to unlock their true power. Tumhe given dependencies ko dekhte hue, spells ko sahi sequence mein arrange karna hai."*  

Nariyal Bhai adds,  
*"Bas, socho ki yeh ek simple task scheduling jaisa hai, jisme kuch tasks (spells) ko pehle karna zaroori hai. It’s simpler than it sounds!"*  

Mayur concludes,  
*"Aao, spells ko sahi order mein arrange karo. Agar order thik hoga, toh magic asar karegi!"*

Iss tarah, tumhari coding journey ab DSA ke basic dependency ordering se judti hai without being too complex.

---

### **🎯 Challenge: Spell Order Arrangement**  
Write a program that:  
1. **Takes a list of spells and their dependencies as input.**  
   - Each dependency is given as: Spell A must be cast before Spell B.
2. **Determines a valid order to cast the spells.**  
   - Assume there are no cycles (a Directed Acyclic Graph scenario).
3. **Prints the ordered sequence of spells.**

*Note:*  
- For simplicity, assume the number of spells is small (e.g., 3-5), and the dependencies are straightforward.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Spells: Fireball, Shield, Heal  
Dependencies:
Fireball -> Shield
Shield -> Heal
```  
**Output:**  
```
Spell Casting Order: Fireball, Shield, Heal
```

#### **Example 2**  
**Input:**  
```
Spells: Charm, Curse, Bless  
Dependencies:
Charm -> Curse
Bless -> Curse
```  
**Output:**  
```
Spell Casting Order: Charm, Bless, Curse
```

---

### **💡 Hints**  
- You can solve this using a simple Depth-First Search (DFS) or even by manually checking dependencies since the number of spells is small.  
- Think of it as sorting tasks based on prerequisites.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day61_spell_order.[ext]` (e.g., `day61_spell_order.py`).

---

### **🌟 Motivational Quote**  
*"Sahi order se hi magic hoti hai. Arrange your spells well, and let your magic unfold!"* 🚀

---

Your Spell Order challenge simplifies dependency ordering into a manageable task. Tumhara solution will arrange the spells in a valid sequence, ensuring the magic works just as intended.  
Ready for **Day 62**? Let's continue our magical journey!