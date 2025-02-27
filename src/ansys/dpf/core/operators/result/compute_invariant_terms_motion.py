"""
compute_invariant_terms_motion
==============================
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class compute_invariant_terms_motion(Operator):
    """Set the required data for the invariant terms computation (reduced
    matrices, lumped mass matrix, modes ...)

    Parameters
    ----------
    rom_matrices : FieldsContainer
        Fieldscontainers containing the reduced
        matrices
    mode_shapes : FieldsContainer
        Fieldscontainers containing the mode shapes,
        which are cst and nor for the cms
        method
    lumped_mass : FieldsContainer
        Fieldscontainers containing the lumped mass
    model_data : FieldsContainer
        Data describing the finite element model
    field_coordinates : Field
        Coordinates of all nodes
    nod :


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.result.compute_invariant_terms_motion()

    >>> # Make input connections
    >>> my_rom_matrices = dpf.FieldsContainer()
    >>> op.inputs.rom_matrices.connect(my_rom_matrices)
    >>> my_mode_shapes = dpf.FieldsContainer()
    >>> op.inputs.mode_shapes.connect(my_mode_shapes)
    >>> my_lumped_mass = dpf.FieldsContainer()
    >>> op.inputs.lumped_mass.connect(my_lumped_mass)
    >>> my_model_data = dpf.FieldsContainer()
    >>> op.inputs.model_data.connect(my_model_data)
    >>> my_field_coordinates = dpf.Field()
    >>> op.inputs.field_coordinates.connect(my_field_coordinates)
    >>> my_nod = dpf.()
    >>> op.inputs.nod.connect(my_nod)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.result.compute_invariant_terms_motion(
    ...     rom_matrices=my_rom_matrices,
    ...     mode_shapes=my_mode_shapes,
    ...     lumped_mass=my_lumped_mass,
    ...     model_data=my_model_data,
    ...     field_coordinates=my_field_coordinates,
    ...     nod=my_nod,
    ... )

    >>> # Get output data
    >>> result_model_data = op.outputs.model_data()
    >>> result_mode_shapes = op.outputs.mode_shapes()
    >>> result_lumped_mass = op.outputs.lumped_mass()
    >>> result_field_coordinates_and_euler_angles = op.outputs.field_coordinates_and_euler_angles()
    >>> result_nod = op.outputs.nod()
    >>> result_used_node_index = op.outputs.used_node_index()
    >>> result_eigenvalue = op.outputs.eigenvalue()
    >>> result_translational_mode_shape = op.outputs.translational_mode_shape()
    >>> result_rotational_mode_shape = op.outputs.rotational_mode_shape()
    >>> result_invrt_1 = op.outputs.invrt_1()
    >>> result_invrt_2 = op.outputs.invrt_2()
    >>> result_invrt_3 = op.outputs.invrt_3()
    >>> result_invrt_4 = op.outputs.invrt_4()
    >>> result_invrt_5 = op.outputs.invrt_5()
    >>> result_invrt_6 = op.outputs.invrt_6()
    >>> result_invrt_7 = op.outputs.invrt_7()
    >>> result_invrt_8 = op.outputs.invrt_8()
    """

    def __init__(
        self,
        rom_matrices=None,
        mode_shapes=None,
        lumped_mass=None,
        model_data=None,
        field_coordinates=None,
        nod=None,
        config=None,
        server=None,
    ):
        super().__init__(
            name="compute_invariant_terms_motion", config=config, server=server
        )
        self._inputs = InputsComputeInvariantTermsMotion(self)
        self._outputs = OutputsComputeInvariantTermsMotion(self)
        if rom_matrices is not None:
            self.inputs.rom_matrices.connect(rom_matrices)
        if mode_shapes is not None:
            self.inputs.mode_shapes.connect(mode_shapes)
        if lumped_mass is not None:
            self.inputs.lumped_mass.connect(lumped_mass)
        if model_data is not None:
            self.inputs.model_data.connect(model_data)
        if field_coordinates is not None:
            self.inputs.field_coordinates.connect(field_coordinates)
        if nod is not None:
            self.inputs.nod.connect(nod)

    @staticmethod
    def _spec():
        description = """Set the required data for the invariant terms computation (reduced
            matrices, lumped mass matrix, modes ...)"""
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="rom_matrices",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fieldscontainers containing the reduced
        matrices""",
                ),
                1: PinSpecification(
                    name="mode_shapes",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fieldscontainers containing the mode shapes,
        which are cst and nor for the cms
        method""",
                ),
                2: PinSpecification(
                    name="lumped_mass",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fieldscontainers containing the lumped mass""",
                ),
                3: PinSpecification(
                    name="model_data",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Data describing the finite element model""",
                ),
                4: PinSpecification(
                    name="field_coordinates",
                    type_names=["field"],
                    optional=False,
                    document="""Coordinates of all nodes""",
                ),
                5: PinSpecification(
                    name="nod",
                    type_names=["vector<int32>"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="model_data",
                    type_names=["property_field"],
                    optional=False,
                    document="""Data describing the finite element model""",
                ),
                1: PinSpecification(
                    name="mode_shapes",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fieldscontainers containing the mode shapes,
        which are cst and nor for the cms
        method""",
                ),
                2: PinSpecification(
                    name="lumped_mass",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Fieldscontainers containing the lumped mass""",
                ),
                3: PinSpecification(
                    name="field_coordinates_and_euler_angles",
                    type_names=["fields_container"],
                    optional=False,
                    document="""Coordinates and euler angles of all nodes""",
                ),
                4: PinSpecification(
                    name="nod",
                    type_names=["vector<int32>"],
                    optional=False,
                    document="""""",
                ),
                5: PinSpecification(
                    name="used_node_index",
                    type_names=["vector<int32>"],
                    optional=False,
                    document="""""",
                ),
                6: PinSpecification(
                    name="eigenvalue",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                7: PinSpecification(
                    name="translational_mode_shape",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                8: PinSpecification(
                    name="rotational_mode_shape",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                9: PinSpecification(
                    name="invrt_1",
                    type_names=["double"],
                    optional=False,
                    document="""""",
                ),
                10: PinSpecification(
                    name="invrt_2",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                11: PinSpecification(
                    name="invrt_3",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                12: PinSpecification(
                    name="invrt_4",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                13: PinSpecification(
                    name="invrt_5",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                14: PinSpecification(
                    name="invrt_6",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                15: PinSpecification(
                    name="invrt_7",
                    type_names=["vector<double>"],
                    optional=False,
                    document="""""",
                ),
                16: PinSpecification(
                    name="invrt_8",
                    type_names=["vector<double>"],
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
            name="compute_invariant_terms_motion", server=server
        )

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsComputeInvariantTermsMotion
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluating it

        Returns
        --------
        outputs : OutputsComputeInvariantTermsMotion
        """
        return super().outputs


class InputsComputeInvariantTermsMotion(_Inputs):
    """Intermediate class used to connect user inputs to
    compute_invariant_terms_motion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.compute_invariant_terms_motion()
    >>> my_rom_matrices = dpf.FieldsContainer()
    >>> op.inputs.rom_matrices.connect(my_rom_matrices)
    >>> my_mode_shapes = dpf.FieldsContainer()
    >>> op.inputs.mode_shapes.connect(my_mode_shapes)
    >>> my_lumped_mass = dpf.FieldsContainer()
    >>> op.inputs.lumped_mass.connect(my_lumped_mass)
    >>> my_model_data = dpf.FieldsContainer()
    >>> op.inputs.model_data.connect(my_model_data)
    >>> my_field_coordinates = dpf.Field()
    >>> op.inputs.field_coordinates.connect(my_field_coordinates)
    >>> my_nod = dpf.()
    >>> op.inputs.nod.connect(my_nod)
    """

    def __init__(self, op: Operator):
        super().__init__(compute_invariant_terms_motion._spec().inputs, op)
        self._rom_matrices = Input(
            compute_invariant_terms_motion._spec().input_pin(0), 0, op, -1
        )
        self._inputs.append(self._rom_matrices)
        self._mode_shapes = Input(
            compute_invariant_terms_motion._spec().input_pin(1), 1, op, -1
        )
        self._inputs.append(self._mode_shapes)
        self._lumped_mass = Input(
            compute_invariant_terms_motion._spec().input_pin(2), 2, op, -1
        )
        self._inputs.append(self._lumped_mass)
        self._model_data = Input(
            compute_invariant_terms_motion._spec().input_pin(3), 3, op, -1
        )
        self._inputs.append(self._model_data)
        self._field_coordinates = Input(
            compute_invariant_terms_motion._spec().input_pin(4), 4, op, -1
        )
        self._inputs.append(self._field_coordinates)
        self._nod = Input(
            compute_invariant_terms_motion._spec().input_pin(5), 5, op, -1
        )
        self._inputs.append(self._nod)

    @property
    def rom_matrices(self):
        """Allows to connect rom_matrices input to the operator.

        Fieldscontainers containing the reduced
        matrices

        Parameters
        ----------
        my_rom_matrices : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> op.inputs.rom_matrices.connect(my_rom_matrices)
        >>> # or
        >>> op.inputs.rom_matrices(my_rom_matrices)
        """
        return self._rom_matrices

    @property
    def mode_shapes(self):
        """Allows to connect mode_shapes input to the operator.

        Fieldscontainers containing the mode shapes,
        which are cst and nor for the cms
        method

        Parameters
        ----------
        my_mode_shapes : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> op.inputs.mode_shapes.connect(my_mode_shapes)
        >>> # or
        >>> op.inputs.mode_shapes(my_mode_shapes)
        """
        return self._mode_shapes

    @property
    def lumped_mass(self):
        """Allows to connect lumped_mass input to the operator.

        Fieldscontainers containing the lumped mass

        Parameters
        ----------
        my_lumped_mass : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> op.inputs.lumped_mass.connect(my_lumped_mass)
        >>> # or
        >>> op.inputs.lumped_mass(my_lumped_mass)
        """
        return self._lumped_mass

    @property
    def model_data(self):
        """Allows to connect model_data input to the operator.

        Data describing the finite element model

        Parameters
        ----------
        my_model_data : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> op.inputs.model_data.connect(my_model_data)
        >>> # or
        >>> op.inputs.model_data(my_model_data)
        """
        return self._model_data

    @property
    def field_coordinates(self):
        """Allows to connect field_coordinates input to the operator.

        Coordinates of all nodes

        Parameters
        ----------
        my_field_coordinates : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> op.inputs.field_coordinates.connect(my_field_coordinates)
        >>> # or
        >>> op.inputs.field_coordinates(my_field_coordinates)
        """
        return self._field_coordinates

    @property
    def nod(self):
        """Allows to connect nod input to the operator.

        Parameters
        ----------
        my_nod :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> op.inputs.nod.connect(my_nod)
        >>> # or
        >>> op.inputs.nod(my_nod)
        """
        return self._nod


class OutputsComputeInvariantTermsMotion(_Outputs):
    """Intermediate class used to get outputs from
    compute_invariant_terms_motion operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.result.compute_invariant_terms_motion()
    >>> # Connect inputs : op.inputs. ...
    >>> result_model_data = op.outputs.model_data()
    >>> result_mode_shapes = op.outputs.mode_shapes()
    >>> result_lumped_mass = op.outputs.lumped_mass()
    >>> result_field_coordinates_and_euler_angles = op.outputs.field_coordinates_and_euler_angles()
    >>> result_nod = op.outputs.nod()
    >>> result_used_node_index = op.outputs.used_node_index()
    >>> result_eigenvalue = op.outputs.eigenvalue()
    >>> result_translational_mode_shape = op.outputs.translational_mode_shape()
    >>> result_rotational_mode_shape = op.outputs.rotational_mode_shape()
    >>> result_invrt_1 = op.outputs.invrt_1()
    >>> result_invrt_2 = op.outputs.invrt_2()
    >>> result_invrt_3 = op.outputs.invrt_3()
    >>> result_invrt_4 = op.outputs.invrt_4()
    >>> result_invrt_5 = op.outputs.invrt_5()
    >>> result_invrt_6 = op.outputs.invrt_6()
    >>> result_invrt_7 = op.outputs.invrt_7()
    >>> result_invrt_8 = op.outputs.invrt_8()
    """

    def __init__(self, op: Operator):
        super().__init__(compute_invariant_terms_motion._spec().outputs, op)
        self._model_data = Output(
            compute_invariant_terms_motion._spec().output_pin(0), 0, op
        )
        self._outputs.append(self._model_data)
        self._mode_shapes = Output(
            compute_invariant_terms_motion._spec().output_pin(1), 1, op
        )
        self._outputs.append(self._mode_shapes)
        self._lumped_mass = Output(
            compute_invariant_terms_motion._spec().output_pin(2), 2, op
        )
        self._outputs.append(self._lumped_mass)
        self._field_coordinates_and_euler_angles = Output(
            compute_invariant_terms_motion._spec().output_pin(3), 3, op
        )
        self._outputs.append(self._field_coordinates_and_euler_angles)
        self._nod = Output(compute_invariant_terms_motion._spec().output_pin(4), 4, op)
        self._outputs.append(self._nod)
        self._used_node_index = Output(
            compute_invariant_terms_motion._spec().output_pin(5), 5, op
        )
        self._outputs.append(self._used_node_index)
        self._eigenvalue = Output(
            compute_invariant_terms_motion._spec().output_pin(6), 6, op
        )
        self._outputs.append(self._eigenvalue)
        self._translational_mode_shape = Output(
            compute_invariant_terms_motion._spec().output_pin(7), 7, op
        )
        self._outputs.append(self._translational_mode_shape)
        self._rotational_mode_shape = Output(
            compute_invariant_terms_motion._spec().output_pin(8), 8, op
        )
        self._outputs.append(self._rotational_mode_shape)
        self._invrt_1 = Output(
            compute_invariant_terms_motion._spec().output_pin(9), 9, op
        )
        self._outputs.append(self._invrt_1)
        self._invrt_2 = Output(
            compute_invariant_terms_motion._spec().output_pin(10), 10, op
        )
        self._outputs.append(self._invrt_2)
        self._invrt_3 = Output(
            compute_invariant_terms_motion._spec().output_pin(11), 11, op
        )
        self._outputs.append(self._invrt_3)
        self._invrt_4 = Output(
            compute_invariant_terms_motion._spec().output_pin(12), 12, op
        )
        self._outputs.append(self._invrt_4)
        self._invrt_5 = Output(
            compute_invariant_terms_motion._spec().output_pin(13), 13, op
        )
        self._outputs.append(self._invrt_5)
        self._invrt_6 = Output(
            compute_invariant_terms_motion._spec().output_pin(14), 14, op
        )
        self._outputs.append(self._invrt_6)
        self._invrt_7 = Output(
            compute_invariant_terms_motion._spec().output_pin(15), 15, op
        )
        self._outputs.append(self._invrt_7)
        self._invrt_8 = Output(
            compute_invariant_terms_motion._spec().output_pin(16), 16, op
        )
        self._outputs.append(self._invrt_8)

    @property
    def model_data(self):
        """Allows to get model_data output of the operator

        Returns
        ----------
        my_model_data : PropertyField

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_model_data = op.outputs.model_data()
        """  # noqa: E501
        return self._model_data

    @property
    def mode_shapes(self):
        """Allows to get mode_shapes output of the operator

        Returns
        ----------
        my_mode_shapes : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mode_shapes = op.outputs.mode_shapes()
        """  # noqa: E501
        return self._mode_shapes

    @property
    def lumped_mass(self):
        """Allows to get lumped_mass output of the operator

        Returns
        ----------
        my_lumped_mass : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_lumped_mass = op.outputs.lumped_mass()
        """  # noqa: E501
        return self._lumped_mass

    @property
    def field_coordinates_and_euler_angles(self):
        """Allows to get field_coordinates_and_euler_angles output of the operator

        Returns
        ----------
        my_field_coordinates_and_euler_angles : FieldsContainer

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_field_coordinates_and_euler_angles = op.outputs.field_coordinates_and_euler_angles()
        """  # noqa: E501
        return self._field_coordinates_and_euler_angles

    @property
    def nod(self):
        """Allows to get nod output of the operator

        Returns
        ----------
        my_nod :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_nod = op.outputs.nod()
        """  # noqa: E501
        return self._nod

    @property
    def used_node_index(self):
        """Allows to get used_node_index output of the operator

        Returns
        ----------
        my_used_node_index :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_used_node_index = op.outputs.used_node_index()
        """  # noqa: E501
        return self._used_node_index

    @property
    def eigenvalue(self):
        """Allows to get eigenvalue output of the operator

        Returns
        ----------
        my_eigenvalue :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_eigenvalue = op.outputs.eigenvalue()
        """  # noqa: E501
        return self._eigenvalue

    @property
    def translational_mode_shape(self):
        """Allows to get translational_mode_shape output of the operator

        Returns
        ----------
        my_translational_mode_shape :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_translational_mode_shape = op.outputs.translational_mode_shape()
        """  # noqa: E501
        return self._translational_mode_shape

    @property
    def rotational_mode_shape(self):
        """Allows to get rotational_mode_shape output of the operator

        Returns
        ----------
        my_rotational_mode_shape :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_rotational_mode_shape = op.outputs.rotational_mode_shape()
        """  # noqa: E501
        return self._rotational_mode_shape

    @property
    def invrt_1(self):
        """Allows to get invrt_1 output of the operator

        Returns
        ----------
        my_invrt_1 : float

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_1 = op.outputs.invrt_1()
        """  # noqa: E501
        return self._invrt_1

    @property
    def invrt_2(self):
        """Allows to get invrt_2 output of the operator

        Returns
        ----------
        my_invrt_2 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_2 = op.outputs.invrt_2()
        """  # noqa: E501
        return self._invrt_2

    @property
    def invrt_3(self):
        """Allows to get invrt_3 output of the operator

        Returns
        ----------
        my_invrt_3 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_3 = op.outputs.invrt_3()
        """  # noqa: E501
        return self._invrt_3

    @property
    def invrt_4(self):
        """Allows to get invrt_4 output of the operator

        Returns
        ----------
        my_invrt_4 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_4 = op.outputs.invrt_4()
        """  # noqa: E501
        return self._invrt_4

    @property
    def invrt_5(self):
        """Allows to get invrt_5 output of the operator

        Returns
        ----------
        my_invrt_5 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_5 = op.outputs.invrt_5()
        """  # noqa: E501
        return self._invrt_5

    @property
    def invrt_6(self):
        """Allows to get invrt_6 output of the operator

        Returns
        ----------
        my_invrt_6 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_6 = op.outputs.invrt_6()
        """  # noqa: E501
        return self._invrt_6

    @property
    def invrt_7(self):
        """Allows to get invrt_7 output of the operator

        Returns
        ----------
        my_invrt_7 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_7 = op.outputs.invrt_7()
        """  # noqa: E501
        return self._invrt_7

    @property
    def invrt_8(self):
        """Allows to get invrt_8 output of the operator

        Returns
        ----------
        my_invrt_8 :

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.result.compute_invariant_terms_motion()
        >>> # Connect inputs : op.inputs. ...
        >>> result_invrt_8 = op.outputs.invrt_8()
        """  # noqa: E501
        return self._invrt_8
