# kontext-github-check

Test bed for Kontext's GitHub tool checks (`kontext-mvp/work/github-checks/check_toolsets.py`).

The code here is deliberately weak so GitHub's security features have something to report:
`requirements.txt` pins an old `requests` (Dependabot alert) and `app.py` passes a request value to a shell (code scanning alert).
Do not use any of it. The repository is deleted after the tool review.
