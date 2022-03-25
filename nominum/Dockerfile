FROM mediagis/nominatim:4.0

ARG MAP
ENV ENV_MAP=$MAP

COPY ${ENV_MAP} /nominatim/data/${ENV_MAP}
