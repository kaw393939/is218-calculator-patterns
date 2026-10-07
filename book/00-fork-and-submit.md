# Start here: fork, build, and submit

A fork is your own copy of this repository on GitHub. A clone is a copy on your computer. You will change your fork and submit its URL. Forking is the recommended starting point. If you continue in an existing repository instead, follow the same requirements and include the test workflow.

1. Sign in to GitHub and open [the instructor repository](https://github.com/kaw393939/is218-calculator-patterns).
2. Click **Fork**, choose your own account, and click **Create fork**. You cannot fork a repository into the same account that owns it; students should use their own accounts. Keep the repository public, or give the instructor access if it is private.
3. Open **your fork**, click **Code**, and copy its HTTPS clone URL.
4. In a terminal, run `git clone` with that copied URL. Then enter the new folder. For example, replace `YOUR-USERNAME` with your real GitHub username:

```bash
git clone https://github.com/YOUR-USERNAME/is218-calculator-patterns.git
cd is218-calculator-patterns
```

5. Follow the chapters. Keep the book and write your own explanation in `STUDENT_README.md`. The provided addition and calculation code is only a starting point.
6. Commit and push your work as you finish each part:

```bash
git add calculator tests STUDENT_README.md requirements.txt .github/workflows/tests.yml
git commit -m "Implement calculator commands and tests"
git push origin main
```

Use a commit message that describes your actual change. Include any new source files you create.

7. Open **Actions** in your fork. If GitHub says workflows are disabled for the fork, click **I understand my workflows, go ahead and enable them** (wording may vary). Push a commit, or use **Run workflow** on Calculator tests. Fix failures until the latest run passes with 100% coverage.
8. Add that successful Actions run URL to `STUDENT_README.md`.
9. Submit **your completed repository URL** in your Canvas assignment. Do not open a pull request to the instructor repository to submit.

The starter's tests can pass before you finish. That only proves the starter works. Full completion also requires all operations, commands, history, a working CLI, meaningful tests, and your explanations.

Check Canvas for your assignment deadline. If a fork is private, verify that the instructor can open it before submitting.

[Back to the contents](../README.md) · [Next: calculator requirements](01-what-your-calculator-must-do.md)
