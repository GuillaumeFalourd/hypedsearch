'''
exec.py

Author: Zachary McGrath 
Date: 6 April 2020

Executor for the program
In charge of the flow of the program
'''
from os import walk
from src import identification
from src import summary

def run(args: dict) -> None:
    '''
    Executing function for the program

    Inputs:
        args:   object arguments from main. Should be validated in main. Attributes of args:
            spectra_folder:             (str) full path the the directory containing all spectra files
            database_file:              (str) full path to the .fasta database file
            output_dir:                 (str) full path the the directory to save output to
            min_peptide_len:            (int) minimum peptide length to consider
            max_peptide_len:            (int) maximum peptide length to consider
            tolerance:                  (float) the ppm tolerance to allow in search
            precursor_tolerance:        (float) the tolerance (in Da) to allow when matching precursors
            peak_filter:                (int) the number of peaks to filter by 
            relative_abundance_filter:  (float) the percentage of the total abundance a peak must
                                            be to pass the filter
            digest:                     (str) the digest performed
            missed_cleavages:           (int) the number of missed cleavages allowed in digest
            verbose:                    (bool) extra printing
            DEBUG:                      (bool) debuging print messages. Default=False
    Outputs:
        None
    '''
    # get all the spectra file names
    spectra_files = []
    for (_, _, filenames) in walk(args['spectra_folder']):
        for fname in filenames:
            if '.mzml' not in fname.lower():
                continue
            spectra_files.append(args['spectra_folder'] + fname)
        break

    matched_spectra = identification.id_spectra(
        spectra_files, args['database_file'], 
        min_peptide_len=args['min_peptide_len'], 
        max_peptide_len=args['max_peptide_len'], 
        ppm_tolerance=args['tolerance'], 
        precursor_tolerance=args['precursor_tolerance'],
        peak_filter=args['peak_filter'],
        relative_abundance_filter=args['relative_abundance_filter'],
        digest=args['digest'], 
        missed_cleavages=args['missed_cleavages'],
        verbose=True, 
        DEBUG=args['DEBUG'], 
        truth_set=args['truth_set'], 
        output_dir=args['output_dir']
    )
    print('\nFinished search. Writting results to {}...'.format(args['output_dir']))
    summary.generate(matched_spectra, args['output_dir'])
    
    