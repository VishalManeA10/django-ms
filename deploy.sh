docker build -t python-ms-practice-test-1 .

docker tag python-ms-practice-test-1 us-phoenix-1.ocir.io/axqel8fpeyhe/python-ms-practice-test-1:vmane
docker push us-phoenix-1.ocir.io/axqel8fpeyhe/python-ms-practice-test-1:vmane
kubectl delete -f ./python-ms-deployment.yaml
kubectl apply -f ./python-ms-deployment.yaml