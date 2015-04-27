
import os
from run_shell_cmd import *
import nibabel
import numpy

dlh={}
volume={}
cdata={}
minclust={}

for n in [25,50,75,100,125]:
    if not dlh.has_key(n):
        print n,': estimating smoothness'
        l=run_shell_cmd('smoothest -d %d -r data/res4d_%dsubs.nii.gz -m mask.nii.gz'%(n,n))
        dlh[n]=float(l[0].split(' ')[1])
        volume[n]=float(l[1].split(' ')[1])
    
    if not os.path.exists('data/tt_%dsubs_tstat1.nii.gz'%n):
        print 'running randomize'
        cmd='randomise -i data/funcdata_%dsubs.nii.gz -o tt_%dsubs -1 -n 1'%(n,n)
        run_shell_cmd(cmd)

    # convert t to z stat
    tstat_img=nibabel.load('data/tt_%dsubs_tstat1.nii.gz'%n)
    tstat=tstat_img.get_data()
    zstat=t_to_z(tstat)
    zstat_img=nibabel.Nifti1Image(zstat,tstat.get_affine())
    zstat_img.to_filename('data/tt_%dsubs_zstat1.nii.gz'%n)
    cmd='cluster -i tt_%dsubs_tstat1.nii.gz -t 2.3 -p 0.05 --mm -d %f --volume=%d --minclustersize --othresh=data/thresh_%dsubs'%(n,dlh[n],volume[n],n)
    print cmd
    cdata[n]=run_shell_cmd(cmd)
    minclust[n]=int(cdata[n][0].split(' = ')[1])
