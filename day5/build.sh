#!/usr/bin/env bash


# create atifacts folder if does not exist 
mkdir -p artifacts

# creating timestamp 
timestamp=$(date +"%Y%m%d_%H%M%S")


build_name="build-${timestamp}.tgz"

echo "Creating build artifact: $build_name"


if ./validate.sh; then
  echo "Validation passed"
else
  echo "Validation failed — Build aborted."
  exit 1
fi

# creating the tarball inculding 
tar -czf "artifacts/$build_name" src logs config.json package.json eslint.config.js .prettierrc

# generating checksum 
sha256sum "artifacts/$build_name" > "artifacts/${build_name}.sha256"

echo "Hurray Build created successfully 🥳🥳 !"
echo "File: artifacts/$build_name"
echo "Checksum: artifacts/${build_name}.sha256"