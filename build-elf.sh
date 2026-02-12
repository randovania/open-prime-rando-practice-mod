#!/bin/bash

set -ex

OUTPUT_ELF=$1

test -n "${OUTPUT_ELF}" || (echo "Output ELF path not provided" && exit 1)

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "${DIR}"

IMAGE="ghcr.io/metroidprimemodding/gcn-static-patcher/build:latest"
CMAKE_DIR="cmake-build-release-docker"
EXTERNAL_SRC_DIR="$(pwd)/"
EXTERNAL_BUILD_DIR="${EXTERNAL_SRC_DIR}${CMAKE_DIR}"
DOCKER_SRC_DIR="/tmp/prime2-practice-mod/"
DOCKER_BUILD_DIR="${DOCKER_SRC_DIR}${CMAKE_DIR}"

ls -l "${EXTERNAL_SRC_DIR}"

mkdir -p "${EXTERNAL_BUILD_DIR}"

# launch a build in a docker container first (this does the same thing intellij would do)
docker run --rm \
    -w "${DOCKER_BUILD_DIR}" \
    -v "${EXTERNAL_SRC_DIR}":"${DOCKER_SRC_DIR}" \
    "${IMAGE}" \
    bash -c "cmake '${DOCKER_SRC_DIR}/external/prime2-practice-mod' -DCMAKE_BUILD_TYPE=Release -G Ninja && cmake --build . --config Release"

# Copy the elf
cp "${EXTERNAL_BUILD_DIR}/prime2-practice" "${OUTPUT_ELF}"