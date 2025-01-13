
WORKDIR = app

all:
	black $(WORKDIR)
	uvicorn app.main:app --port 8000