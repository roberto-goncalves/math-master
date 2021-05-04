MATH-MASTER

Welcome! This API provides calculations on math functions:

- ackermann(n,m)
- factorial(n)
- fibonacci(n)

But not only that! It also provides the whole stack for your development using docker-compose! Those tools are in the stack:

- kibana - elasticsearch data visualization tool
- elasticsearch - data handler and cluster for indexing
- logstash - data handler to send logs to elasticsearch
- logspout - it reads the docker API and send all logs on sysout to logstash

Cool, right? 

But it does not finish on that:

- The API code uses pylint and pytest, you can see it on the Dockerfile located on api's folder, pylint have a score following PEP8
recomendations, said that, the score goes to 0 to 10, and the code treshold for failure is 9
- pytest sets multiple tests (unity and functional) which the docker-compose build will fail if something is wrong with the code

Said that, let's begin!

You just need to install docker-compose and docker https://docs.docker.com/compose/install/ https://docs.docker.com/get-docker/

Then, go to the math_master root where you can see the docker-compose.yaml and just type:

docker-compose up

After that, if everything goes right with the code you will see that it will build and then start the execution, wait until LOGSTASH
says that it is completely started

After that, go to http://0.0.0.0:5601 and with elastic username and changeme password, log into elasticsearch, go to Kibana and set logstash-* as a data-source!

Then, just test the requests as you like:

oberto@roberto-mac math_ma

After that, if everything goes right with the code you will see that it will build and then start the execution, wait until LOGSTASH
says that it is completely started

After that, go to http://0.0.0.0:5601 and with elastic username and changeme password, log into elasticsearch, go to Kibana and set logstash-* as a data-source!

Then, just test the requests as you like:

curl -H "Content-Type: application/json" --request POST --data '{"n": 3, "m": 3}' http://0.0.0.0:5678/math/ackermann

curl -H "Content-Type: application/json" --request POST --data '{"n": 10}' http://0.0.0.0:5678/math/factorial

curl -H "Content-Type: application/json" --request POST --data '{"n":10}' http://0.0.0.0:5678/math/fibonacci

Then, as described on images folder, you should see it on kibana :)

Also, the structure:

math_master - api
|
|-app.py
|-instance (configutations)
|-logging_module (log_handler)
|-resources (math_functions)
|-tests (functional and unit)

math_master - images
- images of kibana running and architecture

math_master - elasticsearch
- Dockerfile along with configs

math_master - kibana
- Dockerfile along with configs

math_master - logstash
- Dockerfile along with configs

math_master - logspout
- Dockerfile along with configs


And, at last, how it supposed to be deployed on cloud?

We have a lot of IaaC tools to do it, but I'll just go with Pulumi, since we can develop it in python. So, basically, I would create a AWS EKS Cluster for ELK stack, with Kubernetes Services for scalling Elasticsearch.

After, I would create a separate cluster for math_master, since it is now, a small application it can grow a lot! 

And the Pipeline? Would use some git ops with Gitlab or Github pipeline :)

That's all folks!
