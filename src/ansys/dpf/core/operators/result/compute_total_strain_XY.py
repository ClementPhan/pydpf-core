"""
compute_total_strain_XY
=======================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class compute_total_strain_XY(Operator):
    """Computes the strain from a displacement field. Only SOLID185 (B-Bar,
    Simplified Enhanced Strain, Enhanced Strain formulations),
    SOLID186 (Full Integration) & SOLID187 elements are supported.
    Layered elements are not supported. Thermal strains are not
    supported. Only one value of material properties are allowed per
    element for isotropic and orthotropic elasticity. Material
    nonlinearity is not supported Only linear analysis are supported
    without On Demand Expansion. All coordinates are global
    coordinates. Euler Angles need to be included in the database. Get
    the XY shear component (01 component).

    Parameters
    ----------
    time_scoping : Scoping or int or float or Field, optional
        Time/freq values (use doubles or field),
        time/freq set ids (use ints or
        scoping) or time/freq step ids (use
        scoping with timefreq_steps location)
        required in output.to specify
        time/freq values at specific load
        steps, put a field (and not a list)
        in input with a scoping located on
        "timefreq_steps".linear time freq
        intrapolation is performed if the
        values are not in the result files
        and the data at the max time or freq
        is taken when time/freqs are higher
        than available time/freqs in result
        files.. will only be used if no
        displacement input is given (will be
        applied on displacement operator).
    scoping : Scoping, optional
        The element scoping on which the result is
        computed.
    streams_container : StreamsContainer, optional
        Optional if a mesh or a data_sources have
        been connected. required if no
        displacement input have been
        connected.
    data_sources : DataSources
        Optional if a mesh or a streams_container
        have been connected, or if the
        displacement's field has a mesh
        support. required if no displacement
        input have been connected.
    extrapolate : int, optional
        Whether to extrapolate the data from the
        integration points to the nodes.
    nonlinear : int, optional
        Whether to use nonlinear geometry or
        nonlinear material (1 = large strain,
        2 = hyperelasticity).
    abstract_meshed_region : MeshedRegion, optional
        The underlying mesh. optional if a
        data_sources or a streams_container
        have been connected, or if the
        displacement's field has a mesh
        support.
    requested_location : str, optional
        Average the elemental nodal result to the
        requested location.
    displacement : FieldsContainer or Field, optional
        Field/or fields container containing only the
        displacement field (nodal). if none
        specified, read displacements from
        result file using the data_sources.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.compute_total_strain_XY()

    >>> # Make input connections
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_extrapolate = int()
    >>> op.inputs.extrapolate.connect(my_extrapolate)
    >>> my_nonlinear = int()
    >>> op.inputs.nonlinear.connect(my_nonlinear)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_displacement = dpf.FieldsContainer()
    >>> op.inputs.displacement.connect(my_displacement)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.compute_total_strain_XY(
    ...     time_scoping=my_time_scoping,
    ...     scoping=my_scoping,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ...     extrapolate=my_extrapolate,
    ...     nonlinear=my_nonlinear,
    ...     abstract_meshed_region=my_abstract_meshed_region,
    ...     requested_location=my_requested_location,
    ...     displacement=my_displacement,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        time_scoping=None,
        scoping=None,
        streams_container=None,
        data_sources=None,
        extrapolate=None,
        nonlinear=None,
        abstract_meshed_region=None,
        requested_location=None,
        displacement=None,
        config=None,
        server=None,
    ):
        super().__init__(name="compute_total_strain_XY", config=config, server=server)
        self._inputs = InputsComputeTotalStrainXy(self)
        self._outputs = OutputsComputeTotalStrainXy(self)
        if time_scoping is not None:
            self.inputs.time_scoping.connect(time_scoping)
        if scoping is not None:
            self.inputs.scoping.connect(scoping)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)
        if extrapolate is not None:
            self.inputs.extrapolate.connect(extrapolate)
        if nonlinear is not None:
            self.inputs.nonlinear.connect(nonlinear)
        if abstract_meshed_region is not None:
            self.inputs.abstract_meshed_region.connect(abstract_meshed_region)
        if requested_location is not None:
            self.inputs.requested_location.connect(requested_location)
        if displacement is not None:
            self.inputs.displacement.connect(displacement)

    @staticmethod
    def _spec():
        description = """Computes the strain from a displacement field. Only SOLID185 (B-Bar,
            Simplified Enhanced Strain, Enhanced Strain formulations),
            SOLID186 (Full Integration) &amp; SOLID187 elements are
            supported. Layered elements are not supported. Thermal
            strains are not supported. Only one value of material
            properties are allowed per element for isotropic and
            orthotropic elasticity. Material nonlinearity is not
            supported Only linear analysis are supported without On
            Demand Expansion. All coordinates are global coordinates.
            Euler Angles need to be included in the database. Get the
            XY shear component (01 component)."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="time_scoping",
                    type_names=[
                        "scoping",
                        "int32",
                        "vector<int32>",
                        "double",
                        "field",
                        "vector<double>",
                    ],
                    optional=True,
                    document="""Time/freq values (use doubles or field),
        time/freq set ids (use ints or
        scoping) or time/freq step ids (use
        scoping with timefreq_steps location)
        required in output.to specify
        time/freq values at specific load
        steps, put a field (and not a list)
        in input with a scoping located on
        "timefreq_steps".linear time freq
        intrapolation is performed if the
        values are not in the result files
        and the data at the max time or freq
        is taken when time/freqs are higher
        than available time/freqs in result
        files.. will only be used if no
        displacement input is given (will be
        applied on displacement operator).""",
                ),
                1: PinSpecification(
                    name="scoping",
                    type_names=["scoping"],
                    optional=True,
                    document="""The element scoping on which the result is
        computed.""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""Optional if a mesh or a data_sources have
        been connected. required if no
        displacement input have been
        connected.""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""Optional if a mesh or a streams_container
        have been connected, or if the
        displacement's field has a mesh
        support. required if no displacement
        input have been connected.""",
                ),
                5: PinSpecification(
                    name="extrapolate",
                    type_names=["int32"],
                    optional=True,
                    document="""Whether to extrapolate the data from the
        integration points to the nodes.""",
                ),
                6: PinSpecification(
                    name="nonlinear",
                    type_names=["int32"],
                    optional=True,
                    document="""Whether to use nonlinear geometry or
        nonlinear material (1 = large strain,
        2 = hyperelasticity).""",
                ),
                7: PinSpecification(
                    name="abstract_meshed_region",
                    type_names=["abstract_meshed_region"],
                    optional=True,
                    document="""The underlying mesh. optional if a
        data_sources or a streams_container
        have been connected, or if the
        displacement's field has a mesh
        support.""",
                ),
                9: PinSpecification(
                    name="requested_location",
                    type_names=["string"],
                    optional=True,
                    document="""Average the elemental nodal result to the
        requested location.""",
                ),
                10: PinSpecification(
                    name="displacement",
                    type_names=["fields_container", "field"],
                    optional=True,
                    document="""Field/or fields container containing only the
        displacement field (nodal). if none
        specified, read displacements from
        result file using the data_sources.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=False,
                    document="""The computed result fields container
        (elemental nodal).""",
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
        return Operator.default_config(name="compute_total_strain_XY", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComputeTotalStrainXy
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsComputeTotalStrainXy
        """
        return super().outputs


class InputsComputeTotalStrainXy(_Inputs):
    """Intermediate class used to connect user inputs to
    compute_total_strain_XY operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.compute_total_strain_XY()
    >>> my_time_scoping = dpf.Scoping()
    >>> op.inputs.time_scoping.connect(my_time_scoping)
    >>> my_scoping = dpf.Scoping()
    >>> op.inputs.scoping.connect(my_scoping)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    >>> my_extrapolate = int()
    >>> op.inputs.extrapolate.connect(my_extrapolate)
    >>> my_nonlinear = int()
    >>> op.inputs.nonlinear.connect(my_nonlinear)
    >>> my_abstract_meshed_region = dpf.MeshedRegion()
    >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
    >>> my_requested_location = str()
    >>> op.inputs.requested_location.connect(my_requested_location)
    >>> my_displacement = dpf.FieldsContainer()
    >>> op.inputs.displacement.connect(my_displacement)
    """

    def __init__(self, op: Operator):
        super().__init__(compute_total_strain_XY._spec().inputs, op)
        self._time_scoping = Input(
            compute_total_strain_XY._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._time_scoping)
        self._scoping = Input(compute_total_strain_XY._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._scoping)
        self._streams_container = Input(
            compute_total_strain_XY._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(
            compute_total_strain_XY._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._data_sources)
        self._extrapolate = Input(
            compute_total_strain_XY._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._extrapolate)
        self._nonlinear = Input(compute_total_strain_XY._spec().input_pin(6), 6, op, -1)
        self._inputs.append(self._nonlinear)
        self._abstract_meshed_region = Input(
            compute_total_strain_XY._spec().input_pin(7), 7, op, -1
        )
        self._inputs.append(self._abstract_meshed_region)
        self._requested_location = Input(
            compute_total_strain_XY._spec().input_pin(9), 9, op, -1
        )
        self._inputs.append(self._requested_location)
        self._displacement = Input(
            compute_total_strain_XY._spec().input_pin(10), 10, op, -1
        )
        self._inputs.append(self._displacement)

    @property
    def time_scoping(self):
        """Allows to connect time_scoping input to the operator.

        Time/freq values (use doubles or field),
        time/freq set ids (use ints or
        scoping) or time/freq step ids (use
        scoping with timefreq_steps location)
        required in output.to specify
        time/freq values at specific load
        steps, put a field (and not a list)
        in input with a scoping located on
        "timefreq_steps".linear time freq
        intrapolation is performed if the
        values are not in the result files
        and the data at the max time or freq
        is taken when time/freqs are higher
        than available time/freqs in result
        files.. will only be used if no
        displacement input is given (will be
        applied on displacement operator).

        Parameters
        ----------
        my_time_scoping : Scoping or int or float or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.time_scoping.connect(my_time_scoping)
        >>> # or
        >>> op.inputs.time_scoping(my_time_scoping)
        """
        return self._time_scoping

    @property
    def scoping(self):
        """Allows to connect scoping input to the operator.

        The element scoping on which the result is
        computed.

        Parameters
        ----------
        my_scoping : Scoping

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.scoping.connect(my_scoping)
        >>> # or
        >>> op.inputs.scoping(my_scoping)
        """
        return self._scoping

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Optional if a mesh or a data_sources have
        been connected. required if no
        displacement input have been
        connected.

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Optional if a mesh or a streams_container
        have been connected, or if the
        displacement's field has a mesh
        support. required if no displacement
        input have been connected.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources

    @property
    def extrapolate(self):
        """Allows to connect extrapolate input to the operator.

        Whether to extrapolate the data from the
        integration points to the nodes.

        Parameters
        ----------
        my_extrapolate : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.extrapolate.connect(my_extrapolate)
        >>> # or
        >>> op.inputs.extrapolate(my_extrapolate)
        """
        return self._extrapolate

    @property
    def nonlinear(self):
        """Allows to connect nonlinear input to the operator.

        Whether to use nonlinear geometry or
        nonlinear material (1 = large strain,
        2 = hyperelasticity).

        Parameters
        ----------
        my_nonlinear : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.nonlinear.connect(my_nonlinear)
        >>> # or
        >>> op.inputs.nonlinear(my_nonlinear)
        """
        return self._nonlinear

    @property
    def abstract_meshed_region(self):
        """Allows to connect abstract_meshed_region input to the operator.

        The underlying mesh. optional if a
        data_sources or a streams_container
        have been connected, or if the
        displacement's field has a mesh
        support.

        Parameters
        ----------
        my_abstract_meshed_region : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.abstract_meshed_region.connect(my_abstract_meshed_region)
        >>> # or
        >>> op.inputs.abstract_meshed_region(my_abstract_meshed_region)
        """
        return self._abstract_meshed_region

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator.

        Average the elemental nodal result to the
        requested location.

        Parameters
        ----------
        my_requested_location : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> # or
        >>> op.inputs.requested_location(my_requested_location)
        """
        return self._requested_location

    @property
    def displacement(self):
        """Allows to connect displacement input to the operator.

        Field/or fields container containing only the
        displacement field (nodal). if none
        specified, read displacements from
        result file using the data_sources.

        Parameters
        ----------
        my_displacement : FieldsContainer or Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> op.inputs.displacement.connect(my_displacement)
        >>> # or
        >>> op.inputs.displacement(my_displacement)
        """
        return self._displacement


class OutputsComputeTotalStrainXy(_Outputs):
    """Intermediate class used to get outputs from
    compute_total_strain_XY operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.compute_total_strain_XY()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(compute_total_strain_XY._spec().outputs, op)
        self._fields_container = Output(
            compute_total_strain_XY._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._fields_container)

    @property
    def fields_container(self):
        """Allows to get fields_container output of the operator

        Returns
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_total_strain_XY()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
