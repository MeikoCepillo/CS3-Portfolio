# Annex B: Computational Thinking Exercise - Smart Vending Machine

**Section:** Balingkilat  
**C# / Name:** #8 - Cepillo, Ryan Meiko L.  
**Date:** August 12, 2026

---

## Step 1: Identify the Big Problem

**Main Problem:**  
The school’s vending machine is very unreliable, inefficient, and faulty resulting in poor user experience and slow service.

---

## Step 2: Identify Sub-Problems

1. **Incorrect Change:** The machine miscalculates or fails to dispense the accurate change to its users.
2. **Lack of Inventory Tracking:** Items run out without notifying staff or updating the display, causing the users to attempt to buy out-of-stock items.
3. **User Selection Errors:** Users frequently press the wrong buttons, resulting in purchasing unintended items.
4. **Transaction Efficiency:** The system processes requests slowly during peak usage times when multiple users use it consecutively.

---

## Step 3: Define Computational Thinking Approaches

| Sub-Problem | CT Skill | Example Solution |
| :--- | :--- | :--- |
| **1. Incorrect Change** | **Algorithm Design** | Write a precise logic routine: $\text{Change} = \text{Amount Paid} - \text{Item Cost}$. Verify available bills/coins in the hopper before accepting payment, then dispense exact change. |
| **2. Unnotified Out-of-Stock Items** | **Pattern Recognition / Data Processing** | Track stock counts using inventory sensors. When an item count reaches 0, automatically display "Out of Stock" on screen and send a notification to the supplier/staff. |
| **3. Accidental Item Selection** | **Abstraction** | Simplify the user interface by adding a screen preview with a confirmation prompt (e.g., *"You selected Item A: [Yes/No]"*) before charging the user. |
| **4. Slow Performance** | **Decomposition** | Break down the checkout sequence into parallel processes so hardware checks (coin validation, dispenser initialization) run concurrently rather than sequentially. |

---

## Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

### **Selected Sub-Problem:** Item Selection & Change Calculation
```mermaid
graph TD
    A([START: Student Approaches]) --> B[Display: Welcome! Enter Item Code]
    B --> C[/Read Keypad / Touch Input/]
    C --> D{Is Item Code Valid?}
    
    D -- No --> E[Display: Invalid Code. Try Again]
    E --> B
    
    D -- Yes --> F[Fetch Item Details: Name, Price, Stock]
    F --> G{Is Item In Stock?}
    
    G -- No --> H[Display: Out of Stock!]
    H --> I{Select another item?}
    I -- Yes --> B
    I -- No --> Z([END])
    
    G -- Yes --> J[Display Preview: Item Name & Price]
    J --> K[Prompt: 'Confirm Selection? Yes / No / Change']
    K --> L[/Read User Decision/]
    
    L -- Change / No --> M[Display: Selection Cancelled]
    M --> I
    
    L -- Yes --> N[Display: Please Insert Payment]
    N --> O[/Read Inserted Cash/]
    O --> P{Payment >= Price?}
    
    P -- No --> Q[Display: Insufficient Funds]
    Q --> R[Prompt: Insert More Cash or Cancel?]
    R -- Insert More --> N
    R -- Cancel --> S[Refund Payment] --> Z
    
    P -- Yes --> T[Calculate Change = Payment - Price]
    T --> U[Dispense Selected Item]
    U --> V[Dispense Change]
    V --> W[Display: Thank You!]
    W --> Z
```
