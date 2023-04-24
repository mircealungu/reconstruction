FILENAME := 3_EvolutionaryAnalysis

.PHONY: all watch preview

all:
	echo "REDOING THE ALL TARGET" && cat $(FILENAME).md | sed 's_\!\[\](\(.*\))_<img src="\1" style="width:100%"/>_g' | sed 's_\!\[\(.*\)\](\(.*\))_<img src="\2" style="width:\1px"/>_g' > $(FILENAME)-Live.md && tools/remark_presi.py $(FILENAME)-Live.md ./$(FILENAME).html && rm -rf $(FILENAME)-Live.md

live: 
	fswatch -o $(FILENAME).md | xargs -n1 -I{} make & reload -b -s $(FILENAME).html