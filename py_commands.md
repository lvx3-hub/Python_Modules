## 🐍 PYTHON PRO COMMANDS

### 🔍 Show Installed Python Path
```
python -c "import sys; print(sys.executable)"
```

### 📦 List All Installed Packages + Locations
```
python -m site
pip show somepackage
```

### 🧪 Run an Inline Python One-Liner
```
python -c "print(sum(range(1, 101)))"
```

### 📁 Start a Temporary HTTP Server
```
python -m http.server
```

### 🐚 Start Python with Shell Access
```
python -i script.py
```

### 🐛 Run a Script in Debug Mode
```
python -m pdb script.py
```

### 📦 Create .pyc Compiled Files
```
python -m compileall your_script.py
```

### 🔬 Inspect Object from Terminal
```
python -c "import math; print(dir(math))"
```

### 🧪 Test Version Info of Anything
```
python -c "import numpy; print(numpy.__version__)"
```

## 📦 PRO `pip` COMMANDS

### 🔍 List Outdated Packages
```
pip list --outdated
```

### ⬆️ Upgrade All Outdated Packages in One Line (PowerShell)
```
pip list --outdated --format=freeze | % { $_.split('==')[0] } | % { pip install --upgrade $_ }
```

### 🧼 Uninstall All Installed Packages
```
pip freeze > uninstall.txt
pip uninstall -y -r uninstall.txt
```

### 📁 Export and Reinstall Dependencies
```
pip freeze > requirements.txt
pip install -r requirements.txt
```

### 🔬 Check What Depends on a Package
```
pipdeptree --reverse --packages pandas
```

### 📊 Visualize Package Tree
```
pipdeptree
```

### 🔍 Find Where a Package Is Installed From
```
pip show requests
```

### 💣 Check for Known Security Issues
```
pip install pip-audit
pip-audit
```

## 💡 BONUS: ENVIRONMENT MANAGEMENT

### 📦 Create a Clean Virtual Environment
```
python -m venv env
env\Scripts\activate
```

### 🧪 Show Which Virtual Environment You're In
```
where python
python -c "import sys; print(sys.prefix)"
```

