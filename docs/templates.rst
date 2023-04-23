SDRF-Proteomics Templates
########################################

The sample metadata **Templates** are a set of guidelines to annotate the different types of proteomics experiments (use cases) to ensure that Minimum Metadata and characteristics are provided to understand the dataset. These templates respond to the distribution and frequency of experiment types in public databases like PRIDE and ProteomeXchange. The Python/Java validators will check the columns checklists depending on the template.

NOTE: It is planned that, unlike in other PSI formats, regular updates will need to be done to be able to explain how new use cases for the format can be accommodated.

- **Default proteomics experiment**: Minimum information for any proteomics experiment - `Default template <https://github.com/bigbio/proteomics-metadata-standard/blob/master/templates/sdrf-default.tsv>`_
- **Human experiment**: All experiments that use `Human samples <https://github.com/bigbio/proteomics-metadata-standard/blob/master/templates/sdrf-human.tsv>`_
- **Vertebrates experiment**: Vertebrate experiment - `Vertebrate template <https://github.com/bigbio/proteomics-metadata-standard/blob/master/templates/sdrf-vertebrates.tsv>`_
- **Non-vertebrates experiment**: Non-vertebrate experiment - `Non-vertebrate template <https://github.com/bigbio/proteomics-metadata-standard/blob/master/templates/sdrf-nonvertebrates.tsv>`_
- **Plants experiment**: Plant experiment - `Plant template https://github.com/bigbio/proteomics-metadata-standard/blob/master/templates/sdrf-plants.tsv>`_
- **Cell lines experiment**: Experiments using cell-lines - `Cell lines template <https://github.com/bigbio/proteomics-metadata-standard/blob/master/templates/sdrf-cell-line.tsv>`_

.. note:: Each of the template is a tsv file with the minimum columns to describe the experiment. The community can create they are own templates for example for meta-proteomics experiments, imaging proteomics or top-down. If the community would like to add a new template, the following table should be modified and the corresponding tsv should be created in this folder.

**Sample attributes**: Minimum sample attributes for primary cells from different species and cell lines

.. list-table:: SDRF-Proteomics templates sample attributes
   :widths: 14 14 14 14 14 14 14
   :header-rows: 1

   * -
     - Default
     - Human
     - Vertebrates
     - Non-vertebrates
     - Plants
     - Cell lines
    * - source name
      - :white_check_mark:
      - :white_check_mark:
      - :white_check_mark:
      - :white_check_mark:
      - :white_check_mark:
      - :white_check_mark:


|===
|                                       | Default            |Human              | Vertebrates       | Non-vertebrates   | Plants            | Cell lines
|source name                            | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|characteristics[organism]              | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|characteristics[strain/breed]          |                    |                   |                   |:zero:             |                   |:zero:
|characteristics[ecotype/cultivar]      |                    |                   |                   |                   |:zero:             |
|characteristics[ancestry category]     |                    |:white_check_mark: |                   |                   |                   |
|characteristics[age]                   |                    |:white_check_mark: |:zero:             |                   |:zero:             |
|characteristics[developmental stage]   |                    |:zero:             |:zero:             |                   |:zero:             |
|characteristics[sex]                   |                    |:white_check_mark: |:zero:             |                   |                   |
|characteristics[disease]               | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |                   |:white_check_mark:
|characteristics[organism part]         | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|characteristics[cell type]             | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|technology type                        | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|characteristics[individual]            |                    |:zero:             |:zero:             |:zero:             |:zero:             |:zero:
|characteristics[cell line]             |                    |                   |                   |                   |                   |:white_check_mark:
|characteristics[biological replicate]  |:white_check_mark:  |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|                                       |                    |                   |                   |                   |                   |
|assay name                             | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|comment[data file]                     | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|comment[technical replicate]           | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|comment[fraction identifier]           | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|comment[label]                         | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|comment[cleavage agent details]        | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:
|comment[instrument]                    | :white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark: |:white_check_mark:

|===

* :white_check_mark: : Required Attributes for each sample Type (e.g. Human, Vertebrates).
* :zero: : Optional Attribute