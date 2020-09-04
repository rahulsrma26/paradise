develop:
	uvicorn src.paradise.server:app --reload --port 8000

clean:
	rm -rf src/paradise.egg-info
	rm -rf build
	rm -rf dist
	rm -rf .tox

package:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

major:
	bump2version --allow-dirty major

minor:
	bump2version --allow-dirty minor

patch:
	bump2version --allow-dirty patch
