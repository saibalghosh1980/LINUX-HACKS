#!/bin/sh
COMMAND_TO_RUN='docker service update --force ' #Replace it with your favourite command
for DOCKER_IMAGE in $(docker service ls|awk '{print $2}'|tail -n +2)
do
	echo 'DOCKER IMAGE IS -->'$DOCKER_IMAGE
    $COMMAND_TO_RUN $DOCKER_IMAGE
done