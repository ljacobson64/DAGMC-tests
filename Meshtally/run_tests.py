import os, sys, inspect

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import mcnp_testing as mt

args = mt.parse_args()

names = ["conformal_cyl1", "conformal_cyl2", "energy_groups", "gradient_flux",
         "material_discontinuity", "metroid", "mode_np",
         "reflecting_boundaries", "squares", "stu_cyl", "stu_cyl2",
         "tally_multipliers", "uniform_flux", "uniform_vol_source"]

if args.tests == "all":
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = mt.mcnp_test(name, args)
    test = tests[name]

    # Directories
    test.dirs["orig"] = current_dir
    test.dirs["input"] = os.path.join("Inputs", test.name)

    # Common input
    test.inputs["inp"] = test.name + ".inp"

    # Common output
    test.outputs["outp"] = "outp"
    test.outputs["mctal"] = "mctal"

    # Special input
    if name in ["conformal_cyl1", "conformal_cyl2", "metroid", "stu_cyl",
                "stu_cyl2"]:
        test.dirs["gcad"] = test.dirs["input"]
        test.inputs["gcad"] = "geom_" + test.name + ".h5m"
    if name in ["stu_cyl", "stu_cyl2"]:
        test.dirs["sat"] = test.dirs["input"]
        test.other["sat"] = "geom_" + test.name + ".sat"

    # Mesh tallies
    if name in ["conformal_cyl1"]:
        test.meshtals.append("left_cylinder.h5m")
    if name in ["conformal_cyl2"]:
        test.meshtals.append("right_cylinder.h5m")
    if name in ["energy_groups"]:
        test.meshtals.append("mcnp_mesh.h5m")
        test.meshtals.append("boron_tet_mesh.h5m")
        test.meshtals.append("water_tet_mesh.h5m")
    if name in ["gradient_flux"]:
        test.meshtals.append("mcnp_mesh.h5m")
        test.meshtals.append("tet_mesh.h5m")
    if name in ["material_discontinuity"]:
        test.meshtals.append("mcnp_mesh.h5m")
        test.meshtals.append("steel_tet_mesh.h5m")
        test.meshtals.append("water_tet_mesh.h5m")
    if name in ["metroid"]:
        test.meshtals.append("vol2345.h5m")
    if name in ["mode_np"]:
        test.meshtals.append("mcnp_mesh.h5m")
        test.meshtals.append("steel_tet_mesh.h5m")
        test.meshtals.append("water_tet_mesh.h5m")
    if name in ["reflecting_boundaries"]:
        test.meshtals.append("mcnp_mesh.h5m")
        test.meshtals.append("tet_mesh.h5m")
    if name in ["squares"]:
        test.meshtals.append("cylinder.h5m")
        test.meshtals.append("twospheres.h5m")
    if name in ["stu_cyl"]:
        test.meshtals.append("tallyTetMesh.h5m")
    if name in ["stu_cyl2"]:
        test.meshtals.append("tallyTetMesh.h5m")
    if name in ["tally_multipliers"]:
        test.meshtals.append("mcnp_mesh.h5m")
        test.meshtals.append("steel_tet_mesh.h5m")
        test.meshtals.append("water_tet_mesh.h5m")
    if name in ["uniform_flux"]:
        test.meshtals.append("mcnp_mesh.h5m")
        test.meshtals.append("tet_mesh.h5m")
    if name in ["uniform_vol_source"]:
        test.meshtals.append("tet_mesh.h5m")

mt.run_multiple_tests(names_to_run, tests, args)
