# DPF - Ansys Data Processing Framework
[![PyAnsys](https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC)](https://docs.pyansys.com/)
[![Python](https://img.shields.io/pypi/pyversions/ansys-dpf-core?logo=pypi)](https://pypi.org/project/ansys-dpf-core/)
[![pypi](https://img.shields.io/pypi/v/ansys-dpf-core.svg?logo=python&logoColor=white)](https://pypi.org/project/ansys-dpf-core)
[![freq-PyDPF-Core](https://img.shields.io/github/commit-activity/m/ansys/pydpf-core)](https://github.com/ansys/pydpf-core)
[![GH-CI](https://github.com/ansys/pydpf-core/actions/workflows/ci.yml/badge.svg)](https://github.com/ansys/pydpf-core/actions/workflows/ci.yml)
[![docs](https://img.shields.io/website?down_color=lightgrey&down_message=invalid&label=documentation&up_color=brightgreen&up_message=up&url=https%3A%2F%2Fdpfdocs.pyansys.com%2F)](https://dpfdocs.pyansys.com)
[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![pypidl](https://img.shields.io/pypi/dm/ansys-dpf-core.svg?label=PyPI%20downloads)](https://pypi.org/project/ansys-dpf-core/)
[![cov](https://codecov.io/gh/ansys/pydpf-core/branch/master/graph/badge.svg)](https://codecov.io/gh/ansys/pydpf-core)
[![codacy](https://app.codacy.com/project/badge/Grade/61b6a519aea64715ad1726b3955fcf98)](https://www.codacy.com/gh/ansys/pydpf-core/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ansys/pydpf-core&amp;utm_campaign=Badge_Grade)

The Data Processing Framework (DPF) provides numerical simulation 
users and engineers with a toolbox for accessing and transforming simulation 
data. With DPF, you can perform complex preprocessing or postprocessing of
large amounts of simulation data within a simulation workflow.

DPF is an independent, physics-agnostic tool that you can plug into many 
apps for both data input and data output, including visualization and 
result plots. It can access data from solver result files and other neutral
formats, such as CSV, HDF5, and VTK files.

Using the many DPF operators that are available, you can manipulate and
transform this data. You can also chain operators together to create simple
or complex data-processing workflows that you can reuse for repeated or
future evaluations.

The data in DPF is defined based on physics-agnostic mathematical quantities 
described in self-sufficient entities called **fields**. This allows DPF to be 
a modular and easy-to-use tool with a large range of capabilities. 

.. image:: https://github.com/ansys/pydpf-core/raw/main/docs/source/images/drawings/dpf-flow.png
  :width: 670
  :alt: DPF flow

The ``ansys.dpf.core`` package provides a Python interface to DPF, enabling
rapid postprocessing of a variety of Ansys file formats and physics solutions
without ever leaving the Python environment.

## Documentation

Visit the [DPF-Core Documentation](https://dpfdocs.pyansys.com) for
comprehensive information on this library. See the
[Examples](https://dpfdocs.pyansys.com/version/stable/examples/index.html)
for how-to information.

## Installation

PyDPF-Core requires DPF to be available. You can either have a compatible Ansys version installed
or install the standalone ``ansys-dpf-server`` server package. For more information, see
[Getting Started with DPF Server](https://dpf.docs.pyansys.com/version/stable/user_guide/getting_started_with_dpf_server.html) in the PyDPF-Core documentation.

For the compatibility between PyDPF-Core and Ansys, see
[Compatibility](https://dpf.docs.pyansys.com/version/stable/getting_started/compatibility.html) in
the PyDPF-Core documentation.

To use PyDPF-Core with the ``ansys-dpf-server`` server package or with Ansys 2021 R2 or later, 
install the latest version with this command:

```con
   pip install ansys-dpf-core
```

PyDPF-Core plotting capabilities require `PyVista <https://pyvista.org/>`_ to be installed.
To install PyDPF-Core with its optional plotting functionalities, use this command:

```con
   pip install ansys-dpf-core[plotting]
```

For more information on PyDPF-Core plotting capabilities, see [Plot](https://dpf.docs.pyansys.com/version/stable/user_guide/plotting.html) in the PyDPF-Core documentation.

To use PyDPF-Core with Ansys 2021 R1, install the latest version
with this command:

```con
   pip install ansys-dpf-core<0.3.0
```

### Brief demo

Provided you have DPF available, a DPF server automatically starts once you start using PyDPF-Core.

To open a result file and explore what's inside, use this code:

```pycon
>>> from ansys.dpf import core as dpf
>>> from ansys.dpf.core import examples
>>> model = dpf.Model(examples.find_simple_bar())
>>> print(model)

    DPF Model
    ------------------------------
    Static analysis
    Unit system: Metric (m, kg, N, s, V, A)
    Physics Type: Mechanical
    Available results:
         -  displacement: Nodal Displacement
         -  element_nodal_forces: ElementalNodal Element nodal Forces
         -  elemental_volume: Elemental Volume
         -  stiffness_matrix_energy: Elemental Energy-stiffness matrix
         -  artificial_hourglass_energy: Elemental Hourglass Energy
         -  thermal_dissipation_energy: Elemental thermal dissipation energy
         -  kinetic_energy: Elemental Kinetic Energy
         -  co_energy: Elemental co-energy
         -  incremental_energy: Elemental incremental energy
         -  structural_temperature: ElementalNodal Temperature
    ------------------------------
    DPF  Meshed Region: 
      3751 nodes 
      3000 elements 
      Unit: m 
      With solid (3D) elements
    ------------------------------
    DPF  Time/Freq Support: 
      Number of sets: 1 
    Cumulative     Time (s)       LoadStep       Substep         
    1              1.000000       1              1               


```

Read a result with this command:

```pycon
>>> result = model.results.displacement.eval()
```

Then, start connecting operators with this code:

```pycon
>>> from ansys.dpf.core import operators as ops
>>> norm = ops.math.norm(model.results.displacement())
```

### Starting the service

The ``ansys.dpf.core`` library automatically starts a local instance of the DPF service in the
background and connects to it.  If you need to connect to an existing
remote or local DPF instance, use the ``connect_to_server`` method:

```pycon
>>> from ansys.dpf import core as dpf
>>> dpf.connect_to_server(ip='10.0.0.22', port=50054)
```

Once connected, this connection remains for the duration of the
module. It closes when you exit Python or connect to a different server.
