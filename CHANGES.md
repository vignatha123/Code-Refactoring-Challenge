Major Issues Identified
All code in one file (no separation of concerns)
No input validation
Passwords stored in plain text
Poor error handling
Hardcoded secrets
Changes Made
Split code into modules (routes, models, services)
Used bcrypt for secure password storage
Added request payload validation using Pydantic
Used environment variables for sensitive info
Improved error handling with proper HTTP status codes
Assumptions & Trade-offs
Assumed Flask as the original framework
Did not implement full authentication flow (JWT) due to time
Wrote only minimal tests to prove functionality
With More Time...
Add token-based authentication
Add pagination to /users
Add full unit test coverage
Dockerize the application
AI Tools Used
ChatGPT: to guide refactoring and validation logic
Copilot: for quick code suggestions
