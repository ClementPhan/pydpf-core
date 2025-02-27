"""
assemble_scalars_to_matrices_fc
===============================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class assemble_scalars_to_matrices_fc(Operator):
    """Take nine scalar fields and assemble them as a 3x3 matrix field.

    Parameters
    ----------
    fields_container : FieldsContainer, optional
    yy : Field, optional
    zz : Field, optional
    xy : Field, optional
    yz : Field, optional
    xz : Field, optional
    yx : Field, optional
    zy : Field, optional
    zx : Field, optional


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()

    >>> # Make input connections
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_yy = dpf.Field()
    >>> op.inputs.yy.connect(my_yy)
    >>> my_zz = dpf.Field()
    >>> op.inputs.zz.connect(my_zz)
    >>> my_xy = dpf.Field()
    >>> op.inputs.xy.connect(my_xy)
    >>> my_yz = dpf.Field()
    >>> op.inputs.yz.connect(my_yz)
    >>> my_xz = dpf.Field()
    >>> op.inputs.xz.connect(my_xz)
    >>> my_yx = dpf.Field()
    >>> op.inputs.yx.connect(my_yx)
    >>> my_zy = dpf.Field()
    >>> op.inputs.zy.connect(my_zy)
    >>> my_zx = dpf.Field()
    >>> op.inputs.zx.connect(my_zx)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc(
    ...     fields_container=my_fields_container,
    ...     yy=my_yy,
    ...     zz=my_zz,
    ...     xy=my_xy,
    ...     yz=my_yz,
    ...     xz=my_xz,
    ...     yx=my_yx,
    ...     zy=my_zy,
    ...     zx=my_zx,
    ... )

    >>> # Get output data
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(
        self,
        fields_container=None,
        yy=None,
        zz=None,
        xy=None,
        yz=None,
        xz=None,
        yx=None,
        zy=None,
        zx=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="assemble_scalars_to_matrices_fc", config=config, server=server
        )
        self._inputs = InputsAssembleScalarsToMatricesFc(self)
        self._outputs = OutputsAssembleScalarsToMatricesFc(self)
        if fields_container is not None:
            self.inputs.fields_container.connect(fields_container)
        if yy is not None:
            self.inputs.yy.connect(yy)
        if zz is not None:
            self.inputs.zz.connect(zz)
        if xy is not None:
            self.inputs.xy.connect(xy)
        if yz is not None:
            self.inputs.yz.connect(yz)
        if xz is not None:
            self.inputs.xz.connect(xz)
        if yx is not None:
            self.inputs.yx.connect(yx)
        if zy is not None:
            self.inputs.zy.connect(zy)
        if zx is not None:
            self.inputs.zx.connect(zx)

    @staticmethod
    def _spec():
        description = (
            """Take nine scalar fields and assemble them as a 3x3 matrix field."""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
                    optional=True,
                    document="""""",
                ),
                1: PinSpecification(
                    name="yy",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                2: PinSpecification(
                    name="zz",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                3: PinSpecification(
                    name="xy",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                4: PinSpecification(
                    name="yz",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                5: PinSpecification(
                    name="xz",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                6: PinSpecification(
                    name="yx",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                7: PinSpecification(
                    name="zy",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
                8: PinSpecification(
                    name="zx",
                    type_names=["field"],
                    optional=True,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="fields_container",
                    type_names=["fields_container"],
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
        return Operator.default_config(
            name="assemble_scalars_to_matrices_fc", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsAssembleScalarsToMatricesFc
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsAssembleScalarsToMatricesFc
        """
        return super().outputs


class InputsAssembleScalarsToMatricesFc(_Inputs):
    """Intermediate class used to connect user inputs to
    assemble_scalars_to_matrices_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
    >>> my_fields_container = dpf.FieldsContainer()
    >>> op.inputs.fields_container.connect(my_fields_container)
    >>> my_yy = dpf.Field()
    >>> op.inputs.yy.connect(my_yy)
    >>> my_zz = dpf.Field()
    >>> op.inputs.zz.connect(my_zz)
    >>> my_xy = dpf.Field()
    >>> op.inputs.xy.connect(my_xy)
    >>> my_yz = dpf.Field()
    >>> op.inputs.yz.connect(my_yz)
    >>> my_xz = dpf.Field()
    >>> op.inputs.xz.connect(my_xz)
    >>> my_yx = dpf.Field()
    >>> op.inputs.yx.connect(my_yx)
    >>> my_zy = dpf.Field()
    >>> op.inputs.zy.connect(my_zy)
    >>> my_zx = dpf.Field()
    >>> op.inputs.zx.connect(my_zx)
    """

    def __init__(self, op: Operator):
        super().__init__(assemble_scalars_to_matrices_fc._spec().inputs, op)
        self._fields_container = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._fields_container)
        self._yy = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._yy)
        self._zz = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._zz)
        self._xy = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._xy)
        self._yz = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._yz)
        self._xz = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._xz)
        self._yx = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(6), 6, op, -1
        )
        self._inputs.append(self._yx)
        self._zy = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(7), 7, op, -1
        )
        self._inputs.append(self._zy)
        self._zx = Input(
            assemble_scalars_to_matrices_fc._spec().input_pin(8), 8, op, -1
        )
        self._inputs.append(self._zx)

    @property
    def fields_container(self):
        """Allows to connect fields_container input to the operator.

        Parameters
        ----------
        my_fields_container : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.fields_container.connect(my_fields_container)
        >>> # or
        >>> op.inputs.fields_container(my_fields_container)
        """
        return self._fields_container

    @property
    def yy(self):
        """Allows to connect yy input to the operator.

        Parameters
        ----------
        my_yy : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.yy.connect(my_yy)
        >>> # or
        >>> op.inputs.yy(my_yy)
        """
        return self._yy

    @property
    def zz(self):
        """Allows to connect zz input to the operator.

        Parameters
        ----------
        my_zz : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.zz.connect(my_zz)
        >>> # or
        >>> op.inputs.zz(my_zz)
        """
        return self._zz

    @property
    def xy(self):
        """Allows to connect xy input to the operator.

        Parameters
        ----------
        my_xy : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.xy.connect(my_xy)
        >>> # or
        >>> op.inputs.xy(my_xy)
        """
        return self._xy

    @property
    def yz(self):
        """Allows to connect yz input to the operator.

        Parameters
        ----------
        my_yz : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.yz.connect(my_yz)
        >>> # or
        >>> op.inputs.yz(my_yz)
        """
        return self._yz

    @property
    def xz(self):
        """Allows to connect xz input to the operator.

        Parameters
        ----------
        my_xz : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.xz.connect(my_xz)
        >>> # or
        >>> op.inputs.xz(my_xz)
        """
        return self._xz

    @property
    def yx(self):
        """Allows to connect yx input to the operator.

        Parameters
        ----------
        my_yx : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.yx.connect(my_yx)
        >>> # or
        >>> op.inputs.yx(my_yx)
        """
        return self._yx

    @property
    def zy(self):
        """Allows to connect zy input to the operator.

        Parameters
        ----------
        my_zy : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.zy.connect(my_zy)
        >>> # or
        >>> op.inputs.zy(my_zy)
        """
        return self._zy

    @property
    def zx(self):
        """Allows to connect zx input to the operator.

        Parameters
        ----------
        my_zx : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> op.inputs.zx.connect(my_zx)
        >>> # or
        >>> op.inputs.zx(my_zx)
        """
        return self._zx


class OutputsAssembleScalarsToMatricesFc(_Outputs):
    """Intermediate class used to get outputs from
    assemble_scalars_to_matrices_fc operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
    >>> # Connect inputs : op.inputs. ...
    >>> result_fields_container = op.outputs.fields_container()
    """

    def __init__(self, op: Operator):
        super().__init__(assemble_scalars_to_matrices_fc._spec().outputs, op)
        self._fields_container = Output(
            assemble_scalars_to_matrices_fc._spec().output_pin(0), 0, op
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
        >>> op = dpf.operators.utility.assemble_scalars_to_matrices_fc()
        >>> # Connect inputs : op.inputs. ...
        >>> result_fields_container = op.outputs.fields_container()
        """  # noqa: E501
        return self._fields_container
