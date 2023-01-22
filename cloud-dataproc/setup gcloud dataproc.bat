gcloud auth list

gcloud dataproc clusters create cluster-spark \
    --optional-components=JUPYTER \
    --region europe-west1 \
	--zone europe-west1-b \
	--master-machine-type n2-standard-2 \ 
	--master-boot-disk-size 200 \
	--num-workers 2 \
	--worker-machine-type n2-standard-2 \
	--worker-boot-disk-size 200 \
    --enable-component-gateway
    
gcloud dataproc clusters create cluster-spark \
    --optional-components=ANACONDA,JUPYTER \
    --region=europe-west1  \
    --image-version=1.5 \
	--num-workers 2 \
    --enable-component-gateway








