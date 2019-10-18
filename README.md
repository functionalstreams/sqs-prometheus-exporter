# SQS Prometheus Exporter

![Build Status](https://github.com/functionalstreams/sqs-prometheus-exporter/workflows/Build%20and%20publish/badge.svg) 

A simple SQS prometheus exporter written in python. It reads the attributes from the SQS queue and exposes the 
corresponding prometheus metrics.

Example response from `/metrics` endpoint:

```
# HELP approximate_number_of_messages Number of messages available
# TYPE approximate_number_of_messages gauge
approximate_number_of_messages{queue="queue1"} 0.0
# HELP approximate_number_of_messages_delayed Number of messages delayed
# TYPE approximate_number_of_messages_delayed gauge
approximate_number_of_messages_delayed{queue="queue1"} 2.0
# HELP approximate_number_of_messages_not_visible Number of messages in flight
# TYPE approximate_number_of_messages_not_visible gauge
approximate_number_of_messages_not_visible{queue="queue1"} 1.0
```

### Access configuration
Credentials for AWS are provided in the following order:

* Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_SESSION_TOKEN)
* Shared credentials file (~/.aws/credentials)
* IAM role for Amazon EC2

### Run with docker

```
docker run -p 9095:9095 -it -e AWS_REGION=eu-west-1 \
    -e AWS_ACCESS_KEY_ID={{ACCESS_KEY_ID}} \
    -e AWS_SECRET_ACCESS_KEY={{SECRET_ACCESS_KEY}} \
    -e AWS_SESSION_TOKEN={{SESSION_TOKEN}} \ 
    -e QUEUES_TO_MONITOR=queue1,queue2 \
     functionalstreams/sqs-prometheus-exporter:0.1.1
```

Docker images are hosted [here](https://cloud.docker.com/u/functionalstreams/repository/docker/functionalstreams/sqs-prometheus-exporter)

### Installing with helm

Helm chart repository is hosted [here](https://functionalstreams.github.io/helm-repo/). More info on the helm chart can
be found [here](https://github.com/functionalstreams/sqs-prometheus-exporter/tree/master/kubernetes/sqs-prometheus-exporter)

_For simplicity when managing versions, helm chart and docker image they always have the same version and so app_version is omitted from the helm chart._