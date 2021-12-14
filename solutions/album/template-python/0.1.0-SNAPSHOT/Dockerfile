# syntax=docker/dockerfile:1
FROM albumsolutions/album:0.1.0
COPY . /tmp
RUN ["/bin/bash","-c", "sed -i '$ d' /album/src/album/docker/entrypoint.sh ; source /album/src/album/docker/entrypoint.sh ; album install /tmp/album_template-python_0.1.0-SNAPSHOT.zip; sed -i 's/<solution call>/album:template-python:0.1.0-SNAPSHOT/' /album/src/album/docker/entrypoint-solution.sh"]
ENTRYPOINT ["/album/src/album/docker/entrypoint-solution.sh"]
CMD [""]
LABEL MAINTAINER=Your name

