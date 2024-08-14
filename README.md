# search

A Helm chart for Helx Search components. This chart installs Dug, TranQL , Airflow and Redis.

### Architecture of Search Chart

For full architeture overview please refer to our documentation [here](https://dug.readthedocs.io/en/latest/architecture/roger/).

![Version: 5.2.0](https://img.shields.io/badge/Version-5.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: v2.13.2](https://img.shields.io/badge/AppVersion-v2.13.2-informational?style=flat-square) 


## Values

### Airflow

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| airflow.airflow.config | object | `{"AIRFLOW__CORE__LOAD_EXAMPLES":"FALSE","AIRFLOW__KUBERNETES__DELETE_WORKER_PODS":"TRUE","AIRFLOW__LOGGING_LEVEL":"INFO","AIRFLOW__SCHEDULER__SCHEDULE_AFTER_TASK_EXECUTION":"FALSE","AIRFLOW__WEBSERVER__BASE_URL":""}` | Airflow config |
| airflow.airflow.extraEnv | list | `[{"name":"ROGER_LAKEFS__CONFIG_ENABLED","valueFrom":{"configMapKeyRef":{"key":"lakefs_enabled","name":"search-data-config"}}},{"name":"ROGER_LAKEFS__CONFIG_HOST","valueFrom":{"configMapKeyRef":{"key":"lakefs_host","name":"search-data-config"}}},{"name":"ROGER_LAKEFS__CONFIG_ACCESS__KEY__ID","valueFrom":{"configMapKeyRef":{"key":"lakefs_access_key_id","name":"search-data-config"}}},{"name":"ROGER_LAKEFS__CONFIG_SECRET__ACCESS__KEY","valueFrom":{"configMapKeyRef":{"key":"lakefs_secret_access_key","name":"search-data-config"}}},{"name":"ROGER_LAKEFS__CONFIG_BRANCH","valueFrom":{"configMapKeyRef":{"key":"lakefs_branch","name":"search-data-config"}}},{"name":"ROGER_LAKEFS__CONFIG_REPO","valueFrom":{"configMapKeyRef":{"key":"lakefs_repo","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_NORMALIZER","valueFrom":{"configMapKeyRef":{"key":"normalizer_url","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__TYPE","valueFrom":{"configMapKeyRef":{"key":"annotator_type","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_MONARCH_URL","valueFrom":{"configMapKeyRef":{"key":"annotator_monarch_url","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_CLASSIFICATION__URL","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_classification_url","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_ANNOTATOR__URL","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_annotator_url","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_ENABLED","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_bagel_enabled","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_URL","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_bagel_url","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_PROMPT","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_bagel_prompt","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_LLM__ARGS_LLM__MODEL__NAME","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_bagel_llm_model_name","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_LLM__ARGS_ORGANIZATION","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_bagel_llm_organization","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_BAGEL_LLM__ARGS_ACCESS__KEY","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_bagel_llm_access_key","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_ANNOTATOR__ARGS_SAPBERT_SCORE__THRESHOLD","valueFrom":{"configMapKeyRef":{"key":"annotator_sapbert_score_threshold","name":"search-data-config"}}},{"name":"ROGER_ANNOTATION_SYNONYM__SERVICE","valueFrom":{"configMapKeyRef":{"key":"synonymizer_url","name":"search-data-config"}}},{"name":"ROGER_DATA_DIR","valueFrom":{"configMapKeyRef":{"key":"data_directory","name":"search-data-config"}}},{"name":"ROGER_DUG__INPUTS_DATA__SETS","valueFrom":{"configMapKeyRef":{"key":"input_sets","name":"search-data-config"}}},{"name":"ROGER_DUG__INPUTS_DATA__SOURCE","valueFrom":{"configMapKeyRef":{"key":"data_source","name":"search-data-config"}}},{"name":"ROGER_ELASTICSEARCH_HOST","valueFrom":{"configMapKeyRef":{"key":"host","name":"search-elastic-config"}}},{"name":"ROGER_ELASTICSEARCH_PASSWORD","valueFrom":{"secretKeyRef":{"key":"password","name":"search-elastic-secret"}}},{"name":"ROGER_ELASTICSEARCH_USERNAME","valueFrom":{"secretKeyRef":{"key":"username","name":"search-elastic-secret"}}},{"name":"ROGER_ELASTICSEARCH_SCHEME","value":"https"},{"name":"ROGER_ELASTICSEARCH_CA__PATH","value":"/opt/certs/es.crt"},{"name":"ROGER_REDISGRAPH_HOST","valueFrom":{"configMapKeyRef":{"key":"host","name":"search-redis-config"}}},{"name":"ROGER_REDISGRAPH_GRAPH","valueFrom":{"configMapKeyRef":{"key":"graph","name":"search-redis-config"}}},{"name":"ROGER_REDISGRAPH_PASSWORD","valueFrom":{"secretKeyRef":{"key":"password","name":"search-redis-secret"}}},{"name":"ROGER_REDISGRAPH_PORT","valueFrom":{"configMapKeyRef":{"key":"port","name":"search-redis-config"}}},{"name":"ROGER_S3_ACCESS__KEY","valueFrom":{"configMapKeyRef":{"key":"s3_access_key","name":"search-data-config"}}},{"name":"ROGER_S3_BUCKET","valueFrom":{"configMapKeyRef":{"key":"s3_bucket","name":"search-data-config"}}},{"name":"ROGER_S3_HOST","valueFrom":{"configMapKeyRef":{"key":"s3_host","name":"search-data-config"}}},{"name":"ROGER_S3_SECRET__KEY","valueFrom":{"configMapKeyRef":{"key":"s3_secret_key","name":"search-data-config"}}},{"name":"ROGER_KGX_DATA__SETS","valueFrom":{"configMapKeyRef":{"key":"kgx_data_sets","name":"search-data-config"}}},{"name":"ROGER_INDEXING_NODE__TO__ELEMENT__QUERIES_ENABLED","valueFrom":{"configMapKeyRef":{"key":"node_to_queries_enabled","name":"search-data-config"}}},{"name":"ROGER_INDEXING_ELEMENT__MAPPING","valueFrom":{"configMapKeyRef":{"key":"element_mappings","name":"search-data-config"}}},{"name":"ROGER_ELASTICSEARCH_NBOOST__HOST","value":"nboost $ TODO compute this"},{"name":"ROGER_INDEXING_TRANQL__ENDPOINT","valueFrom":{"configMapKeyRef":{"key":"tranql_endpoint","name":"search-data-config"}}},{"name":"AIRFLOW__CORE__FERNET_KEY","valueFrom":{"secretKeyRef":{"key":"fernet-key","name":"airflow-config-secrets"}}}]` | Environment variables used by roger. For full option please refer to [Roger config.yaml](https://github.com/helxplatform/roger/blob/develop/dags/roger/config/config.yaml) |
| airflow.airflow.extraVolumeMounts | list | `[{"mountPath":"/opt/airflow/share/data","name":"airflow-data"},{"mountPath":"/opt/certs/es.crt","name":"es-cert","subPath":"ca.crt"}]` | These volumes are mounted on all airflow pods , aswell as executor pods. |
| airflow.airflow.extraVolumes | list | `[{"name":"airflow-data","persistentVolumeClaim":{"claimName":"search-data"}},{"name":"es-cert","secret":{"defaultMode":511,"secretName":"elasticsearch-master-certs"}}]` | Volumes section for all airflow pods, including executor pods. |
| airflow.airflow.image | object | `{"pullPolicy":"Always","repository":"containers.renci.org/helxplatform/roger","tag":"latest"}` | Airflow custom image, that contains dug and other libraries installed. |
| airflow.airflow.kubernetesPodTemplate | object | `{"resources":{"limits":{"cpu":2,"memory":"16G"},"requests":{"cpu":2,"memory":"16G"}}}` | Executor pod configuration |
| airflow.airflow.usersUpdate | bool | `true` | Update user table on deployments |
| airflow.dags | object | `{"gitSync":{"branch":"main","enabled":true,"repo":"https://github.com/helxplatform/roger.git","repoSubPath":"dags","revision":"HEAD","syncWait":60}}` | Defines the location of dags |
| airflow.enabled | bool | `true` | Enable airflow deployment |
| airflow.scheduler | object | `{"logCleanup":{"enabled":true},"resources":{"limits":{"cpu":2,"memory":"4G"},"requests":{"cpu":2,"memory":"4G"}}}` | Airflow scheduler config |
| airflow.web | object | `{"resources":{"limits":{"cpu":3,"ephemeral-storage":"1G","memory":"4G"},"requests":{"cpu":3,"ephemeral-storage":"1G","memory":"4G"}}}` | Airflow webui config |
| persistence | object | `{"pvcSize":"32Gi","storageClass":""}` | Airflow storage for executors , scheduler and web pods. This is a shared volume. |

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
| chat | object | `{"apiPort":8080,"config":{"api_url":"http://koios-llama-koios-chart.ner/"},"enabled":false,"image":{"repository":"containers.renci.org/helxplatform/dug-chatbot","tag":"v0.0.2"},"replicas":1,"resources":{"limits":{"cpu":1,"memory":"1Gi"}},"root_path":"/chat","service":{"type":"ClusterIP"}}` | Configuration option for Dug chatbot UI |

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
| config.lakefs.access_key | string | `""` | Lakefs access key |
| config.lakefs.branch | string | `""` | Branch to write output files to. |
| config.lakefs.enable | bool | `false` | Enables lakefs usage for input and output on data ingest. |
| config.lakefs.host | string | `""` | Lakefs host address |
| config.lakefs.repo | string | `""` | Lakefs repo to write outputs to |
| config.lakefs.secret_key | string | `""` | Lakefs secret key |
| config.node_to_queries_enabled | string | `"false"` | Enables CDE extraction from Knowledge graph. |

### Elasticsearch

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| elasticsearch | object | `{"clusterHealthCheckParams":"wait_for_status=green&timeout=1s","enabled":true,"esJavaOpts":"-Xmx6g -Xms6g -Dlog4j2.disable.jmx=true -Dlog4j2.formatMsgNoLookups=true","extraEnvs":[{"name":"ELASTIC_PASSWORD","valueFrom":{"secretKeyRef":{"key":"password","name":"search-elastic-secret"}}},{"name":"ELASTIC_USERNAME","valueFrom":{"secretKeyRef":{"key":"username","name":"search-elastic-secret"}}},{"name":"LOG4J_FORMAT_MSG_NO_LOOKUPS","value":"true"}],"imageTag":"8.5.2","maxUnavailable":0,"replicas":3,"resources":{"limits":{"cpu":1,"ephemeral-storage":"256Mi","memory":"8G"},"requests":{"cpu":1,"ephemeral-storage":"256Mi","memory":"8G"}},"secret":{"enabled":false},"sysctlInitContainer":{"enabled":false}}` | Elastic search for more information checkout full elasticsearch chart options at [https://github.com/elastic/helm-charts/tree/v8.5.1](https://github.com/elastic/helm-charts/tree/v8.5.1) |

### Ingress

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| ingress | object | `{"annotations":{"nginx.ingress.kubernetes.io/cors-allow-headers":"Content-Type","nginx.ingress.kubernetes.io/cors-allow-methods":"POST, OPTIONS","nginx.ingress.kubernetes.io/cors-allow-origin":"*","nginx.ingress.kubernetes.io/enable-cors":"true"},"basicAuth":{"enabled":false,"password":"","username":""},"className":"","enabled":false,"hosts":[{"host":"chart-example.local"}],"labels":{},"pathType":"Prefix","paths":[{"name":"ui","path":"/","port":80,"prepend":true},{"name":"web","path":"/airflow","port":8080,"prepend":true},{"name":"tranql","path":"/tranql","port":8081,"prepend":true}],"rewrite_paths":[{"name":"api","path":"/search-api(/|$)(.*)","port":5551,"prepend":true}],"tls":[]}` | Values to enable ingress |

### Redis

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| redis | object | `{"auth":{"existingSecret":"search-redis-secret","existingSecretPasswordKey":"password"},"clusterDomain":"cluster.local","enabled":true,"image":{"repository":"falkordb/falkordb","tag":"edge"},"master":{"command":"","extraFlags":["--loadmodule","/FalkorDB/bin/src/falkordb.so","THREAD_COUNT","8","OMP_THREAD_COUNT","16"],"livenessProbe":{"enabled":false},"persistence":{"size":"50Gi"},"readinessProbe":{"enabled":true,"failureThreshold":1,"periodSeconds":1},"resources":{"limits":{"cpu":2,"memory":"45Gi"},"requests":{"cpu":1,"memory":"45Gi"}}},"replica":{"autoscaling":{"enabled":true,"maxReplicas":1,"minReplicas":1,"targetCPU":100},"extraFlags":["--loadmodule","/FalkorDB/bin/src/falkordb.so","THREAD_COUNT","8","OMP_THREAD_COUNT","16"],"livenessProbe":{"enabled":false},"persistence":{"size":"50G"},"readinessProbe":{"enabled":true,"failureThreshold":1,"periodSeconds":1,"successThreshold":5},"resources":{"limits":{"cpu":2,"memory":"45Gi"},"requests":{"cpu":1,"memory":"45Gi"}}},"usePassword":true}` | Redis (Redis Graph)  for more information checkout full redis  chart options at [https://github.com/bitnami/charts/tree/redis/18.1.1/bitnami/redis](https://github.com/bitnami/charts/tree/redis/18.1.1/bitnami/redis) |

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
| fullnameOverride | string | `""` |  |
| nameOverride | string | `""` |  |