#!/bin/bash
echo "$CAFFE_ROOT"
if [ -z ${CAFFE_ROOT+x} ]; then 
 echo "CAFFE_ROOT is unset"
else 
 echo "CAFFE_ROOT is set to '$CAFFE_ROOT'"
 target_dir=$(dirname $0)
 pushd $target_dir
 caffe train -solver e1.solver.txt -weights $CAFFE_ROOT/models/bvlc_alexnet/bvlc_alexnet.caffemodel -gpu 0 &> e1.log
 popd
fi
