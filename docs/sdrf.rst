SDRF: ample and Data Relationship Format
========================================

The SDRF-Proteomics file format describes the sample characteristics and the relationships between samples and data files. The file format is a tab-delimited one where each ROW corresponds to a relationship between a Sample and a Data file (and MS signal corresponding to labelling in the context of multiplexed experiments), each column corresponds to an attribute/property of the Sample and the value in each cell is the specific value of the property for a given Sample (**Figure 1**).


.. image:: images/sdrf-nutshell.png
   :width: 600
   :align: center

**Figure 2**: SDRF-Proteomics in a nutshell. The file format is a tab-delimited one where columns are properties of the sample, the data file or the variables under study. The rows are the samples of origin and the cells are the values for one property in a specific sample.

SDRF-Proteomics format rules
--------------------------------

There are general scenarios/use cases that are addressed by the following rules:

- **Unknown values**: In some cases, the column is mandatory in the format but for some samples the corresponding value is unknown. In those cases, users SHOULD use ‘not available’.
- **Not Applicable values**: In some cases, the column is mandatory but for some samples the corresponding value is not applicable. In those cases, users SHOULD use ‘not applicable’.
- **Case sensitivity**: By specification the SDRF is case insensitive, but we RECOMMEND using lowercase characters throughout all the text (Column names and values).
- **Spaces**: By specification the SDRF is case sensitive to spaces (sourcename != source name).
- **Column order**: The SDRF MUST start with the source name column (accession/name of the sample of origin), then all the sample characteristics; followed by the assay name corresponding to the MS run. Finally, after the assay name all the comments (properties of the data file generated).
- **Extension**: The extension of the SDRF should be .tsv or .txt.

SDRF-Proteomics values
----------------------------

The value for each property (e.g. characteristics, comment) corresponding to each sample can be represented in multiple ways.

- Free Text (Human readable): In the free text representation, the value is provided as text without Ontology support (e.g. colon or providing accession numbers). This is only RECOMMENDED when the text inserted in the table is the exact name of an ontology/CV term in EFO. If the term is not in EFO, other ontologies can be used.

.. list-table:: SDRF values annotated in free text
   :widths: 50 50
   :header-rows: 1

   * - source name
     - characteristics[organism]
   * - sample 1
     - homo sapiens
   * - sample 2
     - homo sapiens

- Ontology url (Computer readable): Users can provide the corresponding URI (Uniform Resource Identifier) of the ontology/CV term as a value. This is recommended for enriched files where the user does not want to use intermediate tools to map from free text to ontology/CV terms.

.. list-table:: SDRF with ontology terms
   :widths: 50 50
   :header-rows: 1

   * - source name
     - characteristics[organism]
   * - sample 1
     - http://purl.obolibrary.org/obo/NCBITaxon_9606
   * - sample 2
     - http://purl.obolibrary.org/obo/NCBITaxon_9606

- Key=value representation (Human and Computer readable): The current representation aims to provide a mechanism to represent the complete information of the ontology/CV term including Accession, Name and other additional properties. In the key=value pair representation the Value of the property is represented as an Object with multiple properties, where the key is one of the properties of the object and the value is the corresponding value for the particular key. An example of key value pairs is post-translational modification <<ptms>>

`NT=Glu->pyro-Glu; MT=fixed; PP=Anywhere; AC=Unimod:27; TA=E`

SDRF-Proteomics: Samples metadata
-----------------------------------

The Sample metadata has different Categories/Headings to organize all the attributes/ column headers of a given sample. Each Sample contains a `source name` (accession) and a set of `characteristics`. Any proteomics sample MUST contain the following characteristics:

- **source name**: Unique sample name (it can be present multiple times if the same sample is used several times in the same dataset).

- **characteristics[organism]**: The organism of the Sample of origin.

- **characteristics[disease]**: The disease under study in the Sample.

- **characteristics[organism part]**: The part of organism's anatomy or substance arising from an organism from which the biomaterial was derived (e.g. liver).

- **characteristics[cell type]**: A cell type is a distinct morphological or functional form of cell. Examples are epithelial, glial etc.

Example:

.. list-table:: Minimun sample metadata for any proteomics dataset
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - source name
     - characteristics[organism]
     - characteristics[organism part]
     - characteristics[disease]
     - characteristics[cell type]
   * - sample_treat
     - homo sapiens
     - liver
     - liver cancer
     - liver cancer cell
   * - sample_control
     - homo sapiens
     - liver
     - liver cancer
     - liver

.. note:: Additional characteristics can be added depending on the type of the experiment and sample. The https://github.com/bigbio/proteomics-metadata-standard/tree/master/templates[SDRF-Proteomics templates] defines a set of templates and checklists of properties that should be provided depending on the proteomics experiment.

Some important notes:

- Each characteristics name in the column header SHOULD be a CV term from the EFO ontology. For example, the header _characteristics[organism]_ corresponds to the ontology term Organism.

- Multiple values (columns) for the same characteristics term are allowed in SDRF-Proteomics. However, it is RECOMMENDED not to use the same column in the same file. If you have multiple phenotypes, you can specify what it refers to or use another more specific term, e.g. "immunophenotype".

SDRF-Proteomics: Data files metadata
----------------------------------------

The connection between the Samples to the Data files is done by using a series of properties and attributes. All the properties referring to the MS run (file) itself are annotated with the category/prefix **comment**. The use of comment is mainly aimed at differentiating sample properties from the data properties. It matches a given sample to the corresponding file(s). The word comment is used for backwards-compatibility with gene expression experiments (RNA-Seq and Microarrays experiments).

The order of the columns is important, **assay name** MUST always be located before the comments. It is RECOMMENDED to put the last column as `comment[data file]`. The following properties MUST be provided for each data file (ms run) file:

- **assay name**: assay name is an accession for each msrun. Because of back-compatibility with SDRF in transcriptomics we don't use the term ms run but the more generic term `assay name`. Examples of assay names are: “run 1”, “run_fraction_1_2”, it must be a unique accession for every msrun.

- **comment[fraction identifier]**: The fraction identifier allows to record the number of a given fraction. The fraction identifier corresponds to this ontology term. It MUST start from 1 and if the experiment is not fractionated, 1 MUST be used for each MSRun (assay).

- **comment[label]**: label describes the label applied to each Sample (if any). In case of multiplex experiments such as TMT, SILAC, and/or ITRAQ the corresponding label SHOULD be added. For Label-free experiments the label free sample term MUST be used <<label-data>>.
- **comment[data file]**: T
he data file provides the name of the raw file generated  by the instrument. The data files can be instrument raw files but also converted peak lists such as mzML, MGF or result files like mzIdentML.
- **comment[instrument]**: Instrument model used to capture the sample <<instrument>>.

Example:

.. list-table:: Minimum data metadata for any proteomics dataset
   :widths: 14 14 14 14 14 14 14
   :header-rows: 1

   * - source name
     - ....
     - assay name
     - comment[label]
     - comment[fraction identifier]
     - comment[instrument]
     - comment[data file]
   * - sample 1
     - ....
     - run 1
     - label free sample
     - 1
     - NT=LTQ Orbitrap XL
     - 000261_C05_P0001563_A00_B00K_R1.RAW
   * - sample 1
     - ....
     - run 2
     - label free sample
     - 2
     - NT=LTQ Orbitrap XL
     - 000261_C05_P0001563_A00_B00K_R2.RAW


TIP: All the possible _label_ values can be seen in the in the PRIDE CV under the https://www.ebi.ac.uk/ols/ontologies/pride/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FPRIDE_0000514&viewMode=All&siblings=false[Label] node.




