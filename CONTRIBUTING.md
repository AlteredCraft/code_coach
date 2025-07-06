# Contributing to Learn Python with AI

## 🧪 This is an Experiment!

This project is a **work in progress** exploring AI-assisted learning. We're testing new approaches to teaching programming through guided discovery. **All ideas are welcome** - there are no bad suggestions when we're learning together!

## 📁 How to Contribute Content

### Contributing a Module

A module is a collection of related lessons (e.g., "Foundations", "Data Structures", "Web Development").

**Required structure:**
```
modules/
└── XX-module-name/
    ├── CLAUDE.md    # Module-level AI coaching instructions
    └── lessons/     # Directory containing all lessons
```

**Module CLAUDE.md should include:**
- General principles for teaching this module's concepts
- Progressive difficulty guidelines across lessons
- Common misconceptions to address
- Module-specific analogies and explanations that work well

### Contributing a Lesson

Each lesson focuses on a specific concept with hands-on exercises.

**Required structure:**
```
lessons/
└── XX-lesson-name/
    ├── README.md              # Lesson content and exercises
    ├── CLAUDE.md              # Lesson-specific AI coaching
    ├── test_exercises.py      # Simple tests for validation
    └── solution/              # Skeleton files for learners
        ├── exercise1_descriptive_name.py
        ├── exercise2_descriptive_name.py
        ├── exercise3_descriptive_name.py
        └── mini_project_descriptive_name.py
```

**README.md must include:**
- Learning objectives (2-4 bullet points)
- 3-4 exercises of increasing difficulty
- Clear instructions for each exercise
- A mini-project that combines concepts
- Checklist for completion

**CLAUDE.md must include:**
- Solution file workflow instructions
- Exercise-specific guidance (guiding questions, common mistakes, success responses)
- Emotional support notes for challenging parts
- Positive session-ending messages

**Solution files must have:**
- Docstring with exercise description
- Example usage showing expected output
- Helpful step-by-step comments
- NO actual solution code (learners fill this in)

### Contributing an Exercise

Exercises should follow this progression:
1. **Exercise 1**: Simple concept introduction (confidence builder)
2. **Exercise 2**: Add one new concept or variation
3. **Exercise 3**: Debug or modify existing code
4. **Mini-Project**: Combine all concepts in a practical application

**Each exercise needs:**
- Clear, single-objective goal
- Skeleton file in `solution/` directory
- Example usage in the docstring
- Entry in lesson's CLAUDE.md with coaching guidance
- Test case in `test_exercises.py`

## 🛠️ Setup and Testing

1. **Fork and clone the repository**
2. **Install dependencies:**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh  # Install uv if needed
   uv sync
   ```
3. **Test your contribution:**
   ```bash
   # Run skeleton files (should run without errors even if empty)
   uv run python modules/your-module/lessons/your-lesson/solution/*.py
   
   # Check code style
   uv run ruff check modules/your-module/lessons/your-lesson/solution/
   
   # Test the exercises
   uv run python modules/your-module/lessons/your-lesson/test_exercises.py
   ```

## 📝 Submission Checklist

Before submitting a PR:

- [ ] All skeleton files run without errors
- [ ] Example usage in docstrings matches actual behavior
- [ ] CLAUDE.md provides helpful coaching without giving away answers
- [ ] Exercises progress logically in difficulty
- [ ] Code passes `ruff` linting
- [ ] You've completed all exercises yourself as a beginner would
- [ ] File naming follows the pattern: `exerciseN_descriptive_name.py`

## 💡 Design Principles

When creating content, remember:

- **Guided discovery** > Direct instruction
- **Questions** > Answers
- **Small wins** > Perfect code
- **Understanding** > Memorization
- **Encouragement** > Criticism

## 🤝 Code of Conduct

- Be kind and respectful
- Remember we're all learning
- Constructivly criticize ideas, not people
- Welcome newcomers warmly
- Share both successes AND failures

## 📮 Getting Help

- Open an issue with the "question" label
- Check existing lessons for examples
- Read through CLAUDE.md files for coaching patterns
- Join discussions about pedagogical approaches

---

*Thank you for helping us reimagine programming education through AI-assisted learning!*