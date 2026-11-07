# Curling League Manager

A Python desktop application prototype for managing curling leagues, teams, team members, and competitions. The project combines a small object-oriented domain model with a PyQt6 interface and supporting tests.

## Project overview

- **League** — maintains collections of teams and competitions.
- **Team** — represents a team and its members.
- **Team member** — stores an individual participant's information.
- **Competition** — represents a competition involving teams.
- **League database** — contains CSV import/export and persistence-related functionality.
- **PyQt6 interface** — provides windows and dialogs for interacting with league data.

This repository is a coursework project and should be considered a work in progress. Some interface and data-management paths may require additional implementation and testing before they are suitable for production use.

## Technology

- Python 3
- PyQt6
- Qt Designer UI files
- Python unittest

## Repository structure

```text
.
├── Curling_League_Manager/   # Domain model and data-management code
├── tests/                    # Unit tests
├── ui/                       # PyQt6 windows and Qt Designer files
└── README.md
```

## Getting started

1. Install Python 3.
2. Create and activate a virtual environment.
3. Install the desktop UI dependency:

   ```bash
   python -m pip install PyQt6
   ```

4. Review the entry-point and import paths in ui/main_window.py before launching. The current project layout and relative Qt Designer file paths may require running the interface from the ui directory or adjusting the paths.

## Testing

Tests are located in tests/ and use Python's built-in unittest framework. The test suite and import paths should be verified in a clean environment before relying on a passing test run.

## Development notes

- Keep generated Python bytecode and local virtual environments out of version control.
- Do not commit local IDE settings, personal workspace state, or machine-specific files.
- Add screenshots and a verified run-through once the interface is stable.

## Project status

This is an educational software project demonstrating object-oriented Python, desktop UI development, and test organization. It is not presented as a production-ready league management system.
