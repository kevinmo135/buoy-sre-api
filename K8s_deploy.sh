#!/bin/bash
docker build --pull --rm -t buoy-sre-api .
kubectl apply -f webapi.dep.yaml
kubectl apply -f webapi.svc.yaml

NODEPORT=$(kubectl get svc -o json | jq -r .items[].spec.ports[].nodePort)
echo "=================================================="
echo "== WEBAPI is deployed on Port: $NODEPORT"
