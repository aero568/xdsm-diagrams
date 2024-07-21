import openmdao.api as om
from omxdsm import write_xdsm

# build the model
prob = om.Problem()
prob.model.add_subsystem(
    "function",
    om.ExecComp("obj = (1 - x1) ** 2 + (1 - x2) ** 2 + 0.5 * (2 * x2 - x1**2) ** 2"),
    promotes=["x1", "x2", "obj"],
)
prob.model.add_subsystem(
    "constraint1",
    om.ExecComp("g1 = x1**2+x2**2"),
    promotes=["x1", "x2", "g1"],
)
prob.model.add_subsystem(
    "constraint2",
    om.ExecComp("g2 = x1-3*x2+0.5"),
    promotes=["x1", "x2", "g2"],
)

# setup the optimization
prob.driver = om.ScipyOptimizeDriver()
prob.driver.options["optimizer"] = "SLSQP"
prob.model.add_design_var("x1", lower=0)
prob.model.add_design_var("x2", lower=0)
prob.model.add_constraint("g1", upper=1.0)
prob.model.add_constraint("g2", lower=0.0)
prob.model.add_objective("obj")
prob.setup()

# set initial values
prob.set_val("x1", 0.0)
prob.set_val("x2", 0.0)

# xsdm diagram
write_xdsm(
    prob,
    filename="two-dimensional",
    out_format="pdf",
    show_browser=True,
    quiet=False,
    output_side="left",
    include_indepvarcomps=False,
    class_names=False,
)
