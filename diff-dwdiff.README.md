# steps:
* get the ocr text and the gutenberg version of it.  
* delete intro and outro stuff
* search and replace all [CR] with spaces
* remove all excess whitespace.
* If there are headers and page numbers in the text of the OCR version, do a search and replace on whatever is possible to remove.  
* You should now have two long single line files (streams)
* get the noise profile by running diff-dwdiff.sh (might neec to adjust the filenames)

# 2 do:
* figure out a way to mark the noisy sections in the OCR text with the noise removed.
* many of these are close to correct, being hypenation problems or junk combined with a good word.  
