mkdir data
pushd data
curl -O http://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz
tar -xvf cifar-10-binary.tar.gz
rm cifar-10-binary.tar.gz
popd