# Core Dependencies
flask                       # Web framework for the bot/game
python-dotenv               # Manage environment variables
telegraf                    # For handling Telegram bot interactions
beautifulsoup4              # Web scraping (if needed)
lxml                        # XML/HTML parsing
pandas                      # Data processing for structured game data

# AI/NLP (Optional Enhancements)
openai                      # OpenAI API for generating responses
nltk                        # Natural Language Toolkit for text analysis
transformers                # AI text processing (if using language models)

# Security
cryptography                # Token storage and encryption
pyjwt                       # JSON Web Token handling (authentication)

# Task Automation
apscheduler                 # Automate background tasks

# Logging
loguru                      # Advanced logging framework
colorlog                    # Adds color to logging output

# Development and Testing Extras
pytest                      # Testing framework
black                       # Code formatter
isort                       # Auto-sorts Python imports
flake8                      # Linter for code quality
mypy                        # Type checking
pre-commit                  # Run linters before commits

# Deployment and Monitoring Extras
[deploy]
gunicorn                    # WSGI server for Flask
uvicorn                     # ASGI server for FastAPI
docker                      # Containerized deployments
sentry-sdk                  # Error tracking and monitoring