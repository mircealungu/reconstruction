

files=( *$1*.md )
FILE=$(basename -- "${files[0]}")
WITHOUT_EXTENSION="${FILE%%.*}"

MDFILE=$WITHOUT_EXTENSION.md
HTMLFILE=$WITHOUT_EXTENSION.html

fswatch -o $MDFILE | xargs -n1 -I{} ../remark_presi.py $MDFILE $HTMLFILE & reload -b -s $HTMLFILE
