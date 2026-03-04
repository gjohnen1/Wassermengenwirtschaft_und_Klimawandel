model BlueRiver
  import SI = Modelica.SIunits;
  //
  // Model objects: nodes
  // The inflow boundary condition node for the Trout Lake reservoir:
  Deltares.ChannelFlow.SimpleRouting.BoundaryConditions.Inflow TroutIn(Q(nominal = 0.8)) annotation(Placement(visible = true, transformation(origin = {11, -2}, extent = {{-5, -5}, {5, 5}}, rotation = 90)));
  // The reservoir node for Trout Lake. The nominal value is important for the optimization accuracy and performance. Ideally, the nominal value, the bounds (maximum specified here) and the goals (specified in Python) have the same order of magnitue.
  Deltares.ChannelFlow.SimpleRouting.Reservoir.Reservoir TroutLake(V(min = 0, max = 740089102.5285000, nominal = 616740918.7737500),  n_QForcing = 0) annotation(Placement(visible = true, transformation(origin = {-20, 19}, extent = {{-5, -5}, {5, 5}}, rotation = 180)));
  // the inflow point for lateral flow at Alder
  Deltares.ChannelFlow.SimpleRouting.BoundaryConditions.Inflow InflowAlder(Q(nominal = 0.2)) annotation(Placement(visible = true, transformation(origin = {-78, 19}, extent = {{-10, -10}, {4, 4}}, rotation = 90)));  
// The node that represents the confluence "Alder"
  Deltares.ChannelFlow.SimpleRouting.Nodes.Node Alder(nin = 2, nout = 1, n_QForcing = 0, QIn.Q(each nominal = 0.3), QOut.Q(each nominal = 10)) annotation(Placement(visible = true, transformation(origin = {-41, 44}, extent = {{-5, -5}, {5, 5}}, rotation = 90)));
  // The downstream node, River City
  Deltares.ChannelFlow.SimpleRouting.BoundaryConditions.Terminal RiverCity(Q(nominal = 10)) annotation(Placement(visible = true, transformation(origin = {-70, 77}, extent = {{-5, -5}, {5, 5}}, rotation = 90)));
  //
  // Model objects: branches
  // from inflow gauge to the Trout Lake Reservoir
  Deltares.ChannelFlow.SimpleRouting.Branches.Steady Inflow_TroutLake annotation(Placement(visible = true, transformation(origin = {-7, 9}, extent = {{-10, -10}, {4, 4}}, rotation = 170)));  
// the branch between Trout Lake Reservoir and Alder
  Deltares.ChannelFlow.SimpleRouting.Branches.Steady TroutLake_Alder annotation(Placement(visible = true, transformation(origin = {-33.8536, 28.5}, extent = {{-4.45711, -4.45711}, {4.45711, 4.45711}}, rotation = 135)));
  // the lateral branch
  Deltares.ChannelFlow.SimpleRouting.Branches.Steady Lateral_Alder annotation(Placement(visible = true, transformation(origin = {-60.5, 29.5}, extent = {{-4.5, -4.5}, {4.5, 4.5}}, rotation = 0)));
  // the branch between Alder and RiverCity
  Deltares.ChannelFlow.SimpleRouting.Branches.Steady Alder_RiverCity annotation(Placement(visible = true, transformation(origin = {-57.5, 58.5}, extent = {{-5.95052, -5.95052}, {5.95052, 5.95052}}, rotation = 110)));
  // External input. These variables are fed by time series.
  //
  // Inflow
  input SI.VolumeFlowRate TroutLake_Inflow(fixed = true);
  input SI.VolumeFlowRate Alder_Inflow(fixed = true);
  // The optimization variables. These are determined within the optimization
  input SI.VolumeFlowRate TroutLake_Q_turbine(min = 0, max = 115.1323355, nominal = 46.05282095, fixed = false);
  input SI.VolumeFlowRate TroutLake_Q_spill(min = 0, max = 460, nominal = 1, fixed = false);
  // the water level in the reservoir lake, only used for simulation model
  input SI.Length TroutLake_H(fixed = false);
  // Results. These variables are output in the result file.
  // Reservoir storage volume
  output SI.Volume TroutLake_V;
  // Total reservoir outflow
  output SI.VolumeFlowRate TroutLake_Q_out(min = 0, max = 575.1323355, nominal = 46.05282095);
  // Reservoir turbine flow
  output SI.VolumeFlowRate RiverCity_Q(min = 0, max = 1000, nominal = 10, fixed = false);
equation
//
// connections
  connect(Alder.QOut[1], Alder_RiverCity.QIn) annotation(
    Line(points = {{-41, 48}, {-56, 54}}));
  connect(Alder_RiverCity.QOut, RiverCity.QIn) annotation(
    Line(points = {{-59, 63}, {-70, 73}}));
  connect(TroutLake_Alder.QOut, Alder.QIn[1]) annotation(
    Line(points = {{-36, 31}, {-41, 40}}));
  connect(TroutLake.QOut, TroutLake_Alder.QIn) annotation(
    Line(points = {{-24, 19}, {-31, 26}}));
  connect(Lateral_Alder.QOut, Alder.QIn[2]) annotation(
    Line(points = {{-57, 29.5}, {-41, 40}}));
  connect(Inflow_TroutLake.QOut, TroutLake.QIn) annotation(
    Line(points = {{-9, 12}, {-16, 19}}));
  connect(TroutIn.QOut, Inflow_TroutLake.QIn) annotation(
    Line(points = {{11, 2}, {2, 10}}));
  connect(InflowAlder.QOut, Lateral_Alder.QIn) annotation(
    Line(points = {{-75, 22}, {-64, 29.5}}));
//
// Assign external time series (input and output) or values to the model objects
  TroutIn.Q = TroutLake_Inflow;
  InflowAlder.Q = Alder_Inflow;
  TroutLake.Q_turbine = TroutLake_Q_turbine;
  TroutLake.Q_spill = TroutLake_Q_spill;
  TroutLake_Q_out = TroutLake.QOut.Q;
  TroutLake_V = TroutLake.V;
  RiverCity_Q = RiverCity.Q;
//
// Information for graphical display in Open Modelica Editor
  annotation(Diagram(coordinateSystem(grid = {1, 1}, initialScale = 0.1, extent = {{-90, 100}, {30, -10}}), graphics = {Line(origin = {22.5, 53}, points = {{-6.5, 2}})}), Icon(coordinateSystem(grid = {1, 1})), version = "", uses, __OpenModelica_commandLineOptions = "");
end BlueRiver;
