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


