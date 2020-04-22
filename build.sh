git submodule init
git submodule update

echo "You have protoc version: $(protoc --version)"

cd protobuf/python

echo "Build"
python3 setup.py build

echo "Test"
python3 setup.py test

cd ../..

echo "Done"
