# Employee-Management-System-Python

Idea:
Model different types of employees in a company.

- Base class: Employee (name, salary, work method)
- Subclasses: Manager, Developer, Designer — each with specific duties.

---

## Why inheritance here:

All employees share a salary and a name, but each has unique work behavior or extra attributes.

---

## File structure:

```python

employee_system/
│
├── main.py               # Runs the program
├── employee.py           # Base Employee class
└── roles/
    ├── manager.py        # Manager subclass
    ├── developer.py      # Developer subclass
    └── designer.py       # Designer subclass

```

---

## License

MIT License

Copyright (c) 2025 Ms-Njuguna