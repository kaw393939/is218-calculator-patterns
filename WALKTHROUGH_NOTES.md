# Student walkthrough notes

This is a simulated first-year student's attempt, not a real student's submission or a study of actual students. I started at the published Canvas assignment, read its instructions and attached 100-point rubric, followed its GitHub book link, then made a fresh clone and the `codex/student-walkthrough` branch. I have the course's earlier calculator experience but am treating these patterns as new. No student account, fork, grade, or Canvas submission was created. The requested branch stands in for the student's fork.

## Before writing code

The rubric gives 30 points to CLI behavior, 30 to OOP/patterns, 20 to tests and coverage, 10 to Actions, and 10 to explanations/submission. I made a checklist from those five categories before coding. A passing starter test run is not full completion.

## Findings and decisions, recorded before fixes

| Finding | Evidence or first-year question | Planned resolution |
| --- | --- | --- |
| Course-specific dates in a reusable book | README and the first chapter contained section tables and Canvas links. | Removed them on main; Canvas keeps the deadline. |
| Two places for my explanation | Canvas says STUDENT_README.md; the setup tree, coverage chapter, and rubric say README. | Name STUDENT_README.md consistently and tell me to keep the instructor README. |
| Forking sounds compulsory in the book | Canvas permits an existing repository, but the book only accepts a completed fork. | Recommend a fork; explicitly allow an existing repository with the same requirements. |
| Starter cannot run as a CLI yet | Running `python3 -m calculator` in the fresh clone exits with “No module named calculator.__main__”. | Explain that this is expected until the CLI chapter; provide the thin entry-point example. |
| Strategy snippet is not standalone | It refers to Operations, ArithmeticCalculation, command_name, a, and b without imports or defining the input values. | Supply imports and a runnable one-operation example before the input-loop fragment. |
| CLI chapter makes a large jump | It says “put the loop in cli.py” but does not show how exit/history, wrong input, conversion, or EOF fit together. | Add a plain numbered loop plan and a main() skeleton; leave the core implementation to students. |
| History contents are unspecified | Do I save the numbers, a Calculation, or a string? | Show one possible string format, state that equivalent readable formats are accepted, and explain shared history and its copy. |
| Testing example has a weak assertion | `assert "8" in output` could pass when the program prints 18 or an unrelated message. | Compare a result line to 8 or 8.0; use a real EOFError stub for EOF. |
| Manual Actions instructions disagree with the example | The starter workflow has workflow_dispatch, but the book's replacement YAML omits it. | Match the book to the actual three-trigger workflow and say the file is already present. |
| Some setup assumptions are hidden | Commands assume a usable Python interpreter, Git, the cloned project directory, and activated environment. | Add interpreter/version checks, Windows alternatives, and directory guidance. |
| A green check measures only present code | The initial 100% report covers addition/calculation only. | Preserve the existing warning and add a final rubric checklist covering every feature. |

## Implementation log

- Setup: cloned the public starter from the Canvas link. Created a fresh virtual environment and installed requirements, following the book.
- Operations: keep static methods for arithmetic; division raises ValueError for a zero divisor.
- Calculation: keep the provided ABC, inherited class factory, and instance execute method. Test a different concrete implementation to check the abstraction's promise.
- Commands: keep printing out of command classes. Record history only after successful execution. Return a new list for history viewing.
- CLI: select a function from the operation dictionary, build the calculation, run a command, print the result. Validate the command and number count before indexing; recover from expected input errors.
- Tests: 54 passed with 100% line coverage of all 89 measured application statements. Core behavior has no coverage exclusions.
- Documentation: completed STUDENT_README.md with each method, pattern, OOP property, SOLID principle, setup/run/test command, and rubric evidence.
- Instruction fixes: every planned book clarification above is implemented; main will receive only those book edits, not the completed calculator.
- Actions: [actual branch run](https://github.com/kaw393939/is218-calculator-patterns/actions/runs/37670378046) passed on Python 3.12.
- Real student repository access and Canvas submission remain outside this instructor simulation.

## Simulation limits

The instructor account was used only to read Canvas. Actual GitHub account creation, student permissions, forking, and Canvas upload were not reproduced. I do not infer students' completion time or experience from my own run. The implementation branch is an instructor audit example; the student-facing main branch remains a starter.

## Resolutions and final review

Every instructional issue in the findings table is resolved in the book edits. The README and fork/submission chapters defer dates to Canvas and allow an existing repository. Setup names STUDENT_README.md and documents interpreter checks and direct environment executables. The strategy chapter adds imports and a runnable addition example. Commands explain shared history and an accepted string example. The CLI chapter includes the loop plan, scaffold, entry point, and EOF keys. Tests now check result lines and explain EOFError versus StopIteration. Actions documentation matches the committed workflow. The rubric has a final feature checklist. Next-chapter links sit below all lesson content.

An actual CLI subprocess produced correct answers, recovered from division by zero, showed successful history in order without the failed division, and exited successfully. The full 54-test suite passes with 100% line coverage. GitHub verified the same implementation on Python 3.12.

### Rubric evidence

| Category | Audit evidence |
| --- | --- |
| CLI: 30 | All arithmetic commands, negative/decimal operands, invalid input recovery, ordered history, empty history, exit, and EOF tested. |
| OOP/patterns: 30 | Static methods, ABC, inherited class factory, instance execute, functional strategies, two command classes, and alternative concrete calculation tested. |
| Tests: 20 | 54 passing tests; 89 measured statements; 100% package coverage; only abstract placeholder and thin startup exclusions. |
| Actions: 10 | Actual Python 3.12 workflow passed; 100% threshold retained. |
| Explanations/submission: 10 | STUDENT_README.md and comments cover the requested explanations. Branch is pushed and accessible. Actual student fork/access and Canvas URL submission were deliberately not fabricated. |

The technical work is ready against the rubric. This is not a posted grade. There are no unresolved code or book blockers found in this walkthrough; actual student-account/fork/submission checks remain the simulation limit.

### Overall assignment assessment

The assignment is achievable as a guided follow-up to an earlier calculator. The initial CLI chapter assumed too much: splitting commands, handling two kinds of errors, history, and EOF are several new steps at once. The expanded plan and scaffold make that step less abrupt. Keeping history in memory and strategies as static functions keeps the scope manageable. 100% line coverage is attainable without excluding working behavior, but the feature checklist is still needed because coverage alone cannot detect a missing feature.
