curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://us-central1-aiplatform.googleapis.com/v1/projects/ff-kubeflow-dev/locations/us-central1/featurestores/dragon_fs?force=true"

