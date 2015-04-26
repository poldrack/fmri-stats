
import os



for n in [25,50,75,100,125]:
    if not os.path.exists('randomize_%dsubs'%n):
        os.mkdir('randomize_%dsubs'%n)

    cmd='randomise -i funcdata_%dsubs.nii.gz -o randomize_%dsubs/tt_%dsubs -1 -n 5000 -c 2.3 -C 2.3 -T'%(n,n,n)
    print cmd
    
    if not os.path.exists('randomize_%dsubs_vn'%n):
        os.mkdir('randomize_%dsubs_vn'%n)

    cmd='randomise -i funcdata_%dsubs.nii.gz -o randomize_%dsubs_vn/tt_%dsubs -1 -n 5000 -c 2.3 -C 2.3 -T -v 10'%(n,n,n)

    print cmd
