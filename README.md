# search

![Version: 3.0.24](https://img.shields.io/badge/Version-3.0.24-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.9.8](https://img.shields.io/badge/AppVersion-2.9.8-informational?style=flat-square)

A Helm chart for Helx Search components. This chart installs Dug, TranQL , Airflow and Redis.

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| @helx-charts | redis-insight | 0.1.0 |
| @helx-charts | tranql | 0.4.2 |
| https://airflow-helm.github.io/charts | airflow | 8.6.1 |
| https://charts.bitnami.com/bitnami | redis | 17.1.2 |
| https://helm.elastic.co | elasticsearch | 7.16.3 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| airflow.airflow.config.AIRFLOW__CORE__LOAD_EXAMPLES | string | `"FALSE"` |  |
| airflow.airflow.config.AIRFLOW__CORE__LOGGING_LEVEL | string | `"INFO"` |  |
| airflow.airflow.config.AIRFLOW__KUBERNETES__DELETE_WORKER_PODS | string | `"TRUE"` |  |
| airflow.airflow.config.AIRFLOW__SCHEDULER__SCHEDULE_AFTER_TASK_EXECUTION | string | `"FALSE"` |  |
| airflow.airflow.config.AIRFLOW__WEBSERVER__BASE_URL | string | `""` |  |
| airflow.airflow.configSecretsName | string | `"airflow-config-secrets"` |  |
| airflow.airflow.dbMigrations.enabled | bool | `true` |  |
| airflow.airflow.dbMigrations.runAsJob | bool | `true` |  |
| airflow.airflow.executor | string | `"KubernetesExecutor"` |  |
| airflow.airflow.extraEnv[0].name | string | `"ROGER_ANNOTATION_NORMALIZER"` |  |
| airflow.airflow.extraEnv[0].valueFrom.configMapKeyRef.key | string | `"normalizer_url"` |  |
| airflow.airflow.extraEnv[0].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[10].name | string | `"ROGER_REDISGRAPH_GRAPH"` |  |
| airflow.airflow.extraEnv[10].valueFrom.configMapKeyRef.key | string | `"graph"` |  |
| airflow.airflow.extraEnv[10].valueFrom.configMapKeyRef.name | string | `"search-redis-config"` |  |
| airflow.airflow.extraEnv[11].name | string | `"ROGER_REDISGRAPH_PASSWORD"` |  |
| airflow.airflow.extraEnv[11].valueFrom.secretKeyRef.key | string | `"password"` |  |
| airflow.airflow.extraEnv[11].valueFrom.secretKeyRef.name | string | `"search-redis-secret"` |  |
| airflow.airflow.extraEnv[12].name | string | `"ROGER_REDISGRAPH_PORT"` |  |
| airflow.airflow.extraEnv[12].valueFrom.configMapKeyRef.key | string | `"port"` |  |
| airflow.airflow.extraEnv[12].valueFrom.configMapKeyRef.name | string | `"search-redis-config"` |  |
| airflow.airflow.extraEnv[13].name | string | `"ROGER_S3_ACCESS__KEY"` |  |
| airflow.airflow.extraEnv[13].valueFrom.configMapKeyRef.key | string | `"s3_access_key"` |  |
| airflow.airflow.extraEnv[13].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[14].name | string | `"ROGER_S3_BUCKET"` |  |
| airflow.airflow.extraEnv[14].valueFrom.configMapKeyRef.key | string | `"s3_bucket"` |  |
| airflow.airflow.extraEnv[14].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[15].name | string | `"ROGER_S3_HOST"` |  |
| airflow.airflow.extraEnv[15].valueFrom.configMapKeyRef.key | string | `"s3_host"` |  |
| airflow.airflow.extraEnv[15].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[16].name | string | `"ROGER_S3_SECRET__KEY"` |  |
| airflow.airflow.extraEnv[16].valueFrom.configMapKeyRef.key | string | `"s3_secret_key"` |  |
| airflow.airflow.extraEnv[16].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[17].name | string | `"ROGER_KGX_DATA__SETS"` |  |
| airflow.airflow.extraEnv[17].valueFrom.configMapKeyRef.key | string | `"kgx_data_sets"` |  |
| airflow.airflow.extraEnv[17].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[18].name | string | `"ROGER_INDEXING_NODE__TO__ELEMENT__QUERIES_ENABLED"` |  |
| airflow.airflow.extraEnv[18].valueFrom.configMapKeyRef.key | string | `"node_to_queries_enabled"` |  |
| airflow.airflow.extraEnv[18].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[19].name | string | `"ROGER_ELASTICSEARCH_NBOOST__HOST"` |  |
| airflow.airflow.extraEnv[19].value | string | `"nboost $ TODO compute this"` |  |
| airflow.airflow.extraEnv[1].name | string | `"ROGER_ANNOTATION_ANNOTATOR"` |  |
| airflow.airflow.extraEnv[1].valueFrom.configMapKeyRef.key | string | `"annotator_url"` |  |
| airflow.airflow.extraEnv[1].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[20].name | string | `"ROGER_INDEXING_TRANQL__ENDPOINT"` |  |
| airflow.airflow.extraEnv[20].value | string | `nil` |  |
| airflow.airflow.extraEnv[20].valueFrom.configMapKeyRef.key | string | `"tranql_endpoint"` |  |
| airflow.airflow.extraEnv[20].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[21].name | string | `"AIRFLOW__CORE__FERNET_KEY"` |  |
| airflow.airflow.extraEnv[21].valueFrom.secretKeyRef.key | string | `"fernet-key"` |  |
| airflow.airflow.extraEnv[21].valueFrom.secretKeyRef.name | string | `"airflow-config-secrets"` |  |
| airflow.airflow.extraEnv[2].name | string | `"ROGER_ANNOTATION_SYNONYM__SERVICE"` |  |
| airflow.airflow.extraEnv[2].valueFrom.configMapKeyRef.key | string | `"synonymizer_url"` |  |
| airflow.airflow.extraEnv[2].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[3].name | string | `"ROGER_DATA_DIR"` |  |
| airflow.airflow.extraEnv[3].valueFrom.configMapKeyRef.key | string | `"data_directory"` |  |
| airflow.airflow.extraEnv[3].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[4].name | string | `"ROGER_DUG__INPUTS_DATA__SETS"` |  |
| airflow.airflow.extraEnv[4].valueFrom.configMapKeyRef.key | string | `"input_sets"` |  |
| airflow.airflow.extraEnv[4].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[5].name | string | `"ROGER_DUG__INPUTS_DATA__SOURCE"` |  |
| airflow.airflow.extraEnv[5].valueFrom.configMapKeyRef.key | string | `"data_source"` |  |
| airflow.airflow.extraEnv[5].valueFrom.configMapKeyRef.name | string | `"search-data-config"` |  |
| airflow.airflow.extraEnv[6].name | string | `"ROGER_ELASTICSEARCH_HOST"` |  |
| airflow.airflow.extraEnv[6].valueFrom.configMapKeyRef.key | string | `"host"` |  |
| airflow.airflow.extraEnv[6].valueFrom.configMapKeyRef.name | string | `"search-elastic-config"` |  |
| airflow.airflow.extraEnv[7].name | string | `"ROGER_ELASTICSEARCH_PASSWORD"` |  |
| airflow.airflow.extraEnv[7].valueFrom.secretKeyRef.key | string | `"password"` |  |
| airflow.airflow.extraEnv[7].valueFrom.secretKeyRef.name | string | `"search-elastic-secret"` |  |
| airflow.airflow.extraEnv[8].name | string | `"ROGER_ELASTICSEARCH_USERNAME"` |  |
| airflow.airflow.extraEnv[8].valueFrom.secretKeyRef.key | string | `"username"` |  |
| airflow.airflow.extraEnv[8].valueFrom.secretKeyRef.name | string | `"search-elastic-secret"` |  |
| airflow.airflow.extraEnv[9].name | string | `"ROGER_REDISGRAPH_HOST"` |  |
| airflow.airflow.extraEnv[9].valueFrom.configMapKeyRef.key | string | `"host"` |  |
| airflow.airflow.extraEnv[9].valueFrom.configMapKeyRef.name | string | `"search-redis-config"` |  |
| airflow.airflow.extraVolumeMounts[0].mountPath | string | `"/opt/airflow/share/data"` |  |
| airflow.airflow.extraVolumeMounts[0].name | string | `"airflow-data"` |  |
| airflow.airflow.extraVolumes[0].name | string | `"airflow-data"` |  |
| airflow.airflow.extraVolumes[0].persistentVolumeClaim.claimName | string | `"search-data"` |  |
| airflow.airflow.image.pullPolicy | string | `"Always"` |  |
| airflow.airflow.image.repository | string | `"containers.renci.org/helxplatform/roger"` |  |
| airflow.airflow.image.tag | string | `"latest"` |  |
| airflow.airflow.kubernetesPodTemplate.resources.limits.cpu | int | `2` |  |
| airflow.airflow.kubernetesPodTemplate.resources.limits.ephemeral-storage | string | `"4G"` |  |
| airflow.airflow.kubernetesPodTemplate.resources.limits.memory | string | `"16G"` |  |
| airflow.airflow.kubernetesPodTemplate.resources.requests.cpu | int | `2` |  |
| airflow.airflow.kubernetesPodTemplate.resources.requests.ephemeral-storage | string | `"4G"` |  |
| airflow.airflow.kubernetesPodTemplate.resources.requests.memory | string | `"16G"` |  |
| airflow.airflow.usersUpdate | bool | `true` |  |
| airflow.dags.gitSync.branch | string | `"main"` |  |
| airflow.dags.gitSync.enabled | bool | `true` |  |
| airflow.dags.gitSync.repo | string | `"https://github.com/helxplatform/roger.git"` |  |
| airflow.dags.gitSync.repoSubPath | string | `"dags"` |  |
| airflow.dags.gitSync.revision | string | `"HEAD"` |  |
| airflow.dags.gitSync.syncWait | int | `60` |  |
| airflow.enabled | bool | `true` |  |
| airflow.externalRedis.host | string | `""` |  |
| airflow.externalRedis.passwordSecret | string | `"search-redis-secret"` |  |
| airflow.externalRedis.passwordSecretKey | string | `"password"` |  |
| airflow.flower.enabled | bool | `false` |  |
| airflow.logs.path | string | `"/opt/airflow/share/logs"` |  |
| airflow.logs.persistence.accessMode | string | `"ReadWriteMany"` |  |
| airflow.logs.persistence.enabled | bool | `true` |  |
| airflow.logs.persistence.size | string | `"5Gi"` |  |
| airflow.logs.persistence.storageClass | string | `""` |  |
| airflow.pgbouncer.enabled | bool | `false` |  |
| airflow.redis.enabled | bool | `false` |  |
| airflow.scheduler.logCleanup.enabled | bool | `false` |  |
| airflow.scheduler.resources.limits.cpu | int | `2` |  |
| airflow.scheduler.resources.limits.memory | string | `"4G"` |  |
| airflow.scheduler.resources.requests.cpu | int | `2` |  |
| airflow.scheduler.resources.requests.memory | string | `"4G"` |  |
| airflow.triggerer.enabled | bool | `false` |  |
| airflow.web.resources.limits.cpu | int | `3` |  |
| airflow.web.resources.limits.ephemeral-storage | string | `"1G"` |  |
| airflow.web.resources.limits.memory | string | `"4G"` |  |
| airflow.web.resources.requests.cpu | int | `3` |  |
| airflow.web.resources.requests.ephemeral-storage | string | `"1G"` |  |
| airflow.web.resources.requests.memory | string | `"4G"` |  |
| airflow.workers.enabled | bool | `false` |  |
| api.appName | string | `"webserver"` |  |
| api.debug | bool | `false` |  |
| api.deployment.apiPort | int | `5551` |  |
| api.deployment.apiTimeout | int | `10` |  |
| api.deployment.apiWorkers | int | `4` |  |
| api.deployment.extraEnv | list | `[]` |  |
| api.deployment.imagePullSecrets | list | `[]` |  |
| api.deployment.logLevel | string | `"INFO"` |  |
| api.deployment.resources.limits.cpu | int | `2` |  |
| api.deployment.resources.limits.memory | string | `"2G"` |  |
| api.deployment.resources.requests.cpu | int | `2` |  |
| api.deployment.resources.requests.memory | string | `"2G"` |  |
| api.image.pullPolicy | string | `"IfNotPresent"` |  |
| api.image.repository | string | `"helxplatform/dug"` |  |
| api.image.tag | string | `""` |  |
| api.service.annotations | object | `{}` |  |
| api.service.apiPort | string | `"5551"` |  |
| api.service.name | string | `"search-api"` |  |
| api.service.port | string | `"5551"` |  |
| api.service.type | string | `"ClusterIP"` |  |
| config.annotation.annotator_url | string | `"https://api.monarchinitiative.org/api/nlp/annotate/entities?min_length=4&longest_only=false&include_abbreviation=false&include_acronym=false&include_numbers=false&content="` |  |
| config.annotation.normalizer_url | string | `"http://nn-web-prod-node-normalization-web-service-root.translator.svc.cluster.local:8080/get_normalized_nodes?conflate=false&curie="` |  |
| config.annotation.synonymizer_url | string | `"https://onto.renci.org/synonyms/"` |  |
| config.data_source | string | `"stars"` |  |
| config.input_sets | string | `"bdc-dbGaP,topmed"` |  |
| config.kgx_data_sets | string | `"baseline-graph,cde-graph"` |  |
| config.node_to_queries_enabled | string | `"false"` |  |
| config.s3.access_key | string | `""` |  |
| config.s3.bucket | string | `""` |  |
| config.s3.host | string | `""` |  |
| config.s3.secret_key | string | `""` |  |
| elasticsearch.enabled | bool | `true` |  |
| elasticsearch.esJavaOpts | string | `"-Xmx1g -Xms1g -Dlog4j2.disable.jmx=true -Dlog4j2.formatMsgNoLookups=true"` |  |
| elasticsearch.extraEnvs[0].name | string | `"ELASTIC_PASSWORD"` |  |
| elasticsearch.extraEnvs[0].valueFrom.secretKeyRef.key | string | `"password"` |  |
| elasticsearch.extraEnvs[0].valueFrom.secretKeyRef.name | string | `"search-elastic-secret"` |  |
| elasticsearch.extraEnvs[1].name | string | `"ELASTIC_USERNAME"` |  |
| elasticsearch.extraEnvs[1].valueFrom.secretKeyRef.key | string | `"username"` |  |
| elasticsearch.extraEnvs[1].valueFrom.secretKeyRef.name | string | `"search-elastic-secret"` |  |
| elasticsearch.extraEnvs[2].name | string | `"LOG4J_FORMAT_MSG_NO_LOOKUPS"` |  |
| elasticsearch.extraEnvs[2].value | string | `"true"` |  |
| elasticsearch.imageTag | string | `"7.16.3"` |  |
| elasticsearch.maxUnavailable | int | `0` |  |
| elasticsearch.replicas | int | `1` |  |
| elasticsearch.resources.limits.cpu | int | `1` |  |
| elasticsearch.resources.limits.memory | string | `"2G"` |  |
| elasticsearch.resources.requests.cpu | int | `1` |  |
| elasticsearch.resources.requests.memory | string | `"2G"` |  |
| elasticsearch.sysctlInitContainer.enabled | bool | `false` |  |
| fullnameOverride | string | `""` |  |
| ingress.annotations | object | `{}` |  |
| ingress.enabled | bool | `false` |  |
| ingress.hosts[0].host | string | `"chart-example.local"` |  |
| ingress.labels | object | `{}` |  |
| ingress.paths[0].name | string | `"ui"` |  |
| ingress.paths[0].path | string | `"/"` |  |
| ingress.paths[0].port | int | `80` |  |
| ingress.paths[0].prepend | bool | `false` |  |
| ingress.paths[1].name | string | `"web"` |  |
| ingress.paths[1].path | string | `"/airflow"` |  |
| ingress.paths[1].port | int | `8080` |  |
| ingress.paths[1].prepend | bool | `true` |  |
| ingress.paths[2].name | string | `"tranql"` |  |
| ingress.paths[2].path | string | `"/tranql"` |  |
| ingress.paths[2].port | int | `8081` |  |
| ingress.paths[2].prepend | bool | `true` |  |
| ingress.rewrite_paths[0].name | string | `"api"` |  |
| ingress.rewrite_paths[0].path | string | `"/search-api(/|$)(.*)"` |  |
| ingress.rewrite_paths[0].port | int | `5551` |  |
| ingress.rewrite_paths[0].prepend | bool | `true` |  |
| ingress.tls | list | `[]` |  |
| nameOverride | string | `""` |  |
| nboost.enabled | bool | `false` |  |
| persistence.pvcSize | string | `"32Gi"` |  |
| persistence.storageClass | string | `""` |  |
| redis-insight.enabled | bool | `false` | Enable/Disable Redis UI |
| redis-insight.rootUrl | string | `""` | Url should be same as public ingress url |
| redis.auth.existingSecret | string | `"search-redis-secret"` |  |
| redis.auth.existingSecretPasswordKey | string | `"password"` |  |
| redis.clusterDomain | string | `"cluster.local"` |  |
| redis.enabled | bool | `true` |  |
| redis.image.repository | string | `"redislabs/redisgraph"` |  |
| redis.image.tag | string | `"2.8.4"` |  |
| redis.master.command | string | `""` |  |
| redis.master.extraFlags[0] | string | `"--loadmodule"` |  |
| redis.master.extraFlags[1] | string | `"/usr/lib/redis/modules/redisgraph.so"` |  |
| redis.master.extraFlags[2] | string | `"THREAD_COUNT"` |  |
| redis.master.extraFlags[3] | string | `"8"` |  |
| redis.master.extraFlags[4] | string | `"OMP_THREAD_COUNT"` |  |
| redis.master.extraFlags[5] | string | `"16"` |  |
| redis.master.extraFlags[6] | string | `"--appendonly"` |  |
| redis.master.extraFlags[7] | string | `"no"` |  |
| redis.master.livenessProbe.enabled | bool | `false` |  |
| redis.master.persistence.size | string | `"24G"` |  |
| redis.master.readinessProbe.enabled | bool | `true` |  |
| redis.master.readinessProbe.failureThreshold | int | `1` |  |
| redis.master.readinessProbe.periodSeconds | int | `1` |  |
| redis.master.resources.limits.cpu | int | `2` |  |
| redis.master.resources.limits.memory | string | `"32Gi"` |  |
| redis.master.resources.requests.cpu | int | `1` |  |
| redis.master.resources.requests.memory | string | `"12Gi"` |  |
| redis.persistence.existingClaim | string | `"redis-data"` |  |
| redis.replica.autoscaling.enabled | bool | `true` |  |
| redis.replica.autoscaling.maxReplicas | int | `2` |  |
| redis.replica.autoscaling.minReplicas | int | `1` |  |
| redis.replica.autoscaling.targetCPU | int | `100` |  |
| redis.replica.extraFlags[0] | string | `"--loadmodule"` |  |
| redis.replica.extraFlags[1] | string | `"/usr/lib/redis/modules/redisgraph.so"` |  |
| redis.replica.extraFlags[2] | string | `"THREAD_COUNT"` |  |
| redis.replica.extraFlags[3] | string | `"8"` |  |
| redis.replica.extraFlags[4] | string | `"OMP_THREAD_COUNT"` |  |
| redis.replica.extraFlags[5] | string | `"16"` |  |
| redis.replica.livenessProbe.enabled | bool | `false` |  |
| redis.replica.persistence.size | string | `"24G"` |  |
| redis.replica.readinessProbe.enabled | bool | `true` |  |
| redis.replica.readinessProbe.failureThreshold | int | `1` |  |
| redis.replica.readinessProbe.periodSeconds | int | `1` |  |
| redis.replica.readinessProbe.successThreshold | int | `5` |  |
| redis.replica.resources.limits.cpu | int | `2` |  |
| redis.replica.resources.limits.memory | string | `"32Gi"` |  |
| redis.replica.resources.requests.cpu | int | `1` |  |
| redis.replica.resources.requests.memory | string | `"12Gi"` |  |
| redis.usePassword | bool | `true` |  |
| secrets.elastic.name | string | `"search-elastic-secret"` |  |
| secrets.elastic.passwordKey | string | `"password"` |  |
| secrets.elastic.user | string | `"elastic"` |  |
| secrets.elastic.userKey | string | `"username"` |  |
| secrets.redis.name | string | `"search-redis-secret"` |  |
| secrets.redis.passwordKey | string | `"password"` |  |
| tranql.enabled | bool | `true` |  |
| tranql.existingRedis.host | string | `""` |  |
| tranql.existingRedis.port | int | `6379` |  |
| tranql.existingRedis.secret | string | `"search-redis-secret"` |  |
| tranql.existingRedis.secretPasswordKey | string | `"password"` |  |
| tranql.extraEnv[0].name | string | `"WEB_PATH_PREFIX"` |  |
| tranql.extraEnv[0].value | string | `"/tranql"` |  |
| tranql.gunicorn.workerCount | int | `1` | single worker for now to avoid recomputing of schema per worker |
| tranql.gunicorn.workerTimeout | int | `1600` |  |
| tranql.redis.enabled | bool | `false` |  |
| tranql.resources.limits.cpu | int | `2` |  |
| tranql.resources.limits.memory | string | `"2G"` |  |
| tranql.resources.requests.cpu | string | `"500m"` |  |
| tranql.resources.requests.memory | string | `"2G"` |  |
| tranql.webPrefix | string | `"/tranql"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.11.0](https://github.com/norwoodj/helm-docs/releases/v1.11.0)
