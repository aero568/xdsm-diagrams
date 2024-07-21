from pyxdsm.XDSM import (
    XDSM,
    OPT,
    FUNC,
    LEFT,
)

x = XDSM(
    auto_fade={
        # "inputs": "none",
        "outputs": "connected",
        "connections": "outgoing",
        # "processes": "none",
    }
)

# sytem buildup
x.add_system("opt", OPT, r"\text{Optimizer}")
x.add_system("fun",FUNC, "function")
x.add_system("g1", FUNC, "constraint1")
x.add_system("g2", FUNC, "constraint2")

# function connection
x.add_process(
    ["opt", "fun", "g1", "g2","opt"],
    arrow=True,
)

# functions IO
x.connect("opt", "fun", ["x1", "x2"], label_width=1)
x.connect("opt", "g1", ["x1", "x2"], label_width=1)
x.connect("opt", "g2", ["x1", "x2"], label_width=1)
x.connect("fun", "opt", ["obj"], label_width=1)
x.connect("g1", "opt", ["g1"], label_width=1)
x.connect("g2", "opt", ["g2"], label_width=1)


# inputs
x.add_input("opt", ["x1^{(0)}","x2^{(0)}"])

# outputs
x.add_output("opt", ["x1^*","x2^*"], side=LEFT)
x.add_output("fun","obj^*", side=LEFT)
x.add_output("g1", "g1^*", side=LEFT)
x.add_output("g2", "g2^*", side=LEFT)

# write diagram
x.write("two-dimensional", cleanup=True)
