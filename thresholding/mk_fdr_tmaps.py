nvals=[25,50,75,100,125]
for n in nvals:
    cmd='fslmaths data/fdr_1minusp_%dsubs.nii.gz -mul data/tt_%dsubs_tstat1.nii.gz data/fdr_tstat_%dsubs.nii.gz'%(n,n,n)
    print cmd