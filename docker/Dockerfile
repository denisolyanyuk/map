FROM osrm/osrm-backend
WORKDIR /data
RUN apt-get update

ARG MAP
ENV ENV_MAP=$MAP

COPY data/${ENV_MAP} /data/${ENV_MAP}

RUN osrm-extract -p /opt/car.lua ${ENV_MAP}
RUN osrm-partition ${ENV_MAP}
RUN osrm-customize ${ENV_MAP}

CMD "osrm-routed" "--algorithm" "mld" ${ENV_MAP} "--max-matching-size" "1000"  "--max-table-size" "1000"