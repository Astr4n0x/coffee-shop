# Contributing to Coffee Shop CLI

Thanks for your interest in improving Coffee Shop CLI! This document covers how to set up the project, the coding style we follow, and how to submit changes.

## Getting Started

1. Fork the repository and clone your fork:

   ```bash
   git clone https://github.com/<your-username>/coffee-shop-cli.git
   cd coffee-shop-cli
   ```

2. (Optional but recommended) Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. The project has no runtime dependencies. If you add test tooling, install it:

   ```bash
   pip install pytest
   ```

## Making Changes

1. Create a feature branch off `main`:

   ```bash
   git checkout -b feature/short-description
   ```

2. Make your changes, keeping the existing style in mind (see below).

3. Run the test suite before opening a PR:

   ```bash
   pytest
   ```

4. Commit with a clear, descriptive message:

   ```bash
   git commit -m "Add ability to remove items from cart"
   ```

5. Push and open a Pull Request against `main`. Fill out the PR template and describe:
   - What the change does
   - Why it's needed
   - How you tested it

## Coding Style

- Follow [PEP 8](https://peps.python.org/pep-0008/) for formatting.
- Use descriptive variable and method names (the codebase favors clarity over brevity).
- Keep classes focused on a single responsibility — see `Coffee`, `Order`, and `Colors` as examples.
- Prefer f-strings for string formatting, consistent with the existing code.
- Add or update docstrings/comments for any non-obvious logic.
- If you add a new menu-driven feature, keep the numbered-option pattern used in `main()` consistent (update valid input ranges and printed option numbers together).

## Tests

- New features and bug fixes should include corresponding tests in `tests/`.
- Tests use `pytest`. Aim to test behavior (e.g., `Order.total()`, `add_order`, `checkout` flow) rather than implementation details.
- Run the full suite locally with `pytest` before submitting.

## Reporting Bugs / Requesting Features

Please use the issue templates under **Issues → New Issue**. Include:
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Python version and OS, if relevant

## Code of Conduct

By participating in this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

Open a [Discussion](../../discussions) or an issue — happy to help you get oriented.
