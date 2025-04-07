
WORKDIR = app

all:
	black $(WORKDIR) --line-length 79
	uvicorn app.main:app --port 8000