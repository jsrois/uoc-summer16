

Classifying between positive and negative images, using the evoked *valence* in the Emotion6 dataset.  

### Tasks

- [x] Generate positive(+1)/negative(0) labels for the Emotion6 database using the valence score provided.
- [x] _Fine-tune_ the AlexNet model using the Emotion6 positive/negative labels.
- [ ] _Fine-tune_ the Places CNN model using the Emotion6 positive/negative labels.
- [ ] Compose a mosaic image given the classification results with the different models (e.g. green border for images classified as positive, red for negative).
- [ ] Change the learning rate and decay of the _new_ layer in the places net, so that the weights of this layer during finetuning change faster than the pretrained layers.
- [ ] Represent the response of the hidden layers to the test images with the Places net before and after the finetuning, to compare responses.
- [ ] Repeat the fine tuning with a single output of the net. Instead of using a Softmax-based Loss function, try a Sigmoid-based loss-layer.