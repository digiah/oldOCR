# oldOCR
# Optical Character Recognition of old and noisy print sources.

This project seeks to solve two specific Optical Character Recognition cases on the way to creating a generalized solution or improvement to OCR of old and noisy texts.  The first case study is seventeenth and eighteenth century printed books.  There are extensive archives of poor OCR with scans already in place.  Here the method would be to work with the bad OCR diffed (at word or perhaps character level in a stream) against any known good texts, such as the ones transcoded into Project Gutenberg.  Treat text as a stream.  Try noise removal techniques from DSP.  Use neural net approach from ocrupy family of OCR scripts written in Python.  Overall, we would like to think about the problem from how a reader reads these old texts successfully rather than starting from image processing and computing framework alone.  Our second case is Hawaiian Language Newspapers, which also have some known good texts and a lot of poor OCR.  We would work with Puakea Nogelmeier and his students as the checkers to see if we are on target with our results. The Hawaian Studies and Hawaiian Language programs as well as OHA all think this is an important project..  

We have had promising rounds of success on both projects, running the trainings tens of thousands of times on both old books in English as well as Hawaiian Language materials and then trying the network on texts which it has not been trained against. That has been our main focus the past three semesters, but we also want to explore the possibilities of treating the text as a stream and trying digital signal processing noise reduction routines on it, but that is in its earliest stages still since we are getting promising results from the neural net approach.  The best approach according to the literature, is to combine multiple approaches including standard dictionary and font based approaches that do not work well on noisy texts alone.  

Issues besides noise and quality in both cases:  
* Alternate spellings
* Alternate orthographies
* poor existing scans
* odd hyphenation
* headers, callouts, page numbers (i.e., what needs to be factored out in creating a DSP stream)

## Components to start with:  
* "[Beyond OCR](https://github.com/digiah/2do/issues/69)" grant application for reference.
  write a new grant as part of the process*
* [High performance computing cluster](https://github.com/digiah/2do/issues/70).
* [Ocropy](https://github.com/tmbdev/ocropy).
* Context: [IO framework](https://github.com/digiah/IO/issues/2).
* This solution would be a component of [CorText](https://github.com/digiah/cortext/issues/6).
