# Apache Beam Apps

## Instructions on setting up Apache Beam in GCP Cloud Shell

In GCP Cloud Shell, type **python3** command at command line. If this returns an error, follow these steps ( otherwise type exit() )...

```
# install pyenv to install python on persistent home directory
curl https://pyenv.run | bash

# add to path
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# updating bashrc
source ~/.bashrc

# install python 3.7.4 and make default
pyenv install 3.7.4
pyenv global 3.7.4
```  


**Now to install Apache Beam with [gcp] components**  
so you can also utilise the Google Dataflow implementation of Beam**

``` 
pip install wheel
pip install 'apache-beam[gcp]'
``` 


## GCS to GCS

If you are here for the GCS to GCS sample, it is assumed you have Python3 and apache_beam python package installed.
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