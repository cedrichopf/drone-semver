# Drone CI Plugin for Semantic Versioning

- [Drone CI Plugin for Semantic Versioning](#drone-ci-plugin-for-semantic-versioning)
  - [Overview](#overview)
  - [Usage](#usage)
  - [Settings](#settings)
  - [Environment Variables](#environment-variables)
  - [Auto-Increment](#auto-increment)
    - [Example](#example)

---

## Overview

This plugin will fetch the current semantic version of the repository
and store it into a file named `semver`. If no semantic version is available,
the plugin will generate an initial version based on the configuration.

Additionally, the plugin can be configured to automatically increment the semantic version
based on the content of a file, e.g. `CHANGELOG.md`.

## Usage

```yaml
---
kind: pipeline
type: docker
name: semantic-version

trigger:
  event:
    - tag

steps:
  - name: semver
    image: cedrichopf/drone-semver
    settings:
      initial_version: 1.0.0
      autoincrement: true
      file: CHANGELOG.md
```

## Settings

```yaml
settings:
  initial_version: 1.0.0
  autoincrement: true
  file: CHANGELOG.md
  file_regex: "\[(\d\.){2}\d\]"
  major_keyword: Major
  minor_keyword: Minor
```

All settings will be passed into the container using environment variables.
A complete overview of the available environment variables can be found in the table below.

## Environment Variables

The following table contains an overview of the available environment variables to configure
the application.

| Name                   | Description                                    | Default Value     |
| ---------------------- | ---------------------------------------------- | ----------------- |
| DRONE_SEMVER           | Drone CI semver string, injected by Drone CI   | `-`               |
| PLUGIN_INITIAL_VERSION | Initial version to use, e.g. `1.0.0`           | `1.0.0`           |
| PLUGIN_AUTOINCREMENT   | Enable / disable autoincrement                 | `false`           |
| PLUGIN_FILE            | File to detect autoincrement version           | `CHANGELOG.md`    |
| PLUGIN_USE_REGEX       | Enable / disable file regex                    | `true`            |
| PLUGIN_FILE_REGEX      | Regex to split the file into multiple sections | `\[(\d\.){2}\d\]` |
| PLUGIN_MAJOR_KEYWORD   | Keyword for Major update                       | `Major`           |
| PLUGIN_MINOR_KEYWORD   | Keyword for Minor update                       | `Minor`           |

## Auto-Increment

The plugin can automatically increment the semantic version by checking the content of a
given file. Per default, it will look for a file called `CHANGELOG.md` in the root folder
of the repository. The content of the file will be divided by the given regular expression
configured using `PLUGIN_FILE_REGEX`. The default expression is dividing the content by
versions in the format `[*.*.*]`.

### Example

The following content shows an example of a changelog file containing a major update:

```markdown
# [Unreleased]

- Something else
- **Major** New update

# [1.0.0]

- Something
```

The plugin will evaluate the following section:

```markdown
# [Unreleased]

- Something else
- **Major** New update
```

Since this section contains the keyword `Major`, which is the default keyword configured
using `PLUGIN_MAJOR_KEYWORD`, it will increment the semantic version using a major update.
