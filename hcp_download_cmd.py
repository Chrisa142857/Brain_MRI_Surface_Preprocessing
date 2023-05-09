with open('hcp_ya_subject_list.txt','r') as f:
    lines = f.read().split('\n')

save_r = '/lichtman/HCP_YA_surface'
lines =lines[:-1]
s3_cmd = 'aws s3 cp s3://hcp-openaccess'
cmdlines=''
for l in lines:
    items =  l.split('/HCP_1200/')
    id = items[1]
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.L.pial.164k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.pial.164k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.L.pial_MSMAll.164k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.pial_MSMAll.164k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.R.pial.164k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.pial.164k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.R.pial_MSMAll.164k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.pial_MSMAll.164k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.L.aparc.164k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.aparc.164k_fs_LR.label.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.L.aparc.a2009s.164k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.aparc.a2009s.164k_fs_LR.label.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.R.aparc.164k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.aparc.164k_fs_LR.label.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/'+id+'.R.aparc.a2009s.164k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.aparc.a2009s.164k_fs_LR.label.gii\n'

    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.L.pial.32k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.pial.32k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.L.pial_MSMAll.32k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.pial_MSMAll.32k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.R.pial.32k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.pial.32k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.R.pial_MSMAll.32k_fs_LR.surf.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.pial_MSMAll.32k_fs_LR.surf.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.L.aparc.32k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.aparc.32k_fs_LR.label.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.L.aparc.a2009s.32k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.L.aparc.a2009s.32k_fs_LR.label.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.R.aparc.32k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.aparc.32k_fs_LR.label.gii\n'
    cmdlines += s3_cmd+'/HCP_1200/'+id+'/MNINonLinear/fsaverage_LR32k/'+id+'.R.aparc.a2009s.32k_fs_LR.label.gii '+save_r+'/'+id+'/MNINonLinear/'+id+'.R.aparc.a2009s.32k_fs_LR.label.gii\n'

with open('download_cmd.sh','w') as f:
    f.write(cmdlines)