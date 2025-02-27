"""
coordinate_system
=================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class coordinate_system(Operator):
    """Extracts the Rotation Matrix and Origin of a specific coordinate
    system

    Parameters
    ----------
    cs_id : int
    streams_container : StreamsContainer, optional
    data_sources : DataSources


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.coordinate_system()

    >>> # Make input connections
    >>> my_cs_id = int()
    >>> op.inputs.cs_id.connect(my_cs_id)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.coordinate_system(
    ...     cs_id=my_cs_id,
    ...     streams_container=my_streams_container,
    ...     data_sources=my_data_sources,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(
        self,
        cs_id=None,
        streams_container=None,
        data_sources=None,
        config=None,
        server=None,
    ):
        super().__init__(name="mapdl::rst::CS", config=config, server=server)
        self._inputs = InputsCoordinateSystem(self)
        self._outputs = OutputsCoordinateSystem(self)
        if cs_id is not None:
            self.inputs.cs_id.connect(cs_id)
        if streams_container is not None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources is not None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        description = """Extracts the Rotation Matrix and Origin of a specific coordinate
            system"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="cs_id",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
                ),
                3: PinSpecification(
                    name="streams_container",
                    type_names=["streams_container"],
                    optional=True,
                    document="""""",
                ),
                4: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""The first 9 double are the rotation (3x3
        matrix) and the last 3 is the
        translation vector""",
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
        return Operator.default_config(name="mapdl::rst::CS", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCoordinateSystem
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsCoordinateSystem
        """
        return super().outputs


class InputsCoordinateSystem(_Inputs):
    """Intermediate class used to connect user inputs to
    coordinate_system operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.coordinate_system()
    >>> my_cs_id = int()
    >>> op.inputs.cs_id.connect(my_cs_id)
    >>> my_streams_container = dpf.StreamsContainer()
    >>> op.inputs.streams_container.connect(my_streams_container)
    >>> my_data_sources = dpf.DataSources()
    >>> op.inputs.data_sources.connect(my_data_sources)
    """

    def __init__(self, op: Operator):
        super().__init__(coordinate_system._spec().inputs, op)
        self._cs_id = Input(coordinate_system._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._cs_id)
        self._streams_container = Input(
            coordinate_system._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._streams_container)
        self._data_sources = Input(coordinate_system._spec().input_pin(4), 4, op, -1)
        self._inputs.append(self._data_sources)

    @property
    def cs_id(self):
        """Allows to connect cs_id input to the operator.

        Parameters
        ----------
        my_cs_id : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.coordinate_system()
        >>> op.inputs.cs_id.connect(my_cs_id)
        >>> # or
        >>> op.inputs.cs_id(my_cs_id)
        """
        return self._cs_id

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator.

        Parameters
        ----------
        my_streams_container : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.coordinate_system()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> # or
        >>> op.inputs.streams_container(my_streams_container)
        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator.

        Parameters
        ----------
        my_data_sources : DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.coordinate_system()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> # or
        >>> op.inputs.data_sources(my_data_sources)
        """
        return self._data_sources


class OutputsCoordinateSystem(_Outputs):
    """Intermediate class used to get outputs from
    coordinate_system operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.coordinate_system()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(coordinate_system._spec().outputs, op)
        self._field = Output(coordinate_system._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.result.coordinate_system()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
