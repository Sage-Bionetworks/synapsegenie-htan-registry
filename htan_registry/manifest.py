import logging
import os
import subprocess
import re

from synapsegenie.example_filetype_format import FileTypeFormat
from synapsegenie import process_functions

logger = logging.getLogger(__name__)

here = os.path.abspath(os.path.dirname(__file__))


class Manifest(FileTypeFormat):

    _filetype = "Manifest"

    _process_kwargs = ["databaseSynId"]

    def _validate_filetype(self, filePath):
        assert os.path.basename(filePath[0]).endswith("synapse_storage_manifest.csv")

    def _process(self, df):
        df.columns = [df.upper() for col in df.columns]
        return df

    def read_file(self, filePathList):
        '''
        Each file is to be read in for validation and processing.
        This is not to be changed in any functions.

        Args:
            filePathList:  A list of file paths (Max is 2 for the two
                           clinical files)

        Returns:
            df: Pandas dataframe of file
        '''
        # This file isn't a dataframe, so just return the filepath
        filepath = filePathList[0]
        return filepath

    def process_steps(self, df, newPath, databaseSynId):
        df = self._process(df)
        process_functions.updateData(self.syn, databaseSynId, df, self.center,
                                     toDelete=True)
        df.to_csv(newPath, sep="\t", index=False)
        return newPath

    def _validate(self, path_or_df):
        total_error = []
        warning = []

        # Read the manifest as a panda df

        # Pull the component and get the colums from the schema

        # Error if there are non-schema columns used

        # If component==ImagingLevel2
        # Check that channel_metadata_filename exists as a path within the synapse project
        # If exists check that it contains specific columns


        if total_error == []:
            total_error = ""
        if warning == []:
            warning = ""

        # TODO: Add validation function here.
        return str(total_error), str(warning)
