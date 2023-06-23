#!/usr/bin/env bash

# cat dev.env | grep -v User-Agent | xargs -L 1 -I {} sh -c "export {}"
source dev.env