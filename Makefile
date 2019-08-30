all: benchmarks_including_copy.txt benchmarks_without_copy.txt

benchmarks_including_copy.txt: benchmarks_with_data_transfer.py
	python3 $< > $@

benchmarks_without_copy.txt: benchmarks_no_conversion2.py
	python3 $< > $@
