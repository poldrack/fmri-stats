import nibabel
import numpy
from statsmodels.sandbox.stats.multicomp import multipletests
import scipy.stats


maskimg=nibabel.load('mask.nii.gz')
mask=maskimg.get_data()
maskvox=numpy.where(mask)

for n in [25,50,75,100,125]:
    img=nibabel.load('tt_%dsubs_tstat1.nii.gz'%n)
    data=img.get_data()
    
    d=data[maskvox]
    p=1 - scipy.stats.t.cdf(d,n)
    fdr_p=multipletests(p,0.05,method='fdr_by')
    oneminusp=1 - fdr_p[1]
    oneminusp_img=numpy.zeros(mask.shape)
    oneminusp_img[maskvox]=oneminusp
    newimg=nibabel.Nifti1Image(oneminusp_img,maskimg.get_affine())
    newimg.to_filename('fdr_1minusp_%dsubs.nii.gz'%n)
