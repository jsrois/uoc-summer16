# uoc-summer16
Results and documentation related to my 2-month stay at the [SUnAI group](http://sunai.uoc.edu) (Universitat Oberta de Catalunya).
The stay is related to (convolutional) Deep Neural Networks and the experiments are
carried out using state-of-the-art tools such as Caffe (BVLC), TensorFlow (Google) and Torch.

Go to the [experiments](doc/experiments.md) section to see the different tests and whacky experiments carried out with neural nets or visit the [documentation and resources](doc/resources.md) section for a list of interesting publications and tools (including some remarks and comments). 

### General setup

Remember to download the required image databases and models by running `setup.sh` before you run any of the experiments.

All the experiments require the `CAFFE_ROOT` environment variable to be set to the location of your `caffe` instalation. Also, adding `$CAFFE_ROOT/build/tools` to your `PATH` can be handy. For instance, you can place the following line in your `~/.bash_profile` file:
 
```
 export CAFFE_ROOT=$HOME/caffe
 export PATH=$CAFFE_ROOT/build/tools:$PATH
```
