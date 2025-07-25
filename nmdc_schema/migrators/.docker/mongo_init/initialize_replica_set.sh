#! /bin/sh

###############################################################################
# Overview
# --------
# This shell script uses `mongosh` to: (a) check whether the specified MongoDB
# instance is a member of a replica set and, if is isn't, (b) creates a replica
# set of which that MongoDB instance is the sole member.
#
# This shell script was designed to be run within a Docker container based upon
# the `mongo:8.0.4` container image (i.e., https://hub.docker.com/_/mongo).
#
# Positional parameters
# ---------------------
# 1. MongoDB hostname (e.g., "mongo")
# 2. MongoDB port     (e.g., "27017")
# 3. MongoDB username (e.g., "admin")
# 4. MongoDB password (e.g., "root")
#
# References
# ----------
# 1. https://www.mongodb.com/docs/manual/reference/method/rs.status/
# 2. https://www.mongodb.com/docs/mongodb-shell/reference/options/
# 3. https://www.warp.dev/terminus/docker-compose-health-check
###############################################################################

echo 'Setting up replica set.'

echo '
  try {
    rs.status();
  } catch (e) {
    rs.initiate({ _id: "rs0", members: [{ _id: 0, host: "localhost" }] });
  }
' | mongosh \
  --host "${1}" \
  --port "${2}" \
  --username "${3}" \
  --password "${4}"

echo 'Finished setting up replica set.'

# Exit with a status code of 0.
exit 0
