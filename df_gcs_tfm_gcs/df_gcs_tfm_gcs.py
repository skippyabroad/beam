#-*- coding: utf-8 -*-
import apache_beam as beam
#import csv
#import json
#import os
#import re


job = 'sample-transactions-tfm'
src = 'gs://cloud-samples-data/bigquery/sample-transactions/transactions.csv'
pfx = '/output/'
fle = 'results.csv'

def tfm():
    #
    yield ''


def run(project, bucket, region, result_output) :

    argv = [
        "--project={0}".format(project),
        "--job_name={0}".format(job),
        "--save_main_session",
        "--region={0}".format(region),
        "--staging_location=gs://{0}/staging/".format(bucket),
        "--temp_location=gs://{0}/temp/".format(bucket),
        "--max_num_workers=8",
        "--worker_region={0}".format(region),
        "--worker_disk_type=compute.googleapis.com/projects//zones//diskTypes/pd-ssd",
        "--autoscaling_algorithm=THROUGHPUT_BASED",
        "--runner=DataflowRunner"
    ]

    pipeline = beam.Pipeline(argv=argv)
    ptransform = (pipeline
                    | "Read from GCS" >> beam.io.ReadFromText(src)
                    # FlatMap is like :class:ParDo except it takes a callable to specify the transformation.
                    # The callable must return an iterable for each element of the input 
                    | job >> beam.FlatMap(tfm)
                    )
  
    (ptransform
    | "events:out" >> beam.io.WriteToText(
            result_output
        )
     )
    
    pipeline.run()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run pipeline using this module")
    parser.add_argument("--region",     dest="region",  help="region for processing, match to destintation Bucket region")
    parser.add_argument("--project",    dest="project", help="projectID for processing", required=True)
    parser.add_argument("--bucket",     dest="bucket",  help="destintation Bucket", required=True)

    args = vars(parser.parse_args())

    region  = args["region"]
    project = args["project"]
    bucket  = args["bucket"]

    result_output = 'gs://{}/{}/{}'.format(bucket, pfx, fle)
    print( "Proceeding to perform {} from {} to {}".format(job, src, result_output) )

    run( region, project, bucket, result_output )