"""
normals_provider_nl
===================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class normals_provider_nl(Operator):
    """Computes the normals on nodes/elements based on integration points
    (more accurate for non-linear elements) on a skin mesh.

    Parameters
    ----------
    mesh : MeshedRegion
        Skin or shell mesh region.
    mesh_scoping : Scoping, optional
        Elemental, elementalnodal, or nodal scoping.
        location derived from this.
    requested_location : str, optional
        If no scoping, specifies location. if scoping
        is elemental or elementalnodal this
        overrides scoping. default is
        elemental.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.geo.normals_provider_nl()

    >>> # Make input connections
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.geo.normals_provider_nl(
    ...     mesh=my_mesh,
    ...     mesh_scoping=my_mesh_scoping,
    ...     requested_location=my_requested_location,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        mesh=None,
        mesh_scoping=None,
        requested_location=None,
        config=None,
        server=None,
    ):
        super().__init__(name="normals_provider_nl", config=config, server=server)
        self._inputs = InputsNormalsProviderNl(self)
        self._outputs = OutputsNormalsProviderNl(self)
        if mesh is not None:
            self.inputs.mesh.connect(mesh)
        if mesh_scoping is not None:
            self.inputs.mesh_scoping.connect(mesh_scoping)
        if requested_location is not None:
            self.inputs.requested_location.connect(requested_location)

    @staticmethod
    def _spec():
        description = """Computes the normals on nodes/elements based on integration points
            (more accurate for non-linear elements) on a skin mesh."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""Skin or shell mesh region.""",
                ),
                1: PinSpecification(
                    name="mesh_scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""Elemental, elementalnodal, or nodal scoping.
        location derived from this.""",
                ),
                9: PinSpecification(
                    name="requested_location",
                    type_names=["string"],
                    optional=True,
                    document="""If no scoping, specifies location. if scoping
        is elemental or elementalnodal this
        overrides scoping. default is
        elemental.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the global server.
        """
        return Operator.default_config(name="normals_provider_nl", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsNormalsProviderNl
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsNormalsProviderNl
        """
        return super().outputs


class InputsNormalsProviderNl(_Inputs):
    """Intermediate class used to connect user inputs to
    normals_provider_nl operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.normals_provider_nl()
    >>> my_mesh = dpf.MeshedRegion()
    >>> op.inputs.mesh.connect(my_mesh)
    >>> my_mesh_scoping = dpf.Scoping()
    >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    """

    def __init__(self, op: Operator):
        super().__init__(normals_provider_nl._spec().inputs, op)
        self._mesh = Input(normals_provider_nl._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._mesh)
        self._mesh_scoping = Input(normals_provider_nl._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._mesh_scoping)
        self._requested_location = Input(
            normals_provider_nl._spec().input_pin(9), 9, op, -1
        )
        self._inputs.append(self._requested_location)

    @property
    def mesh(self):
        """Allows to connect mesh input to the operator.

        Skin or shell mesh region.

        Parameters
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> op.inputs.mesh.connect(my_mesh)
        >>> # or
        >>> op.inputs.mesh(my_mesh)
        """
        return self._mesh

    @property
    def mesh_scoping(self):
        """Allows to connect mesh_scoping input to the operator.

        Elemental, elementalnodal, or nodal scoping.
        location derived from this.

        Parameters
        ----------
        my_mesh_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> op.inputs.mesh_scoping.connect(my_mesh_scoping)
        >>> # or
        >>> op.inputs.mesh_scoping(my_mesh_scoping)
        """
        return self._mesh_scoping

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator.

        If no scoping, specifies location. if scoping
        is elemental or elementalnodal this
        overrides scoping. default is
        elemental.

        Parameters
        ----------
        my_requested_location : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> # or
        >>> op.inputs.requested_location(my_requested_location)
        """
        return self._requested_location


class OutputsNormalsProviderNl(_Outputs):
    """Intermediate class used to get outputs from
    normals_provider_nl operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.geo.normals_provider_nl()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(normals_provider_nl._spec().outputs, op)
        self._field = Output(normals_provider_nl._spec().output_pin(0), 0, op)
        self._outputs.append(self._field)

    @property
    def field(self):
        """Allows to get field output of the operator

        Returns
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.geo.normals_provider_nl()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
