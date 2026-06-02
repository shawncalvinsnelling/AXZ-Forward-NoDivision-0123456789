PYTHONPATH := src

.PHONY: verify test

verify:
	PYTHONPATH=$(PYTHONPATH) python scripts/verify_runtime_safety.py
	PYTHONPATH=$(PYTHONPATH) python scripts/verify_challenge_3.py
	PYTHONPATH=$(PYTHONPATH) python scripts/verify_data_hashes.py
	PYTHONPATH=$(PYTHONPATH) python -m pytest -q

test:
	PYTHONPATH=$(PYTHONPATH) python -m pytest -q
