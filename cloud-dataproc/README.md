# Google Cloud Dataproc

## Create a Dataproc cluster 
```
gcloud dataproc clusters create cluster-spark \
    --optional-components=ANACONDA,JUPYTER \
    --region=europe-west1  \
    --image-version=1.5 \
	  --num-workers 2 \
    --enable-component-gateway
 ```
 
## Spark code to write, read the data Python


## Submit the PySpark job
``` 
gcloud dataproc jobs submit pyspark \
--project=${PROJECT} \
  --region=${REGION} \
  --cluster=${CLUSTER} \
  --properties='gs://dataproc-staging-europe-west1-195784541669-dywzhoac/notebooks/jupyter/aggr_air_quality_data.py'
```  

### PySpark Succeded
![image](https://user-images.githubusercontent.com/92388643/213895148-b7545f6f-dd5b-40ec-9954-5cc71fcda006.png)
