
train_italics_normal2S:   Training set for Hume Dialogs characters, to synthesize a model for recognizing italics letters.
train_normal_italics2S:   Training set for Hume Dialogs characters, to synthesize a model for recognizing normal letters.

    To run, just cd to a directory, type run_train and enter. This loads all the png and txt files and runs ocropus-rtrain. Models are written out by Ocropus once every 1000 iterations. For example, since the default model, en-default.pyrnn.gz, is loaded to begin with, Ocropus starts with iteration # 100000.
100000 53.20 (478, 48) line462.bin.png
When the iteration number reaches 101000, you can expect to see a model file written out. It will be called hume-model-*****-??????.pyrnnn.gz. The next model will be written out when the iteration number reaches 102000 and so on.
