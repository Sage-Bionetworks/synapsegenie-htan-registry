import logging
import os
import subprocess
import re

from synapsegenie.example_filetype_format import FileTypeFormat
from synapsegenie import process_functions

logger = logging.getLogger(__name__)

here = os.path.abspath(os.path.dirname(__file__))


class Imaging(FileTypeFormat):

    _filetype = "imaging"

    _process_kwargs = ["databaseSynId"]

    def _validate_filetype(self, filePath):
        assert os.path.basename(filePath[0]).endswith(("tif","tiff",".svs",".ndpi"))

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

        # Validate is bioformats compatiable with showinf
        showinf_cmd = os.path.join(here, '../bftools/showinf')
        showinf_exc = subprocess.run([showinf_cmd, path_or_df, "-nopix"], capture_output=True, text=True)
        # If error, set the set a warning
        if showinf_exc.returncode:
            total_error.append(f"showinf failed: {showinf_exc.stdout}")

        # Validate the OME-XML with xmlvalid if file type is ome.tiff
        if os.path.basename(filePath[0]).endswith(("ome.tif",".ome.tiff")):
            xmlvalid_cmd = os.path.join(here, '../bftools/xmlvalid')
            xmlvalid_exc = subprocess.run([xmlvalid_cmd, path_or_df], capture_output=True, text=True)
            # If error, set the set a warning
            if xmlvalid_exc.returncode:
                total_error.append("ERROR xmlvalid failed:\n\t{xmlvalid_exc.stdout}\n")

        # Get all information on the file from tiffinfo
        tiffinfo_exc = subprocess.run(["tiffinfo", path_or_df], capture_output=True, text=True)
        # If error, set the error
        if tiffinfo_exc.returncode:
            total_error.append("ERROR tiffinfo failed:\n\t{tiffinfo_exc.stdout}\n")
        # If dates found, make an error
        finddate = len(re.findall(r'date', tiffinfo_exc.stdout, re.IGNORECASE))
        # If likely redacted dates are found make a warning instead
        redacted_dates = len(re.findall(r'1970:01:01 00:00:00', tiffinfo_exc.stdout))
        if redacted_dates:
            total_error.append(f'WARNING: {finddate} occurences of DATE in TIFF headers that are potentially redacted to "1970:01:01 00:00:00"\n')
        elif finddate:
            total_error.append(f'ERROR: {finddate} occurences of DATE in TIFF headers\n')
        # If times found make a warning
        findtime = len(re.findall(r'time', tiffinfo_exc.stdout, re.IGNORECASE))
        if findtime:
            total_error.append(f'WARNING: {findtime} occurences of TIME in TIFF headers\n') 
        # If label found make a warning
        findlabel = len(re.findall(r'label \d+x\d+', tiffinfo_exc.stdout, re.IGNORECASE))
        if findlabel:
            total_error.append(f'WARNING: {findlabel} possible label images\n') 

        if total_error == []:
            total_error = ""
        if warning == []:
            warning = ""

        # TODO: Add validation function here.
        return str(total_error), str(warning)
