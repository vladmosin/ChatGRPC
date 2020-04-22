# ChatGRPC

* `git submodule init`

* `git submodule update`

* `bash build.sh`

* `bash build_proto.sh`

* `export PYTHONPATH=$PYTHONPATH:resources`

Дальше запускаем сервер

* `python3 Application.py --port 8888`

И клиентов

* `python3 Application.py --address localhost --port 8888` x 2
 
