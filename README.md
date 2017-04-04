# oldOCR
# Optical Character Recognition of old and noisy print sources.

This project seeks to solve two specific Optical Character Recognition cases on the way to creating a generalized solution or improvement to OCR of old and noisy texts.  The two case studies are seventeenth and eighteenth century printed books.  There are extensive archives of poor OCR with scans already in place.  Here the method would be to work with the bad OCR diffed (at word or perhaps character level in a stream) against any known good texts, such as the ones transcoded into Project Gutenberg.  Treat text as a stream.  Try noise removal techniques from DSP.  Think about the problem from how a reader reads these old texts successfully rather than starting from image processing and computing framework alone.  The second case would be Hawaiian Language Newspapers, which also have some known good texts and a lot of poor OCR.  We would work with Puakea on these, and possibly with University of (??? in Canada, Karen Fox)

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

## collaborators
* Karen Fox's Python dev
* Puakea
* the letter writers from the grant app.
