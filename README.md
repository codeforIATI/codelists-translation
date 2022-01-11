# Codelists translation using Transifex

This repository integrates with Transifex.com to translate IATI codelists.

The workflow is as follows:

1. Clone IATI XML codelist repositories.
2. Extract metadata, names and descriptions from each codelist and save as JSON files for each language and codelist.
   1. Transifex automatically pulls in this data
   2. Transifex users can do translation work
   3. When codelists are 100% translated, changes are automatically pushed back as PRs to the JSON files
3. Merge PR containing changes to the JSON files [NOT YET IMPLEMENTED]
   1. Make changes to the relevant XML file
   2. Makes a PR to the relevant codelist repository for this XML file
