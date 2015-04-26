import glob

images=glob.glob('data/randomize*/*nii.gz')+glob.glob('data/*nii.gz')

for i in images:
    cmd='fslcpgeom data/bg_image.nii.gz %s'%i
    print cmd