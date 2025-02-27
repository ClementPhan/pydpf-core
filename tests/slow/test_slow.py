import pytest
import numpy as np

from ansys.dpf import core as dpf
from ansys.dpf.core import examples
from ansys.dpf.core.custom_fields_container import ElShapeFieldsContainer


def check_fc(fc, fc2):
    for i, f in enumerate(fc):
        assert fc.get_label_space(i) == fc2.get_label_space(i)
        ftocheck = fc2[i].deep_copy()
        iden = dpf.operators.logic.identical_fields(f, ftocheck)
        assert iden.outputs.boolean()
        assert np.allclose(f.data, fc2[i].data)
        assert np.allclose(f.scoping.ids, fc2[i].scoping.ids)
        assert np.allclose(f.data, ftocheck.data)
        assert np.allclose(f.scoping.ids, ftocheck.scoping.ids)
    idenfc = dpf.operators.logic.identical_fc(fc, fc2.deep_copy())
    assert idenfc.outputs.boolean()


@pytest.fixture()
def all_kind_of_complexity_models(local_server):
    return (
        dpf.Model(examples.download_all_kinds_of_complexity()),
        dpf.Model(examples.download_all_kinds_of_complexity(), server=local_server),
    )


def test_model_different_results_big_multi_server(all_kind_of_complexity_models):
    tf = all_kind_of_complexity_models[0].metadata.time_freq_support
    time_scoping = len(tf.time_frequencies)

    results = all_kind_of_complexity_models[0].results
    results2 = all_kind_of_complexity_models[1].results

    op = results.displacement()
    op.inputs.time_scoping(time_scoping)
    op2 = results2.displacement()
    op2.inputs.time_scoping(time_scoping)
    fc = op.outputs.fields_container()
    fc2 = op2.outputs.fields_container()
    check_fc(fc, fc2)

    op = results.stress()
    op.inputs.time_scoping(time_scoping)
    op2 = results2.stress()
    op2.inputs.time_scoping(time_scoping)
    fc = op.outputs.fields_container()
    fc2 = op2.outputs.fields_container()
    check_fc(fc, fc2)

    op = results.elastic_strain()
    op.inputs.time_scoping(time_scoping)
    op2 = results2.elastic_strain()
    op2.inputs.time_scoping(time_scoping)
    fc = op.outputs.fields_container()
    fc2 = op2.outputs.fields_container()
    check_fc(fc, fc2)

    op = results.elemental_volume()
    op.inputs.time_scoping(time_scoping)
    op2 = results2.elemental_volume()
    op2.inputs.time_scoping(time_scoping)
    fc = op.outputs.fields_container()
    fc2 = op2.outputs.fields_container()
    check_fc(fc, fc2)


@pytest.mark.slow
def test_el_shape_fc(allkindofcomplexity):
    model = dpf.Model(allkindofcomplexity)
    fc = model.results.stress.split_by_shape.eval()
    assert isinstance(fc, ElShapeFieldsContainer)
    assert len(fc.beam_fields()) == 1
    assert len(fc.shell_fields()) == 1
    assert len(fc.solid_fields()) == 1
    mesh = model.metadata.meshed_region

    f = fc.beam_field()
    for id in f.scoping.ids:
        assert mesh.elements.element_by_id(id).shape == "beam"

    f = fc.shell_field()
    for id in f.scoping.ids:
        assert mesh.elements.element_by_id(id).shape == "shell"

    f = fc.solid_field()
    for id in f.scoping.ids:
        assert mesh.elements.element_by_id(id).shape == "solid"
