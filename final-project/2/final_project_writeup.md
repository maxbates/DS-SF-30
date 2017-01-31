# DNA Assembly Prediction

**When a researcher is designing and ordering segments of DNA, can we predict what larger organism / gene they are designing?**

### Background

DNA is generally ordered in small fragments, ranging from about 20 bases, and technologically limited at 2000 bases.

Genes are generally on the order of hundreds of bases of DNA. Each 3 base combination of A, C, G, T correlates with a specific amino acid, the building blocks of proteins.

In genetic engineering, scientists often seek to introduce novel or mutated genes into an organism to change its metabolism, often to generate some molecular product. Genetic engineers sometimes combine genes from different organisms, but more common is to randomly or slightly but specifically modify a gene to modify its effect.

### Motivation

There is significant effort that goes into buildilng the experimental organisms, screening them for metabolic changes, and finding similar genes to further fine-tune the designer gene or metabolic circuit.

In the design space, offering suggestions of similar parts, especially when those parts are tied to known metabolic perturbations, greatly tightens the cycle of designing and then building and screening engineering organisms.

Companies which synthesize DNA are also keen to sell you more DNA, and would greatly benefit from being able to offer helpful suggestions ad additions.

Screening genes being designed is also important in the context of biosecurity, to ensure that the designers are not attempting to build nefarious organisms, or engineer metabolic circuits which produce dangerous or illegal compounds.

Currently, the only screening which happens at all but a handful of companies is at the time of order, without looking at all the customer's orders, and there is no screening in design software.

## Outline

### Data Available

As a foundational step to the above goals, we will attempt to determine the genes / organisms a customer is attempting to design, based on the several sequences of DNA which they order.

Many genes and organisms have been sequenced, and their sequence is available online at NCBI, each with a unique accession ID. There is a querying method called BLAST which allows a scientist to find DNA and protein sequences which are similar to the one passed. BLAST queries return several hits, each with a DNA alignment and score measuring the probability of the match.

Companies do not distribute their placed orders, though may if this model proves to be of potential benefit. 

There is also effectively no public information tying variations of sequences with any experimental data, so optimization is difficult to model. This IP is closesly guarded in the couple of companies which curate it.

### Generating data

The millions of sequences available in NCBI can be broken up into smaller fragments, and BLASTed - generating a large feature set of fragments and their alignments, with each fragment still associated with its source organism.

This data can be used to build a model, given some random or curated subset of fragments, which predicts the genes / organisms being designed or modified.

The pipeline will pull in records from NCBI, ranging from small segments to genes to chromosomes. It will generate a collection of fragments, and run a BLAST query for each of them, and store the raw XML results as a file. The results will then be parsed, and stored separately.

BLAST query results include expectation score, alignment length, several parameters, information about the match, etc. [described here](http://biopython.org/DIST/docs/tutorial/Tutorial.html#fig:blastrecord).

BLAST queries often take between 10-60 seconds.

## Questions + risks, definition of success

There is a lot of work to do for this project. Setting up the infrastructure for the information processing pipeline is no small feat.

The major hypothesis is that aggregating BLAST queries across multiple fragments or orders for a particular customer will allow for predictions that are more insightful than simple BLAST querying of the individual component fragments.

Generating a reasonable large dataset will not be too difficult, but it may be necessary to scope it to a few organisms for training, in order to generate the BLAST information sets in reasonable time. Training and assessing a model with just a few input organisms should not dramatically affect its translatability to information sets with more organisms.

More difficult to approximate will be a realistic set of fragments comprising an order. For this initial project, a probably not super valid assumption will be that that the fragmentation and aggregation into an "order" that I do is at all realistic.


