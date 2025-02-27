.. _ref_dpf_operators_reference:

=========
Operators
=========

DPF operators provide for manipulating and transforming simulation data.

From DPF Server for Ansys 2023 R2 and later, the licensing logic for operators in DPF depend on the active
`ServerContext <https://dpf.docs.pyansys.com/api/ansys.dpf.core.server_context.html#servercontext>`_.

The available contexts are **Premium** and **Entry**.
Licensed operators are marked as in the documentation using the ``license`` property.
Operators with the ``license`` property as **None** do not require a license check-out.
For more information about using these two contexts, see :ref:`user_guide_server_context`.
Click below to access the operators documentation.

.. grid:: 1

   .. grid-item::
        .. card:: Operators
            :link-type: doc
            :link: operator_reference_load

            Click here to get started with operators available in DPF.

            +++
            .. button-link:: OPEN
               :color: secondary
               :expand:
               :outline:
               :click-parent:              


.. note::
    For Ansys 2023 R1 and earlier, the context is equivalent to Premium, with all operators loaded.
    For DPF Server 2023.2.pre0, the server context defines which operators are loaded and
    accessible. Use the `PyDPF-Core 0.7 operator documentation<https://dpf.docs.pyansys.com/version/0.7/operator_reference.html#>`_ to learn more.
    Some operators in the documentation might not be available for a particular server version.