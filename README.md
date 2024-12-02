
---

# Melon Library

**Melon Library** provides simple tools for creating terminal-based games.  
Currently, it includes 6 tools.

---

## Features

### 1. Print a Beautiful Line  
No more manually using `=` or `-` symbols!  
```python
melon.whiteline()
```

---

### 2. Clear the Terminal  
Clear the terminal without the **os** library:  
```python
melon.clear()
```

---

### 3. Check if a Number is Odd  
Quickly check if a number is odd:  
```python
melon.is_odd(5)  # Output: True
melon.is_odd(2)  # Output: False
```

---

### 4. Run a Python File  
A better way to run Python files:  

**Using subprocess:**  
```python
subprocess.run(["python", "file.py"])
```

**Using Melon Library:**  
```python
melon.run("file.py")
```

---

### 5. Generate a Random Number  
A simple alternative to the **random** library:  
```python
melon.randomize(1, 3)
```

---

### 6. Print text with hex color
A colored printer(may not work on all terminals)

```python
melon.colorize("#ee00ff", "this is a purple colored text")
```
Enter string values please

---

## Installation  
You cant download this library with "pip install melon"
Follow these steps to install the library:  

1. Download as a ZIP file.  
2. Unzip the file to `/username123/melon`.  
3. Open a terminal and run the following commands:  
   ```bash
   cd melon
   ```
   ```bash
   python setup.py sdist bdist_wheel
   ```  
   ```bash
   pip install .
   ```  

---

## Contact  
If want contact with me:
**feedback5383@gmail.com**  

--- 