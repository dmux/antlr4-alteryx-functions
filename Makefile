all:
	antlr -visitor -Dlanguage=Python3 -o AlteryxFunctionsTranspiler AlteryxFunctions.g4
test:
	python -m unittest discover -s tests