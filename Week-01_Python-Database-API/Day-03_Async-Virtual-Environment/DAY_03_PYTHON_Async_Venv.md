# Day 3 — Async Programming & Virtual Environment

## Overview

In Day 3, I learned Python Virtual Environment, package management,
Async/Await programming, asynchronous HTTP requests, and Git/GitHub.

---

## Topics Covered

- Virtual Environment
- `venv`
- `pip`
- `requirements.txt`
- `async` / `await`
- `asyncio`
- `asyncio.run()`
- `asyncio.sleep()`
- `asyncio.gather()`
- `aiohttp`
- `ClientSession`
- `async with`
- HTTP GET Request
- Git & GitHub
- `.gitignore`

---

## Virtual Environment Commands

### Create Environment

```powershell
python -m venv .venv
```

### Create Without pip

```powershell
python -m venv .venv --without-pip
```

### Create With pip

```powershell
python -m venv .venv
```

### Activate

```powershell
.\.venv\Scripts\Activate.ps1
```

### Deactivate

```powershell
deactivate
```

### Check Python

```powershell
python --version
```

```powershell
python -c "import sys; print(sys.executable)"
```

---

## pip Commands

### Install Package

```powershell
pip install aiohttp
```

### List Packages

```powershell
pip list
```

### Package Information

```powershell
pip show aiohttp
```

### Save Dependencies

```powershell
pip freeze > requirements.txt
```

### Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## Async / Await

### Basic Example

```python
   import asyncio

async def Task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def Task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def Task3():
    print("Task 3 started")
    await asyncio.sleep(3)
    print("Task 3 completed")


```

### Multiple Tasks

```python
async def main():
    await asyncio.gather(Task1(), Task2(), Task3())

# Run the main function
asyncio.run(main())

```

---

## Async HTTP Request

Used `aiohttp` to make an asynchronous API request.

```python
import asyncio
import aiohttp


async def fetch(session, url):

    async with session.get(url) as response:

        return await response.text()


async def main():

    url = "https://jsonplaceholder.typicode.com/todos"

    async with aiohttp.ClientSession() as session:

        result = await fetch(session, url)

        print(result)


asyncio.run(main())
```

### Main Concepts

```text
aiohttp
    ↓
ClientSession
    ↓
session.get()
    ↓
HTTP GET Request
    ↓
response
    ↓
response.text()
```

---

## PowerShell Commands

```powershell
pwd
```

Check current directory.

```powershell
dir
```

List files and folders.

```powershell
cd "Folder Name"
```

Enter a folder.

```powershell
cd ..
```

Go to the parent folder.

```powershell
Get-Content .gitignore
```

Read a file.

```powershell
code .gitignore
```

Open a file in VS Code.

---

## Git Commands

```powershell
git status
```

Check repository status.

```powershell
git add .
```

Stage changes.

```powershell
git commit -m "Add Day 3 practice"
```

Commit changes.

```powershell
git push
```

Push changes to GitHub.

---

## .gitignore

The following files were ignored:

```gitignore
**/.venv/
__pycache__/
*.pyc
.env
```

`.venv` is not uploaded to GitHub because it is a local
Virtual Environment.

Instead, dependencies are stored in:

```text
requirements.txt
```

---

## Project Structure

```text
Day-03_Async-Virtual-Environment/
│
├── Async-Await-Practice/
├── Async-HTTP-Request/
├── Virtual_ Environment/
│   └── .venv/
├── requirements.txt
├── DAY_03_PYTHON_Async_Venv.md
└── .gitignore
```

---

## What I Learned

- How to create and manage a Virtual Environment
- How to install Python packages using `pip`
- How to use `requirements.txt`
- Basics of Async/Await
- How `asyncio` works
- How to make asynchronous HTTP requests
- How `aiohttp` and `ClientSession` work
- How to use `.gitignore`
- Basic Git and GitHub workflow

---

## Status

**Day 3 — Completed ✅**
