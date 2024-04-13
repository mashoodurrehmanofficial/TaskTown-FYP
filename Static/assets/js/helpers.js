function populateTableCheckBoxes(parent_identifier, child_identifier) {
    $(`#${parent_identifier}`).change(function (e) {
        var total_childs_checked = $(`.${child_identifier}:checkbox:checked`).length
        $(`input.${child_identifier}:checkbox`).prop('checked', $(this).prop("checked"));
    })
    $(`.${child_identifier}`).change(function (e) {
        var total_childs_checked = $(`.${child_identifier}:checkbox:checked`).length
        if (total_childs_checked == 0) {
            $(`#${parent_identifier}`).prop('checked', $(this).prop("checked"));
        } else {
            $(`#${parent_identifier}`).prop('checked', true);
        }
    })
}


function getSelectedChildIds(child_identifier) {
    var selected_childs = $(`.${child_identifier}:checkbox:checked`)
    console.log(selected_childs)
    var selected_child_ids = []
    for (var i = 0; i < selected_childs.length; i++) {
        selected_child_ids.push($(selected_childs[i]).prop('id'))
    }
    return selected_child_ids
}