ARG ELK_VERSION

# https://www.docker.elastic.co/
FROM docker.elastic.co/logstash/logstash:${ELK_VERSION}

RUN logstash-plugin install logstash-filter-json
RUN logstash-plugin install --no-verify logstash-input-syslog
