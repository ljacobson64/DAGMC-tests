import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['conformal_cyl1', 'conformal_cyl2', 'energy_groups', 'gradient_flux',
         'material_discontinuity', 'metroid', 'mode_np',
         'reflecting_boundaries', 'squares', 'stu_cyl', 'stu_cyl2',
         'tally_multipliers', 'uniform_flux', 'uniform_vol_source']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp5'

    # Input file name format
    test.inputs['inp'] = test.name + '.inp'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # No GCAD input
    if name in ['energy_groups', 'gradient_flux', 'material_discontinuity',
                'mode_np', 'reflecting_boundaries', 'tally_multipliers',
                'uniform_flux', 'uniform_vol_source']:
        del test.inputs['gcad']

    # Tetmeshes
    test.dirs['meshes'] = 'Files'
    if name in ['conformal_cyl1']:
        test.meshes.append('left_cylinder.h5m')
    if name in ['conformal_cyl2']:
        test.meshes.append('right_cylinder.h5m')
    if name in ['energy_groups']:
        test.meshes.append('mcnp_mesh.h5m')
        test.meshes.append('boron_tet_mesh.h5m')
        test.meshes.append('water_tet_mesh.h5m')
    if name in ['gradient_flux']:
        test.meshes.append('mcnp_mesh.h5m')
        test.meshes.append('tet_mesh.h5m')
    if name in ['material_discontinuity']:
        test.meshes.append('mcnp_mesh.h5m')
        test.meshes.append('steel_tet_mesh.h5m')
        test.meshes.append('water_tet_mesh.h5m')
    if name in ['metroid']:
        test.meshes.append('vol2345.h5m')
    if name in ['mode_np']:
        test.meshes.append('mcnp_mesh.h5m')
        test.meshes.append('steel_tet_mesh.h5m')
        test.meshes.append('water_tet_mesh.h5m')
    if name in ['reflecting_boundaries']:
        test.meshes.append('mcnp_mesh.h5m')
        test.meshes.append('tet_mesh.h5m')
    if name in ['squares']:
        test.meshes.append('cylinder.h5m')
        test.meshes.append('twospheres.h5m')
    if name in ['stu_cyl']:
        test.meshes.append('tallyTetMesh.h5m')
    if name in ['stu_cyl2']:
        test.meshes.append('tallyTetMesh.h5m')
    if name in ['tally_multipliers']:
        test.meshes.append('mcnp_mesh.h5m')
        test.meshes.append('steel_tet_mesh.h5m')
        test.meshes.append('water_tet_mesh.h5m')
    if name in ['uniform_flux']:
        test.meshes.append('mcnp_mesh.h5m')
        test.meshes.append('tet_mesh.h5m')
    if name in ['uniform_vol_source']:
        test.meshes.append('tet_mesh.h5m')

    # MESHTAL output
    test.outputs['meshtal'] = 'meshtal'

    # VTK output
    if name in ['mode_np', 'stu_cyl2']:
        test.outputs['meshtal4'] = 'test_meshtal4.vtk'
    if name in ['energy_groups', 'material_discontinuity', 'metroid',
                'mode_np', 'tally_multipliers']:
        test.outputs['meshtal14'] = 'test_meshtal14.vtk'
    if name in ['conformal_cyl1', 'conformal_cyl2', 'energy_groups',
                'gradient_flux', 'material_discontinuity', 'mode_np',
                'reflecting_boundaries', 'stu_cyl', 'tally_multipliers',
                'uniform_flux', 'uniform_vol_source']:
        test.outputs['meshtal24'] = 'test_meshtal24.vtk'
    if name in ['conformal_cyl1', 'conformal_cyl2', 'energy_groups',
                'gradient_flux', 'material_discontinuity', 'mode_np',
                'reflecting_boundaries', 'squares', 'stu_cyl',
                'tally_multipliers', 'uniform_flux', 'uniform_vol_source']:
        test.outputs['meshtal34'] = 'test_meshtal34.vtk'
    if name in ['conformal_cyl1', 'conformal_cyl2', 'energy_groups',
                'gradient_flux', 'material_discontinuity', 'mode_np',
                'reflecting_boundaries', 'squares', 'stu_cyl',
                'tally_multipliers', 'uniform_flux', 'uniform_vol_source']:
        test.outputs['meshtal44'] = 'test_meshtal44.vtk'
    if name in ['conformal_cyl1', 'conformal_cyl2', 'energy_groups',
                'gradient_flux', 'material_discontinuity', 'mode_np',
                'reflecting_boundaries', 'squares', 'stu_cyl',
                'tally_multipliers', 'uniform_vol_source']:
        test.outputs['meshtal54'] = 'test_meshtal54.vtk'
    if name in ['stu_cyl', 'stu_cyl2']:
        test.outputs['meshtal64'] = 'test_meshtal64.vtk'

    return test

def setup_tests(names, args):
    tests = []
    for name in names:
        tests.append(setup_test(name, args))
    return tests

args = dagtest.parse_args()

if __name__ != '__main__':
    args.tests = 'all'
if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = setup_tests(names_to_run, args)

if __name__ == '__main__':
    dagtest.run_multiple_tests(names_to_run, tests, args)
