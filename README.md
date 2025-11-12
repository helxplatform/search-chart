# search

A Helm chart for Helx Search components. This chart installs Dug, TranQL , Airflow and Redis.

### Architecture of Search Chart

For full architeture overview please refer to our documentation [here](https://dug.readthedocs.io/en/latest/architecture/roger/).

![Version: 7.0.0](https://img.shields.io/badge/Version-7.0.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v2.13.12](https://img.shields.io/badge/AppVersion-v2.13.12-informational?style=flat-square) 

> [!Note]
> When installing you might notice a warning from bitnami postgres chart about the use of unknown postgres docker image, that warning is safe to ignore.

## Values

### Dug API Server

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| api.certMountPath | string | `"/usr/lib/ssl/certs/ca_elastic.crt"` | Default location to elastic search tls certificate |
| api.deployment | object | `{"apiPort":5551,"apiTimeout":10,"apiWorkers":8,"extraEnv":[],"imagePullSecrets":[],"logLevel":"INFO","resources":{"limits":{"cpu":2,"memory":"2Gi"},"requests":{"cpu":"500m","memory":"1Gi"}}}` | Deployment pod Configuration |
| api.elasticScheme | string | `"https"` | Connection Scheme to elastic search |
| api.image | object | `{"pullPolicy":"Always","repository":"containers.renci.org/helxplatform/dug","tag":""}` | Container image |
| api.replicas | int | `4` | Number of relicas for Dug API server |
| api.service.annotations | object | `{}` | Search service annotation |
| api.service.apiPort | string | `"5551"` | API port on deployment |
| api.service.name | string | `"search-api"` | This should match release name in this example the helm release name was `search` |
| api.service.port | string | `"5551"` | Service port |
| api.service.type | string | `"ClusterIP"` | Service type |

### Koios Chat UI

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| chat | object | `{"apiPort":8080,"config":{"api_url":null,"public_url":null},"enabled":false,"image":{"repository":"containers.renci.org/helxplatform/koios-ui","tag":"v0.0.1"},"replicas":1,"resources":{},"root_path":"/chat","service":{"type":"ClusterIP"}}` | Configuration option for Dug chatbot UI |
| chat_2 | object | `{"apiPort":8080,"config":{"api_url":null,"public_url":null},"enabled":false,"image":{"repository":"containers.renci.org/helxplatform/koios-ui","tag":"v1.0.0"},"replicas":1,"resources":{},"root_path":"/chat-v2","service":{"type":"ClusterIP"}}` | Configuration option for Dug chatbot UI |

### Application Config

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| config.annotation.annotator_type | string | `"sapbert"` | Annotator type to use , options are `sapbert` or `monarch` |
| config.annotation.monarch | object | `{"url":"https://api.monarchinitiative.org/api/nlp/annotate/entities?min_length=4&longest_only=false&include_abbreviation=false&include_acronym=false&include_numbers=false&content="}` | Monarch annotator config |
| config.annotation.normalizer_url | string | `"https://nodenormalization-sri.renci.org/get_normalized_nodes?conflate=false&description=true&curie="` | Node normalization url to use during annotation |
| config.annotation.sapbert | object | `{"annotator_url":"https://sap-qdrant.apps.renci.org/annotate/","bagel":{"enabled":false,"llm_args":{"access_key":"","llm_model_name":"gpt-4o-2024-05-13","organization":""},"prompt":"bagel/ask_classes","url":"https://bagel.apps.renci.org/group_synonyms_openai"},"classification_url":"https://med-nemo.apps.renci.org/annotate/","score_threshold":0.8}` | Sapbert annotator config |
| config.annotation.synonymizer_url | string | `"https://name-resolution-sri.renci.org/reverse_lookup"` | Name resolution url to use to find synonyms |
| config.element_mappings | string | `""` | colon seperated mappings list by comma, eg : dbgap:Non-HEAL Studies,bacpac:HEAL Research Programs, used to map parser outputs to other values. |
| config.input_sets | string | `"bdc:v2.0,topmed:v2.0"` | Input dataset to include during ingestion. These refer to repo names on lakefs. With version (branch) tags. |
| config.kgx_data_sets | string | `"baseline-graph:v5.0,cde-graph:v5.0"` | Knowledge graph input datasets to ingest for the dug Knowledge graph. These are lakefs repo names with version(branches) as tags. |
| config.lakefs.access_key | string | `"accesskey"` | Lakefs access key |
| config.lakefs.branch | string | `"main"` | Branch to write output files to. |
| config.lakefs.enabled | bool | `true` | Enables lakefs usage for input and output on data ingest. |
| config.lakefs.host | string | `"https://lakefs.apps.renci.org"` | Lakefs host address |
| config.lakefs.repo | string | `"test-repo"` | Lakefs repo to write outputs to |
| config.lakefs.secret_key | string | `"secretkey"` | Lakefs secret key |
| config.node_to_queries_enabled | string | `"false"` | Enables CDE extraction from Knowledge graph. |

### Elasticsearch

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| elasticsearch | object | `{"clusterHealthCheckParams":"wait_for_status=green&timeout=1s","enabled":true,"esJavaOpts":"-Xmx6g -Xms6g -Dlog4j2.disable.jmx=true -Dlog4j2.formatMsgNoLookups=true","extraEnvs":[{"name":"ELASTIC_PASSWORD","valueFrom":{"secretKeyRef":{"key":"password","name":"search-elastic-secret"}}},{"name":"ELASTIC_USERNAME","valueFrom":{"secretKeyRef":{"key":"username","name":"search-elastic-secret"}}},{"name":"LOG4J_FORMAT_MSG_NO_LOOKUPS","value":"true"}],"imageTag":"8.19.6","maxUnavailable":0,"replicas":3,"resources":{"limits":{"cpu":1,"ephemeral-storage":"256Mi","memory":"8G"},"requests":{"cpu":1,"ephemeral-storage":"256Mi","memory":"8G"}},"secret":{"enabled":false},"sysctlInitContainer":{"enabled":false}}` | Elastic search for more information checkout full elasticsearch chart options at [https://github.com/elastic/helm-charts/tree/v8.5.1](https://github.com/elastic/helm-charts/tree/v8.5.1) |

### Ingress

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| ingress | object | `{"annotations":{"nginx.ingress.kubernetes.io/cors-allow-headers":"Content-Type","nginx.ingress.kubernetes.io/cors-allow-methods":"POST, OPTIONS","nginx.ingress.kubernetes.io/cors-allow-origin":"*","nginx.ingress.kubernetes.io/enable-cors":"true"},"basicAuth":{"enabled":false,"password":"","username":""},"className":"","enabled":false,"hosts":[{"host":"chart-example.local"}],"labels":{},"pathType":"ImplementationSpecific","paths":[{"name":"ui","path":"/","port":80,"prepend":true},{"name":"tranql","path":"/tranql","port":8081,"prepend":true},{"name":"api-server","path":"/airflow","port":8080,"prepend":true}],"rewrite_paths":[{"name":"api","path":"/search-api(/|$)(.*)","port":5551,"prepend":true}],"tls":[]}` | Values to enable ingress |

### Redis

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| redis | object | `{"auth":{"existingSecret":"search-redis-secret","existingSecretPasswordKey":"password"},"clusterDomain":"cluster.local","commonConfiguration":"# Enable AOF https://redis.io/topics/persistence#append-only-file\nappendonly no\n# Disable RDB persistence, AOF persistence already enabled.\nsave 300 100000","enabled":true,"fullnameOverride":"","image":{"registry":"containers.renci.org","repository":"helxplatform/falkor","tag":"v4.14.4-alpine"},"master":{"command":"","extraFlags":["--loadmodule","/var/lib/falkordb/bin/falkordb.so","THREAD_COUNT","8","OMP_THREAD_COUNT","16"],"livenessProbe":{"enabled":false},"persistence":{"size":"50Gi"},"readinessProbe":{"enabled":true,"failureThreshold":1,"periodSeconds":1},"resources":{"limits":{"cpu":2,"memory":"45Gi"},"requests":{"cpu":1,"memory":"45Gi"}}},"replica":{"autoscaling":{"enabled":false,"maxReplicas":1,"minReplicas":1,"targetCPU":100},"extraFlags":["--loadmodule","/FalkorDB/bin/src/falkordb.so","THREAD_COUNT","8","OMP_THREAD_COUNT","16"],"livenessProbe":{"enabled":false},"persistence":{"size":"50G"},"readinessProbe":{"enabled":true,"failureThreshold":1,"periodSeconds":1,"successThreshold":5},"replicaCount":0,"resources":{"limits":{"cpu":2,"memory":"45Gi"},"requests":{"cpu":1,"memory":"45Gi"}}},"serviceAccount":{"create":false},"usePassword":true}` | Redis (Redis Graph)  for more information checkout full redis  chart options at [https://github.com/bitnami/charts/tree/redis/18.1.1/bitnami/redis](https://github.com/bitnami/charts/tree/redis/18.1.1/bitnami/redis) |

### Elastic / Redis secrets

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| secrets | object | `{"elastic":{"name":"search-elastic-secret","passwordKey":"password","user":"elastic","userKey":"username"},"redis":{"name":"search-redis-secret","passwordKey":"password"}}` | Secrets for passwords |

### Tranql

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| tranql | object | `{"enabled":true,"existingRedis":{"host":"","port":6379,"secret":"search-redis-secret","secretPasswordKey":"password"},"extraEnv":[{"name":"WEB_PATH_PREFIX","value":"/tranql"}],"gunicorn":{"workerCount":1,"workerTimeout":1600},"redis":{"enabled":false},"resources":{"limits":{"cpu":2,"memory":"2G"},"requests":{"cpu":"500m","memory":"2G"}},"webPrefix":"/tranql"}` | Tranql API configuration. Please refer to [https://github.com/helxplatform/tranql-chart/tree/main](https://github.com/helxplatform/tranql-chart/tree/main) for more details. |

### Dug (Helx) UI

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| ui | object | `{"config":{"analytics":{"enabled":false},"brand_description":{"html":"<html></html>"},"brand_name":"","hidden_result_tabs":"cdes","meta":{"description":"Dug semantic search","title":"Dug semantic search"},"search":{"enabled":"true","url":""},"support":{"faqs_url":"","help_portal_url":"","user_guide_url":""},"tranql_enabled":"true","tranql_url":"","workspaces":{"enabled":"false"}},"enabled":false}` | Dug search UI configuration please refer to [https://github.com/helxplatform/ui-chart/tree/master](https://github.com/helxplatform/ui-chart/tree/master) for more options |

### Other Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| airflow.airflowVersion | string | `"3.1.1"` |  |
| airflow.apiServer.resources.limits.cpu | int | `1` |  |
| airflow.apiServer.resources.limits.memory | string | `"2Gi"` |  |
| airflow.config.api.auth_backends | string | `"airflow.api.auth.backend.basic_auth"` |  |
| airflow.config.core.internal_api_secret_key | string | `"{{ .Values.webserverSecretKey }}"` |  |
| airflow.dagProcessor.enabled | bool | `true` |  |
| airflow.dagProcessor.logGroomerSidecar.enabled | bool | `false` |  |
| airflow.dagProcessor.resources.limits.cpu | int | `2` |  |
| airflow.dagProcessor.resources.limits.memory | string | `"2Gi"` |  |
| airflow.dags.gitSync.branch | string | `"main"` |  |
| airflow.dags.gitSync.enabled | bool | `true` |  |
| airflow.dags.gitSync.repo | string | `"https://github.com/helxplatform/roger.git"` |  |
| airflow.dags.gitSync.subPath | string | `"dags"` |  |
| airflow.dags.persistence.enabled | bool | `false` |  |
| airflow.data.metadataConnection.pass | string | `"postgres"` |  |
| airflow.defaultAirflowRepository | string | `"airflow"` |  |
| airflow.executor | string | `"KubernetesExecutor"` |  |
| airflow.extraEnv | string | `"- name: ROGER_LAKEFS__CONFIG_ENABLED\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: lakefs_enabled\n- name: ROGER_LAKEFS__CONFIG_HOST\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: lakefs_host\n- name: ROGER_LAKEFS__CONFIG_ACCESS__KEY__ID\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: lakefs_access_key_id\n- name: ROGER_LAKEFS__CONFIG_SECRET__ACCESS__KEY\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: lakefs_secret_access_key\n- name: ROGER_LAKEFS__CONFIG_BRANCH\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: lakefs_branch\n- name: ROGER_LAKEFS__CONFIG_REPO\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: lakefs_repo\n- name: ROGER_ANNOTATION_NORMALIZER\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: normalizer_url\n- name: ROGER_ANNOTATION_ANNOTATOR__TYPE\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_type\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_MONARCH_URL\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_monarch_url\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_CLASSIFICATION__URL\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_classification_url\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_ANNOTATOR__URL\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_annotator_url\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_ENABLED\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_bagel_enabled\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_URL\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_bagel_url\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_PROMPT\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_bagel_prompt\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_LLM__ARGS_LLM__MODEL__NAME\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_bagel_llm_model_name\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_LLM__ARGS_ORGANIZATION\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_bagel_llm_organization\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_LLM__ARGS_ACCESS__KEY\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_bagel_llm_access_key\n- name: ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_SCORE__THRESHOLD\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: annotator_sapbert_score_threshold\n- name: ROGER_ANNOTATION_SYNONYM__SERVICE\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: synonymizer_url\n- name: ROGER_DATA_DIR\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: data_directory\n- name: ROGER_DUG__INPUTS_DATA__SETS\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: input_sets\n- name: ROGER_ELASTICSEARCH_HOST\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-elastic-config\"\n      key: host\n- name: ROGER_ELASTICSEARCH_PASSWORD\n  valueFrom:\n    secretKeyRef:\n      name: \"{{ .Release.Name }}-elastic-secret\"\n      key: password\n- name: ROGER_ELASTICSEARCH_USERNAME\n  valueFrom:\n    secretKeyRef:\n      name: \"{{ .Release.Name }}-elastic-secret\"\n      key: username\n- name: ROGER_REDISGRAPH_HOST\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-redis-config\"\n      key: host\n- name: ROGER_REDISGRAPH_GRAPH\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-redis-config\"\n      key: graph\n- name: ROGER_REDISGRAPH_PASSWORD\n  valueFrom:\n    secretKeyRef:\n      name: \"{{ .Release.Name }}-redis-secret\"\n      key: password\n- name: ROGER_REDISGRAPH_PORT\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-redis-config\"\n      key: port\n- name: ROGER_S3_ACCESS__KEY\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: s3_access_key\n- name: ROGER_S3_BUCKET\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: s3_bucket\n- name: ROGER_S3_HOST\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: s3_host\n- name: ROGER_S3_SECRET__KEY\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: s3_secret_key\n- name: ROGER_KGX_DATA__SETS\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: kgx_data_sets\n- name: ROGER_INDEXING_NODE__TO__ELEMENT__QUERIES_ENABLED\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: node_to_queries_enabled\n- name: ROGER_INDEXING_ELEMENT__MAPPING\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: element_mappings\n- name: ROGER_ELASTICSEARCH_NBOOST__HOST\n  value: nboost $ TODO compute this\n- name: ROGER_INDEXING_TRANQL__ENDPOINT\n  valueFrom:\n    configMapKeyRef:\n      name: \"{{ .Release.Name }}-data-config\"\n      key: tranql_endpoint\n- name: AIRFLOW__KUBERNETES_EXECUTOR__DELETE_WORKER_PODS\n  value: \"FALSE\"\n- name: \"AIRFLOW__LOGGING__LOGGING_LEVEL\"\n  value: \"DEBUG\"\n- name: \"AIRFLOW__LOGGING__BASE_LOG_FOLDER\"\n  value: \"/opt/airflow/share/logs\"\n- name: \"AIRFLOW__WEBSERVER__APPLICATION_ROOT\"\n  value: \"/airflow\"\n- name: ROGER_ELASTICSEARCH_SCHEME\n  value: \"https\"\n- name: ROGER_ELASTICSEARCH_CA__PATH\n  value: \"/opt/certs/es.crt\"\n"` |  |
| airflow.images.airflow.repository | string | `"containers.renci.org/helxplatform/airflow"` |  |
| airflow.images.airflow.tag | string | `"3.1.1"` |  |
| airflow.postgresql.auth.password | string | `"postgres"` |  |
| airflow.postgresql.auth.postgresPassword | string | `"postgres"` |  |
| airflow.postgresql.image.registry | string | `"containers.renci.org"` |  |
| airflow.postgresql.image.repository | string | `"vgl/postgres-alpine"` |  |
| airflow.postgresql.image.tag | string | `"18.0.1"` |  |
| airflow.redis.enabled | bool | `false` |  |
| airflow.redis.serviceAccount.create | bool | `false` |  |
| airflow.scheduler.env[0].name | string | `"AIRFLOW__CORE__EXECUTOR"` |  |
| airflow.scheduler.env[0].value | string | `"KubernetesExecutor"` |  |
| airflow.scheduler.livenessProbe.command[0] | string | `"bash"` |  |
| airflow.scheduler.livenessProbe.command[1] | string | `"-c"` |  |
| airflow.scheduler.livenessProbe.command[2] | string | `"airflow jobs check --job-type SchedulerJob --hostname \"$(hostname)\"\n"` |  |
| airflow.scheduler.logGroomerSidecar.enabled | bool | `false` |  |
| airflow.scheduler.resources.limits.cpu | int | `1` |  |
| airflow.scheduler.resources.limits.memory | string | `"2Gi"` |  |
| airflow.scheduler.startupProbe.command[0] | string | `"bash"` |  |
| airflow.scheduler.startupProbe.command[1] | string | `"-c"` |  |
| airflow.scheduler.startupProbe.command[2] | string | `"airflow jobs check --job-type SchedulerJob --hostname \"$(hostname)\"\n"` |  |
| airflow.statsd.enabled | bool | `false` |  |
| airflow.triggerer.enabled | bool | `false` |  |
| airflow.volumeMounts[0].mountPath | string | `"/opt/airflow/share/data"` |  |
| airflow.volumeMounts[0].name | string | `"airflow-data"` |  |
| airflow.volumeMounts[1].mountPath | string | `"/opt/airflow/share/logs"` |  |
| airflow.volumeMounts[1].name | string | `"airflow-logs"` |  |
| airflow.volumeMounts[2].mountPath | string | `"/opt/certs/es.crt"` |  |
| airflow.volumeMounts[2].name | string | `"es-cert"` |  |
| airflow.volumeMounts[2].subPath | string | `"ca.crt"` |  |
| airflow.volumes[0].name | string | `"airflow-data"` |  |
| airflow.volumes[0].persistentVolumeClaim.claimName | string | `"search-data"` |  |
| airflow.volumes[1].name | string | `"es-cert"` |  |
| airflow.volumes[1].secret.defaultMode | int | `511` |  |
| airflow.volumes[1].secret.secretName | string | `"elasticsearch-master-certs"` |  |
| airflow.volumes[2].name | string | `"airflow-logs"` |  |
| airflow.volumes[2].persistentVolumeClaim.claimName | string | `"search-airflow-logs"` |  |
| airflow.webServer.defaultUser.email | string | `"admin@example.com"` |  |
| airflow.webServer.defaultUser.enabled | bool | `true` |  |
| airflow.webServer.defaultUser.firstName | string | `"admin"` |  |
| airflow.webServer.defaultUser.lastName | string | `"user"` |  |
| airflow.webServer.defaultUser.password | string | `"admin"` |  |
| airflow.webServer.defaultUser.role | string | `"Admin"` |  |
| airflow.webServer.defaultUser.username | string | `"admin"` |  |
| airflow.webserverSecretKey | string | `"your-secret-key-here"` |  |
| airflow.workers.logGroomerSidecar.enabled | bool | `false` |  |
| airflow.workers.replicas | int | `0` |  |
| fullnameOverride | string | `""` |  |
| nameOverride | string | `""` |  |