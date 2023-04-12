FILENAME := Reconstruction_2_Lecture_11

.PHONY: all watch preview

all:
	cat $(FILENAME).md | sed 's_\!\[\](\(.*\))_<img src="\1" style="width:100%"/>_g' | sed 's_\!\[\(.*\)\](\(.*\))_<img src="\2" style="width:\1px"/>_g' > $(FILENAME)-Live.md && ../remark_presi.py $(FILENAME)-Live.md ./$(FILENAME).html && rm -rf $(FILENAME)-Live.md

preview:
	../../remark_presi.py --preview Slides.md ./Slides.html

Slides.pdf: Slides.md
	pandoc --pdf-engine=xelatex Slides.md -o Slides.pdf

watch:
	fswatch -o Slides.md | xargs -n1 -I{} make preview

live: 
	fswatch -o $(FILENAME).md | xargs -n1 -I{} make & reload -b -s $(FILENAME).html