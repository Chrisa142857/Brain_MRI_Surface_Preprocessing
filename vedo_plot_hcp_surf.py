"""Manually build a mesh from points and faces"""
from vedo import Mesh, show
import nibabel as nib
import os, random

def load_unproc_surf():
    r = r'C:\Users\home\Documents\HCP YA\100206'
    lh_path = os.path.join(r, 'lh.pial')
    lh_label = os.path.join(r, 'lh.aparc.annot')
    lh=nib.freesurfer.io.read_geometry(lh_path)
    labels = nib.freesurfer.io.read_annot(lh_label)[0]
    verts = lh[0]
    faces = lh[1]
    return verts, faces, labels

def load_proc_surf():
    r = r'C:\Users\home\Documents\HCP YA\100206\MNINonLinear'
    lh_path = os.path.join(r, 'lh.pial')
    lh_label = os.path.join(r, 'lh.aparc.annot')
    lh=nib.freesurfer.io.read_geometry(lh_path)
    labels = nib.freesurfer.io.read_annot(lh_label)[0]
    verts = lh[0]
    faces = lh[1]
    return verts, faces, labels

verts, faces, labels = load_proc_surf()
# Build the polygonal Mesh object from the vertices and faces
mesh = Mesh([verts, faces])
colors = []
for i in range(labels.max()):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors.append((r / 255.0, g / 255.0, b / 255.0))
# Set the backcolor of the mesh to violet
# and show edges with a linewidth of 2
mesh.backcolor('violet').linecolor(None)#.linewidth(0.5)
mesh.cmap(colors, labels, alpha=1).add_scalarbar()

# Create labels for all vertices in the mesh showing their ID
# tlabs = mesh.labels('id').c('black')

# Print the points and faces of the mesh as numpy arrays
print('points():', mesh.points().shape)
print('faces() :', len(mesh.faces()))

# Show the mesh, vertex labels, and docstring
show(mesh, __doc__, viewup='z', axes=1).close()