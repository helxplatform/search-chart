# Image for the esdump export/import jobs (templates/esdump-job.yaml).
# Everything is fetched and pinned at build time, so at runtime the jobs only
# talk to Elasticsearch and the lakeFS API.
#
#   docker build -t containers.renci.org/helxplatform/esdump:<tag> esdump/

FROM golang:1.26-alpine@sha256:a2012b4a1d1f9f7e9f44e0d39b805a901e856b1dd80b4e6ee4338db547050308 AS esdump
ARG ESDUMP_COMMIT=b3dd41ead31f8b228eeefe930409591583b91d45
RUN apk add --no-cache git \
 && git clone https://github.com/RENCI/ElasticSearchDump /src \
 && cd /src \
 && git checkout "$ESDUMP_COMMIT" \
 # the repo ships no go.sum
 && go mod tidy \
 && CGO_ENABLED=0 go build -ldflags="-extldflags=-static" -o /esdump .

FROM python:3.12-alpine@sha256:e6dae589c1c05976188fd3bd019afd091445fc533ed2ea29001beddc7368a9c8
ARG DUG_COMMIT=7f04f2881fa95ff54527e72d2d5e9d2aed29500d
# index_init.py only needs the sync client; dug pins 8.5.2. pip is removed
# afterwards since nothing installs at runtime and it carries its own CVEs.
RUN pip install --no-cache-dir elasticsearch==8.5.2 \
 && pip uninstall -y pip
ADD https://raw.githubusercontent.com/helxplatform/dug/${DUG_COMMIT}/src/dug/core/index_init.py /opt/esdump/index_init.py
# stdlib lakeFS client in place of lakectl, whose Go dependencies carry most of
# the image's CVEs
COPY lakefs.py /opt/esdump/lakefs.py
# dug sets replicas = node count, i.e. one copy more than there are nodes, so
# every index it creates stays yellow; use node count - 1 (fails the build if
# upstream changes the line, so the patch never silently stops applying)
RUN sed -i 's/replicas = es.nodes.info()\["_nodes"\]\["total"\]$/replicas = max(es.nodes.info()["_nodes"]["total"] - 1, 0)/' /opt/esdump/index_init.py \
 && grep -q 'replicas = max(es.nodes.info()\["_nodes"\]\["total"\] - 1, 0)' /opt/esdump/index_init.py \
 && chmod -R a+rX /opt/esdump
COPY --from=esdump /esdump /usr/local/bin/esdump
ENV PYTHONDONTWRITEBYTECODE=1 \
    HOME=/tmp
USER 1000:1000
WORKDIR /esdata
