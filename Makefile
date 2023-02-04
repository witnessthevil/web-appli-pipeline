network:
	docker network create web-app-2

build_kafka_server:
	docker build . -f Dockerfile_kafka -t kafka-server 

run_kafka_server:
	docker run -it -p 9092:9092 --network web-app-2 --name kafka-server kafka-server /bin/bash

create_topic_for_user_login:
	/usr/local/kafka/bin/kafka-topics.sh --create --topic kafka-login-data --partitions 3 --bootstrap-server 172.21.0.2:29092

build_hadoop_server:
	docker build . -f Dockerfile_hadoop -t hadoop-server 

run_hadoop_server:
	docker run -it --network web-app-2 --name hadoop-server hadoop-server /bin/bash

build_maxwell_server:
	docker build . -f Dockerfile_maxwell -t maxwell