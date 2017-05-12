
	This directory contains example files to run image processing on the Hume Dialogs OCR images, using the processing software Ocropy. The script run-test executes each one of the Ocropus scripts in order.
	Ocropus-nlbin		: Image binarization using non-linear processing.
	Ocropus-gpageseg	: Segment the image by rows and columns and lines
	Ocropus-rpred		: Apply a (previously trained) Recurrent Neural Network (LSTM) recognizer
	Ocropus-hocr		: Construct an HTML output file in hOCR format by putting together the recognition results for each page in sequence.
	Ocropus-visualize	: Generate HTML for debugging a book directory. Input: a directory in standard OCRopus book format Output: index.html files and thumbnails showing recognition results
	Ocropus-gtedit 		: Create html file for user interface

	Once done, Ocropus writes temp a directory with all the results. The Hume dialog text recognition requires training and usage of at least two models, one for recognition of italics letters and one for recognition of normal letters. These can be found in the directories named italics and normal, respectively. The work on combining these two results and creating one result page is ongoing.
