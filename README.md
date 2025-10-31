# README


## Prerequsities

* [Python](https://www.python.org/) (3.10+) instaled

  <details>
  <summary>Windows</summary>

  * Install with [Python Releases for Windows](https://www.python.org/downloads/windows/) or [Python Install Manager](https://apps.microsoft.com/detail/9nq7512cxl7t)
  * Open [Cmd.exe](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) or [Windows Terminal](https://apps.microsoft.com/detail/9n0dx20hk701)
  * Make sure the command "python" gives you the [Python REPL environment](https://realpython.com/python-repl/). If not, try to [add Python to PATH](https://realpython.com/add-python-to-path/).
  </details>

  <details>
  <summary>macOS</summary>

  * [Open Terminal](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac)

  * Install [HomeBrew](https://docs.brew.sh/Installation) with the latest instructions, such as:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

  * Use HomeBrew to install the latest Python 3 version, for example:
    ```bash
    brew install python@3.14
    ```
  </details>

  <details>
  <summary>Linux</summary>
  Use your distributions package manager (e.g. apt / dnf)
  </details>

* [uv](https://docs.astral.sh/uv/) (0.8.9+) installed

  <details>
  <summary>Windows</summary>

  ```posh
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```
  </details>

  <details>
  <summary>macOS / Linux</summary>

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
  </details>

* Make sure both "python" and "uv" set to the system path that you can run "python" in your command environment.


## Setup and Run `dummy_mcp_server`

1. Open terminal or other Cmd.exe

2. Initialize virtual environment and install dependencies
   ```
   uv sync
   ```

3. Activate the enviornment

   In Linux or macOS:
   ```
   source .venv/bin/activate.sh
   ```

   Or in Windows (Cmd.exe):
   ```
   .venv\Scripts\activate.bat
   ```

   Check venv's official documentation here:
   https://docs.python.org/3/library/venv.html#how-venvs-work

4. Run the MCP server
   ```
   python -m dummy_mcp_server
   ```

## Javis setup

### System Prompt

```
You are a helpful AI assistant. Your primary goal is to assist users with their questions and tasks to the best of your abilities and the best use of tools.

When responding:
- Consider if you know the answer directly. If you know it, just answer.
- If you do not know the answer, always then check what tools are at your disposal.
- Consider any possible tool use, or chain of tools, that may help answer the question.
- If you may use tool to answer, use tool.
- Be concise, clear, and helpful
- Admit when you’re unsure rather than making things up

If tools are available to you:
- Only use tools when they add real value to your response
- Use tools when the user explicitly asks (e.g., "search for...", "calculate...", "run this code")
- Use tools for information you don’t know or that needs verification
- Never use tools just because they’re available

When using tools:
- Use one tool at a time and wait for results
- Use actual values as arguments, not variable names
- Learn from each result before deciding next steps
- Avoid repeating the same tool call with identical parameters

Remember: Most questions can be answered without tools. Think first whether you need them.
```
