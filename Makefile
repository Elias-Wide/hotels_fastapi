
WORKDIR = app

all:
	black $(WORKDIR)
	uvicorn app.main:app --reload --port 8000