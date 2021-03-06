#!/bin/bash
echo "$CAFFE_ROOT"
if [ -z ${CAFFE_ROOT+x} ]; then 
 echo "CAFFE_ROOT is unset"
else 
 echo "CAFFE_ROOT is set to '$CAFFE_ROOT'"
 target_dir=$(dirname $0)
 pushd $target_dir
 caffe train -solver e4.solver.txt -weights $CAFFE_ROOT/extra_models/placesCNN_upgraded/places205CNN_iter_300000_upgraded.caffemodel -gpu all &> e4.log
 popd
fi
