all: benchmarks_including_copy.txt

benchmarks_including_copy.txt: benchmarks_with_data_transfer.py
	python3 $< > $@
