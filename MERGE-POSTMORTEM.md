# MERGE-POSTMORTEM

## Summary
We simulated a merge conflict between two clones (`repo1` and `repo2`) of the same repository.

## What Happened
- `repo1` pushed a change to `temp.js`.
- `repo2` made a different change on the same line.
- When `repo2` pulled, Git detected a merge conflict.

## Resolution
We manually edited `temp.js` to repo1 changes:

```js
// change from repo1
// change from repo2
