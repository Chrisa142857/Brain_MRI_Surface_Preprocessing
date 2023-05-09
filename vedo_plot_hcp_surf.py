"""Manually build a mesh from points and faces"""
from vedo import Mesh, show
import nibabel as nib
import os, random
import numpy as np

def load_unproc_surf():
    r1 = r'C:\Users\home\Documents\freesurfer_7.3.2\fs_out\subject_test\surf'
    r2 = r'C:\Users\home\Documents\freesurfer_7.3.2\fs_out\subject_test\label'
    lh_path = os.path.join(r1, 'lh.pial')
    lh_label = os.path.join(r2, 'lh.aparc.annot')
    lh=nib.freesurfer.io.read_geometry(lh_path)
    labels = nib.freesurfer.io.read_annot(lh_label)[0]
    verts = lh[0]
    faces = lh[1]
    return verts, faces, labels

def load_proc_surf():
    r = r'C:\Users\home\Documents\HCP YA\average_surf'
    p = os.path.join(r, 'HCP_YA_L_average_surf_vertex.npy')
    verts = np.load(p)
    p = os.path.join(r, 'HCP_YA_L_average_surf_triangle_face.npy')
    faces = np.load(p)
    p = os.path.join(r, 'HCP_YA_L_average_surf_label.npy')
    labels = np.load(p)
    return verts, faces, labels

def load_bold_time_series_in_surf(surf_p, fmri_p):
    fmri = nib.load(fmri_p).get_fdata()
    mri_shape = fmri.shape
    print("mri_shape", mri_shape)
    surf = nib.load(surf_p).darrays
    lvert = surf[0].data
    lface = surf[1].data
    surf = nib.load(surf_p.replace('L.pial.32k_fs_LR.surf.gii', 'R.pial.32k_fs_LR.surf.gii')).darrays
    rvert = surf[0].data
    rface = surf[1].data
    lvert[:, 0] += (mri_shape[0])
    lvert[:, 1] += (mri_shape[1])+18
    lvert[:, 2] += (mri_shape[2])-16
    rvert[:, 0] += (mri_shape[0])
    rvert[:, 1] += (mri_shape[1])+18
    rvert[:, 2] += (mri_shape[2])-16
    verts = np.concatenate([lvert, rvert])
    vol = mesh_to_volume(verts, mri_shape[:3])
    vol = nib.Nifti1Image(vol, np.eye(4))
    nib.save(vol, 'mesh_to_volume.nii.gz')
    # exit()
    return verts, np.concatenate([lface, rface+len(lvert)])

def mesh_to_volume(vert, shape):
    shape = (260, 311, 260)
    vert = (vert/0.7).astype(np.int32)
    # vert[vert[:, 0]>=91, 0] = 90
    # vert[vert[:, 1]>=109, 1] = 108
    # vert[vert[:, 2]>=91, 2] = 90
    vol = np.zeros(shape)
    vol[vert[:,0], vert[:, 1], vert[:, 2]] = 1
    return vol

verts, faces, labels = load_unproc_surf()
# verts, faces = load_bold_time_series_in_surf(
#     r'C:\Users\home\Documents\HCP YA\100206\MNINonLinear\fsaverage_LR32k\100206.L.pial.32k_fs_LR.surf.gii',
#     r'C:\Users\home\Documents\HCP YA\100206\MNINonLinear\Results\rfMRI_REST1_LR\rfMRI_REST1_LR.nii.gz'
# )
# Build the polygonal Mesh object from the vertices and faces
mesh = Mesh([verts, faces])

mesh.backcolor('violet').linecolor(None)#.linewidth(0.5)
colors = []
for i in range(labels.max()):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors.append((r / 255.0, g / 255.0, b / 255.0))
mesh.cmap(colors, labels, alpha=1).add_scalarbar()

# Print the points and faces of the mesh as numpy arrays
print('points():', mesh.points().shape)
print('faces() :', len(mesh.faces()))
# print("labels:", labels.max(), labels.shape)

# Show the mesh, vertex labels, and docstring
show(mesh, __doc__, viewup='z', axes=1).close()