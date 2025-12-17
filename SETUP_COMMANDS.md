# Setup Commands for MediPredict Lite Stack

## Docker Infrastructure Setup

1. **Start Docker services:**
```bash
docker compose up -d
```

2. **Check service status:**
```bash
docker compose ps
```

3. **View logs:**
```bash
docker compose logs -f
```

4. **Stop services:**
```bash
docker compose down
```

5. **Stop and remove volumes (clean slate):**
```bash
docker compose down -v
```

## Frontend Setup (/client)

1. **Initialize Vue 3 project with Vite and TypeScript:**
```bash
npm create vite@latest client -- --template vue-ts
```

2. **Navigate to client directory:**
```bash
cd client
```

3. **Install base dependencies:**
```bash
npm install
```

4. **Install additional frontend dependencies:**
```bash
npm install vuetify axios chart.js pinia vue-router
```

5. **Install Vuetify dependencies:**
```bash
npm install @mdi/font
```

6. **Return to root directory:**
```bash
cd ..
```

## Backend Setup (/server)

### Option 1: Using Poetry (Recommended)

**⚠️ Important for macOS users:** Before installing Poetry, ensure you're using Python 3.10 or higher (required by pydantic-settings). If you encounter crashes or errors related to Python 3.6 or older, see the troubleshooting section below. Consider using Homebrew Python for a clean setup.

