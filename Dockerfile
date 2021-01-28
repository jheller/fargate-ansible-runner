FROM ansible/ansible-runner:latest

WORKDIR /runner

COPY project/ project/
COPY env/ env/
COPY inventory/ inventory/
ADD runner_entry.sh /bin/runner_entry
RUN rm -f inventory/hosts
RUN pip3 install awscli boto3

ENTRYPOINT ["/bin/runner_entry"]
