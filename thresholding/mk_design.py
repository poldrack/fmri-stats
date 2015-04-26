import glob,os

basedir='/corral-repl/utexas/poldracklab/UCLA/CNP/CONTROLS'

featdirs=glob.glob(os.path.join(basedir,'CNP_*B/analysis/STOPSIGNAL/level1_STOPSIGNAL_model1.feat'))


# need to add:
# #set fmri(outputdir) "go_cluster"
# set feat_files(1) "/corral-repl/utexas/poldracklab/UCLA/CNP/CONTROLS/CNP_10150B/analysis/STOPSIGNAL/level1_STOPSIGNAL_model1.feat"
# #set fmri(ncopeinputs) 9

run_file=open('run_feats.sh','w')

for nsubs in [25,50,75,100,125,len(featdirs)]:
    stub=open('design_cluster.stub').readlines()

    outfile=open('design_cluster_%dsubs.fsf'%nsubs,'w')
    for l in stub:
        outfile.write(l)
    outfile.write('set fmri(outputdir) "go_cluster_%dsubs"\n'%nsubs)
    outfile.write('set fmri(npts) %d\n'%nsubs)
    outfile.write('set fmri(multiple) %d\n'%nsubs)

    ctr=1
    for f in featdirs[:nsubs]:
        outfile.write('set feat_files(%d) "%s"\n'%(ctr,f))
        outfile.write('set fmri(evg%d.1) 1\n'%ctr)
        outfile.write('set fmri(groupmem.%d) 1\n'%ctr)

        ctr+=1
    outfile.close()
    run_file.write('feat design_cluster_%dsubs.fsf\n'%nsubs)
run_file.close()
