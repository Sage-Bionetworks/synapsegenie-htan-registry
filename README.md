# synapsegenie: HTAN registry

## Introduction

This is the HTAN file format synapsegenie registry

## Installation

Dependencies:
- Python 3.7 or higher
- [synapseclient](http://python-docs.synapse.org) (`pip install synapseclient`)
- Python [pandas](http://pandas.pydata.org) (`pip install pandas`)
- [bftools](https://docs.openmicroscopy.org/bio-formats/6.9.1/users/comlinetools/): xmlvalid

```
pip install synapsegenie
synapsegenie -v
# Install this registry
pip install -e .
```

## Usage

### Creating your own registry
`synapsegenie` allows a user to create a registry package with a list of file formats.  Each of these file format classes should extend `synapsegenie.example_filetype_format.FileTypeFormat`.  Learn more about creating Python packages [here](https://packaging.python.org/tutorials/packaging-projects/).  Once you have installed your registry package, you can now use the `synapsegenie` command line client.

### synapsegenie Synapse project
A `synapsegenie` Synapse project must exist for you to fully utilize this package.  There is now a command to create this infrastructure in Synapse.  If you already have an existing Synapse Project you would like to use, please use the `--project_id` parameter, otherwise please use the `--project_name` parameter to create a new Synapse project.

```
synapsegenie bootstrap-infra --format_registry_packages htan_registry \
                             --project_name "HTAN synapsegenie prototype"
                             --centers TEST
```

If you decide to add centers at a later date, you can re-run this command and the center will be added

```
synapsegenie bootstrap-infra --format_registry_packages htan_registry \
                             --project_id syn30847334
                             --centers TEST HTAN_SRRS
```

### File Validator
The `synapsegenie` package also has a function to run the validator locally on all of your files. Please view the help to see how to run to validator.

```
synapsegenie validate-single-file -h

synapsegenie /path/to/file center_name \
             --format_registry_packages example_registry \
             --project_id syn30847334 \ # Run bootstrap-infra to create a Synapse project
```

### Validation/Processing
`synapsegenie` will validate and process all the files uploaded by centers.  Every valid file will be processed and uploaded into Synapse tables.

```
synapsegenie process -h

# only validate
synapsegenie process --format_registry_packages htan_registry \
                     --project_id syn30847334
                     --only_validate

# validate + process
synapsegenie process --format_registry_packages htan_registry \
                     --project_id syn30847334
```

## Contributing

To learn how to contribute, please read the [contributing guide](CONTRIBUTING.md)
