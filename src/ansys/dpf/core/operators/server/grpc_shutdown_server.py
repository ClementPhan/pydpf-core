"""
grpc_shutdown_server
====================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class grpc_shutdown_server(Operator):
    """Shutdowns dpf's grpc server

    Parameters
    ----------
    grpc_stream : StreamsContainer
        Dpf streams handling the server


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.server.grpc_shutdown_server()

    >>> # Make input connections
    >>> my_grpc_stream = dpf.StreamsContainer()
    >>> op.inputs.grpc_stream.connect(my_grpc_stream)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.server.grpc_shutdown_server(
    ...     grpc_stream=my_grpc_stream,
    ... )

    """

    def __init__(self, grpc_stream=None, config=None, server=None):
        super().__init__(name="grpc_server_shutdown", config=config, server=server)
        self._inputs = InputsGrpcShutdownServer(self)
        self._outputs = OutputsGrpcShutdownServer(self)
        if grpc_stream is not None:
            self.inputs.grpc_stream.connect(grpc_stream)

    @staticmethod
    def _spec():
        description = """Shutdowns dpf's grpc server"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="grpc_stream",
                    type_names=["streams_container"],
                    optional=False,
                    document="""Dpf streams handling the server""",
                ),
            },
            map_output_pin_spec={},
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
        return Operator.default_config(name="grpc_server_shutdown", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsGrpcShutdownServer
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsGrpcShutdownServer
        """
        return super().outputs


class InputsGrpcShutdownServer(_Inputs):
    """Intermediate class used to connect user inputs to
    grpc_shutdown_server operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.server.grpc_shutdown_server()
    >>> my_grpc_stream = dpf.StreamsContainer()
    >>> op.inputs.grpc_stream.connect(my_grpc_stream)
    """

    def __init__(self, op: Operator):
        super().__init__(grpc_shutdown_server._spec().inputs, op)
        self._grpc_stream = Input(grpc_shutdown_server._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._grpc_stream)

    @property
    def grpc_stream(self):
        """Allows to connect grpc_stream input to the operator.

        Dpf streams handling the server

        Parameters
        ----------
        my_grpc_stream : StreamsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.server.grpc_shutdown_server()
        >>> op.inputs.grpc_stream.connect(my_grpc_stream)
        >>> # or
        >>> op.inputs.grpc_stream(my_grpc_stream)
        """
        return self._grpc_stream


class OutputsGrpcShutdownServer(_Outputs):
    """Intermediate class used to get outputs from
    grpc_shutdown_server operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.server.grpc_shutdown_server()
    >>> # Connect inputs : op.inputs. ...
    """

    def __init__(self, op: Operator):
        super().__init__(grpc_shutdown_server._spec().outputs, op)
