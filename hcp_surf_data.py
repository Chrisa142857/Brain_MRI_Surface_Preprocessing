import os
import nibabel as nib
import numpy as np
from tqdm import trange

def load_bold_time_series_in_surf(surf_p, fmri_p):
    fmri = nib.load(fmri_p).get_fdata()
    mri_shape = fmri.shape
    surf = nib.load(surf_p).darrays
    lvert = surf[0].data
    lface = surf[1].data
    surf = nib.load(surf_p.replace('L.pial.32k_fs_LR.surf.gii', 'R.pial.32k_fs_LR.surf.gii')).darrays
    rvert = surf[0].data
    rface = surf[1].data
    lvert[:, 0] += (mri_shape[0])
    lvert[:, 1] += (mri_shape[1])
    lvert[:, 2] += (mri_shape[2])
    rvert[:, 0] += (mri_shape[0])
    rvert[:, 1] += (mri_shape[1])
    rvert[:, 2] += (mri_shape[2])
    verts = np.concatenate([lvert, rvert])

def main(_root):
    save_r = 'data'
    LorR = 'L'
    flist = os.listdir(_root)
    surf_paths = [os.path.join(_root, f, 'MNINonLinear', f'{f}.{LorR}.pial.32k_fs_LR.surf.gii') for f in flist]
    label_paths = [os.path.join(_root, p.split('/')[-3], 'MNINonLinear', '%s.%s.aparc.32k_fs_LR.label.gii' % (p.split('/')[-3], LorR)) for p in surf_paths]
    surf_paths = [p for p, lp in zip(surf_paths, label_paths) if os.path.exists(p) and os.path.exists(lp)]
    label_paths = [os.path.join(_root, p.split('/')[-3], 'MNINonLinear', '%s.%s.aparc.32k_fs_LR.label.gii' % (p.split('/')[-3], LorR)) for p in surf_paths]
    label_paths = [lp for p, lp in zip(surf_paths, label_paths) if os.path.exists(p) and os.path.exists(lp)]
    # label_paths = [os.path.join(_root, f, 'MNINonLinear', 'lh.aparc.annot') for f in flist]
    average_surf = []
    labels = []
    fmri = nib.load('data/rfMRI_REST1_LR.nii.gz').get_fdata()
    mri_shape = fmri.shape
    for i in trange(len(surf_paths)):
        # surf = nib.freesurfer.io.read_geometry(surf_paths[i])
        # label = nib.load(label_paths[i]).darrays[0].data
        surf = nib.load(surf_paths[i]).darrays
        lvert = surf[0].data
        surf = nib.load(surf_paths[i].replace('L.pial.32k_fs_LR.surf.gii', 'R.pial.32k_fs_LR.surf.gii')).darrays
        rvert = surf[0].data
        # average_surf.append(vert)
        # labels.append(label)

    average_surf = np.stack(average_surf)
    average_surf = average_surf.mean(0)
    print(average_surf.shape)
    np.save(f'{save_r}/HCP_YA_{LorR}_average_surf_vertex.npy', average_surf)
    np.save(f'{save_r}/HCP_YA_{LorR}_average_surf_triangle_face.npy', surf[1].data)
    np.save(f'{save_r}/HCP_YA_{LorR}_average_surf_label.npy', labels[-1])

if __name__ == "__main__":
    main('/lichtman/HCP_YA_surface/')