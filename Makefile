.PHONY: build
build: 
	@docker build -t devops-configuration-generator-api .
	@echo "Docker image built successfully: devops-configuration-generator-api"
	@docker volume create devops-configuration-generator-api-volume
	@echo "Docker volume created successfully: devops-configuration-generator-api-volume"

.PHONY: run
run:
	@docker run -dp 8000:8000 --name devops-configuration-generator-api devops-configuration-generator-api
	@echo "Docker container started successfully: devops-configuration-generator-api"

.PHONY: stop
stop:
	@docker stop devops-configuration-generator-api
	@echo "Docker container stopped successfully: devops-configuration-generator-api"

.PHONY: start
start:
	@docker start devops-configuration-generator-api
	@echo "Docker container started successfully: devops-configuration-generator-api"

.PHONY: restart
restart:
	@docker restart devops-configuration-generator-api
	@echo "Docker container restarted successfully: devops-configuration-generator-api"

.PHONY: rm
rm:
	@docker rm -f devops-configuration-generator-api
	@echo "Docker container removed successfully: devops-configuration-generator-api"

.PHONY: clean
clean:
	@docker rmi devops-configuration-generator-api
	@echo "Docker image removed successfully: devops-configuration-generator-api"