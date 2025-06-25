## **Day 64: The Spell Evaluator – Unleash the Final Magic** ✨🧮

### **📜 Kahani / Story**  
After successfully converting the ancient spells into a clear postfix format on Day 63, it’s now time to reveal the ultimate power of the spell. In the mystical archives, the final incantation remains locked behind an expression that must be evaluated to unleash its magic.  

Echo explains,  
*"Ab jab tumhare paas ek perfect postfix expression hai, tumhe usse evaluate karna hoga. Yeh process, jo stack ka istemal karke hota hai, bilkul waise hi hai jaise real-world calculators ya compilers complex expressions ko solve karte hain. Tumhara kaam hai is expression ko evaluate karke final spell power ko calculate karna."*

Nariyal Bhai adds,  
*"Yeh bilkul simple hai – jaise tum daily problems solve karte ho, waise hi tumhe yeh expression solve karna hai using a stack. Bas har operator ko sahi tarah apply karo aur final value dekh lo."*

Mayur concludes,  
*"Let your code be the wand that transforms a series of numbers and operators into a single, potent force of magic. Evaluate the spell and reveal its true power!"*

Iss tarah, tumhari coding journey DSA ke stack concepts ko real-world expression evaluation se jodti hai, ensuring that the magic of the spell is fully unleashed.

---

### **🎯 Challenge: Postfix Expression Evaluator**  
Write a program that:  
1. **Takes a valid postfix expression as input.**  
   - The expression can include single-digit operands (0-9) and operators (+, -, *, /).  
2. **Evaluates the postfix expression using a stack-based approach.**  
3. **Prints the final computed value.**

*Note:*  
- Assume that the input expression is well-formed.  
- Division should be handled as integer division or float division based on your implementation.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter postfix expression: 231*+9-
```  
**Calculation:**  
- Process:  
  - 2 3 1 * → 3*1 = 3  
  - 2 + 3 = 5  
  - 5 9 - → 5 - 9 = -4  
**Output:**  
```
Result: -4
```

#### **Example 2**  
**Input:**  
```
Enter postfix expression: 57+82-*
```  
**Calculation:**  
- Process:  
  - 5 7 + → 12  
  - 8 2 - → 6  
  - 12 * 6 = 72  
**Output:**  
```
Result: 72
```

#### **Example 3**  
**Input:**  
```
Enter postfix expression: 42/3*
```  
**Calculation:**  
- Process:  
  - 4 2 / → 2  
  - 2 3 * = 6  
**Output:**  
```
Result: 6
```

---

### **💡 Hints**  
- **Stack Usage:**  
  - Traverse the expression from left to right.  
  - If the element is an operand, push it onto the stack.  
  - If the element is an operator, pop the required number of operands, perform the operation, and push the result back onto the stack.
- **Final Result:**  
  - After processing the entire expression, the stack will contain the final result.
- **Real-World Connection:**  
  - This is similar to how compilers and calculators evaluate complex expressions quickly using stack-based algorithms.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day64_spell_evaluator.[ext]` (for example, `day64_spell_evaluator.py`).

---

### **🌟 Motivational Quote**  
*"When every element is combined with precision, even the most complex spells reveal their power. Let your code evaluate and transform chaos into magic!"* 🚀

---

Your Spell Evaluator challenge blends DSA stack concepts with real-world expression evaluation techniques, unlocking the final magic of the ancient spell.  
Ready for **Day 65**? Let's continue our journey through the enchanted realms of code!