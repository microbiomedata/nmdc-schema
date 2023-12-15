# Enum: FileTypeEnum



URI: [FileTypeEnum](FileTypeEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| Metagenome Raw Reads | None | Interleaved paired-end raw sequencing data |
| Metagenome Raw Read 1 | None | Read 1 raw sequencing data, aka forward reads |
| Metagenome Raw Read 2 | None | Read 2 raw sequencing data, aka reverse reads |
| FT ICR-MS Analysis Results | None | FT ICR-MS-based molecular formula assignment results table |
| GC-MS Metabolomics Results | None | GC-MS-based metabolite assignment results table |
| Metaproteomics Workflow Statistics | None | Aggregate workflow statistics file |
| Protein Report | None | Filtered protein report file |
| Peptide Report | None | Filtered peptide report file |
| Unfiltered Metaproteomics Results | None | MSGFjobs and MASIC output file |
| Read Count and RPKM | None | Annotation read count and RPKM per feature JSON |
| QC non-rRNA R2 | None | QC removed rRNA reads (R2) fastq |
| QC non-rRNA R1 | None | QC removed rRNA reads (R1) fastq |
| Metagenome Bins | None | Metagenome bin contigs fasta |
| Metagenome Bins Compression File | None | Compressed file containing all metagenome bins and associated files |
| Metagenome Bins Info File | None | File containing version information on the binning workflow |
| CheckM Statistics | None | CheckM statistics report |
| Read Based Analysis Info File | None | File containing reads based analysis information |
| GTDBTK Bacterial Summary | None | GTDBTK bacterial summary |
| GTDBTK Archaeal Summary | None | GTDBTK archaeal summary |
| GOTTCHA2 Krona Plot | None | GOTTCHA2 krona plot HTML file |
| GOTTCHA2 Classification Report | None | GOTTCHA2 classification report file |
| GOTTCHA2 Report Full | None | GOTTCHA2 report file |
| Kraken2 Krona Plot | None | Kraken2 krona plot HTML file |
| Centrifuge Krona Plot | None | Centrifuge krona plot HTML file |
| Centrifuge output report file | None | Centrifuge output report file |
| Kraken2 Classification Report | None | Kraken2 output report file |
| Kraken2 Taxonomic Classification | None | Kraken2 output read classification file |
| Centrifuge Classification Report | None | Centrifuge output report file |
| Centrifuge Taxonomic Classification | None | Centrifuge output read classification file |
| Structural Annotation GFF | None | GFF3 format file with structural annotations |
| Structural Annotation Stats Json | None | Structural annotations stats json |
| Functional Annotation GFF | None | GFF3 format file with functional annotations |
| Annotation Info File | None | File containing annotation info |
| Annotation Amino Acid FASTA | None | FASTA amino acid file for annotated proteins |
| Annotation Enzyme Commission | None | Tab delimited file for EC annotation |
| Annotation KEGG Orthology | None | Tab delimited file for KO annotation |
| Assembly Info File | None | File containing assembly info |
| Assembly Coverage BAM | None | Sorted bam file of reads mapping back to the final assembly |
| Assembly AGP | None | An AGP format file that describes the assembly |
| Assembly Scaffolds | None | Final assembly scaffolds fasta |
| Assembly Contigs | None | Final assembly contigs fasta |
| Assembly Coverage Stats | None | Assembled contigs coverage information |
| Contig Mapping File | None | Contig mappings between contigs and scaffolds |
| Error Corrected Reads | None | Error corrected reads fastq |
| Filtered Sequencing Reads | None | Reads QC result fastq (clean data) |
| Read Filtering Info File | None | File containing read filtering information |
| QC Statistics Extended | None | Extended report including methods and results for read filtering |
| QC Statistics | None | Reads QC summary statistics |
| TIGRFam Annotation GFF | None | GFF3 format file with TIGRfam |
| CRT Annotation GFF | None | GFF3 format file with CRT |
| Genemark Annotation GFF | None | GFF3 format file with Genemark |
| Prodigal Annotation GFF | None | GFF3 format file with Prodigal |
| TRNA Annotation GFF | None | GFF3 format file with TRNA |
| Misc Annotation GFF | None | GFF3 format file with Misc |
| RFAM Annotation GFF | None | GFF3 format file with RFAM |
| TMRNA Annotation GFF | None | GFF3 format file with TMRNA |
| Crispr Terms | None | Crispr Terms |
| Product Names | None | Product names file |
| Gene Phylogeny tsv | None | Gene Phylogeny tsv |
| Scaffold Lineage tsv | None | phylogeny at the scaffold level |
| Clusters of Orthologous Groups (COG) Annotation GFF | None | GFF3 format file with COGs |
| KO_EC Annotation GFF | None | GFF3 format file with KO_EC |
| CATH FunFams (Functional Families) Annotation GFF | None | GFF3 format file with CATH FunFams |
| SUPERFam Annotation GFF | None | GFF3 format file with SUPERFam |
| SMART Annotation GFF | None | GFF3 format file with SMART |
| Pfam Annotation GFF | None | GFF3 format file with Pfam |
| Annotation Statistics | None | Annotation statistics report |
| Direct Infusion FT ICR-MS Raw Data | None | Direct infusion 21 Tesla Fourier Transform ion cyclotron resonance mass spect... |
| LC-DDA-MS/MS Raw Data | None | Liquid chromatographically separated MS1 and Data-Dependent MS2 binary instru... |




## Slots

| Name | Description |
| ---  | --- |
| [data_object_type](data_object_type.md) | The type of file represented by the data object |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/nmdc/nmdc




## LinkML Source

<details>
```yaml
name: file type enum
from_schema: https://w3id.org/nmdc/nmdc
rank: 1000
permissible_values:
  Metagenome Raw Reads:
    text: Metagenome Raw Reads
    description: Interleaved paired-end raw sequencing data
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: ^\.fastq(\.gz)?$
  Metagenome Raw Read 1:
    text: Metagenome Raw Read 1
    description: Read 1 raw sequencing data, aka forward reads
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: ^.+_R1\.fastq(\.gz)?$
    examples:
    - value: BMI_H25VYBGXH_19S_31WellG1_R1.fastq.gz
  Metagenome Raw Read 2:
    text: Metagenome Raw Read 2
    description: Read 2 raw sequencing data, aka reverse reads
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: ^.+_R2\.fastq(\.gz)?$
    examples:
    - value: BMI_H25VYBGXH_19S_31WellG1_R2.fastq.gz
  FT ICR-MS Analysis Results:
    text: FT ICR-MS Analysis Results
    description: FT ICR-MS-based molecular formula assignment results table
  GC-MS Metabolomics Results:
    text: GC-MS Metabolomics Results
    description: GC-MS-based metabolite assignment results table
  Metaproteomics Workflow Statistics:
    text: Metaproteomics Workflow Statistics
    description: Aggregate workflow statistics file
  Protein Report:
    text: Protein Report
    description: Filtered protein report file
  Peptide Report:
    text: Peptide Report
    description: Filtered peptide report file
  Unfiltered Metaproteomics Results:
    text: Unfiltered Metaproteomics Results
    description: MSGFjobs and MASIC output file
  Read Count and RPKM:
    text: Read Count and RPKM
    description: Annotation read count and RPKM per feature JSON
  QC non-rRNA R2:
    text: QC non-rRNA R2
    description: QC removed rRNA reads (R2) fastq
  QC non-rRNA R1:
    text: QC non-rRNA R1
    description: QC removed rRNA reads (R1) fastq
  Metagenome Bins:
    text: Metagenome Bins
    description: Metagenome bin contigs fasta
  Metagenome Bins Compression File:
    text: Metagenome Bins Compression File
    description: Compressed file containing all metagenome bins and associated files
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[mag_wf_activity_id]_hqmq_bin.zip'
  Metagenome Bins Info File:
    text: Metagenome Bins Info File
    description: File containing version information on the binning workflow
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[mag_wf_activity_id]_bin.info'
  CheckM Statistics:
    text: CheckM Statistics
    description: CheckM statistics report
  Read Based Analysis Info File:
    text: Read Based Analysis Info File
    description: File containing reads based analysis information
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: profiler.info
  GTDBTK Bacterial Summary:
    text: GTDBTK Bacterial Summary
    description: GTDBTK bacterial summary
  GTDBTK Archaeal Summary:
    text: GTDBTK Archaeal Summary
    description: GTDBTK archaeal summary
  GOTTCHA2 Krona Plot:
    text: GOTTCHA2 Krona Plot
    description: GOTTCHA2 krona plot HTML file
  GOTTCHA2 Classification Report:
    text: GOTTCHA2 Classification Report
    description: GOTTCHA2 classification report file
  GOTTCHA2 Report Full:
    text: GOTTCHA2 Report Full
    description: GOTTCHA2 report file
  Kraken2 Krona Plot:
    text: Kraken2 Krona Plot
    description: Kraken2 krona plot HTML file
  Centrifuge Krona Plot:
    text: Centrifuge Krona Plot
    description: Centrifuge krona plot HTML file
  Centrifuge output report file:
    text: Centrifuge output report file
    description: Centrifuge output report file
  Kraken2 Classification Report:
    text: Kraken2 Classification Report
    description: Kraken2 output report file
  Kraken2 Taxonomic Classification:
    text: Kraken2 Taxonomic Classification
    description: Kraken2 output read classification file
  Centrifuge Classification Report:
    text: Centrifuge Classification Report
    description: Centrifuge output report file
  Centrifuge Taxonomic Classification:
    text: Centrifuge Taxonomic Classification
    description: Centrifuge output read classification file
  Structural Annotation GFF:
    text: Structural Annotation GFF
    description: GFF3 format file with structural annotations
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_structural_annotation.gff'
  Structural Annotation Stats Json:
    text: Structural Annotation Stats Json
    description: Structural annotations stats json
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_structural_annotation_stats.json'
  Functional Annotation GFF:
    text: Functional Annotation GFF
    description: GFF3 format file with functional annotations
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_functional_annotation.gff'
  Annotation Info File:
    text: Annotation Info File
    description: File containing annotation info
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_imgap.info'
  Annotation Amino Acid FASTA:
    text: Annotation Amino Acid FASTA
    description: FASTA amino acid file for annotated proteins
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_proteins.faa'
  Annotation Enzyme Commission:
    text: Annotation Enzyme Commission
    description: Tab delimited file for EC annotation
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_ec.tsv'
  Annotation KEGG Orthology:
    text: Annotation KEGG Orthology
    description: Tab delimited file for KO annotation
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_ko.tsv'
  Assembly Info File:
    text: Assembly Info File
    description: File containing assembly info
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: README.txt
  Assembly Coverage BAM:
    text: Assembly Coverage BAM
    description: Sorted bam file of reads mapping back to the final assembly
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_pairedMapped.sam.gz'
  Assembly AGP:
    text: Assembly AGP
    description: An AGP format file that describes the assembly
  Assembly Scaffolds:
    text: Assembly Scaffolds
    description: Final assembly scaffolds fasta
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_assembly.contigs.fasta'
  Assembly Contigs:
    text: Assembly Contigs
    description: Final assembly contigs fasta
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: assembly.contigs.fasta
  Assembly Coverage Stats:
    text: Assembly Coverage Stats
    description: Assembled contigs coverage information
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_pairedMapped_sorted.bam.cov'
  Contig Mapping File:
    text: Contig Mapping File
    description: Contig mappings between contigs and scaffolds
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_contig_names_mapping.tsv'
  Error Corrected Reads:
    text: Error Corrected Reads
    description: Error corrected reads fastq
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: input.corr.fastq.gz
  Filtered Sequencing Reads:
    text: Filtered Sequencing Reads
    description: Reads QC result fastq (clean data)
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '/.+?(?=filter)/filter-METAGENOME.fastq.gz '
  Read Filtering Info File:
    text: Read Filtering Info File
    description: File containing read filtering information
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[rqc_wf_activity_id]_readsQC.info'
  QC Statistics Extended:
    text: QC Statistics Extended
    description: Extended report including methods and results for read filtering
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: /.+?(?=filter)/filtered-report.txt
  QC Statistics:
    text: QC Statistics
    description: Reads QC summary statistics
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[rqc_wf_activity_id]_filterStats2.txt'
  TIGRFam Annotation GFF:
    text: TIGRFam Annotation GFF
    description: GFF3 format file with TIGRfam
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_tigrfam.gff'
  CRT Annotation GFF:
    text: CRT Annotation GFF
    description: GFF3 format file with CRT
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_crt.gff'
  Genemark Annotation GFF:
    text: Genemark Annotation GFF
    description: GFF3 format file with Genemark
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_genemark.gff'
  Prodigal Annotation GFF:
    text: Prodigal Annotation GFF
    description: GFF3 format file with Prodigal
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_prodigal.gff'
  TRNA Annotation GFF:
    text: TRNA Annotation GFF
    description: GFF3 format file with TRNA
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_trna.gff'
  Misc Annotation GFF:
    text: Misc Annotation GFF
    description: GFF3 format file with Misc
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_rfam_misc_bind_misc_feature_regulatory.gff'
  RFAM Annotation GFF:
    text: RFAM Annotation GFF
    description: GFF3 format file with RFAM
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_rfam.gff'
  TMRNA Annotation GFF:
    text: TMRNA Annotation GFF
    description: GFF3 format file with TMRNA
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_rfam_ncrna_tmrna.gff'
  Crispr Terms:
    text: Crispr Terms
    description: Crispr Terms
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_crt.crisprs'
  Product Names:
    text: Product Names
    description: Product names file
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_product_names.tsv'
  Gene Phylogeny tsv:
    text: Gene Phylogeny tsv
    description: Gene Phylogeny tsv
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_gene_phylogeny.tsv'
  Scaffold Lineage tsv:
    text: Scaffold Lineage tsv
    description: phylogeny at the scaffold level
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_scaffold_lineage.tsv'
  Clusters of Orthologous Groups (COG) Annotation GFF:
    text: Clusters of Orthologous Groups (COG) Annotation GFF
    description: GFF3 format file with COGs
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_cog.gff'
  KO_EC Annotation GFF:
    text: KO_EC Annotation GFF
    description: GFF3 format file with KO_EC
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_ko_ec.gff'
  CATH FunFams (Functional Families) Annotation GFF:
    text: CATH FunFams (Functional Families) Annotation GFF
    description: GFF3 format file with CATH FunFams
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_cath_funfam.gff'
  SUPERFam Annotation GFF:
    text: SUPERFam Annotation GFF
    description: GFF3 format file with SUPERFam
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_supfam.gff'
  SMART Annotation GFF:
    text: SMART Annotation GFF
    description: GFF3 format file with SMART
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_smart.gff'
  Pfam Annotation GFF:
    text: Pfam Annotation GFF
    description: GFF3 format file with Pfam
    annotations:
      file_name_pattern:
        tag: file_name_pattern
        value: '[GOLD-AP]_pfam.gff'
  Annotation Statistics:
    text: Annotation Statistics
    description: Annotation statistics report
  Direct Infusion FT ICR-MS Raw Data:
    text: Direct Infusion FT ICR-MS Raw Data
    description: Direct infusion 21 Tesla Fourier Transform ion cyclotron resonance
      mass spectrometry raw data acquired in broadband full scan mode
  LC-DDA-MS/MS Raw Data:
    text: LC-DDA-MS/MS Raw Data
    description: Liquid chromatographically separated MS1 and Data-Dependent MS2 binary
      instrument file

```
</details>