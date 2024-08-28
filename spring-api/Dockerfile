FROM openjdk:17-jdk-alpine
# VOLUME /tmp
ARG DEPENDENCY=target/dependency
COPY target/dependency/BOOT-INF/lib /app/lib
COPY target/dependency/META-INF /app/META-INF
COPY target/dependency/BOOT-INF/classes /app
ENTRYPOINT ["java", "-cp", "app:app/lib/*", "com.ericsson.springapi.SpringApiApplication"]