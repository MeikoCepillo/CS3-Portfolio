# Annex C : Code Quality Assessment Worksheet

**Section:** Balingkilat  
**C# / Name:**
#7 - Cass, lane William L.  
#8 - Cepillo, Ryan Meiko L.  
#9 - Coloma, Khalix D.    
**Date:** August 16, 2026

---
# Question with Checklist

**1. Efficiency**  
Which algorithm is faster when the list of numbers is very large? Why?:  
Pseudocode 1 is faster because it only checks each number once, and pseudocode 2 compares every number against each other, making it slower on large lists.  

---

| Pseudocode 1 | Pseudocode 2 | 
|:---|:---|
| [x] Does the algorithm use one loop or two nested loops? | [x] Does the algorithm use one loop or two nested loops? |
| [] Does the algorithm repeat work unnecessarily? | [x] Does the algorithm repeat work unnecessarily? | 
| [x] Which algorithm finishes in fewer steps? | [] Which algorithm finishes in fewer steps? |

---

**2. Readability**  
Which algorithm is easier to understand at first glance? What makes it clearer?:  
Pseudocode 1 is easier to understand, as it keeps the highest number in a clear variable, and pseudocode 2 is confusing with nested loops.  

| Pseudocode 1 | Pseudocode 2 | 
|:---|:---|
| [x] Are variable names meaningful (e.g., max vs. bigger)? | [x] Are variable names meaningful (e.g., max vs. bigger)? |
| [simple] Is the logic simple or complicated? | [complicated] Is the logic simple or complicated? | 
| [x] Are there fewer lines of code? | [] Are there fewer lines of code? |

---

**3. Maintainability**  
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?:  
Pseudocode 1 is much easier to update due to its simplicity, and pseudocode 2 would require a lot of extra steps, making it easy to break.  

| Pseudocode 1 | Pseudocode 2 | 
|:---|:---|
| [x] Is the structure straightforward? | [] Is the structure straightforward? |
| [] Would adding new steps break the code easily? | [x] Would adding new steps break the code easily? | 
| [x] Is there less chance of errors when updating? | [] Is there less chance of errors when updating? |

---

**4. Testability**  
Which algorithm is easier to test with different inputs? Why?:  
Pseudocode 1 is easier to test because it is straightforward and logical. Pseudocode 2 has complex loops, making it harder to test and fix errors.  

| Pseudocode 1 | Pseudocode 2 | 
|:---|:---|
| [x] Can you test with small lists easily? | [] Can you test with small lists easily? |
| [x] Does the algorithm have fewer conditions to check? | [] Does the algorithm have fewer conditions to check? | 
| [x] Is the output predictable and clear? | [] Is the output predictable and clear? |

---

**5. Security**  
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?:  
Check if the list is empty and if all items are integers.  

| Pseudocode 1 | Pseudocode 2 | 
|:---|:---|
| [x] Does the algorithm check if the list is empty? | [] Does the algorithm check if the list is empty? |
| [] Does it handle invalid inputs (like letters instead of numbers)? | [x] Does it handle invalid inputs (like letters instead of numbers)? | 
| [x] Does it avoid crashing when inputs are unusual? | [] Does it avoid crashing when inputs are unusual? |

---

**6. Final Answer**  
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer:  
Pseudocode 1 is better being simpler, faster, easier to use, and maintain.  

---
