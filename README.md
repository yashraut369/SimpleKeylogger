# Updated Repository Structure

Here's the correct directory structure for the SimpleKeylogger project:

```
SimpleKeylogger/
├── LICENSE
├── README.md
├── requirements.txt
├── main.py
└── keylogger/
    ├── __init__.py
    ├── keylogger.py
    └── utils.py
```

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yashraut369/SimpleKeylogger.git
cd SimpleKeylogger
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the keylogger:
```bash
python main.py
```

To run with custom options:
```bash
python main.py --output logs/keystrokes.txt --hidden
```
