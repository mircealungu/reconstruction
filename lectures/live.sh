


FILE=$(basename -- $1)
WITHOUT_EXTENSION="${FILE%%.*}"

MDFILE=$WITHOUT_EXTENSION.md
HTMLFILE=$WITHOUT_EXTENSION.html

echo "File:" $FILE
echo $WITHOUT_EXTENSION
echo $MDFILE
echo $HTMLFILE



# Generate a first version such that the server does not complain 
../remark_presi.py $MDFILE Live.html


# cat Slides.md | sed 's_\!\[\](\(.*\))_<img src="\1" style="width:100%"/>_g' | sed 's_\!\[\(.*\)\](\(.*\))_<img src="\2" style="width:\1px"/>_g' > Slides-ML.md && ../../remark_presi.py Slides-ML.md ./Slides.html


# | sed 's_\!\[\](\(.*\))_<img src="\1" style="width:100%"/>_g' | sed 's_\!\[\(.*\)\](\(.*\))_<img src="\2" style="width:\1px"/>_g'\

# fswatch -o $MDFILE | xargs -n1 -I{} cat $MDFILE > Live.md &

fswatch -o Reconstruction_2_Lecture_11.md | xargs -n1 -I{} cat Reconstruction_2_Lecture_11.md > Live.md & 

fswatch -o Live.md | xargs -n1 -I{} ../remark_presi.py Live.md Live.html & 

reload -b -s Live.html