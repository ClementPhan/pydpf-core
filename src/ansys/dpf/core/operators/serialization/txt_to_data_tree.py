"""
txt_to_data_tree
================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class txt_to_data_tree(Operator):
    """Reads a txt file or string to a DataTree

    Parameters
    ----------
    string_or_path : str or DataSources


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.serialization.txt_to_data_tree()

    >>> # Make input connections
    >>> my_string_or_path = str()
    >>> op.inputs.string_or_path.connect(my_string_or_path)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.serialization.txt_to_data_tree(
    ...     string_or_path=my_string_or_path,
    ... )

    >>> # Get output data
    >>> result_data_tree = op.outputs.data_tree()
    """

    def __init__(self, string_or_path=None, config=None, server=None):
        super().__init__(name="txt_to_data_tree", config=config, server=server)
        self._inputs = InputsTxtToDataTree(self)
        self._outputs = OutputsTxtToDataTree(self)
        if string_or_path is not None:
            self.inputs.string_or_path.connect(string_or_path)

    @staticmethod
    def _spec():
        description = """Reads a txt file or string to a DataTree"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="string_or_path",
                    type_names=["string", "data_sources"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="data_tree",
                    type_names=["abstract_data_tree"],
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
        return Operator.default_config(name="txt_to_data_tree", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsTxtToDataTree
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsTxtToDataTree
        """
        return super().outputs


class InputsTxtToDataTree(_Inputs):
    """Intermediate class used to connect user inputs to
    txt_to_data_tree operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.txt_to_data_tree()
    >>> my_string_or_path = str()
    >>> op.inputs.string_or_path.connect(my_string_or_path)
    """

    def __init__(self, op: Operator):
        super().__init__(txt_to_data_tree._spec().inputs, op)
        self._string_or_path = Input(txt_to_data_tree._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._string_or_path)

    @property
    def string_or_path(self):
        """Allows to connect string_or_path input to the operator.

        Parameters
        ----------
        my_string_or_path : str or DataSources

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.txt_to_data_tree()
        >>> op.inputs.string_or_path.connect(my_string_or_path)
        >>> # or
        >>> op.inputs.string_or_path(my_string_or_path)
        """
        return self._string_or_path


class OutputsTxtToDataTree(_Outputs):
    """Intermediate class used to get outputs from
    txt_to_data_tree operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.serialization.txt_to_data_tree()
    >>> # Connect inputs : op.inputs. ...
    >>> result_data_tree = op.outputs.data_tree()
    """

    def __init__(self, op: Operator):
        super().__init__(txt_to_data_tree._spec().outputs, op)
        self._data_tree = Output(txt_to_data_tree._spec().output_pin(0), 0, op)
        self._outputs.append(self._data_tree)

    @property
    def data_tree(self):
        """Allows to get data_tree output of the operator

        Returns
        ----------
        my_data_tree : DataTree

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.serialization.txt_to_data_tree()
        >>> # Connect inputs : op.inputs. ...
        >>> result_data_tree = op.outputs.data_tree()
        """  # noqa: E501
        return self._data_tree
