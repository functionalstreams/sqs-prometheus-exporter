version := $(shell cat VERSION)

docker:
	docker build -t functionalstreams/sqs-prometheus-exporter:$(version) .

push: docker
	docker push functionalstreams/sqs-prometheus-exporter:$(version)