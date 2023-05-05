import os
import nibabel as nib
import numpy as np
from tqdm import trange

def main(_root):
    save_r = 'data'
    LorR = 'L'
    flist = os.listdir(_root)
    surf_paths = [os.path.join(_root, f, 'MNINonLinear', f'{f}.{LorR}.pial.32k_fs_LR.surf.gii') for f in flist]
    surf_paths = [p for p in surf_paths if os.path.exists(p)]
    # label_paths = [os.path.join(_root, f, 'MNINonLinear', 'lh.aparc.annot') for f in flist]
    average_surf = []
    for i in trange(len(surf_paths)):
        # surf = nib.freesurfer.io.read_geometry(surf_paths[i])
        surf = nib.load(surf_paths[i]).darrays
        vert = surf[0].data
        average_surf.append(vert)

    average_surf = np.stack(average_surf)
    average_surf = average_surf.mean(0)
    print(average_surf.shape)
    np.save(f'{save_r}/HCP_YA_{LorR}_average_surf_vertex.npy', average_surf)
    np.save(f'{save_r}/HCP_YA_{LorR}_average_surf_triangle_face.npy', surf[1].data)

if __name__ == "__main__":
    main('/lichtman/HCP_YA_surface/')