1. **Install Poetry (if not already installed):**

   **Method A: Using pipx (Recommended for macOS, avoids symlink issues):**
   ```bash
   # Install pipx if not already installed
   pip3 install --user pipx
   
   # Find where pipx was installed (check Python version)
   python3 --version  # e.g., Python 3.14.x
   # For Python 3.14, pipx is typically at: ~/Library/Python/3.14/bin/pipx
   # Or if installed via Python.org installer: /Library/Frameworks/Python.framework/Versions/3.14/bin/pipx
   # Find the exact location:
   python3 -m site --user-base
   # This will show something like: /Users/username/Library/Python/3.14
   # So pipx will be at: /Users/username/Library/Python/3.14/bin/pipx
   
   # Add pipx to PATH (replace 3.14 with your Python version)
   # For zsh (default on macOS):
   echo 'export PATH="$HOME/Library/Python/3.14/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   # OR for bash:
   # echo 'export PATH="$HOME/Library/Python/3.14/bin:$PATH"' >> ~/.bash_profile
   # source ~/.bash_profile
   
   # Install Poetry via pipx
   pipx install poetry
   
   # If pipx still not found, use full path (replace 3.14 with your Python version):
   # ~/Library/Python/3.14/bin/pipx install poetry
   # OR if using Python.org installer:
   # /Library/Frameworks/Python.framework/Versions/3.14/bin/pipx install poetry
   ```

   **Method B: Using pip (Alternative):**
   ```bash
   pip3 install --user poetry
   # Add Poetry to PATH (add to ~/.zshrc or ~/.bash_profile)
   export PATH="/Library/Frameworks/Python.framework/Versions/3.14/bin:$PATH"
   ```

   **Method C: Official installer (if Methods A/B don't work):**
   ```bash
   # First install Python via Homebrew (supports symlinks)
   brew install python@3.14
   
   # Then use Homebrew Python for Poetry installation
   curl -sSL https://install.python-poetry.org | /opt/homebrew/bin/python3.14 -
   ```

   **Note for macOS users:** If you encounter "cannot create venvs without using symlinks" error, use Method A (pipx) or Method B (pip) instead of the official installer. After installation, configure Poetry to use symlinks:
   ```bash
   poetry config virtualenvs.options.symlinks true
   ```

2. **Create server directory and initialize Poetry:**
```bash
mkdir -p server
cd server

# Check if pyproject.toml already exists
if [ -f "pyproject.toml" ]; then
  echo "pyproject.toml already exists. Skipping poetry init."
  echo "If you need to update it, edit pyproject.toml directly or remove it first."
else
  poetry init --no-interaction --name medipredict-backend --description "MediPredict Lite Backend API" --author "Your Name <your.email@example.com>" --python ">=3.10,<4.0"
  # Tell Poetry which Python executable to use for this project
  poetry env use $(which python3)
fi
```

   **Note:** The Python version must be >=3.10 because `pydantic-settings` requires Python 3.10 or higher.
   
   **Important:** After `poetry init`, run `poetry env use $(which python3)` to explicitly tell Poetry which Python executable to use. This is especially important when you have multiple Python installations on your system.
   
   **If pyproject.toml already exists:** You can either:
   - Edit the existing `pyproject.toml` file to update the Python version requirement (see troubleshooting section)
   - Remove it and reinitialize: `rm pyproject.toml poetry.lock 2>/dev/null && poetry init ...`
   - Skip initialization and proceed directly to adding dependencies

3. **Add backend dependencies:**
```bash
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

4. **Install dependencies:**
```bash
# Install dependencies without installing the project itself (recommended for backend projects)
poetry install --no-root

# OR if you want to install the project as a package, create a README.md file first:
# touch README.md
# poetry install
```

   **Note:** Using `--no-root` is recommended for backend projects that don't need to be packaged. If you prefer to disable package mode entirely, add `package-mode = false` to the `[tool.poetry]` section in `pyproject.toml`.

5. **Return to root directory:**
```bash
cd ..
```

### Option 2: Using pip and venv

1. **Create server directory and virtual environment:**
```bash
mkdir -p server
cd server
# Use Python 3.10 or higher (required by pydantic-settings)
python3.14 -m venv venv  # or python3.10, python3.11, python3.12, python3.13, etc.
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Upgrade pip:**
```bash
pip install --upgrade pip
```

3. **Install backend dependencies:**
```bash
pip install fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

4. **Create requirements.txt:**
```bash
pip freeze > requirements.txt
```

5. **Return to root directory:**
```bash
cd ..
```

## Quick Start (All-in-One)

Run these commands in sequence from the project root:

```bash
# 1. Start Docker services
docker compose up -d

# 2. Setup Frontend
npm create vite@latest client -- --template vue-ts
cd client
npm install
npm install vuetify axios chart.js pinia vue-router @mdi/font
cd ..

# 3. Setup Backend (Poetry)
# Install Poetry via pipx (recommended for macOS, avoids symlink issues)
pip3 install --user pipx
# Find where pipx was installed (replace 3.14 with your Python version)
# python3 -m site --user-base  # Shows base directory
# Add pipx to PATH (replace 3.14 with your Python version):
export PATH="$HOME/Library/Python/3.14/bin:$PATH"
# OR if using Python.org installer:
# export PATH="/Library/Frameworks/Python.framework/Versions/3.14/bin:$PATH"
# OR use full path: ~/Library/Python/3.14/bin/pipx install poetry
pipx install poetry
# Configure Poetry to use symlinks (if needed on macOS)
poetry config virtualenvs.options.symlinks true
mkdir -p server
cd server
# Note: Python must be >=3.10 (required by pydantic-settings)
# If pyproject.toml already exists, skip init and go directly to adding dependencies
if [ ! -f "pyproject.toml" ]; then
  poetry init --no-interaction --name medipredict-backend --description "MediPredict Lite Backend API" --author "Your Name <your.email@example.com>" --python ">=3.10,<4.0"
  # Tell Poetry which Python executable to use for this project
  poetry env use $(which python3)
fi
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
poetry install --no-root
cd ..
```

## Access Points

- **MySQL**: `localhost:3306`
- **Redis**: `localhost:6379`
- **Adminer**: `http://localhost:8080`
  - System: MySQL
  - Server: mysql
  - Username: mediuser (or root)
  - Password: medipassword (or rootpassword)
  - Database: medipredict

## Troubleshooting

### Docker Config.json Typo

If you encounter issues with Docker authentication, check your `~/.docker/config.json` file. Some auto-generated configurations may have a typo where `credsStore` should be `credStore` (without the 's'). 

To fix:
```bash
# Edit the config file
nano ~/.docker/config.json

# Change "credsStore" to "credStore"
```

The correct format should be:
```json
{
  "credStore": "osxkeychain"
}
```

Not:
```json
{
  "credsStore": "osxkeychain"  // ❌ Wrong - has extra 's'
}
```

### Poetry: pyproject.toml Already Exists

If you get the error "A pyproject.toml file with a project and/or a poetry section already exists" when running `poetry init`, this means the file was already created.

**Option 1: Edit existing pyproject.toml (Recommended)**
```bash
cd server
# Edit the file directly
nano pyproject.toml  # or use your preferred editor

# Ensure the [tool.poetry.dependencies] section has:
# python = ">=3.10,<4.0"
# And the [tool.poetry] section has:
# requires-python = ">=3.10,<4.0"

# Then proceed to add dependencies
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

**Option 2: Remove and reinitialize (if you want to start fresh)**
```bash
cd server
# Backup existing file if needed
cp pyproject.toml pyproject.toml.backup 2>/dev/null

# Remove existing files
rm pyproject.toml poetry.lock 2>/dev/null

# Reinitialize
poetry init --no-interaction --name medipredict-backend --description "MediPredict Lite Backend API" --author "Your Name <your.email@example.com>" --python ">=3.10,<4.0"

# Tell Poetry which Python executable to use for this project
poetry env use $(which python3)

# Add dependencies
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

**Option 3: Skip initialization and add dependencies directly**
```bash
cd server
# If pyproject.toml exists, you can add dependencies directly
# But first, ensure Poetry knows which Python to use
poetry env use $(which python3)

# Then add dependencies
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

### Poetry Dependency Resolution: Python Version Requirement

If you encounter an error about `pydantic-settings` requiring Python >=3.10, this means your project's Python version constraint is too low.

**Error message example:**
```
pydantic-settings requires Python >=3.10, so it will not be installable for Python >=3.9,<3.10
```

**Solution: Update Python version requirement in pyproject.toml**
```bash
# Edit pyproject.toml in your server directory
cd server
nano pyproject.toml  # or use your preferred editor

# Change the requires-python line from:
# requires-python = "^3.9"  or  ">=3.9,<4.0"
# To:
# requires-python = ">=3.10,<4.0"

# Then try installing dependencies again
poetry install --no-root
```

**Or reinitialize Poetry with correct Python version:**
```bash
cd server
# Remove existing pyproject.toml if you want to start fresh
rm pyproject.toml poetry.lock 2>/dev/null

# Reinitialize with correct Python version
poetry init --no-interaction --name medipredict-backend --description "MediPredict Lite Backend API" --author "Your Name <your.email@example.com>" --python ">=3.10,<4.0"

# Tell Poetry which Python executable to use for this project
poetry env use $(which python3)

# Add dependencies
poetry add fastapi uvicorn[standard] sqlalchemy aiomysql redis loguru pydantic-settings
```

**Important:** Ensure you're using Python 3.10 or higher:
```bash
python3 --version  # Should show 3.10.x, 3.11.x, 3.12.x, 3.13.x, 3.14.x, etc.
```

### Poetry: Setting Python Executable

After running `poetry init`, it's recommended to explicitly tell Poetry which Python executable to use, especially when you have multiple Python installations on your system.

**Command:**
```bash
poetry env use $(which python3)
```

This command:
- Tells Poetry exactly which Python executable to use for this project
- Prevents Poetry from using the wrong Python version
- Ensures consistency across different environments

**When to use:**
- Right after `poetry init`
- If Poetry is using the wrong Python version
- When switching between different Python installations

**Alternative: Specify Python version directly**
```bash
# Use a specific Python version
poetry env use python3.14
# OR
poetry env use /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
```

### Poetry: README.md Path Error

If you encounter the error "Readme path `/path/to/server/README.md` does not exist" when running `poetry install`, this means Poetry is trying to install your project as a package, but the required README.md file is missing.

**Error message example:**
```
The current project could not be installed: Readme path `/Users/username/project/server/README.md` does not exist.
If you do not want to install the current project use --no-root.
```

**Solution 1: Use --no-root flag (Recommended for backend projects)**
```bash
# Install dependencies without installing the project itself
poetry install --no-root
```

**Solution 2: Disable package mode in pyproject.toml (Permanent fix)**
```bash
cd server
nano pyproject.toml  # or use your preferred editor

# Add this line to the [tool.poetry] section:
# package-mode = false

# Then install dependencies normally
poetry install
```

**Solution 3: Create a minimal README.md file**
```bash
cd server
touch README.md
# Or create a basic README
echo "# MediPredict Backend" > README.md

# Then install dependencies
poetry install
```

**Note:** For backend projects that don't need to be packaged, Solution 1 (`--no-root`) or Solution 2 (`package-mode = false`) are recommended. Solution 3 is only needed if you actually want to package and install your project.

### Poetry Installation: Python Venv Symlink Error (macOS)

If you encounter the error "This build of python cannot create venvs without using symlinks" **during Poetry installation** on macOS, this is because the official Poetry installer tries to create a virtual environment, but your Python installation doesn't support creating venvs without symlinks.

**Solution 1: Install Poetry via pipx (Recommended - bypasses the issue)**
```bash
# Install pipx if not already installed
pip3 install --user pipx

# Find where pipx was installed
python3 -m site --user-base
# This shows the base directory, e.g., /Users/username/Library/Python/3.14
# pipx will be at: [base]/bin/pipx

# Add pipx to PATH (replace 3.14 with your Python version)
# For zsh (default on macOS):
echo 'export PATH="$HOME/Library/Python/3.14/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
# OR for bash:
# echo 'export PATH="$HOME/Library/Python/3.14/bin:$PATH"' >> ~/.bash_profile
# source ~/.bash_profile

# Install Poetry via pipx
pipx install poetry

# If pipx still not found, use full path (replace 3.14 with your Python version):
# ~/Library/Python/3.14/bin/pipx install poetry
# OR if using Python.org installer:
# /Library/Frameworks/Python.framework/Versions/3.14/bin/pipx install poetry
```

**Solution 2: Install Poetry via pip (Alternative)**
```bash
# Install Poetry directly via pip
pip3 install --user poetry

# Add Poetry to PATH (add to ~/.zshrc or ~/.bash_profile)
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
```

**Solution 3: Install Python via Homebrew first, then use official installer**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.14 via Homebrew (supports symlinks)
brew install python@3.14

# Use Homebrew Python for Poetry installation
curl -sSL https://install.python-poetry.org | /opt/homebrew/bin/python3.14 -
```

After installing Poetry using any method, configure it to use symlinks (if needed):
```bash
poetry config virtualenvs.options.symlinks true
```

Verify Poetry works:
```bash
poetry --version
```

### pipx "command not found" Error

If you get "command not found" after installing pipx, this means pipx is not in your PATH.

**Step 1: Find where pipx was installed**
```bash
# Check your Python version
python3 --version

# Find the user base directory
python3 -m site --user-base
# Example output: /Users/username/Library/Python/3.14
# pipx will be at: [output]/bin/pipx
```

**Quick fix (temporary):**
```bash
# Add pipx to PATH manually (replace 3.14 with your Python version)
export PATH="$HOME/Library/Python/3.14/bin:$PATH"
# OR if using Python.org installer:
# export PATH="/Library/Frameworks/Python.framework/Versions/3.14/bin:$PATH"

# Then install Poetry
pipx install poetry
```

**Permanent fix:**
```bash
# For zsh (default on macOS) - replace 3.14 with your Python version:
echo 'export PATH="$HOME/Library/Python/3.14/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# OR for bash:
# echo 'export PATH="$HOME/Library/Python/3.14/bin:$PATH"' >> ~/.bash_profile
# source ~/.bash_profile

# Then install Poetry
pipx install poetry
```

**Alternative: Use full path directly**
```bash
# Use full path to pipx (replace 3.14 with your Python version)
~/Library/Python/3.14/bin/pipx install poetry
# OR if using Python.org installer:
# /Library/Frameworks/Python.framework/Versions/3.14/bin/pipx install poetry

# Or use the output from python3 -m site --user-base:
# [output from site command]/bin/pipx install poetry
```

### Python 3.6 CoreFoundation Crash (DYLD Library Missing)

If you encounter a crash with "Library not loaded: CoreFoundation.framework" referencing Python 3.6, this means an old Python 3.6 installation is being invoked, which is incompatible with modern macOS versions.

**Diagnosis:**
```bash
# Check which Python is being used
which python3
python3 --version

# Check for old Python installations
ls -la /Library/Frameworks/Python.framework/Versions/
```

**Solution 1: Remove old Python 3.6 installation (Recommended)**
```bash
# Remove the old Python 3.6 framework
sudo rm -rf /Library/Frameworks/Python.framework/Versions/3.6

# Also remove from Applications if present
sudo rm -rf /Applications/Python\ 3.6/
```

**Solution 2: Use Homebrew Python (Recommended for clean setup)**
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.14 via Homebrew
brew install python@3.14

# Ensure Homebrew Python is in PATH (add to ~/.zshrc)
echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Verify correct Python is being used
which python3
python3 --version  # Should show 3.14.x

# Now install pipx and Poetry using Homebrew Python
pip3 install --user pipx
export PATH="$HOME/Library/Python/3.14/bin:$PATH"
pipx install poetry
```

**Solution 3: Use pyenv for Python version management**
```bash
# Install pyenv via Homebrew
brew install pyenv

# Add to ~/.zshrc
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
source ~/.zshrc

# Install Python 3.14 via pyenv
pyenv install 3.14.0
pyenv global 3.14.0

# Verify
python3 --version  # Should show 3.14.0

# Now install pipx and Poetry
pip3 install --user pipx
export PATH="$HOME/Library/Python/3.14/bin:$PATH"
pipx install poetry
```

**Important:** After fixing the Python installation, you may need to reinstall pipx and Poetry using the correct Python version.

