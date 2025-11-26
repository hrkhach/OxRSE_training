import pybamm

model = pybamm.lithium_ion.DFN()

# simulation = pybamm.Simulation(model=model)
#
# simulation.solve([0,3600])
#
# simulation.plot()
#
# models = [
#     pybamm.lithium_ion.SPM(),
#     pybamm.lithium_ion.SPMe(),
#     pybamm.lithium_ion.DFN(),
# ]
#
# simulations = []
# for model in models:
#     simulation = pybamm.Simulation(model=model)
#     simulation.solve([0,3600])
#     simulations.append(simulation)
#
# pybamm.dynamic_plot(simulations)
#
# # Basic plotting
# output_variables = ["Voltage [V]", "Current [A]"]
# simulation.plot(output_variables=output_variables)
#
# output_variables = [
#     "Voltage [V]",
#     ["Electrode current density [A.m-2]", "Electrolyte current density [A.m-2]"],
# ]
# simulation.plot(output_variables=output_variables)
#
# print(model.variable_names())
# print(model.variables.search("electrolyte"))
#
# parameter_values = pybamm.ParameterValues("Chen2020")
# simulation = pybamm.Simulation(model=model, parameter_values=parameter_values)
# simulation.solve([0,3600])
# simulation.plot()
#
#
# # Running experiments
# simulation = pybamm.Simulation(model, experiment="Discharge at 3C until 3.3 V")
# simulation.solve([0,3600])
# simulation.plot()

# Printing citations
pybamm.print_citations()