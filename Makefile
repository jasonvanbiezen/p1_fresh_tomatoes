run:
	./run_fresh_tomatoes.py
all: test
test:
	./test_*.py
clean:
	rm *.pyc *.html
