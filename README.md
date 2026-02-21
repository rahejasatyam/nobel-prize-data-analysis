#  Nobel Prize Data Analysis

> A simple Python project that automatically fetches Nobel Prize data from the internet and shows you interesting facts about it — like how many prizes were given each year, who won them, and in which fields.

---

##  What Does This Project Do?

The **Nobel Prize** is one of the most prestigious awards in the world, given every year to people who make outstanding contributions in fields like Physics, Chemistry, Medicine, Literature, Peace, and Economics.

This project:
1. **Automatically downloads** Nobel Prize data from the official Nobel Prize website (no manual downloading needed!)
2. **Analyzes** the data — counting prizes, laureates (winners), and categories
3. **Shows a bar chart** so you can visually see how many prizes were given each year

Think of it like a mini research tool that does all the hard work for you!

---

##  What Information Will You See?

After running the project, you'll get:

-  **Total Years** — How many different years are covered in the data
-  **Total Prizes Awarded** — The overall number of Nobel Prizes given
-  **Total Laureates** — The total number of people who have won a Nobel Prize
-  **Unique Categories** — How many different fields (like Physics, Peace, etc.) have prizes
-  **A Bar Chart** — A visual graph showing prizes given per year

---

##  Who Is This For?

- **Curious people** who love history and want to explore Nobel Prize data
- **Beginners** — no advanced technical knowledge is needed!

---

##  What You Need Before Starting

###  1. Python 3

Python is a free programming language. Check if you have it:

1. Open your **Terminal** (Mac/Linux) or **Command Prompt** (Windows)
2. Type this and press Enter:
   ```
   python --version
   ```
3. If you see `Python 3.x.x`, you're ready! 
4. If not, download it free from [python.org](https://www.python.org/downloads/)

---


###  2. Required Python Libraries

This project uses some extra Python tools (called **libraries**) that aren't included with Python by default. Here's what they do:

| Library | What It Does |
|---|---|
| `requests` | Downloads data from the internet |
| `numpy` | Helps with number calculations |
| `pandas` | Organizes and analyzes data like a spreadsheet |
| `matplotlib` | Creates charts and graphs |

You'll install all of these in the next section — it only takes one command!

---

##  How to Set It Up (Step by Step)

### Step 1 — Download the project

Download all the project files. You should have:
- `assignment.py` — the main Python script
- `README.md` — this guide

Put all files in the **same folder** on your computer.

---

### Step 2 — Open your Terminal or Command Prompt

- **Windows:** Press `Win + R`, type `cmd`, press Enter
- **Mac:** Press `Cmd + Space`, type `Terminal`, press Enter
- **Linux:** Press `Ctrl + Alt + T`

---

### Step 3 — Navigate to the project folder

In the terminal, go to the folder where you saved the files. For example:

```bash
cd Desktop/nobel-prize-analysis
```

>  `cd` means "change directory" — it's how you move between folders in the terminal.

---

### Step 4 — Install the required libraries

Type this command and press Enter:

```bash
pip install requests numpy pandas matplotlib
```

This will automatically download and install all the tools the project needs. Wait for it to finish (it may take a minute or two).

>  `pip` is Python's built-in tool for installing extra libraries. Think of it like an app store for Python tools.

---

### Step 5 — Run the project

Once everything is installed, type this and press Enter:

```bash
python assignment.py
```

The program will now:
1. Connect to the internet and download Nobel Prize data
2. Analyze the data
3. Print the results in your terminal
4. Open a bar chart window showing prizes per year

---

## 👀 What to Expect After Running

Your terminal will show something like this:

```
--- Nobel Prize Data Analysis ---
Total Years Present: 122
Total Prizes Awarded: 621
Total Laureates Honored: 989
Unique Categories: 6

Prizes Per Year:
1901    6
1902    6
1903    5
...
```

And a **bar chart window** will pop up that looks like a graph showing prize counts across different years.

>  Close the chart window when you're done viewing it. The program will end automatically after that.

---

##  How to Stop the Program

If the program is running and you want to stop it before it finishes, go to your terminal and press:

```
Ctrl + C
```

---

##  Common Problems & Fixes

| Problem | Fix |
|---|---|
| `python: command not found` | Try `python3` instead of `python` |
| `pip: command not found` | Try `pip3` instead of `pip` |
| `ModuleNotFoundError` | Run the install command in Step 4 again |
| `Failed to fetch data` | Check your internet connection and try again |
| Chart window doesn't appear | Make sure `matplotlib` installed correctly; try reinstalling it |

---

##  Project Files Overview

```
📂 your-folder/
 ├── assignment.py    ← The main Python script that runs everything
 ├── prize.json       ← A sample of the Nobel Prize data (for reference)
 └── README.md        ← This guide
```

##  Data Source

All Nobel Prize data comes from the **official Nobel Prize API**:

🔗 [https://api.nobelprize.org/v1/prize.json](https://api.nobelprize.org/v1/prize.json)

This means the data is always up-to-date — whenever a new Nobel Prize is awarded, it will appear the next time you run the project!
