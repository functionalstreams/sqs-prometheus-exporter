# SQS Prometheus exporter Helm Chart

[Kafka Manager](https://github.com/yahoo/kafka-manager) is a tool for managing [Apache Kafka](http://kafka.apache.org/).

## TL;DR;

```bash
helm repo add functional-streams https://functionalstreams.github.io/helm-repo 
helm install functionalstreams/sqs-prometheus-exporter
```

## Prerequisites

- Kubernetes 1.9+ with Beta APIs enabled

## Installing the Chart

To install the chart with the release name `my-release`:

```bash
$ helm install --name sqs-prometheus-exporter functionalstreams/sqs-prometheus-exporter
```

The command deploys SQS prometheus exporter on the Kubernetes cluster with the default configuration. 
The [configuration](#configuration) section lists the parameters that can be configured during installation.


## Uninstalling the Chart

To uninstall/delete the `sqs-prometheus-exporter` deployment:

```bash
$ helm delete --purge sqs-prometheus-exporter
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following table lists the configurable parameters of the Kafka Manager chart and their default values.

Parameter | Description | Default
--------- | ----------- | -------
`image.repository` | Container image repository | `zenko/kafka-manager`
`image.tag` | Container image tag | `1.3.3.22`
`image.pullPolicy` | Container image pull policy | `IfNotPresent`
`metrics.serviceMonitor.enabled` | Whether to enable prometheus service monitor | `true`
`queuesToMonitor` | Comma separated list of the queues to monitor | `example`
`awsRegion` | The aws related region | `eu-west-1`
