demo:
	(cd green; make)
	(echo; echo; cd pyxi; python2 pyxi)

clean:
	(cd green; make clean)
	(cd pyxi; rm -f core *.pyc)
