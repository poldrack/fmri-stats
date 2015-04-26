import glob

images=glob.glob('data/randomize*/*')

for i in images:
    cmd='fslcpgeom data/bg_image.nii.gz %s'%i
    print cmd