# syntax=docker/dockerfile:1
FROM albumsolutions/album:0.1.0
COPY . /tmp
RUN ["/bin/bash","-c", "sed -i '$ d' /album/docker/entrypoint.sh ; source /album/docker/entrypoint.sh ; album install /tmp/album_template-bdv_0.1.0-SNAPSHOT.zip; sed -i 's/<solution call>/album:template-bdv:0.1.0-SNAPSHOT/' /album/docker/entrypoint-solution.sh"]
ENTRYPOINT ["/album/docker/entrypoint-solution.sh"]
CMD [""]
LABEL MAINTAINER=Your name

