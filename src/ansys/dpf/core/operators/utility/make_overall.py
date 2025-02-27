"""
make_overall
============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class make_overall(Operator):
    """Extracts a value from a field and makes a new field containing only
    this value, with the associated scoping's location set as
    'overall'.

    Parameters
    ----------
    field : Field
    id : int


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.make_overall()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_id = int()
    >>> op.inputs.id.connect(my_id)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.make_overall(
    ...     field=my_field,
    ...     id=my_id,
    ... )

    >>> # Get output data
    >>> result_field = op.outputs.field()
    """

    def __init__(self, field=None, id=None, config=None, server=None):
        super().__init__(name="make_overall", config=config, server=server)
        self._inputs = InputsMakeOverall(self)
        self._outputs = OutputsMakeOverall(self)
        if field is not None:
            self.inputs.field.connect(field)
        if id is not None:
            self.inputs.id.connect(id)

    @staticmethod
    def _spec():
        description = """Extracts a value from a field and makes a new field containing only
            this value, with the associated scoping's location set as
            'overall'."""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
                1: PinSpecification(
                    name="id",
                    type_names=["int32"],
                    optional=False,
                    document="""""",
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
        return Operator.default_config(name="make_overall", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMakeOverall
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsMakeOverall
        """
        return super().outputs


class InputsMakeOverall(_Inputs):
    """Intermediate class used to connect user inputs to
    make_overall operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_overall()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    >>> my_id = int()
    >>> op.inputs.id.connect(my_id)
    """

    def __init__(self, op: Operator):
        super().__init__(make_overall._spec().inputs, op)
        self._field = Input(make_overall._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)
        self._id = Input(make_overall._spec().input_pin(1), 1, op, -1)
        self._inputs.append(self._id)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Parameters
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_overall()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field

    @property
    def id(self):
        """Allows to connect id input to the operator.

        Parameters
        ----------
        my_id : int

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.make_overall()
        >>> op.inputs.id.connect(my_id)
        >>> # or
        >>> op.inputs.id(my_id)
        """
        return self._id


class OutputsMakeOverall(_Outputs):
    """Intermediate class used to get outputs from
    make_overall operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.make_overall()
    >>> # Connect inputs : op.inputs. ...
    >>> result_field = op.outputs.field()
    """

    def __init__(self, op: Operator):
        super().__init__(make_overall._spec().outputs, op)
        self._field = Output(make_overall._spec().output_pin(0), 0, op)
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
        >>> op = dpf.operators.utility.make_overall()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field = op.outputs.field()
        """  # noqa: E501
        return self._field
