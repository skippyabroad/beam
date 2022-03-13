# Apache Beam apps

## GCS to GCS

If here for the GCS to GCS sample, it is assumed you have Python3 and apache_beam python package installed.
Once this is the case you can run the following code block, which clones the repo, changes into app path and:
- takes gs://cloud-samples-data/bigquery/sample-transactions/transactions.csv
- performs various filtering and aggregations
- outputs result to a git-ignored /output path within this repo

```
git clone https://github.com/skippyabroad/beam.git
cd beam/df_gcs_tfm_gcs
python3 vg_dflow_dataframe.py
```

**NB:**   

**Due to limited time and not having used Apached Beam before, the beam dataframe api was utilized.**  
**Also, only 1 of 2 tasks was attempted.**

While, the correct 3 aggregated results are derived, some limitations were hit with the dataframe api implementation, for which work-arounds could not be found in the time available.

The exact issues are documented inline in vg_dflow_dataframe.py

### DataflowRunner module

In preparation for conversion to beam transform (as opposed to dataframe api use) and in preparation for **Task #2**  
a beam module **df_gcs_tfm_gcs.py** was started and may be continued at a later date.


## other apps (TBC)