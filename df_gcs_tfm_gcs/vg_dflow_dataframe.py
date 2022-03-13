import apache_beam as beam
from apache_beam.dataframe.io import read_csv, to_csv
"""
https://beam.apache.org/releases/pydoc/2.33.0/apache_beam.dataframe.io.html#apache_beam.dataframe.io.read_csv
https://beam.apache.org/releases/pydoc/2.33.0/apache_beam.dataframe.frames.html#apache_beam.dataframe.frames.DeferredSeries.to_csv

non-df
https://beam.apache.org/documentation/transforms/python/aggregation/groupby/

gsutil cat gs://cloud-samples-data/bigquery/sample-transactions/transactions.csv | head
    timestamp, origin, destination, transaction_amount
    2009-01-09 02:54:25 UTC,wallet00000e719adfeaa64b5a,wallet00001866cb7e0f09a890,1021101.99
    2017-01-01 04:22:23 UTC,wallet00000e719adfeaa64b5a,wallet00001e494c12b3083634,19.95
"""

with beam.Pipeline() as p:
   df = p | beam.dataframe.io.read_csv(
        path = 'gs://cloud-samples-data/bigquery/sample-transactions/transactions.csv'
        , usecols = ['timestamp', 'transaction_amount']
        , parse_dates = ['timestamp']
    )
   
   df1 = df[ (df.timestamp >= '2010-01-01 00:00:00 UTC') & (df.transaction_amount > 20) ]
   df1.timestamp = df.timestamp.dt.date

   # ISSUE 1
   # using .reset_index() to retain date column in aggregated output but get...
   #   raise NonParallelOperation("reset_index(level=None) cannot currently be parallelized (BEAM-12182)
   # result > output missing date
   df2 = df1.rename(columns={"timestamp": "date", "transaction_amount": "total_amount"}).groupby('date').sum() #.reset_index()

   # ISSUE 2
   # compression not working, get...
   #   NotImplementedError: compression
   # result > output not compressed
   df2.to_csv(path = './output/results.csv', index = False)
   #df2.to_csv(path = 'gs://dflow-out/output/results.csv', index = False) # compression = 'gzip'