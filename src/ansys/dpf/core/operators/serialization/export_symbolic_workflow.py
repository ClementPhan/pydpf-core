"""
export_symbolic_workflow
========================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.outputs import _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class export_symbolic_workflow(Operator):
    """Transforms a Workflow into a symbolic Workflow and writes it to a file
    (if a path is set in input) or string

    Parameters
    ----------
    workflow : Workflow
    path : str, optional
    format : int, optional
        0 is ascii format and 1 is binary, default is
        0.


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.export_symbolic_workflow()

    >>> # Make input connections
    >>> my_workflow = dpf.Workflow()
    >>> op.inputs.workflow.connect(my_workflow)
    >>> my_path = str()
    >>> op.inputs.path.connect(my_path)
    >>> my_format = int()
    >>> op.inputs.format.connect(my_format)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.export_symbolic_workflow(
    ...     workflow=my_workflow,
    ...     path=my_path,
    ...     format=my_format,
    ... )

    >>> # Get output data
    >>> result_data_sources = op.outputs.data_sources()
    """

    def __init__(self, workflow=None, path=None, format=None, config=None, server=None):
        super().__init__(name="export_symbolic_workflow", config=config, server=server)
        self._inputs = InputsExportSymbolicWorkflow(self)
        self._outputs = OutputsExportSymbolicWorkflow(self)
        if workflow is not None:
            self.inputs.workflow.connect(workflow)
        if path is not None:
            self.inputs.path.connect(path)
        if format is not None:
            self.inputs.format.connect(format)

    @staticmethod
    def _spec():
        description = """Transforms a Workflow into a symbolic Workflow and writes it to a file
            (if a path is set in input) or string"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="workflow",
                    type_names=["workflow"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="path",
                    type_names=["string"],
                    optional=True,
                    document="""""",
                ),
                2: PinSpecification(
                    name="format",
                    type_names=["int32"],
                    optional=True,
                    document="""0 is ascii format and 1 is binary, default is
        0.""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="data_sources",
                    type_names=["data_sources", "string"],
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
        return Operator.default_config(name="export_symbolic_workflow", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsExportSymbolicWorkflow
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsExportSymbolicWorkflow
        """
        return super().outputs


class InputsExportSymbolicWorkflow(_Inputs):
    """Intermediate class used to connect user inputs to
    export_symbolic_workflow operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.export_symbolic_workflow()
    >>> my_workflow = dpf.Workflow()
    >>> op.inputs.workflow.connect(my_workflow)
    >>> my_path = str()
    >>> op.inputs.path.connect(my_path)
    >>> my_format = int()
    >>> op.inputs.format.connect(my_format)
    """

    def __init__(self, op: Operator):
        super().__init__(export_symbolic_workflow._spec().inputs, op)
        self._workflow = Input(export_symbolic_workflow._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._workflow)
        self._path = Input(export_symbolic_workflow._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._path)
        self._format = Input(export_symbolic_workflow._spec().input_pin(2), 2, op, -1)
        self._inputs.append(self._format)

    @property
    def workflow(self):
        """Allows to connect workflow input to the operator.

        Parameters
        ----------
        my_workflow : Workflow

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.export_symbolic_workflow()
        >>> op.inputs.workflow.connect(my_workflow)
        >>> # or
        >>> op.inputs.workflow(my_workflow)
        """
        return self._workflow

    @property
    def path(self):
        """Allows to connect path input to the operator.

        Parameters
        ----------
        my_path : str

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.export_symbolic_workflow()
        >>> op.inputs.path.connect(my_path)
        >>> # or
        >>> op.inputs.path(my_path)
        """
        return self._path

    @property
    def format(self):
        """Allows to connect format input to the operator.

        0 is ascii format and 1 is binary, default is
        0.

        Parameters
        ----------
        my_format : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.export_symbolic_workflow()
        >>> op.inputs.format.connect(my_format)
        >>> # or
        >>> op.inputs.format(my_format)
        """
        return self._format


class OutputsExportSymbolicWorkflow(_Outputs):
    """Intermediate class used to get outputs from
    export_symbolic_workflow operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.export_symbolic_workflow()
    >>> # Connect inputs : op.inputs. ...
    >>> result_data_sources = op.outputs.data_sources()
    """

    def __init__(self, op: Operator):
        super().__init__(export_symbolic_workflow._spec().outputs, op)
        self.data_sources_as_data_sources = Output(
            _modify_output_spec_with_one_type(
                export_symbolic_workflow._spec().output_pin(0), "data_sources"
            ),
            0,
            op,
        )
        self._outputs.append(self.data_sources_as_data_sources)
        self.data_sources_as_string = Output(
            _modify_output_spec_with_one_type(
                export_symbolic_workflow._spec().output_pin(0), "string"
            ),
            0,
            op,
        )
        self._outputs.append(self.data_sources_as_string)
