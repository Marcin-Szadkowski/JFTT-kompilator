env:
	( \
		python3.8 -m venv .venv; \
		echo "\n" >> .venv/bin/activate; \
		. .venv/bin/activate; \
		pip install --upgrade pip poetry; \
		poetry install \
	)