# Drone CI Plugin for Semantic Versioning

## Environment Variables

| Name                   | Description                                                 | Default Value     |
| ---------------------- | ----------------------------------------------------------- | ----------------- |
| DRONE_SEMVER           | Drone CI semver string, injected by Drone CI                | `-`               |
| PLUGIN_INITIAL_VERSION | Initial version to use, e.g. `1.0.0`                        | `1.0.0`           |
| PLUGIN_AUTOINCREMENT   | Enable / disable autoincrement                              | `false`           |
| PLUGIN_FILE            | File to detect autoincrement version                        | `CHANGELOG.md`    |
| PLUGIN_FILE_REGEX      | Regular expression to split the file into multiple sections | `\[(\d\.){2}\d\]` |
| PLUGIN_MAJOR_KEYWORD   | Keyword for Major update                                    | `Major`           |
| PLUGIN_MINOR_KEYWORD   | Keyword for Minor update                                    | `Minor`           |
