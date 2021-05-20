# [iDevOps.io](https://idevops.io/) Public Pipeline Library

This library was created to expedite the deployment of CI/CD oriented environments in a highly customizable manner. These libraries will allow you to create various tasks and processes based upon your specific needs in a way that has been tested and confirmed functional to eliminate guesswork and abstract you from the problems of implementation.

## How to use
- Guide
    - Import the available Pipeline JSON into your own AZDO Pipeline.
    - Create the necessary variables in vault to the values specific to your organization's needs.
    - Run and deploy AZDO runners using available Kubernetes manifests.
- Scripts
  - `Required Arguments` refers to the arguments needed to run said script *and* in which order to call the arguments.
    - Take docker_login as an example:

    | Script Name | Description | Required Arguments | Additional Arguments & Notes |
    | ----------- | ----------- | ------------------ | ---------------------------- |
    | docker_login | Log in to a Docker registry | `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `DOCKER_REGISTRY_URL` |
    - :heavy_check_mark: `docker_login DOCKER_USERNAME DOCKER_PASSWORD DOCKER_REGISTRY_URL`
      - Will work!
    - :x: `docker_login DOCKER_PASSWORD DOCKER_REGISTRY_URL DOCKER_USERNAME`
      - Will **not** work

## Scripts

| Script Name | Description | Required Arguments | Additional Arguments<br /> & Notes |
| ----------- | ----------- | ------------------ | ---------------------------------- |
| anchore_inline_scan | Pulls the specified docker image and anchore scans it | `DOCKER_IMAGE_NAME` |
| create_kubernetes_secret | Creates Kubernetes secrets from a JSON argument. The secret name defaulting to APP_NAME | `keys`, `APP_NAME` | The `keys` argument is passed in JSON format, with single quotes. ex: `create_kubernetes_secret '{ "APP_NAME":"Example", "APP_NAMESPACE":"production", "APP_PORT":"80" }' APP_NAME`
| docker_build | Builds a test and main Docker Image | `DOCKER_IMAGE_NAME` | `APPLICATION_PATH` |
| docker_connect<br />_container_to_network | Connects a container to a network | `NETWORK_NAME`, `CONTAINER` | `IP` is an additional argument you can pass. Referenced here in the [docker connect command](https://docs.docker.com/engine/reference/commandline/network_connect/) |
| docker_container_logs | Shows the logs of a container | `CONTAINER` |
| docker_disconnect<br />_container_from_network | Disconnect a container from a network | `NETWORK_NAME`, `CONTAINER` |
| docker_exec_into_container | Execs into the container | `CONTAINER` |
| docker_history_of_image | Shows the history of a Docker image | `IMAGE` |
| docker_inspect | Inspects the provided construct | `CONSTRUCT` | `CONSTRUCT`'s include images, containers, networks and volumes |
| docker_login | Log in to a Docker registry | `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `DOCKER_REGISTRY_URL` |
| docker_pause_all<br />_running_containers | Pauses all running containers |
| docker_prune_images | Prunes Docker images |
| docker_prune_networks | Prunes Docker networks |
| docker_prune_stopped_containers | Prunes Docker containers |
| docker_prune_volumes | Prunes Docker volumes |
| docker_pull_image | Pulls a Docker image | `DOCKER_IMAGE_NAME` | Might be required to be logged in beforehand |
| docker_push_image | Pushes a Docker image | `DOCKER_IMAGE_NAME` | Might be required to be logged in beforehand |
| docker_remove_all_images  | Removes **ALL** Docker images |
| docker_remove_image | Removes a Docker image | `IMAGE` |
| docker_remove_network | Removes a Docker network | `NETWORK_NAME` |
| docker_remove_volume | Removes a Docker volume | `VOLUME` |
| docker_rename_container | Renames an existing Docker container | `CONTAINER`, `NEW_CONTAINER_NAME` |
| docker_restart_all<br />_running_containers | Restarts all running Docker containers | | `TIME` is an additional argument you can pass. Adds the amount passed as seconds to wait for a stop before killing a container |
| docker_restart_container | Restarts a Docker container | `CONTAINER` | `TIME` is an additional argument you can pass. Adds the amount passed as seconds to wait for a stop before killing a container |
| docker_search_containers | Searches for a specified Docker container | `SEARCH_FOR_CONTAINER` |
| docker_search_images | Searches for a specified Docker image | `SEARCH_FOR_IMAGE` |
| docker_start_all_containers | Starts **ALL** Docker containers |
| docker_start_container | Starts a Docker container | `CONTAINER` |
| docker_stop_all_containers | Stops **ALL** Docker containers |
| docker_stop_and<br />_remove_all_containers | Stops and removes **ALL** Docker containers |
| docker_stop_and<br />_remove_container | Stops and removes a Docker container | `CONTAINER` |
| docker_stop_container | Stops a Docker container | `CONTAINER` |
| docker_unpause_containers | Un-pauses all paused Docker container |
| get_kubernetes_kubeconfig | Gets the kubeconfig for Azure using as aks get credentials | `RESOURCEGROUP_NAME`, `CLUSTER_NAME` |
| install_conda | Installs miniconda onto the Azure Runner if it isn't already installed and exports the PATH | | `SYSTEM_DEFAULT`<br />`WORKINGDIRECTORY` |
| install_jq_if_not_installed | Installs jq if not already installed |
| kubectl_get_logs_namespace | Gets the log of a Kubernetes namespace | `APP_NAMESPACE` |
| kubectl_install | Installs kubectl | `LIBRARY_PATH` |
| kubenetes_delete_stateful | Deletes a Kubernetes stateful set | `APP_NAME`, `APP_NAMESPACE` |
| kubernetes_apply_build | Applies a Kubernetes manifest | `APP_NAME`, `filename`, `APP_NAMESPACE` |
| kubernetes_background_proxycurl | Starts a backgrounded Kubectl proxy in order to curl Elasticsearch deployed in Docker through the Kubernetes proxy running in TMUX. | `APP_NAME` |
| kubernetes_check_rollout | Checks the rollout status of a Kubernetes deployment | `APP_NAME`, `APP_NAMESPACE`, `DEPLOYMENT_TYPE` |
| kubernetes_create_clusterrole_GLW | Creates a Kubernetes cluster role for the provided resource name | `CLUSTERROLE_NAME`, `RESOURCE_TYPE`, `RESOURCEGROUP_NAME`, `verb` | The `verb` argument determines the [permissions](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) for the cluster role and the argument should be provided like: `get,list,watch`. `RESOURCE_TYPE` is the resource the rule is applied to, `RESOURCEGROUP_NAME` is the Resource in the white list that the rule applies to, repeat this flag for multiple items. [Documentation](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#-em-clusterrole-em-)
| kubernetes_create_docker_secret | Deletes the existing Kubernetes Docker secret and creates a new secret | `APP_NAME`, `APP_NAMESPACE`, `key`, `value` | The `key`, `value` arguments are used to create the new secret key: value pair.
| kubernetes_create<br />_fromfilename_namespace | Creates a Kubernetes manifest, for a provided namespace | `APP_NAMESPACE`, `FILENAME` |
| kubernetes_create_namespace | Creates a Kubernetes namespace | `APP_NAMESPACE` |
| kubernetes_create_service | Creates a Kubernetes service for the provided pod and app | `APP_NAME`, `SERVICE_TYPE`, `APP_NAMESPACE`, `LABEL_KEY`, `LABEL_VALUE`, `PORT`, `TARGET_PORT` | `LABEL_KEY` and `LABEL_VALUE` are used to grab the pod name |
| kubernetes_delete_deployment | Deletes a Kubernetes deployment | `APP_NAME`, `APP_NAMESPACE` |
| kubernetes_delete_pods<br />_and_services | Deletes a Kubernetes pod and service | `LABEL_KEY`, `LABEL_VALUE`, `APP_NAMESPACE` |
| kubernetes_delete_pv | Deletes a Kubernetes persistent volume for the provided app and namespace | `APP_NAME`, `APP_NAMESPACE` | 
| kubernetes_delete_pvc | Deletes a Kubernetes persistent volume claim for the provided app and namespace | `APP_NAME`, `APP_NAMESPACE` |
| kubernetes_delete_secret | Deletes a Kubernetes secret for the provided app and namespace | `APP_NAME`, `APP_NAMESPACE` |
| kubernetes_delete_service | Deletes a Kubernetes service | `SERVICE_NAME` |
| kubernetes_delete_statefulset | Deletes a Kubernetes stateful set | `STATEFULSET_NAME` | 
| kubernetes_delete_yaml | Deletes the specified yaml in Kubernetes | `YAML_NAME` |
| kubernetes_events_for_pod | Gets the events for a Kubernetes pod | `APP_NAMESPACE`, `LABEL_KEY`, `LABEL_VALUE` | `LABEL_KEY` and `LABEL_VALUE` are used to grab the Pod |
| kubernetes_exec_into_pod | Execs into a Kubernetes pod | `POD_NAME`, `APP_NAMESPACE` | 
| kubernetes_forward<br />_local_port_to_a_pod_or_service | Port forwards an app or service | `APP_OR_SERVICE_NAME`, `PORTFROM`, `PORTTO`, `APP_NAMESPACE` |
| kubernetes_get_pod_name | Gets the name of a Kubernetes Pod using `LABEL_KEY` and `LABEL_VALUE` | `LABEL_KEY`, `LABEL_VALUE`, `APP_NAMESPACE` | `LABEL_KEY` & `LABEL_VALUE` are the search parameters. There is a `-l` argument that matches the labels. 
| kubernetes_ingress | Creates an ingress with specified app name, path, service type, port and secret | `APP_NAME`, `PATH`, `SERVICE_TYPE`, `PORT`, `SECRET` |
| kubernetes_list_non_running_pods | Lists Kubernetes pods that aren't running |
| kubernetes_retrieve_yaml<br />_pod_allnamespaces | Retrieves a yaml from a specified Kubernetes pod under all namespaces | `POD_NAME` |
| kubernetes_retrieve_yaml<br />_pod_specificnamespace | Retrieves a yaml from a specified Kubernetes pod in a specified namespace | `APP_NAMESPACE`, `POD_NAME` |
| kubernetes_scale_deployment | Scales a Kubernetes deployment to the specified amount, under a specified namespace | `DEPLOYMENT_NAME`, `SCALE_TO_AMOUNT`, `APP_NAMESPACE` |
| kubernetes_scale_resource_in_yaml | Scales the resource in a Kubernetes yaml, under a specified namespace | `YAML`, `SCALE_TO_AMOUNT`, `APP_NAMESPACE` |
| kubernetes_search_pods | Uses `awk` to search for a given pod, and returns a list of matching results | `POD_NAME`, `APP_NAMESPACE` | `POD_NAME` *here* does not need to be the exact name |
| kubernetes_search_services | Uses `awk` to search for a given service, and returns a list of matching results | `SERVICE_NAME`, `APP_NAMESPACE` | `SERVICE_NAME` *here* does not need to be the exact name |
| kubernetes_show_all<br />_objects_in_a_namespace | Shows all the objects in a given namespace | `APP_NAMESPACE` |
| start_sonar | Checks if SonarQube is running, and runs SonarQube if it isn't | 
| sonar_scan | Ensures SonarQube is running. Sets up the `sonar-project.properties` file. Calls `sonar_create_project.py` to make a project inside SonarQube, scans the files and then calls `sonar_project_status.py` to get a report in pretty table. | `SYSTEM_DEFAULT`<br />`WORKINGDIRECTORY`, `APP_NAME` | Will require the use of `install_conda` beforehand. |
| sonarqube_create_project.py | Creates a project in SonarQube | | `APP_NAME` |
| sonar_project_status.py | Uses API/issues to get a report from SonarQube | | `APP_NAME` |
| source_vault_secrets | Grabs variables in Vault and changes them to environment variables | | `SYSTEM_DEFAULT`<br />`WORKINGDIRECTORY` <br /> This script is also used to `export` extra variables for use in the pipeline. |
| vault_to_env.py | The script used in `source_vault_secrets` to grab variables |
| vault_variable_replacement.py | Replaces variables in the templated yaml: `/manifests/deployment.template.yml` and creates a `deployment.yml`. | | Syntax for variables in the template are formatted like: `-=APP_NAME=-`, and replaced with the Vault value of `APP_NAME` |
| template_variable_replacement | Used to call the `vault_variable_replacement.py` | |`SYSTEM_DEFAULT`<br />`WORKINGDIRECTORY` |

### Common Variable Descriptions

- [Azure Predefined Variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/build/variables?view=azure-devops&tabs=yaml)
- [Azure Classic Release & Artifact Variables](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/variables?view=azure-devops&tabs=batch)

| Argument Name | Description |
| ------------- | ----------- |
| APPLICATION_PATH | Is built out of two predefined Azure variables. SYSTEM_DEFAULTWORKINGDIRECTORY & RELEASE_PRIMARYARTIFACTSOURCEALIAS `APPLICATION_PATH=${SYSTEM_DEFAULTWORKINGDIRECTORY}/${RELEASE_PRIMARYARTIFACTSOURCEALIAS}` |
| APP_NAME | Is the name given to the current App being worked on |
| CONTAINER, IMAGE, NETWORK_NAME, VOLUME | Refers to a specific Docker container name or ID, Image name or ID, etc. |
| DOCKER_IMAGE_NAME | Different than just a Docker image name. This variable contains: `DOCKER_IMAGE_NAME=${DOCKER_REGISTRY_URL}/${APP_NAME}:${VERSION}` |
| DOCKER_USERNAME | Username to Docker Registry |
| DOCKER_PASSWORD | Password to Docker Registry |
| DOCKER_REGISTRY_URL | URL to your Docker Registry |
| LABEL_KEY, LABEL_VALUE | `LABEL_KEY` will the App, `LABEL_VALUE` is the name of App |
| LIBRARY_PATH | Is the path to our pipelines library in Azure. `LIBRARY_PATH=${SYSTEM_DEFAULTWORKINGDIRECTORY}/_idevops_pipeline_libraries` |
| POD_NAME | Refers to the specific Pod name in Kubernetes. Can we grabbed by using `kubernetes_get_pod_name` or `kubernetes_search_pods` |
| RESOURCEGROUP_NAME | Refers to your resource group in Azure |
| SERVICE_TYPE | Refers to the service type in Kubernetes|
| SYSTEM_DEFAULTWORKINGDIRECTORY | A Predefined Azure variable |
| YAML_NAME / YAML| Name of the yaml manifest file. ex: `manifest.yaml` |
| filename / FILENAME | The specified filename the script needs to reference. Usually a yaml file also. |