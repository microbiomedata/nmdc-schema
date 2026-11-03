# makefiles/release.Makefile: the release command
#
# Makes a release from main in one step: bumps the version in pyproject.toml
# with `uv version`, rebuilds and tests the artifacts, commits, tags, pushes
# and creates the GitHub release, which triggers the publish workflow.
# It shows the old and new versions and asks before changing anything.
# The logic is in src/scripts/release.py.
#
# Usage:
#   make release BUMP='minor rc'                      # 11.25.0 -> 11.26.0rc1, tag v11.26.0-rc.1
#   make release BUMP=rc                              # 11.26.0rc1 -> 11.26.0rc2
#   make release BUMP=stable                          # 11.26.0rc2 -> 11.26.0
#   make release BUMP=patch RELEASE_OPTS=--no-push    # rehearsal: stop after the local commit and tag
#
# BUMP takes one or more of: major minor patch rc stable.
# From a release candidate, use `stable` to release it; `minor` skips to the next minor.
# RELEASE_OPTS also accepts --yes, which skips the confirmation prompt.
#
# Included by the top-level Makefile. RUN is inherited from it.

.PHONY: release

BUMP ?=
RELEASE_OPTS ?=

release:
	$(RUN) python src/scripts/release.py bump $(foreach component,$(BUMP),--bump $(component)) $(RELEASE_OPTS)
