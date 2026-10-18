# Waggle: Robot Monkey Desktop Pet 🐒

Bring your desktop to life with Waggle, a robotic monkey that reacts, roams, sleeps, hangs, and plays with a draggable ball! Built with Python and PyQt5, Waggle features animated movement and expressive reactions.

## Installation and Running

### 🖥️ Windows Application

1. Visit the [Releases page](https://github.com/Akshita029/Waggle-Robot-Monkey-Desktop-Pet/releases).
2. Download `Waggle-Robot-Monkey.zip`.
3. Extract the ZIP file.
4. Open the extracted `DesktopPet` folder.
5. Run `DesktopPet.exe`.

**Important:** Keep the extracted application files and folders together. Do not move `DesktopPet.exe` out of its folder.

### 💻 Running from Source

**Requirements:** Python 3 and PyQt5.

1. Download or clone this repository.
2. Make sure the `pet` folder and its PNG image assets are present beside `desktop pet.py`.
3. Open a terminal in the project folder.
4. Install PyQt5:

   ```bash
   python -m pip install PyQt5
   ```

5. Run the program:

   ```bash
   python "desktop pet.py"
   ```

### 📁 Project Structure

```text
Waggle-Robot-Monkey-Desktop-Pet/
├── desktop pet.py
├── README.md
└── pet/
    ├── Robot Monkey Idle 1.png
    ├── Robot Monkey Walk 1.png
    └── ...other image assets
```

The `pet` folder must remain beside the Python file so the program can locate its images.

## Built With

- Python
- PyQt5
- PyInstaller (for packaging the Windows application)
