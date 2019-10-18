version := $(shell cat VERSION)

CURRENT_DIR=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

build-docker:
	docker build -t functionalstreams/sqs-prometheus-exporter:$(version) .

package-helm:
	@(cd ${CURRENT_DIR}/kubernetes/sqs-prometheus-exporter \
	&& mkdir -p ${CURRENT_DIR}/.generated && helm package . --version $(version) --app-version $(version) --destination ${CURRENT_DIR}/.generated \
	&& cd ${CURRENT_DIR}/.generated \
	&& wget https://functionalstreams.github.io/helm-repo/index.yaml -O existing_index.yaml \
	&& helm repo index . --merge existing_index.yaml \
	&& rm existing_index.yaml )

push-docker:
	docker push functionalstreams/sqs-prometheus-exporter:$(version)

publish-helm-chart:
	@(git clone https://${GIT_API_TOKEN}@github.com/functionalstreams/helm-repo \
	&& cd helm-repo \
	&& cp ${CURRENT_DIR}/.generated/* . \
	&& git add -A \
	&& git commit -m "Released sqs-prometheus-exporter version $(version)" \
	&& git push)
