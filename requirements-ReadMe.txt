🛠️ Explanation of Dependencies
	•	Core Bot Frameworks: telegraf, python-telegram-bot
	•	Web/API: requests, flask, fastapi
	•	Database: sqlite3, sqlalchemy, redis (pick based on your use case)
	•	AI & NLP (optional, for chat-driven game features): openai, nltk, transformers
	•	Security: cryptography, pyjwt
	•	Testing & Development: pytest, black, isort
	
----------

🔄 How to Use Extras
	1.	Install Core Dependencies (for bot functionality):

pip install -r requirements.txt


	2.	Install Development Tools (if working locally):

pip install -r requirements.txt[dev]


	3.	Install Deployment & Production Dependencies:

pip install -r requirements.txt[deploy]

🔥 Why This is Better
	•	✅ Organized: Dependencies grouped logically (core, dev, deploy).
	•	✅ Scalable: Allows adding new dependencies without bloating installs.
	•	✅ Future-Proof: Covers AI, security, monitoring, and automation.

This setup ensures your bot is production-ready while keeping a clean development environment! 