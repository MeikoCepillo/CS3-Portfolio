# Annex B: Computational Thinking Exercise - Smart Vending Machine

**Section:** 9-Balingkilat  
**C# / Name:** #8 / Ryan Meiko L. Cepillo
**Date:** August 12, 2026

---

## Step 1: Identify the Big Problem

**Main Problem:**  
The school’s vending machine is unreliable, inefficient, and prone to transaction, inventory, and user input errors, resulting in poor user experience and slow service.

---

## Step 2: Identify Sub-Problems

1. **Incorrect Change:** The machine miscalculates or fails to dispense the accurate change to students.
2. **Lack of Inventory Tracking:** Items run out without notifying staff or updating the display, causing students to attempt to buy out-of-stock items.
3. **User Selection Errors:** Students frequently press the wrong buttons, resulting in purchasing unintended items.
4. **Transaction Latency:** The system processes requests slowly during peak usage times when multiple students use it consecutively.

---

## Step 3: Define Computational Thinking Approaches

| Sub-Problem | CT Skill | Example Solution |
| :--- | :--- | :--- |
| **1. Incorrect Change** | **Algorithm Design** | Write a precise logic routine: $\text{Change} = \text{Amount Paid} - \text{Item Cost}$. Verify available bills/coins in the hopper before accepting payment, then dispense exact change. |
| **2. Unnotified Out-of-Stock Items** | **Pattern Recognition / Data Processing** | Track stock counts using inventory sensors. When an item count reaches 0, automatically display "Out of Stock" on screen and send a notification to the supplier/staff. |
| **3. Accidental Item Selection** | **Abstraction** | Simplify the user interface by adding a screen preview with a confirmation prompt (e.g., *"You selected Item A: [Yes/No]"*) before charging the user. |
| **4. Slow Performance** | **Decomposition** | Break down the checkout sequence into parallel processes so hardware checks (coin validation, dispenser initialization) run concurrently rather than sequentially. |

---

## Step 4: Pseudocode for Selected Sub-Problem

### **Selected Sub-Problem:** Item Selection & Change Calculation

```text
START
    DISPLAY "Welcome! Select an item."
    READ SelectedItem
    
    IF SelectedItem is OUT OF STOCK THEN
        DISPLAY "Sorry, item is out of stock."
        EXIT
    ENDIF

    DISPLAY "Price: " + ItemPrice
    DISPLAY "Please insert payment."
    READ InsertedMoney

    IF InsertedMoney < ItemPrice THEN
        DISPLAY "Insufficient money. Transaction cancelled."
        RETURN InsertedMoney
    ELSE
        DISPLAY "Confirm purchase of " + SelectedItemName + "? (YES/NO)"
        READ UserConfirmation
        
        IF UserConfirmation == "YES" THEN
            Calculate Change = InsertedMoney - ItemPrice
            DISPENSE SelectedItem
            DISPENSE Change
            UPDATE InventoryCount = InventoryCount - 1
            DISPLAY "Thank you!"
        ELSE
            DISPLAY "Transaction cancelled."
            RETURN InsertedMoney
        ENDIF
    ENDIF
END
