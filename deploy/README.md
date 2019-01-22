#Pre-requisite: Install `kubectl`, `gcloud`

- brew install kubernetes-helm
- brew install kubernetes-cli
- brew cask install virtualbox

## Deploy to GCP Kubernetes Engine

- use `kubectl` to set the cluster
      kubectl config set-cluster <cluster-info> or keep .kube config - set the value
- `helm init` to add Helm's Tiller to the cluster
- `helm package rest-app --debug`
- `helm install  rest-app-0.1.0.tgz`



