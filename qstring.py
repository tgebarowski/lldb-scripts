import lldb

def utf16string_summary(value, *rest):
    d = value.GetChildMemberWithName("d")
    length = d.GetChildMemberWithName("size").GetValueAsSigned()
    offset = d.GetChildMemberWithName("offset").GetValueAsSigned()
    address = d.GetValueAsUnsigned() + offset
    error = lldb.SBError()
    # UTF-16, so we multiply length by 2
    bytes = value.GetProcess().ReadMemory(address, length * 2, error)
    if bytes is None:
        return '""'
    if length == 0:
        return '""'

    return '"%s"' % (bytes.decode('utf-16').encode('utf-8'))

def __lldb_init_module(debugger, *rest):
    print "registering QString"
    summary = lldb.SBTypeSummary.CreateWithFunctionName("qstring.utf16string_summary")
    summary.SetOptions(lldb.eTypeOptionHideChildren)
    debugger.GetDefaultCategory().AddTypeSummary( lldb.SBTypeNameSpecifier("QString", False), summary )
