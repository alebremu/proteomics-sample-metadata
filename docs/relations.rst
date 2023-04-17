Relationship to other specifications
=======================================

SDRF-Proteomics is fully compatible with the SDRF file format part of MAGE-TAB (https://www.ebi.ac.uk/arrayexpress/help/magetab_spec.html). The MAGE-TAB is the file format to store the metadata and sample information on transcriptomics experiments.
MAGE-TAB (MicroArray Gene Expression Tabular) is a standard format for storing and exchanging microarray and other high-throughput genomics data. It consists of two spreadsheets for each experiment: the Investigation Description Format (IDF) file and the Sample and Data Relationship Format (SDRF) file.

The IDF file contains general information about the experiment, such as the project title, description, and funding sources, as well as details about the experimental design, such as the type of technology used, the organism studied, and the experimental conditions.
The SDRF file contains detailed information about the samples and the data generated from them, including sample annotations, data file locations, and data processing parameters. It also defines the relationships between samples, such as replicates or time-course experiments. Together, the IDF and SDRF files provide a complete description of the experiment and the data generated from it, allowing researchers to share and compare their data with others in a standardized and interoperable format.

SDRF-Proteomics sample information can be embedded into mzTab metadata files.   The mzTab (Mass Spectrometry Tabular) format is a standard format for reporting the results of proteomics and metabolomics experiments. It can be used to store information such as protein identification, peptide sequences, and quantitation results.
The mzTab format allows for the embedding of sample metadata into the file, which includes information about the samples and the experimental conditions. This metadata can be derived from the Sample and Data Relationship Format (SDRF) file in a proteomics experiment.
In the mzTab format, sample metadata is stored in a separate section called the "metadata section," which contains a list of key-value pairs that describe the samples. The keys in the metadata section correspond to the column names in the SDRF file, and the values correspond to the values in the Sample cells.
By embedding sample metadata into the mzTab file, researchers can ensure that all relevant information about the experiment is stored in a single file, making it easier to share and compare data with others.
