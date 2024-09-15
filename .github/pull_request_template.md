# Title

<!-- Add a descriptive title, such as "Add task completion status feature" or "Fix bug in task monitoring view". -->

## Description

<!-- Please include a brief summary of the changes this pull request introduces. Explain the problem this PR addresses or the feature it implements. -->

- **Related Issue:** <!-- Link the issue number if applicable (e.g., Fixes #123) -->
- **Summary of Changes:**
  - List major changes made
  - Mention any new features or bug fixes
  - Outline any important design or architectural decisions made

## How to Test

<!-- Provide instructions on how to test your changes, especially if manual steps are required. Ensure anyone reviewing the PR can easily reproduce the results. -->

1. Check out this branch: `git checkout <branch-name>`
2. Apply migrations (if any): `python manage.py migrate`
3. Run the development server: `python manage.py runserver`
4. Test the following:
   - [ ] Task creation works as expected
   - [ ] Task status updates are correctly monitored
   - [ ] UI displays task progress properly
   - [ ] API endpoints (if applicable) respond with the correct data
   - [ ] Other test scenarios, etc.

## Screenshots (if applicable)

<!-- Add screenshots of the UI changes or anything else to visually describe the impact of the PR. -->

## Checklist

<!-- Make sure all of the following checks are completed before submitting. -->

- [ ] Code follows the project’s style guide (e.g., PEP 8)
- [ ] Tests have been added for new functionality
- [ ] Existing tests pass with the new changes: `python manage.py test`
- [ ] All linting checks pass (e.g., flake8, black)
- [ ] Documentation has been updated (if necessary)

## Deployment Notes

<!-- Provide any special notes regarding deployment if needed (e.g., database migrations, environment variables). -->

- [ ] This PR requires database migrations
- [ ] New environment variables need to be added (describe if any)

## Additional Information

<!-- Any additional information or context that might help the reviewer. -->
