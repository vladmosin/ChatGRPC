python -m grpc_tools.protoc -I=resources/ --python_out=resources/ --grpc_python_out=resources/ resources/service.proto
export PYTHONPATH=$PYTHONPATH:resources
