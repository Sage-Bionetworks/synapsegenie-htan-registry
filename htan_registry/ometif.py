import logging
import os
import subprocess

from synapsegenie.example_filetype_format import FileTypeFormat
from synapsegenie import process_functions

logger = logging.getLogger(__name__)

here = os.path.abspath(os.path.dirname(__file__))


class OmeTif(FileTypeFormat):

    _filetype = "ometif"

    _process_kwargs = ["databaseSynId"]

    def _validate_filetype(self, filePath):
        assert os.path.basename(filePath[0]).endswith(".ome.tif")

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
        total_error = ""
        warning = ""
        xmlvalid_cmd = os.path.join(here, '../bftools/xmlvalid')
        xmlvalid_exc = subprocess.run([xmlvalid_cmd, path_or_df], capture_output=True, text=True)
        # If error, set the error
        if xmlvalid_exc.returncode:
            total_error = xmlvalid_exc.stdout

        # TODO: Add validation function here.
        return total_error, warning
