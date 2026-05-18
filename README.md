# Minecraft Launcher (Tkinter)

A custom Minecraft Launcher built with Python and Tkinter using `minecraft_launcher_lib`.



This project was created mainly as a learning project to explore:
- Tkinter GUI development
- Minecraft launcher integration
- File handling
- Event-driven programming
- Working with subprocesses
- Managing multiple GUI screens

The launcher currently supports offline accounts, mod loader selection, Minecraft version selection, and launching Minecraft directly from a custom GUI.

---

# Features

- Offline account login
- Save usernames locally
- Mod Loader selection
- Minecraft version selection
- Launch Minecraft from GUI
- Multiple Tkinter screens
- Dynamic combobox updates
- Persistent offline usernames

---

# Project Development

The main structure and implementation of the launcher were created by me as part of learning Python GUI development and Minecraft launcher systems.

Main systems implemented by me:
- Main GUI structure
- Tkinter frame system
- Offline login system
- Username saving system
- Combobox integration
- Launcher layout
- Minecraft launcher integration
- Basic launcher workflow
- Frame navigation system

---

# Debugging & Improvements

During development, several issues were debugged and improved while learning.

The following improvements and fixes were added:

### Combobox Fixes
- Fixed incorrect combobox values caused by tuple data from `enumerate()`
- Properly separated loader IDs and loader names

### Minecraft Version Loading
- Fixed unsupported version object display
- Added readable version loading
- Added dynamic version updates when changing mod loaders

### Start Button Logic
- Fixed start button state logic
- Added dynamic enable/disable behavior using Tkinter events

### Username Saving
- Fixed newline issues in saved usernames
- Prevented duplicate usernames
- Updated combobox values dynamically after login

### File Handling
- Fixed crashes caused by missing:

```text
offline_username.txt
```

- Added automatic file creation

### Frame Navigation
- Improved frame switching logic
- Fixed inconsistent screen transitions

### Minecraft Launch Improvements
- Replaced blocking:

```python
subprocess.run()
```

with:

```python
subprocess.Popen()
```

to prevent launcher freezing while Minecraft is running.

### Code Structure Improvements
- Improved variable naming
- Improved loader handling structure
- Improved overall project organization

---

# Contribution Estimate

Approximate contribution split:

### My Work (~80%)
- Project idea
- GUI design
- Tkinter frame system
- Offline login system
- File saving system
- Launcher structure
- Minecraft integration
- Testing and project iteration
- Overall workflow and implementation

### Debugging & Improvement Help (~20%)
- Logic debugging
- Tkinter event handling improvements
- Combobox fixes
- Version loading fixes
- Start button fixes
- Launcher behavior improvements
- Code cleanup suggestions

---

# Requirements

- Python 3.11 or 3.12 recommended
- Java installed and added to PATH

Install dependency:

```bash
pip install minecraft-launcher-lib
```

Run the launcher:

```bash
python tk.py
```

---

# Current Status

### Working
- Offline Login
- Username Saving
- Mod Loader Selection
- Version Selection
- Minecraft Launch

### Planned Features
- Microsoft Authentication
- Better UI Design
- Theme Support
- Settings Menu
- Mod Downloader
- Java Detection
- Progress Bars
- Better Error Handling

---

# Built With

- Python
- Tkinter
- minecraft_launcher_lib

---

# Author

Ankit Kumar
