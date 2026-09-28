# lab04-Failsafe-Protocol
Lab 4 Group Work - Automated Software Testing

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Ria | ria767-lab | conftest.py, test_deposit.py |
| Min Thu Kha | 6705140031-creator | test_withdraw.py, test_shared.py |
| Fode Lamine Fofana | 6705140050 | test_teardown.py |

## Our Merge Conflict

During Round 3, our group intentionally created a merge conflict by editing the same section of README.md.

Ria pushed her changes first. When Min Thu Kha pulled the latest version, Git detected overlapping changes. Lamine also experienced a merge conflict when pulling the updated repository.

**Conflict Markers Encountered:**

Git displayed three conflict markers:

- `<<<<<<< HEAD`
- `=======`
- `>>>>>>> commit-hash`

**Which Lines We Kept:**

We kept the contribution rows from Ria, Min Thu Kha, and Lamine in the final README table. We removed the duplicate heading and conflict markers.

**Why Git Could Not Resolve It Automatically:**

Git could not automatically combine the changes because multiple members edited the same section of README.md independently. We manually combined everyone's contributions and committed the resolved file.








## Git Contribution Summary

The following results were obtained using git shortlog -sn HEAD:

10  ria
 5  6705140031-creator
 5  Fode Lamine Fofana
 1  ria767-lab

## Reflection Questions

1. Why was your push rejected, and how did you fix it?

Our push was rejected because another member had already pushed new commits to the remote repository. We fixed this by pulling the latest changes, merging our work, and pushing again.

2. Why could Git not resolve the README conflict automatically?

Git could not resolve the conflict automatically because multiple group members edited the same section of README.md independently. We manually combined the contributions and removed the conflict markers.

3. What is the difference between committing and pushing?

Committing saves changes in our local Git repository, while pushing uploads those commits to the shared repository on GitHub.

4. How do fixtures reduce duplicated setup code in tests?

Pytest fixtures allow multiple tests to reuse the same setup code, such as creating a BankAccount object. This reduces repetition and makes the tests easier to maintain.
