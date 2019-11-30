from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="asfsadfa", header="sdassadf", footer="sdafskgs"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
