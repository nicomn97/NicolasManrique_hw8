#Make

all : sample_1_10.txt sample_1_100.txt sample_1_1000.txt sample_2_10.txt sample_2_100.txt sample_2_1000.txt 
	python NicolasManrique_generar.py

all : sample_1_10.png sample_1_100.png sample_1_1000.png sample_2_10.png sample_2_100.png sample_2_1000.png
	python NicolasManrique_analisys.py


