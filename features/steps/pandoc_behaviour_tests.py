@given(u'a input markdown file')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a input markdown file')

@when(u'we convert that file through pandoc')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we convert that file through pandoc')

@then(u'we have a docx file as output')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then we have a docx file as output')
