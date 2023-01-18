gcloud auth list

gcloud dataproc clusters create cluster-spark \
    --optional-components=JUPYTER \
    --region europe-west1 \
	--zone europe-west1-b \
	--master-machine-type n2-standard-4 \ 
	--master-boot-disk-size 500 \
	--num-workers 2 \
	--worker-machine-type n2-standard-4 \
	--worker-boot-disk-size 500 \
    --enable-component-gateway \
	--project comp548dl-big-data
    
gcloud dataproc clusters create cluster-spark \
    --optional-components=ANACONDA,JUPYTER \
    --region=europe-west1  \
    --image-version=1.5 \
	--num-workers 2 \
    --enable-component-gateway








