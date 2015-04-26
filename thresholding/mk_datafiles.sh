#cp go_cluster_125subs.gfeat/cope1.feat/filtered_func_data.nii.gz funcdata_125subs.nii.gz
#fslroi funcdata_125subs.nii.gz funcdata_25subs.nii.gz 0 25
#fslroi funcdata_125subs.nii.gz funcdata_50subs.nii.gz 0 50
#fslroi funcdata_125subs.nii.gz funcdata_75subs.nii.gz 0 75
#fslroi funcdata_125subs.nii.gz funcdata_100subs.nii.gz 0 100

cp go_cluster_125subs.gfeat/cope1.feat/stats/res4d.nii.gz res4d_125subs.nii.gz
fslroi res4d_125subs.nii.gz res4d_25subs.nii.gz 0 25
fslroi res4d_125subs.nii.gz res4d_50subs.nii.gz 0 50
fslroi res4d_125subs.nii.gz res4d_75subs.nii.gz 0 75
fslroi res4d_125subs.nii.gz res4d_100subs.nii.gz 0 100
